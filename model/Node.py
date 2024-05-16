from abc import abstractmethod

from builders.ForwardBuilder import ForwardBuilder
from builders.ConstructorBuilder import ConstructorBuilder

class Node(ForwardBuilder, ConstructorBuilder):
    def __init__(self, id: str, node_category: str, node_type_index: int, node_type_name: str, name: str) -> None:
        
        self.id = id
        self.node_category = node_category
        self.node_type_index = node_type_index
        self.node_type_name = node_type_name
        self.name = name
        
        self.next_nodes = []
        self.previous_nodes = []
    
    @abstractmethod 
    def build_constructor(self):
        pass
        
    @abstractmethod  
    def build_forward(self):
        pass
    
    @classmethod
    def from_json(cls, json_data):
        copy_json_data = json_data.copy()
        node_params = json_data["node_params"]
        copy_json_data.pop("node_params")
        input = {**copy_json_data, **node_params}
        #return cls(**json_data)
        return cls(**input)