from flask import render_template, redirect, request, url_for, flash
from app import app, db
from app.forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Collection, Pieces, Dial_Attack, Dial_Damage, Dial_Defense, Dial_Movement, Team
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home Page')

@app.route('/collection', methods=['GET', 'POST'])
def collection():
    colle = Collection.query.all()
    return render_template('collection.html', colle=colle, title='Collection')

@app.route('/col/<id>')
def col(id):
    #col = Pieces.query.filter_by(collection_id = int(id))
    #ncol = Collection.query.get(int(id))
    col = Pieces.query.filter_by(collection_id=int(id)).all()
    #return '<h1>{}</h1>'.format(id)
    return render_template('colpieces.html', col=col, title='Collection Pieces')

@app.route('/pieces/<id>', methods=['GET', 'POST'])
def pieces(id):
    p = Pieces.query.filter_by(id = int(id)).first()
    datk = Dial_Attack.query.filter_by(pieces_id=int(id)).first()
    ddef = Dial_Defense.query.filter_by(pieces_id=int(id)).first()
    ddam = Dial_Damage.query.filter_by(pieces_id=int(id)).first()
    dmov = Dial_Movement.query.filter_by(pieces_id=int(id)).first()
    #return '<h1>{}</h1>'.format(id)
    return render_template('pieces.html', title='Info', p=p, datk=datk, ddef=ddef, ddam=ddam, dmov=dmov)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successfull!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()

    return render_template('user.html', user=user)
