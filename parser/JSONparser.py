from model.Model import Model
from model.Node import Node
from model.Nodes.In import In
from model.Nodes.Out import Out
from model.Nodes.PyTorchNodes.Convolutions.Conv2d import Conv2d
from model.Nodes.PyTorchNodes.NonLinearActivations.ReLU import ReLU
from model.Connection import Connection


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
            node_category = JSON_node['nodecategory']
            node_type_name = JSON_node['nodetypename']
            node_params = JSON_node['zdata']['nodeparams']
            
            self.nodes.append(self.instantiate_node(node_category, node_type_name, node_params))
            
        for JSON_connection in self.JSON_connections:
           self.connections.append(self.instantiate_connection(JSON_connection))
            
        return self.connections, self.nodes
    
    def create_model() -> Model:
        pass
    
    def instantiate_node(node_category: str, node_type_name: str, node_params: list) -> Node:
        match node_category:
            case 'INOUT':
                
                match node_type_name:
                    case 'IN':
                        return In(*node_params)
                    case 'OUT':
                        return Out(*node_params)
                    case _:
                        raise ValueError('Invalid node type')
                
            case 'nnnode':
                
                match node_type_name:
                    case 'Conv2d':
                        return Conv2d(*node_params)
                    case 'ReLU':
                        return ReLU(*node_params)
                    case _:
                        raise ValueError('Invalid node type')
                
            case _:
                raise ValueError('Invalid node category')
    
    def instantitate_connection(connection_params: list) -> Connection:
        return Connection(*connection_params)
    
    