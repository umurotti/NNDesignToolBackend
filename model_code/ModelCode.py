from model_code.CodeBlock import CodeBlock
class ModelCode:
    def __init__(self, imports:CodeBlock, class_definition:CodeBlock, constructor:CodeBlock, forward:CodeBlock) -> None:
        self.imports = imports
        self.class_definition = class_definition
        self.constructor = constructor
        self.forward = forward

    def generate_imports(self, model):
        pass
    
    def generate_class_definition(self, model):
        pass
    
    def generate_constructor(self, model):
        pass
    
    def generate_forward(self, model):
        pass
    
    def save_script(imports:CodeBlock, class_definition:CodeBlock, constructor:CodeBlock, forward:CodeBlock, path:str):
        pass
        
    
    
    