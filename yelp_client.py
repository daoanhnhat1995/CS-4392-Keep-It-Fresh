from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

class YelpClient(object):

    def __init__(self):
        auth = Oauth1Authenticator(
                consumer_key= 'NqKErS1dFKKwfxlc5KpB0Q',
                consumer_secret= 'BzO_xc7Jge-B5YeysLuLi-WkiHE',
                token= '72CDWmpOaC8LEVgjY1bZVQgyX4v3v8fx',
                token_secret='yLfQC1-Vr_B5mpuqKtidnK_gnbo'
                )
        self.client = Client(auth)

    def search(self,params):
        return self.client.get_business(params)
