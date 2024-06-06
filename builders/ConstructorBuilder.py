from abc import ABC, abstractmethod

from model_code.CodeBlock import CodeBlock

class ConstructorBuilder(ABC):
    
    @abstractmethod
    def build_constructor(self) -> str:
        pass
    