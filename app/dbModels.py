from . import db


class Cafe(db.Model):
    __tabelname__ = 'cafe'

    id = db.Column(db.Integer, primary_key=True)
    cafe_name = db.Column(db.String(250), index=True)
    cafe_category = db.Column(db.String(150))
    address = db.Column(db.String(350))
    phone_number = db.Column(db.String(13))
    registration_time = db.Column(db.DateTime)

    menu_of_dishes = db.relationship('MenuOfDishes', backref='cafe', lazy='dynamic')

    def __repr__(self):
        return f'Caffe: <{self.id}>, <{self.cafe_name}, <{self.registration_time}>'

class MenuOfDishes(db.Model):
    __tablename__ = 'menu_of_dishes'

    id = db.Column(db.Integer, primary_key=True)
    name_of_the_dish = db.Column(db.String(150), index=True)
    in_stock = db.Column(db.Boolean, default=False)
    date_added = db.Column(db.DateTime)
    cafe_category = db.Column(db.String(150))

    cafe = db.Column(db.Integer, db.ForeignKey('cafe.id'))

    def __repr__(self):
        return f'Menu_of_dishes: <{self.id}>, <{self.name_of_the_dish}>, <{self.cafe}>, <{self.in_stock}>'