from app import db

class City(db.Model):
    __tablename__ = "citydetails"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    population = db.Column(db.Integer)
    country = db.Column(db.String(50))

class Country(db.Model):
    __tablename__ = "country"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    capital = db.Column(db.String(50))
    callingCode = db.Column(db.String(50))
    numRegions = db.Column(db.Integer)


class CityTime(db.Model):
    __tablename__ = "citytime"
    id = db.Column(db.Integer, primary_key=True)
    cityID = db.Column(db.String(100))
    cityTime = db.Column(db.String(50))


