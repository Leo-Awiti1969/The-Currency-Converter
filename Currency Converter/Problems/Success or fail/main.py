import requests


def check_success(url):
    r = requests.get(url)
    if r.status_code in range(200, 400):
        return "Success"
    return "Fail"
