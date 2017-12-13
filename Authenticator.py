from bittrex import Bittrex, API_V2_0


class Authenticator:
    """
    Class which authenticates and holds session information of the user
    """
    def __init__(self, exchange, api_key, api_secret_key):
        self.exchange = exchange
        self.api_key = api_key
        self.api_secret_key = api_secret_key

    def set_api_key(self, api_key):
        self.api_key = api_key

    def set_api_secret_key(self, secret_api_key):
        self.api_secret_key = secret_api_key

    def get_connection(self):
        return Bittrex(api_key=self.api_key, api_secret= self.api_secret_key, api_version=API_V2_0)

