import torch
from model.Nodes.PyTorchNode import PyTorchNode

class ReLU(PyTorchNode, torch.nn.ReLU):
    
    def __init__(self, custom_name: str, inplace: bool) -> None:
        super().__init__(custom_name, torch.nn.ReLU(inplace))

        self.inplace = inplace
        
    def build_constructor(self):
        pass
    
    def build_forward(self):
        pass