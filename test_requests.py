# POST
import time
from uuid import uuid4

import requests


for _ in range(50000):
    product = {'slug': str(uuid4()), 'description': str(uuid4()), 'price': 2.54}
    requests.post('http://localhost:8000/products/', json=product)
    time.sleep(0.05)


# GET description
from time import monotonic

import requests


for _ in range(100):
    start = monotonic()
    product = {'slug': str(uuid4()), 'description': str(uuid4()), 'price': 2.54}
    response = requests.post(
        'http://localhost:8000/products/?description=1aed704e-df54-4b2b-9f88-9a0241137ad3',
        json=product
    )
    print('Response status_code={}, time={} seconds'.format(
        response.status_code, monotonic() - start
    ))
