from abc import ABC
from model.Node import Node

class PyTorchNode(Node):
    TORCH_CALL = "torch.nn"
    
    def __init__(self, custom_name:str, torch_call: str) -> None:
        super().__init__()
        
        self.custom_name = custom_name
        
        if torch_call is None:
            self.torch_call = self.TORCH_CALL
        else:
            self.torch_call = torch_call