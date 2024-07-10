import torch
class MyClass(torch.nn.Module):
    def __init__(self):
        super().__init__()
        pass	# my_in
        self.my_conv1d = torch.nn.Conv1d(2, 2, 2, 1, 0, 1, 1, True, 'zeros')
        self.my_conv2d = torch.nn.Conv2d(2, 2, 2, 1, 0, 1, 1, True, 'zeros')
        self.my_conv_transpose1d = torch.nn.ConvTranspose1d(2, 2, 2, 1, 0, 0, 1, True, 1)
        self.my_conv_transpose2d = torch.nn.ConvTranspose2d(2, 2, 2, 1, 0, 0, 1, True, 1)
        self.my_relu = torch.nn.ReLU(False)
        self.my_sigmoid = torch.nn.Sigmoid()
        self.my_linear = torch.nn.Linear(2, 2, True)
        self.my_max_pool1d = torch.nn.MaxPool1d(2, 1, 0, 1, True, True)
        self.my_max_pool2d = torch.nn.MaxPool2d(2, 1, 0, 1, True, True)
        self.my_avg_pool1d = torch.nn.AvgPool1d(2, 1, 0, True, False)
        self.my_Avg_pool2d = torch.nn.AvgPool2d(2, 1, 0, True, False)
        pass	# my_mult
        pass	# my_float
        pass	# my_sub
        pass	# my_int
        pass	# my_add
        pass	# my_divide
        pass	# my_out
    
    def forward(self, x):
        
        x = self.my_conv1d(x)
        
        x = self.my_conv2d(x)
        
        x = self.my_conv_transpose1d(x)
        
        x = self.my_conv_transpose2d(x)
        
        x = self.my_relu(x)
        
        x = self.my_sigmoid(x)
        
        x = self.my_linear(x)
        
        x = self.my_max_pool1d(x)
        
        x = self.my_max_pool2d(x)
        
        x = self.my_avg_pool1d(x)
        
        x = self.my_Avg_pool2d(x)
        x = x
        
        x = x * x
        from_my_mult_to_my_add = x
        
        from_my_float_to_my_sub = 0.25
        
        x = x - from_my_float_to_my_sub
        
        from_my_int_to_my_add = 2
        
        from_my_add_to_my_divide = from_my_mult_to_my_add + from_my_int_to_my_add
        
        x = x / from_my_add_to_my_divide
        
        return x
        
