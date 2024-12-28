import requests


class APIError(Exception):
    def __init__(self, status_code, message, url):
        super().__init__(f"APIError {url} {status_code}: {message}")
        self.status_code = status_code
        self.message = message
        self.url = url


class HttpConfig(object):
    """
    Configuration for the client.
    """

    def __init__(self, token: str = None, endpoint: str = None):
        self.token = token
        self.endpoint = endpoint


class HttpClient(object):
    """
    HTTP client for the API.
    """

    def __init__(self, config: HttpConfig, headers: dict):
        self.config = config
        self.headers = headers
        self.headers.update({"Authorization": "Bearer " + self.config.token})

    def get(self, path: str, params: dict):
        response = requests.get(
            self.config.endpoint + path, params, headers=self.headers
        )
        if response.status_code != 200:
            raise APIError(
                response.status_code, tryParseResponse(response), response.url
            )
        return response.json()

    def post(self, path: str, data: dict):
        response = requests.post(
            self.config.endpoint + path, json=data, headers=self.headers
        )
        if response.status_code != 200:
            raise APIError(
                response.status_code, tryParseResponse(response), response.url
            )
        return response.json()


def tryParseResponse(response):
    try:
        return response.json()
    except:
        print("Failed to parse response:", response.text)
        return response.reason
