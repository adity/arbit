from datetime import datetime

class price:
    """
    Class to hold price object
    """
    def __index__(self, exchange, date_time, asset_name):
        self.exchange = exchange
        self.date_time =  date_time
        self.asset_name = asset_name
