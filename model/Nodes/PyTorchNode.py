from model.Node import Node

class PyTorchNode(Node):
    TORCH_CALL = "torch.nn"
    
    def __init__(self, id: str, node_category: str, node_type_index: int, node_type_name: str, name: str, torch_call: str = None) -> None:
        super().__init__(id, node_category, node_type_index, node_type_name, name)
        
        if torch_call is None:
            self.torch_call = self.TORCH_CALL
        else:
            self.torch_call = torch_call