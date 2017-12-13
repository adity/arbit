from Authenticator import Authenticator
from CredReader import CredReader
import sys

def run(args):
    """
    Usage: python Runner.py <path-to-credentials.json>
    """
    reader = CredReader(args[0])
    auth = Authenticator(args[0], reader.get_api_key(), reader.get_api_secret_key())
    connection = auth.get_connection()
    print connection.get_balances()

if __name__ == '__main__':
    run(sys.argv[1:])