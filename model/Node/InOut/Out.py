from model.Node.Node import Node

class Out(Node):
    def __init__(self, id: str, node_full_class_name: str, node_type_name: str, custom_name: str,) -> None:
        Node.__init__(self, id, node_full_class_name, node_type_name, custom_name)
        
    def build_constructor(self) -> str:
        return "pass"
    
    def build_forward(self) -> str:
        return "pass"
    