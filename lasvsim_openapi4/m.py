import json
from lasvsim_openapi4.qxmap import Qxmap

def test_qxmap():
    # 创建一个测试用的 JSON 数据
    data = {
        "header": {
            "north": 1.0,
            "south": -1.0,
            "east": 1.0,
            "west": -1.0,
            "source_type": 1,
            "source_version": "1.0",
            "source_data": "test",
            "source_date": "2024-12-28",
            "source_coordinate_system": "WGS84",
            "source_projection": "UTM",
            "source_unit": "meter"
        },
        "junctions": [
            {
                "id": "j1",
                "name": "Junction 1",
                "type": 1,
                "center": {
                    "x": 0.0,
                    "y": 0.0,
                    "z": 0.0
                },
                "shape": {
                    "points": [
                        {"x": -1.0, "y": -1.0, "z": 0.0},
                        {"x": 1.0, "y": -1.0, "z": 0.0},
                        {"x": 1.0, "y": 1.0, "z": 0.0},
                        {"x": -1.0, "y": 1.0, "z": 0.0}
                    ]
                },
                "movements": [
                    {
                        "id": "m1",
                        "upstream_link_id": "l1",
                        "downstream_link_id": "l2",
                        "junction_id": "j1",
                        "flow_direction": 1
                    }
                ],
                "connections": [
                    {
                        "id": "c1",
                        "junction_id": "j1",
                        "movement_id": "m1",
                        "upstream_lane_id": "lane1",
                        "downstream_lane_id": "lane2",
                        "flow_direction": 1,
                        "upstream_link_id": "l1",
                        "downstream_link_id": "l2",
                        "path": {
                            "points": [
                                {"x": -0.5, "y": 0.0, "z": 0.0},
                                {"x": 0.5, "y": 0.0, "z": 0.0}
                            ]
                        }
                    }
                ],
                "crosswalks": [
                    {
                        "id": "cw1",
                        "heading": 90.0,
                        "shape": {
                            "points": [
                                {"x": -0.5, "y": -0.1, "z": 0.0},
                                {"x": 0.5, "y": -0.1, "z": 0.0},
                                {"x": 0.5, "y": 0.1, "z": 0.0},
                                {"x": -0.5, "y": 0.1, "z": 0.0}
                            ]
                        }
                    }
                ],
                "signal_plan": {
                    "id": "sp1",
                    "junction_id": "j1",
                    "cycle": 90,
                    "offset": 0,
                    "is_yellow": False,
                    "movement_signals": {
                        "m1": {
                            "movement_id": "m1",
                            "traffic_light_pole_id": "tlp1",
                            "position": {
                                "point": {"x": 0.0, "y": 0.0, "z": 0.0},
                                "heading": 90.0
                            },
                            "signal_of_greens": [
                                {
                                    "green_start": 0,
                                    "green_duration": 30,
                                    "yellow": 3,
                                    "red_clean": 2
                                }
                            ]
                        }
                    }
                }
            }
        ],
        "segments": [],
        "links": [],
        "lanes": []
    }
    
    # 将数据转换为 JSON 字符串
    json_str = json.dumps(data)
    
    # 从 JSON 字符串解析
    qxmap = Qxmap(json.loads(json_str))
    
    # 验证解析结果
    assert qxmap.header.north == 1.0
    assert qxmap.header.south == -1.0
    assert qxmap.header.east == 1.0
    assert qxmap.header.west == -1.0
    assert qxmap.header.source_type == 1
    assert qxmap.header.source_version == "1.0"
    assert qxmap.header.source_data == "test"
    assert qxmap.header.source_date == "2024-12-28"
    assert qxmap.header.source_coordinate_system == "WGS84"
    assert qxmap.header.source_projection == "UTM"
    assert qxmap.header.source_unit == "meter"
    
    assert len(qxmap.segments) == 0
    assert len(qxmap.links) == 0
    assert len(qxmap.lanes) == 0
    
    print(qxmap.junctions)
    print("All tests passed!")

if __name__ == "__main__":
    test_qxmap()