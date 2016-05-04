"""

This file contains all Postgresql Data models

"""

from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime, Text,ForeignKeyConstraint, ForeignKey
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.engine.url import URL

import settings

Base = declarative_base()

def db_connect():
    return create_engine(URL(**settings.DATABASE))


def create_tables(engine):
    """
    migrate tables
    """
    Base.metadata.create_all(engine)


class User(Base):
    """
    Sqlalchemy user model
    """
    __tablename__= 'users'
    user_id = Column(String,primary_key='true')
    name = Column(String(100), nullable=True)
    review_count = Column(Integer, default=0)
    average_stars = Column( Float, default=0)
    fans = Column(Integer,default=0)


class  Business(Base):
    """
    Sqlalchemy businesses model
    """

    __tablename__ = 'businesses'
    business_id = Column(String(100), primary_key=True)
    name = Column( String(100))
    neighborhoods = Column(ARRAY(String))
    categories = Column(ARRAY(String))
    address = Column(String(100))
    city = Column(String(100))
    state = Column(String(100))
    latitude = Column(Float,default=0)
    longitude = Column(Float,default=0)
    stars = Column(Float,default=0)
    review_count = Column( Integer, default=0)
    attributes = Column(JSONB)

class Tip(Base):
    """
    Sqlalchemy tips model
    """
    __tablename__ = 'tips'
    tip_id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(String,ForeignKey('users.user_id'))
    business_id = Column(String,ForeignKey('businesses.business_id'))
    content = Column(String)
    likes = Column(Integer,default=0)
    created_date = Column(DateTime,nullable=True)

    def __init__(self,content):
        self.content = content

    @property
    def to_json(self):
        return{
                "content":self.content
        }

class Review(Base):
    """
    Sqlalchemy review model
    """

    __tablename__ = 'reviews'
    review_id  = Column(String,primary_key=True)
    stars = Column(Integer,default=0)
    votes = Column(JSONB,nullable=True)
    content = Column(Text, nullable=True)
    user_id = Column(String,ForeignKey("users.user_id"))
    business_id = Column(String,ForeignKey("businesses.business_id"))
    created_date = Column(DateTime,nullable=True)


class Violation(Base):
    """
    Sqlalchemy violations model
    """
    __tablename__ = "violations"
    violation_id= Column(String,primary_key=True)
    restaurant_id = Column(String)
    created_date = Column(DateTime,nullable=True)
    minor_violation_score = Column(Float,default=0)
    major_violation_score = Column(Float,default=0)
    serve_violation_score = Column(Float,default=0)

class Map(Base):
    """
    Sqlalchemy map model
    to map business_id and restaurant_id specified by Yelp
    """
    __tablename__="maps"
    business_id = Column(String,ForeignKey('businesses.business_id'),primary_key=True)
    restaurant_id= Column(String)

