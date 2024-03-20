#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), primary_key=True,
                             nullable=False, ForeignKey('places.id')),
                      Column('amenity_id', String(60), primary_key=True,
                             nullable=False, ForeignKey('amenities.id')))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenity = relationship('Amenity',
                               secondary=place_amenity,
                               viewonly=False,
                               back_populates='place_amenitites')
    else:
        @property
        def amenities(self):
            """getter method for amenitites."""
            return self.amenity_ids

        @amenitites.setter
        def amenitities(self, obj):
            """Adds an amenity.id to amenity_id."""
            if type(obj) == Amenity and obj not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
