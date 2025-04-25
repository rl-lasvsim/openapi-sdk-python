from lasvsim_openapi.http_client import HttpClient
class TrainTaskFast:
    http_client: HttpClient = None
    def __init__(self, http_client: HttpClient) -> None:
        """Initialize train task client.
        
        Args:
            http_client: HTTP client.
        """
        self.http_client = http_client.clone()

    def get_scene_id_list(self, task_id: int):
        """Copy record.
        
        Args:
            task_id: Task ID    
        Raises:
            APIError: If the request fails
        """
        
        return self.http_client.get(
            f"/openapi/train_task/{task_id}/scene_id_list",
            {},
        )
