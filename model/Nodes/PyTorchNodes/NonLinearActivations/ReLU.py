import torch
from model.Nodes.PyTorchNode import PyTorchNode

class ReLU(PyTorchNode, torch.nn.ReLU):
    
    def __init__(self, id: str, node_category: str, node_type_index: int, node_type_name: str, name: str,
                inplace: bool) -> None:
        PyTorchNode.__init__(self, id, node_category, node_type_index, node_type_name, name)
        torch.nn.ReLU.__init__(self, inplace)
        
    def build_constructor(self):
        pass
    
    def build_forward(self):
        pass