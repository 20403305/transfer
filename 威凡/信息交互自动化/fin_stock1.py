import finnhub
import sys
import os

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
)

from configs import settings

finnhub_client = finnhub.Client(api_key=settings.FINNHUB_APIKEY)

print(finnhub_client.quote('AAPL'))
print(finnhub_client.quote('300003'))
