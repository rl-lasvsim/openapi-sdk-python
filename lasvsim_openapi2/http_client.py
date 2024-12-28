from typing import Dict, Any, Optional, Union
import requests
import json

class APIError(Exception):
    def __init__(self, status_code: int, message: Union[str, dict], url: str, reason: str = ""):
        self.status_code = status_code
        self.message = message
        self.url = url
        self.reason = reason

    def __str__(self):
        return f"APIError {self.url} {self.status_code}: {self.message}"

class ErrorReason:
    CALL_GRPC_ERR = "CALL_GRPC_ERR"
    PARAM_UNVAILABLE = "PARAM_UNVAILABLE"
    NOT_EXIST = "NOT_EXIST"
    GET_HEADER_ERR = "GET_HEADER_ERR"
    SET_HEADER_ERR = "SET_HEADER_ERR"
    SET_KV_ERR = "SET_KV_ERR"

def IsApiError(err: Exception) -> tuple[Optional[APIError], bool]:
    if isinstance(err, APIError):
        return err, True
    return None, False

def MatchErrorReason(err: Exception, err_str: str) -> bool:
    if isinstance(err, APIError):
        return err.reason == err_str
    return False

class HttpClient:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.session = None
        self.base_url = config.get('base_url', '')
        self.headers = config.get('headers', {})
        self.session = requests.Session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.session:
            self.session.close()

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            try:
                err_resp = response.json()
            except json.JSONDecodeError:
                err_resp = response.text
            reason = ""
            if isinstance(err_resp, dict) and "reason" in err_resp:
                reason = err_resp["reason"]
            raise APIError(response.status_code, err_resp, f"GET,{url}", reason)
        return response.json()

    def post(self, endpoint: str, data: Optional[Dict] = None) -> Dict:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, headers=self.headers, json=data)
        if response.status_code != 200:
            try:
                err_resp = response.json()
            except json.JSONDecodeError:
                err_resp = response.text
            reason = ""
            if isinstance(err_resp, dict) and "reason" in err_resp:
                reason = err_resp["reason"]
            raise APIError(response.status_code, err_resp, f"POST,{url}", reason)
        return response.json()

    def put(self, endpoint: str, data: Optional[Dict] = None) -> Dict:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.put(url, headers=self.headers, json=data)
        if response.status_code != 200:
            try:
                err_resp = response.json()
            except json.JSONDecodeError:
                err_resp = response.text
            reason = ""
            if isinstance(err_resp, dict) and "reason" in err_resp:
                reason = err_resp["reason"]
            raise APIError(response.status_code, err_resp, f"PUT,{url}", reason)
        return response.json()

    def delete(self, endpoint: str) -> Dict:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.delete(url, headers=self.headers)
        if response.status_code != 200:
            try:
                err_resp = response.json()
            except json.JSONDecodeError:
                err_resp = response.text
            reason = ""
            if isinstance(err_resp, dict) and "reason" in err_resp:
                reason = err_resp["reason"]
            raise APIError(response.status_code, err_resp, f"DELETE,{url}", reason)
        return response.json()
