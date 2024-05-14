from abc import abstractmethod

from builders.ForwardBuilder import ForwardBuilder
from builders.ConstructorBuilder import ConstructorBuilder

class Node(ForwardBuilder, ConstructorBuilder):
    def __init__(self, name: str, node_category: str, node_type_index: int, node_type_name:str,
                 next_nodes: list, previous_nodes: list) -> None:
        super().__init__()
        
        self.name = name
        self.node_category = node_category
        self.node_type_index = node_type_index
        self.node_type_name = node_type_name
        
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
        return cls(**json_data)