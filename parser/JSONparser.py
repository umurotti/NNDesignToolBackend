from model.Model import Model
from model.Node import Node
from model.Connection import Connection

from parser.utils import create_node_from_module_with_JSON

import json

class JSONparser:
    def __init__(self, JSON_path: str):
        self.json_path = JSON_path
        self.data = json.load(open(self.json_path))
        
        self.JSON_connections = self.data['connections']
        self.JSON_nodes = self.data['nodes']
        
        self.connections = []
        self.nodes = []

    def parse(self):
        for JSON_node in self.JSON_nodes:
            try:
                node_type_name = JSON_node['node_type_name']
            
                #DEBUG
                if node_type_name == "Conv2d":
                    node_category = JSON_node['node_category']
                    node_params = JSON_node
                    self.nodes.append(self.instantiate_node(node_category, node_type_name, node_params))
            finally:
                pass
            
        for JSON_connection in self.JSON_connections:
           self.connections.append(self.instantiate_connection(JSON_connection))
            
        return self.connections, self.nodes
    
    def create_model(self) -> Model:
        pass
    
    def instantiate_node(self, node_category: str, node_type_name: str, node_params: list) -> Node:
        return create_node_from_module_with_JSON(f'model.Nodes.{node_category}.' + node_type_name, node_type_name, node_params)

    def instantitate_connection(self, connection_params: list) -> Connection:
        return Connection(*connection_params)
    
    