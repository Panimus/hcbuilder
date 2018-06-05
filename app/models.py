from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Collection(db.Model):
    colle_id = db.Column(db.Integer, primary_key=True)
    colle_name = db.Column(db.String(64), index=True)
    colle_number = db.Column(db.String(30), index=True, unique=True)
    colle_initials = db.Column(db.String(10), index=True)
    colle_age = db.Column(db.String(60), index=True, unique=True)
    colle_releasedate = db.Column(db.DateTime, unique=True)
    colle_piecequantity = db.Column(db.Integer)

    def __repr__(self):
        return '<Collection {}>'.format(sef.colle_name)

class Units(db.Model):
    units_id = db.Column(db.Integer, primary_key=True)
    units_name = db.Column(db.String(64), index=True)
    units_realname = db.Column(db.String(64), index=True)
    units_trait = db.Column(db.String(300), index=True)
    units_improvedtarget = db.Column(db.String(50), index=True)
    units_range = db.Column(db.Integer)
    units_bolts = db.Column(db.Integer)

    def __repr__(self):
        return '<Units {}>'.format(sef.units_name)

class Dial_Move(db.model):
    dmove_id = db.Column(db.Integer, primary_key=True)
    dmove_pos1 = db.Column(Db.Integer)
    dmove_pos2 = db.Column(Db.Integer)
    dmove_pos3 = db.Column(Db.Integer)
    dmove_pos4 = db.Column(Db.Integer)
    dmove_pos5 = db.Column(Db.Integer)
    dmove_pos6 = db.Column(Db.Integer)
    dmove_pos7 = db.Column(Db.Integer)
    dmove_pos8 = db.Column(Db.Integer)
    dmove_pos9 = db.Column(Db.Integer)
    dmove_pos10 = db.Column(Db.Integer)
    dmove_pos11 = db.Column(Db.Integer)
    dmove_pos12 = db.Column(Db.Integer)
    dmove_cor1 = db.Column(db.String(30))
    dmove_cor2 = db.Column(db.String(30))
    dmove_cor3 = db.Column(db.String(30))
    dmove_cor4 = db.Column(db.String(30))
    dmove_cor5 = db.Column(db.String(30))
    dmove_cor6 = db.Column(db.String(30))
    dmove_cor7 = db.Column(db.String(30))
    dmove_cor8 = db.Column(db.String(30))
    dmove_cor9 = db.Column(db.String(30))
    dmove_cor10 = db.Column(db.String(30))
    dmove_cor11 = db.Column(db.String(30))
    dmove_cor12 = db.Column(db.String(30))
