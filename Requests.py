import requests

def send_requests(url, n):
    for i in range(n):
        response = requests.get(url)
        print(f"Request {i+1} - Status Code: {response.status_code}")

# URL of the server you want to send requests to
url = "http://example.com/api"

# Number of requests to send
n = int(input("Enter the number of requests: "))

send_requests(url, n)
