"""
CS 4392 Project

Clean and migrate yelp academic data to SQL database (PostgreSQL)
and build classifier model to predict health inspection scores for
restaurants

Training and Testing datasets are collected from Yelp Boston Area
can be found at : https://www.drivendata.org/competitions/5/page/33/

Data Migration - pipeline for loading (csv,json) documents into SQL tables

"""
from sqlalchemy.orm import sessionmaker
from models import User, db_connect, create_tables

class KeepItFresh(object):
    """
    Pipeline for storing items in databases
    """


    def __init__(self):
        """Initializes database connection and sessionmaker
        Create:
        users table
        reviews table
        violations table
        restaurants table
        """
        engine = db_connect()
       # engine.echo = True #prints out SQL we are loading
        create_tables(engine)
        self.Session = sessionmaker(bind=engine)


    """Insert a row into table
    Args:
        item: a row (record) for a table
    >>> db = KeepItFresh()
    >>> user = User(name='Example')
    >>> db.process_item(user)
    >>> committed
    """
    def process_item(self,item):
        session = self.Session()
        try:
            session.add(item)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item

    def session(self):
        return self.Session()
