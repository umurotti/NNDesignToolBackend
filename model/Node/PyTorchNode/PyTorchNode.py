from model.Node.Node import Node

class PyTorchNode(Node):
    TORCH_CALL = "torch.nn"
    
    def __init__(self, id: str, node_full_class_name: str, node_type_name: str, custom_name: str,
                 torch_call: str = None) -> None:
        super().__init__(id, node_full_class_name, node_type_name, custom_name)
        
        if torch_call is None:
            self.torch_call = self.TORCH_CALL
        else:
            self.torch_call = torch_call
            
    def build_forward(self) -> list:
        output = []
        # Iterate over the output variables of the node
        for i, out_var_i in enumerate(self.out_vars):
            # If first output variable
            if i == 0:
                processing_line = ""
                processing_line += out_var_i + f" = self.{self.custom_name}("
                
                for j, in_var_i in enumerate(self.in_vars):
                    processing_line += in_var_i
                    if j < len(self.in_vars) - 1:
                        processing_line += ", "
                    
                processing_line += ")"
                
                output.append(processing_line)
                
            # If not the first output variable
            else:
                for line in super(PyTorchNode, self).generate_variable_creation_lines():
                    output.append(line)
                
        return output