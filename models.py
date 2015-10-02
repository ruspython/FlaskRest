from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    company = db.relationship('Company', backref='users')
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.company_id = 1

    def __repr__(self):
        return self.first_name


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
