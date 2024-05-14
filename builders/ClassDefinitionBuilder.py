from abc import ABC, abstractmethod

from model_code.CodeBlock import CodeBlock

class ClassDefinitionBuilder(ABC):
    
    @abstractmethod
    def build_class_definition(self) -> CodeBlock:
        pass
    