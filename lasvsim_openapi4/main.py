from dataclasses import dataclass
from typing import Optional, Type, TypeVar, Any, get_type_hints, List, get_args, get_origin
import json

T = TypeVar('T')

def parse_json_to_object(json_str: str, out_type: Optional[Type[T]] = None) -> Optional[T]:
    """Parse JSON string into specified object type.
    
    Args:
        json_str: JSON string to parse
        out_type: Target class type to parse into
        
    Returns:
        Parsed object of specified type, or None if out_type is None
        
    Raises:
        ValueError: If JSON parsing fails
    """
    if out_type is None:
        return None
        
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON string: {str(e)}")
    
    return _convert_to_type(data, out_type)

def _convert_to_type(data: Any, target_type: Type[T]) -> T:
    """Convert data to target type, handling nested objects and lists."""
    # Handle None
    if data is None:
        return None
        
    # Handle primitive types
    if target_type in (str, int, float, bool):
        return target_type(data)
        
    # Handle lists
    if get_origin(target_type) == list:
        item_type = get_args(target_type)[0]
        return [_convert_to_type(item, item_type) for item in data]
    
    # Handle dataclasses
    if hasattr(target_type, '__annotations__'):
        type_hints = get_type_hints(target_type)
        processed_data = {}
        for key, value in data.items():
            if key in type_hints:
                processed_data[key] = _convert_to_type(value, type_hints[key])
        return target_type(**processed_data)
    
    return data

# Test code
@dataclass
class Point:
    x: float
    y: float

@dataclass
class Road:
    id: str
    name: str
    points: List[Point]  # Now using a list of points

def main():
    # Test with JSON string containing array
    json_str = '''
    {
        "id": "road_1",
        "name": "Main Street",
        "points": [
            {"x": 100.0, "y": 200.0},
            {"x": 150.0, "y": 250.0}
        ]
    }
    '''
    
    # Parse JSON string to Road object
    road = parse_json_to_object(json_str, Road)
    print(f"From JSON string: {road}")
    
    # Test with dict converted to JSON string
    dict_data = {
        "id": "road_2",
        "name": "Side Road",
        "points": [
            {"x": 50.0, "y": 150.0},
            {"x": 75.0, "y": 175.0}
        ]
    }
    json_str = json.dumps(dict_data)
    
    # Parse JSON string to Road object
    road = parse_json_to_object(json_str, Road)
    print(f"From dict->json: {road}")

if __name__ == "__main__":
    main()