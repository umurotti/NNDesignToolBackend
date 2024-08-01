import torch
class MyClass(torch.nn.Module):
    def __init__(self):
        super().__init__()
        pass	# my_in
        self.enc_conv_one = torch.nn.Conv2d(1, 16, 3, 2, 1, 1, 1, True, 'zeros')
        self.enc_relu_one = torch.nn.ReLU(False)
        self.enc_conv_two = torch.nn.Conv2d(16, 32, 3, 2, 1, 1, 1, True, 'zeros')
        self.enc_relu_two = torch.nn.ReLU(False)
        self.residual_conv = torch.nn.Conv2d(32, 32, 3, 1, 1, 1, 1, True, 'zeros')
        pass	# my_add
        self.dec_convT_one = torch.nn.ConvTranspose2d(32, 16, 3, 2, 1, 1, 1, True, 1)
        self.dec_relu_one = torch.nn.ReLU(False)
        self.dec_convT_two = torch.nn.ConvTranspose2d(16, 1, 3, 2, 1, 1, 1, True, 1)
        self.my_sigmoid = torch.nn.Sigmoid()
        pass	# my_out
    
    def forward(self, x):
        
        x = self.enc_conv_one(x)
        
        x = self.enc_relu_one(x)
        
        x = self.enc_conv_two(x)
        
        x = self.enc_relu_two(x)
        from_enc_relu_two_to_my_add = x
        
        x = self.residual_conv(x)
        
        x = x + from_enc_relu_two_to_my_add
        
        x = self.dec_convT_one(x)
        
        x = self.dec_relu_one(x)
        
        x = self.dec_convT_two(x)
        
        x = self.my_sigmoid(x)
        
        return x
        
