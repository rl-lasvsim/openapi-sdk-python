"""
Process task module for the lasvsim API.
"""

from lasvsim_openapi.http_client import HttpClient

class ProcessTaskFast:
    """Process task client for the API."""
    http_client: HttpClient = None

    def __init__(self, http_client: HttpClient):
        """Initialize process task client.
        
        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client.clone()

    def copy_record(self, task_id: int, record_id: int):
        """Copy a record.
        
        Args:
            task_id: Task ID
            record_id: Record ID
            
        Returns:
            Copy record response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/process_task/v2/record/copy",
            {"task_id": task_id, "record_id": record_id},
        )

    def get_record_scenario(self, task_id: int, record_id: int):
        """Get record scenario.
        
        Args:
            task_id: Task ID
            record_id: Record ID
            
        Returns:
            Get record scenario response
            
        Raises:
            APIError: If the request fails
        """        
        return self.http_client.post(
            "/openapi/process_task/v2/record/scenario/get",
            {"task_id": task_id, "record_id": record_id},
        )

    def get_task_record_ids(self, task_id: int):
        """Get task record IDs.
        
        Args:
            task_id: Task ID
            
        Returns:
            Get task record IDs response
            
        Raises:
            APIError: If the request fails
        """
        
        return self.http_client.post(
            "/openapi/process_task/v2/record/id_list",
            {"task_id": task_id},
        )

    def create_task(self, name: str, scene_v2_infos: list, folder_id: int = 0, sim_type: int = 0):
        """Create a simulation task.
        
        Args:
            name: Task name
            scene_v2_infos: List of scenario references (dict or ScenarioRef)
            folder_id: Folder ID (optional)
            sim_type: Simulation type (0:None; 1:TaskSim; 2:RealTimeSim; 3:CoSim; 4:HILSim)
            
        Returns:
            Create task response (dict)
            
        Raises:
            APIError: If the request fails
        """
        # Convert ScenarioRef objects to dict if needed
        scene_infos = []
        for info in scene_v2_infos:
            if hasattr(info, 'to_dict'):
                scene_infos.append(info.to_dict())
            else:
                scene_infos.append(info)
        
        payload = {
            "name": name,
            "folder_id": folder_id,
            "scene_v2_infos": scene_infos,
            "sim_type": sim_type,
        }
        
        return self.http_client.post(
            "/openapi/process_task/v2/task/create",
            payload,
        )
