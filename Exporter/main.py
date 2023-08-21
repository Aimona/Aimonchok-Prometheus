from prometheus_client import start_http_server, Histogram
import os
import time
import requests

REQUEST_TIME_HISTOGRAM = Histogram('request_processing_seconds', 'Time spent processing the request')


@REQUEST_TIME_HISTOGRAM.time()
def process_request(url):
    requests.get(url)


if __name__ == '__main__':
    URL = os.getenv('WEBSITE', 'https://www.google.com/')
    start_http_server(80)
    print(f'Server started at http://localhost/')
    while True:
        process_request(URL)
        time.sleep(5)