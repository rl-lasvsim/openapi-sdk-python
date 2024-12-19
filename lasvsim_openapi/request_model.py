class Point(object):
    def __init__(self, x: float, y: float, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    # 将Point对象转换为字典，以便可以序列化为JSON
    def to_dict(self):
        return {"x": self.x, "y": self.y, "z": self.z}


class ObjBaseInfo(object):
    def __init__(self, length: float, width: float, height: float, weight: float):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

    def to_dict(self):
        return {
            "length": self.length,
            "width": self.width,
            "height": self.height,
            "weight": self.weight,
        }
