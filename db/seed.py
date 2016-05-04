"""
CS 4392 Project

Clean and migrate yelp academic data to SQL database (PostgreSQL)
and build classifier model to predict health inspection scores for
restaurants

Data Migration - seed loaded documents to table schemas
"""


from document import Document
from models import User, Business, Review, Violation, Map, Tip
from pipelines import KeepItFresh
import settings

class Seed(object):
    """
    Seeding for project
    Available methods:

    load_users to seed all users
    load_reviews to seed all reviews and so on

    load_all to seed all tables in sequence
    """
    def __init__(self):
        self.datasets = Document(settings.DATASETS).get_documents()
        self.pipeline = KeepItFresh()

    """Input each record into database
       TODO: find a way to fix 'utf-8' encoding
    """
    def load_users(self):
        table = self.datasets["users"]
        for line in table:
            user = User(
                    name = line["name"].encode('utf-8'),
                    user_id = line["user_id"].encode('utf-8'),
                    review_count = line["review_count"],
                    average_stars = line["average_stars"],
                    fans = line["fans"]
                    )
            self.pipeline.process_item(user)
    def load_businesses(self):
        table = self.datasets["businesses"]
        for line in table:
            business = Business(
                    name = line["name"].encode('utf-8'),
                    city = line["city"].encode('utf-8'),
                    review_count = line["review_count"],
                    attributes = line["attributes"],
                    stars = line["stars"],
                    latitude = line["latitude"],
                    longitude =  line["longitude"],
                    business_id = line["business_id"].encode('utf-8'),
                    state = line["state"].encode('utf-8'),
                    address = line["full_address"].encode('utf-8'),
                    categories = line["categories"],
                    neighborhoods = line["neighborhoods"]
                    )
            self.pipeline.process_item(business)

    def load_reviews(self):
        table = self.datasets["reviews"]
        for line in table:
            review = Review(
                    review_id=line["review_id"],
                    stars = line["stars"],
                    votes = line["votes"],
                    content= line["text"],
                    user_id = line["user_id"],
                    business_id = line["business_id"],
                    created_date = line["date"]
                    )
            self.pipeline.process_item(review)
    def load_violations(self):
        table = self.datasets["violations"].values
        for line in table:
            violation = Violation(
                    violation_id=line[0],
                    restaurant_id =  line[2],
                    created_date = line[1],
                    minor_violation_score = line[3],
                    major_violation_score = line[4],
                    serve_violation_score = line[5]
                    )
            self.pipeline.process_item(violation)
    def load_maps(self):
        table = self.datasets["mapping"].values
        for line in table:

            maps = Map(
                    restaurant_id=line[0],
                    business_id=line[1]
                    )
            self.pipeline.process_item(maps)
    def load_tips(self):
        table = self.datasets["tips"]
        for line in table:
            tip = Tip(
                    user_id=line["user_id"],
                    business_id=line["business_id"],
                    content=line["text"],
                    created_date = line["date"]
                    )
            self.pipeline.process_item(tip)
    def load_all(self):
        self.load_users()
        self.load_businesses()
        self.load_reviews()
        self.load_tips()
        self.load_violations()
        self.load_maps()

seed = Seed()
seed.load_businesses()
