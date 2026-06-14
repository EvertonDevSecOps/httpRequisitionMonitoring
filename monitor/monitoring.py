
import requests
import time
from datetime import datetime



def monitoring(url: str) -> str:
    """
    Sends an HTTP request to a URL and returns monitoring information.

    :param url: URL to be monitored.
    :return: String containing status code, response time,
         availability status, and timestamp.
    """
    try:
        start = time.time()
        r = requests.get(url, timeout=10)
        end = time.time()
        real_time = end - start
        status_code = r.status_code
        aviability = "UP" if status_code < 400 else "DOWN"
        return str(f"URL: {url} "
                     f" Code: {r.status_code}"
                    f" Time: {real_time:.2f} seconds."
                    f" Aviability: {aviability}"
                   f" {datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')}")

    except requests.exceptions.RequestException:
        return "Time: None"
