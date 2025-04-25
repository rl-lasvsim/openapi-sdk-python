"""
HTTP client module for the lasvsim API.
"""
from typing import Any, Dict, Callable, Optional, Type, TypeVar,Tuple
import urllib3
import ujson
from urllib.parse import urlparse,urljoin

class ErrorReason:
    """Error reason constants."""
    CALL_GRPC_ERR = "CALL_GRPC_ERR"
    PARAM_UNAVAILABLE = "PARAM_UNVAILABLE"  # Keep original typo for compatibility
    NOT_EXIST = "NOT_EXIST"
    GET_HEADER_ERR = "GET_HEADER_ERR"


class APIError(Exception):
    """Error returned by the API."""
    status_code: int = 0
    message: Any = None
    url: str = ""
    reason: str = ""

    def __init__(self, status_code: int = 0, message: Any = None, url: str = None, reason: str = ""):
        super().__init__(f"APIError {url} {status_code}: {message}")
        self.status_code = status_code
        self.message = message
        self.url = url
        self.reason = reason

    @staticmethod
    def is_api_error(err: Exception) -> Tuple[Optional['APIError'], bool]:
        """Check if an error is an APIError.
        
        Args:
            err: The error to check
            
        Returns:
            A tuple of (APIError instance if it is an APIError, boolean indicating if it is an APIError)
        """
        if isinstance(err, APIError):
            return err, True
        return None, False

    @staticmethod
    def match_error_reason(err: Exception, err_str: str) -> bool:
        """Check if an error matches a specific error reason.
        
        Args:
            err: The error to check
            err_str: The error reason to match against
            
        Returns:
            True if the error matches the reason, False otherwise
        """
        if isinstance(err, APIError):
            return err.reason == err_str
        return False


class HttpConfig:
    """Configuration for the HTTP client."""
    token: str = ""
    endpoint: str = ""

    def __init__(self, token: str = "", endpoint: str = ""):
        """Initialize HTTP configuration.
        
        Args:
            token: Authentication token
            endpoint: API endpoint URL
        """
        self.token = token
        self.endpoint = endpoint


T = TypeVar('T')

class HttpClient():
    """HTTP client for the API."""
    config: HttpConfig = None
    headers: Dict[str, str] = {}
    
    def __init__(self, config: HttpConfig, headers: Dict[str, str] = None):
        """Initialize HTTP client.
        
        Args:
            config: Client configuration
            headers: Optional custom headers
        """
        self.config = config
        self.headers = headers or {}
        self.headers["Authorization"] = f"Bearer {config.token}"
        self.headers["Content-Type"] = "application/json"
        self.headers["Connection"] = "keep-alive"

        parsed_url = urlparse(config.endpoint)
        host = parsed_url.hostname
        port = parsed_url.port or (443 if parsed_url.scheme == "https" else 80)
        
        if parsed_url.scheme == "http":
            self.http = urllib3.connectionpool.HTTPConnectionPool(
                host=host,
                port=port,
                maxsize=500,
                retries=urllib3.Retry(total=3, backoff_factor=0.5),
            )
        else:
            self.http = urllib3.connectionpool.HTTPSConnectionPool(
                host=host,
                port=port,
                maxsize=500,
                retries=urllib3.Retry(total=3, backoff_factor=0.5),
            )
    def clone(self) -> 'HttpClient':
        """Create a clone of this client.
        
        Returns:
            A new HttpClient instance with the same configuration
        """

        return HttpClient(self.config, dict(self.headers))

    def close(self):
        """Close the underlying HTTP connection"""
        self.http.close()

    def _handle_response(self, response: urllib3.HTTPResponse) -> Optional[T]:
        if response.status != 200:
            try:
                error_data = ujson.loads(response.data)
            except Exception as e:
                error_data = {"message": f'client parse json error:{e},data:{response.data}'}

            reason = error_data.get('reason') if isinstance(error_data, dict) else None
            raise APIError(
                status_code=response.status,
                message=error_data.get('message'),
                reason=reason,
            )
        
        # if out_type is None:
        #     return None
        response_data = ujson.loads(response.data)
        return response_data
    
    def do(self, method, url, fields=None, headers=None, **urlopen_kw):
        try:
            # path join
            url = self.config.endpoint + url
            if 'body' in urlopen_kw:
                body = urlopen_kw.pop('body')
                response = self.http.request(method, url, body=body, headers=headers, **urlopen_kw)
            elif fields:
                response = self.http.request(method, url, fields=fields, headers=headers, **urlopen_kw)
            else:
                response = self.http.request(method, url, headers=headers, **urlopen_kw)

            return self._handle_response(response)
        except APIError as e:
            e.url = f"{method},{url}"
            raise e
        except Exception as e:
            raise APIError(
                message=f"Failed to get response. Error: {e}",
                url=f"{method},{url}"
            )

    def get(self, path: str, params: Dict[str, str] = None):
        try:
            return self.do("GET", path, fields=params, headers=self.headers)
        except Exception as e:
            # 兜底打印
            print(f"http request error{e},method:GET,path:{path}")
            raise e

    def post(self, path: str, data: Any = None):
        try:
            encoded_data = ujson.dumps(data) if data else None
            return self.do("POST", path, body=encoded_data, headers=self.headers)
        except Exception as e:
            # 兜底打印
            print(f"http request error{e},method:POST,path:{path}")
            raise e