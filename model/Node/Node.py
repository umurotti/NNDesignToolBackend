from abc import abstractmethod

from builder.ForwardBuilder import ForwardBuilder
from builder.ConstructorBuilder import ConstructorBuilder
from model.Variable import Variable

from typing import Self

class Node(ForwardBuilder, ConstructorBuilder):
    def __init__(self, id: str, node_full_class_name: str, node_type_name: str, custom_name: str) -> None:
        
        self.id = id
        self.node_full_class_name = node_full_class_name
        self.node_type_name = node_type_name
        self.custom_name = custom_name
        
        self.next_nodes = []
        self.prev_nodes = []
        
        self.in_vars = []
        self.out_vars = []
        
        self.in_degree = 0
        self.out_degree = 0
        
        self.is_critical = False
    
    @abstractmethod 
    def build_constructor(self) -> str:
        pass
        
    @abstractmethod  
    def build_forward(self) -> str:
        pass
    
    def __str__(self):
        return f"{self.custom_name}\tis_critical:{self.is_critical}"
    
    def set_critical(self, is_critical):
        self.is_critical = is_critical
        var_tmp = Variable("x", "x", is_critical=True)
        # if the node is critical, the input and output variables MUST include x
        self.in_vars.insert(0, var_tmp)
        self.out_vars.insert(0, var_tmp)
        
    @classmethod
    def from_json(cls, json_data):
        copy_json_data = json_data.copy()
        node_params = json_data["node_params"]
        copy_json_data.pop("node_params")
        input = {**copy_json_data, **node_params}
        
        return cls(**input)