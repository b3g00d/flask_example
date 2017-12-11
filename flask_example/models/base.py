from flask_example.extensions import db


class ExampleBase(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def as_dict(self):
        pass
