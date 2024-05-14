from builders.ImportsBuilder import ImportsBuilder
from model_code.CodeBlock import CodeBlock

class BaseImports(ImportsBuilder):
    
    def __init__(self, class_name: str, extends: str) -> None:
        super().__init__()
        self.imports = []
        
    def build_imports(self) -> CodeBlock:
        return CodeBlock().add_line(f"from abc import ABC, abstractmethod").add_line(f"from model_code.CodeBlock import CodeBlock")
        