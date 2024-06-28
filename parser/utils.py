import importlib
import os

from model.Node import Node

# Function to import a module and create an instance from a class name
def create_node_from_module_with_JSON(json_data: dict) -> Node:
    class_name = json_data["node_type_name"]
    module_name = import_path_from_multiple_path_components("model", "Nodes", json_data["node_category"], class_name)
    module = importlib.import_module(module_name)
    class_ = getattr(module, class_name)
    try:
        instance = class_.from_json(json_data)
    except AttributeError:
        print(f"Class {class_name} does not have a from_json method.")
        
    return instance

def import_path_from_multiple_path_components(*path_components):
    # Step 1: Join the path components
    joined_path = os.path.join(*path_components)
    
    # Step 2: Replace OS-specific path separators with dots
    module_path = joined_path.replace(os.sep, '.')
    
    # Step 3: Remove the .py extension if present
    if module_path.endswith('.py'):
        module_path = module_path[:-3]
        
    return module_path

def graphify(nodes: list, connections: list):
    for connection in connections:
        for node in nodes:
            if connection.from_node == node.id:
                node.next_nodes.append(connection.to_node)
                node.out_degree += 1
            if connection.to_node == node.id:
                node.prev_nodes.append(connection.from_node)
                node.in_degree += 1