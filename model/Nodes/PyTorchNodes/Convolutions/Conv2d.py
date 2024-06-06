import torch
from model.Nodes.PyTorchNode import PyTorchNode

class Conv2d(PyTorchNode):
    
    def __init__(self, id: str, node_category: str, node_type_index: int, node_type_name: str, name: str,
                 in_channels: int, out_channels: int, kernel_size: int, stride: int, padding: int, dilation: int, groups: int, bias: bool, padding_mode: str) -> None:
        PyTorchNode.__init__(self, id, node_category, node_type_index, node_type_name, name)
        # needed since torch.nn.Conv2d gives " Parameter containing:tensor([-0.0801, -0.1518]"
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.groups = groups
        self.bias = bias
        self.padding_mode = padding_mode
        
    def build_constructor(self) -> str:
        return f"self.{self.name} = torch.nn.Conv2d({self.in_channels}, {self.out_channels}, {self.kernel_size}, {self.stride}, {self.padding}, {self.dilation}, {self.groups}, {self.bias}, \'{self.padding_mode}\')"
    
    def build_forward(self):
        pass