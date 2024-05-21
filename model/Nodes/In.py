from model.Node import Node

class In(Node):
    def __init__(self, id: str, node_category: str, node_type_index: int, node_type_name: str, name: str) -> None:
        Node.__init__(self, id, node_category, node_type_index, node_type_name, name)
        
    def build_constructor(self):
        pass
    
    def build_forward(self):
        pass
    