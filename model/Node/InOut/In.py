from model.Node.Node import Node

class In(Node):
    def __init__(self, id: str, node_full_class_name: str, node_type_name: str, custom_name: str) -> None:
        Node.__init__(self, id, node_full_class_name, node_type_name, custom_name)
        
    def build_constructor(self) -> str:
        return f"pass\t# {self.custom_name}"
    
    def build_forward(self) -> list:
        output = []
        # Iterate over the output variables of the node
        for i, out_var_i in enumerate(self.out_vars):
            # If first output variable
            if i == 0:
                continue
            # If not the first output variable
            else:
                for line in super().generate_variable_creation_lines():
                    output.append(line)
                
        return output
    