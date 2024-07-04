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