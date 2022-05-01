# https://finnhub.io/docs/api/webhook
import requests
import sys
import os

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
)

from configs import settings

# Register new webhook for earnings
r = requests.post(
    f'https://finnhub.io/api/v1/webhook/add?token={settings.FINNHUB_APIKEY}',
    json={'event': 'earnings', 'symbol': 'AAPL'},
)
res = r.json()
print(res)

webhook_id = res['id']
# List webhook
r = requests.get(
    f'https://finnhub.io/api/v1/webhook/list?token={settings.FINNHUB_APIKEY}'
)
res = r.json()
print(res)

# Delete webhook
r = requests.post(
    f'https://finnhub.io/api/v1/webhook/delete?token={settings.FINNHUB_APIKEY}',
    json={'id': webhook_id},
)
res = r.json()
print(res)
