import requests
from concurrent.futures import ThreadPoolExecutor

def send_requests(url, n, total_requests):
    for _ in range(n):
        response = requests.get(url)
        total_requests.append(response.status_code)

# URL of the server you want to send requests to
url = "http://example.com/api"

# Number of requests to send per thread
n = int(input("Enter the number of requests per thread: "))

total_requests = []

# Adjust the number of threads as needed
num_threads = 10

with ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(lambda _: send_requests(url, n, total_requests), range(num_threads))

print(f"Total number of requests: {len(total_requests)}")
