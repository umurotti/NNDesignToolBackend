import importlib

from model.Node import Node

# Function to import a module and create an instance from a class name
def create_node_from_module_with_JSON(module_name, class_name, json_data) -> Node:
    module = importlib.import_module(module_name)
    class_ = getattr(module, class_name)
    try:
        instance = class_.from_json(json_data)
    except AttributeError:
        print(f"Class {class_name} does not have a from_json method.")
        
    return instance