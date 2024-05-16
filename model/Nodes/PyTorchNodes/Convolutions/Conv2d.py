import torch
from model.Nodes.PyTorchNode import PyTorchNode

class Conv2d(PyTorchNode, torch.nn.Conv2d):
    
    def __init__(self, id: str, node_category: str, node_type_index: int, node_type_name: str, name: str,
                 in_channels: int, out_channels: int, kernel_size: int, stride: int, padding: int, dilation: int, groups: int, bias: bool, padding_mode: str) -> None:
        PyTorchNode.__init__(self, id, node_category, node_type_index, node_type_name, name)
        torch.nn.Conv2d.__init__(self, in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias, padding_mode)
        
    def build_constructor(self):
        pass
    
    def build_forward(self):
        pass