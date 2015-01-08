import twitter
from TwitterAPI import TwitterAPI

TWEET_TEXT = "This tweet is from Python code that I wrote."

CONSUMER_KEY = 't5fXZNrCYmLeUHcgzvGDSeCBA'
CONSUMER_SECRET = 'Ro45grugBKZnZqcyvLGRxKE98RzIyA3V9VIxz7e3j7iA2d9sJx'
ACCESS_TOKEN_KEY = '45473548-EB9T6JsBSvZVULFFLJeQpWAGfaLwGrwjQPJIyLH0v'
ACCESS_TOKEN_SECRET = 'JDKwC3xc3GNqm9wQgT4kbKXcM7Gh9vxFch1HpSqMtQW0s'

api = TwitterAPI(
CONSUMER_KEY,
CONSUMER_SECRET,
ACCESS_TOKEN_KEY,
ACCESS_TOKEN_SECRET)

r = api.request('statuses/update', {'status': TWEET_TEXT})

print('SUCCESS' if r.status_code == 200 else 'FAILURE')
