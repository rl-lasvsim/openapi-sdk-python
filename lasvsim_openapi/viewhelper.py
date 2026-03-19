"""
ViewHelper module for the lasvsim API.
"""

from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.viewhelper_fast import ViewHelperFast
from lasvsim_openapi.viewhelper_model import FolderListReq, FolderListRes, FolderInfo


class ViewHelper:
    """ViewHelper client for the API (returns typed objects)."""
    viewhelper_fast: ViewHelperFast

    def __init__(self, http_client: HttpClient):
        """Initialize viewhelper client.

        Args:
            http_client: HTTP client instance
        """
        self.viewhelper_fast = ViewHelperFast(http_client)

    def folder_list(self, service_code: int = 0) -> FolderListRes:
        """Get folder list (tree structure).

        Args:
            service_code: Service category code
                (1=task, 2=scenario, 3=script, 4=map)

        Returns:
            Folder list response with typed FolderInfo tree

        Raises:
            APIError: If the request fails
        """
        reply = self.viewhelper_fast.folder_list(service_code)
        return FolderListRes.from_dict(reply)
