from . import db

class PropertyProfile(db.Model):
    
    __tablename__ = 'property_profiles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180))
    description = db.Column(db.String(255))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.String(80))
    type = db.Column(db.String(20))
    location = db.Column(db.String(180))
    image_name = db.Column(db.String(80))
    
    def __init__(self, title, description, bedrooms, bathrooms, price, type, location, image):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.type = type
        self.location = location
        self.image_name = image