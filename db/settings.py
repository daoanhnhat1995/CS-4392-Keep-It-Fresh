"""

This file contains settings for Postgresql from AlchemySQL

"""

DATABASE = {
        'drivername':'postgres',
        'host':'localhost',
        'port':'5432',
        'username':'nhatdao',
        'password':'',
        'database':'keepitfresh'
        }

DATASETS = {
        'reviews':'datasets/yelp_academic_dataset_review.json',
        'businesses':'datasets/yelp_academic_dataset_business.json',
        'users':'datasets/yelp_academic_dataset_user.json',
        'mapping':'datasets/restaurant_ids_to_yelp_ids.csv',
        'violations':'datasets/AllViolations.csv',
        'tips':'datasets/yelp_academic_dataset_tip.json',
        'checkin':'datasets/yelp_academic_dataset_checkin.json'
        }

