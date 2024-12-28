from dataclasses import dataclass
from typing import Any, Dict, Optional
import requests

@dataclass
class APIError(Exception):
    status_code: int
    message: Any
    url: str
    reason: str = ""

    def __str__(self):
        return f"APIError {self.url} {self.status_code}: {self.message}"

@dataclass
class HttpConfig:
    token: str
    endpoint: str

@dataclass
class HttpClient:
    config: HttpConfig
    headers: Dict[str, str] = None
    client: requests.Session = None

    def __init__(self, config: HttpConfig, headers: Dict[str, str] = None):
        self.config = config
        self.headers = headers or {}
        self.client = requests.Session()
        self.headers["Authorization"] = f"Bearer {config.token}"

    def clone(self) -> 'HttpClient':
        return HttpClient(self.config, self.headers.copy())

    def get(self, path: str, params: Dict[str, str] = None, out: Any = None) -> Optional[Any]:
        url = self.config.endpoint + path
        if params:
            url += "?" + "&".join(f"{k}={v}" for k, v in params.items())

        response = self.client.get(url, headers=self.headers)
        return self._handle_response(response, out)

    def post(self, path: str, data: Any, out: Any = None) -> Optional[Any]:
        url = self.config.endpoint + path
        headers = self.headers.copy()
        headers["Content-Type"] = "application/json"
        
        response = self.client.post(url, json=data, headers=headers)
        return self._handle_response(response, out)

    def _handle_response(self, response: requests.Response, out: Any) -> Optional[Any]:
        if response.status_code != 200:
            error = APIError(
                status_code=response.status_code,
                message=response.json() if response.content else response.text,
                url=f"{response.request.method},{response.request.url}"
            )
            raise error

        if out is None:
            return None
        
        try:
            if isinstance(out, type):
                return out(response.json())
            else:
                return response.json()
        except:
            return response.text
