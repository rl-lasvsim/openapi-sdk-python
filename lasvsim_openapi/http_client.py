"""
HTTP client module for the lasvsim API.
"""
from typing import Any, Dict, Callable, Optional, Type, TypeVar,Tuple
import requests


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

    def __init__(self, status_code: int, message: Any, url: str, reason: str = ""):
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

    def clone(self) -> 'HttpClient':
        """Create a clone of this client.
        
        Returns:
            A new HttpClient instance with the same configuration
        """

        return HttpClient(self.config, dict(self.headers))

    def _handle_response(self, response: requests.Response, out_type: Optional[Type[T]] = None) -> Optional[T]:
        if response.status_code != 200:
            try:
                error_data = response.json()
                reason = error_data.get('reason') if isinstance(error_data, dict) else None
                raise APIError(
                    status_code=response.status_code,
                    message=error_data,
                    url=f"{response.request.method},{response.url}",
                    reason=reason
                )
            except ValueError:
                raise APIError(
                    status_code=response.status_code,
                    message=response.text,
                    url=f"{response.request.method},{response.url}"
                )

        if out_type is None:
            return None
            
        try:
            response_data = response.json()
            return out_type.from_dict(response_data)
        except ValueError:
            raise APIError("Invalid JSON response")

    def get(self, path: str, params: Dict[str, str] = None, out_type: Optional[Type[T]] = None) -> T:
        """Send GET request.
        
        Args:
            path: API endpoint path
            params: Query parameters
            out: Type to parse response into
            
        Returns:
            Response data parsed into specified type
            
        Raises:
            APIError: If the request fails
        """
        response = requests.get(
            self.config.endpoint + path,
            params=params,
            headers=self.headers
        )
        return self._handle_response(response, out_type)

    def post(self, path: str, data: Any = None, out_type: Optional[Type[T]] = None) -> T:
        """Send POST request.
        
        Args:
            path: API endpoint path
            data: Request data
            out: Type to parse response into
            
        Returns:
            Response data parsed into specified type
            
        Raises:
            APIError: If the request fails
        """
        response = requests.post(
            self.config.endpoint + path,
            json=data,
            headers=self.headers
        )
        return self._handle_response(response, out_type)
