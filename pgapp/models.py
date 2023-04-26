from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)

    def __str__(self):
        return self.username

    def get_user_id(self):
        return self.id

    def check_password(self, password):
        return password == 'valid'


class Client(db.Model):
    class MyEnum(db.enum.Enum):
        one = 1
        two = 2
        three = 3
    __tablename__ = "client"

    account = db.Column(db.String(40), unique=True, nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    email = db.Column(db.String(40), unique=True, nullable=False)
    utility = db.Column(db.Enum(MyEnum), primary_key=True)


class BUser(db.Model):
    __tablename__ = 'b_user'
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    token = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return 'Comment ' + str(self.id)
