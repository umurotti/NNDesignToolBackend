from model.Node.Node import Node
from enum import Enum

class Type(Enum):
    STRING = 0
    INT = 1
    FLOAT = 2

class Value(Node):
    
    def __init__(self, id: str, node_full_class_name: str, node_type_name: str, custom_name: str,
                 type: Type, value) -> None:
        super().__init__(id, node_full_class_name, node_type_name, custom_name)
        
        self.type = Type(type)
        self.value = value
    
    def build_constructor(self) -> str:
        return f"pass\t# {self.custom_name}"
    
    def build_forward(self) -> list:
        output = []
        # Iterate over the output variables of the node
        for i, out_var_i in enumerate(self.out_vars):
            # If first output variable
            if i == 0:
                processing_line = ""
                processing_line += out_var_i + f" = {self.value}"
                
                output.append(processing_line)
                
            # If not the first output variable
            else:
                for line in super().generate_variable_creation_lines():
                    output.append(line)
                
        return output