import requests
import threading

def send_requests(url, n):
    def send_request():
        for _ in range(n):
            response = requests.get(url)
            print(f"Status Code: {response.status_code}")

    threads = []
    for _ in range(10):  # Adjust the number of threads as needed
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# URL of the server you want to send requests to
url = "https://noticeboard.pythonanywhere.com"

# Number of requests to send per thread
n = int(input("Enter the number of requests per thread: "))

send_requests(url, n)

