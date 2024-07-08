import torch
class MyClass(torch.nn.Module):
    def __init__(self):
        super().__init__()
        pass
        self.a = torch.nn.Conv2d(2, 2, 2, 1, 0, 1, 1, True, '0')
        self.b = torch.nn.ReLU(False)
        self.d = torch.nn.Conv2d(2, 2, 2, 1, 0, 1, 1, True, '0')
        self.e = torch.nn.Conv2d(2, 2, 2, 1, 0, 1, 1, True, '0')
        self.f = torch.nn.ReLU(False)
        self.c = torch.nn.Conv2d(2, 2, 2, 1, 0, 1, 1, True, '0')
        pass
    
    def forward(self, x):
        from_0_to_d = x
        
        x = self.a(x, )
        
        x = self.b(x, )
        from_b_to_c = x
        
        from_d_to_e = self.d(from_0_to_d, )
        
        from_e_to_f = self.e(from_d_to_e, )
        
        x = self.f(x, from_e_to_f, )
        
        x = self.c(x, from_b_to_c, )
        
        return x
        
