import json

class CredReader:
    """
    Reads the credentials file if present otherwise defaults to None
    """
    def __init__(self, exchangename):
        self.exchange = exchangename
        try:
            print "Using given credentials"
            file = open(self.exchange)
            self.creds = json.load(file)
            self.api_key = self.creds['key']
            self.api_secret_key = self.creds['secret']
        except:
            print "Invalid credentials. Using default."
            self.creds = None
            self.api_key = None
            self.api_secret_key = None

    def get_api_key(self):
        return self.api_key

    def get_api_secret_key(self):
        return self.api_secret_key


