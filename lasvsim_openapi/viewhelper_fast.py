"""
ViewHelper module for the lasvsim API.
"""

from lasvsim_openapi.http_client import HttpClient


class ViewHelperFast:
    """ViewHelper client for the API (returns dict)."""
    http_client: HttpClient = None

    def __init__(self, http_client: HttpClient):
        """Initialize viewhelper client.

        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client.clone()

    def folder_list(self, service_code: int = 0) -> dict:
        """Get folder list (tree structure).

        Args:
            service_code: Service category code
                (1=task, 2=scenario, 3=script, 4=map)

        Returns:
            Folder list response (tree structure)

        Raises:
            APIError: If the request fails
        """
        req = {
            "service_code": service_code,
        }
        return self.http_client.post(
            "/openapi/viewhelper/v2/folder/list",
            req,
        )
