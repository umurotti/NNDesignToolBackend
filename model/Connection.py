class Connection():
    def __init__(self, from_node: str, from_port: int,
                        to_node: str, to_port: int) -> None:
        
        self.from_node = from_node
        self.from_port = from_port
        self.to_node = to_node
        self.to_port = to_port
        
    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)