import torch
from model.Nodes.PyTorchNode import PyTorchNode

class Conv2d(PyTorchNode, torch.nn.Conv2d):
    
    def __init__(self, custom_name: str, in_channels: int, out_channels: int, kernel_size: int, stride: int, padding: int, dilation: int, groups: int, bias: bool, padding_mode: str) -> None:
        super().__init__(custom_name, torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias, padding_mode))
        
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.groups = groups
        self.bias = bias
        self.padding_mode = padding_mode
        
    def build_constructor(self):
        pass
    
    def build_forward(self):
        pass