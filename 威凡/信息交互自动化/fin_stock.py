# https://finnhub.io/docs/api/webhook
import requests
import sys
import os

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
)

from configs import settings

api_key = settings.FINNHUB_APIKEY

# Register new webhook for earnings
r = requests.post(
    f'https://finnhub.io/api/v1/webhook/add?token={api_key}',
    json={'event': 'earnings', 'symbol': 'AAPL'},
)
res = r.json()
print(res)

webhook_id = res['id']
# List webhook
r = requests.get(f'https://finnhub.io/api/v1/webhook/list?token={api_key}')
res = r.json()
print(res)

# Delete webhook
r = requests.post(
    f'https://finnhub.io/api/v1/webhook/delete?token={api_key}', json={'id': webhook_id}
)
res = r.json()
print(res)
