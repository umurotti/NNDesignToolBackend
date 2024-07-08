from model.Node.Node import Node
from enum import Enum

class MathOperation(Enum):
    MULTIPLY = 0
    DIVIDE = 1
    ADD = 2
    SUBTRACT = 3

class SimpleMath(Node):
    # Dictionary to map enum values to their string representations
    OPERATION_TO_STRING = {
        MathOperation.MULTIPLY: '*',
        MathOperation.DIVIDE: '/',
        MathOperation.ADD: '+',
        MathOperation.SUBTRACT: '-'
    }
    
    def __init__(self, id: str, node_full_class_name: str, node_type_name: str, custom_name: str,
                 operation: MathOperation) -> None:
        super().__init__(id, node_full_class_name, node_type_name, custom_name)
        
        self.operation = MathOperation(operation)
        
    def build_constructor(self) -> str:
        return f"pass"
            
    def build_forward(self) -> list:
        output = []
        # Iterate over the output variables of the node
        for i, out_var_i in enumerate(self.out_vars):
            # If first output variable
            if i == 0:
                processing_line = ""
                processing_line += out_var_i + f" = "
                
                for in_var_i in self.in_vars:
                   processing_line += in_var_i + " " + self.OPERATION_TO_STRING[self.operation] + " "
                # Remove the trailing operation symbol and space
                processing_line = processing_line.rstrip(" " + self.OPERATION_TO_STRING[self.operation] + " ")
                
                output.append(processing_line)
                
            # If not the first output variable
            else:
                for line in super().generate_variable_creation_lines():
                    output.append(line)
                
        return output