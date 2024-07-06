from model.Node.Node import Node
from model.Variable import Variable
from model_code.ModelCode import ModelCode

class Model:
    def __init__(self, nodes: list, connections: list) -> None:
        self.nodes = nodes
        self.connections = connections
        
        # Set the input and output nodes
        self.in_node = self.__get_in_node__()
        self.out_node = self.__get_out_node__()
        
        # Create a hash map for the nodes
        self.node_hash_map = self.__create_hash_map()
        
        # Fill the previous and next nodes for each node
        self.__graphify__()
        
        # Find the topological order of the nodes
        self.topological_order = self.__topological_sort__()
        
        # Find the critical path in the graph
        self.critical_path = self.__find_critical_path__()
        
        # Mark the critical nodes in the graph
        self.__mark_critical_nodes__()
        
        self.model_code = None

    def generate_model_code(self) -> ModelCode:
        code = ModelCode()
        
        # 1. Add imports
        code.add_imports()
        # 2. Add class definition
        code.add_class_definition()
        # 3. Add constructor
        code.add_constructor(self)
        # 4. Add forward
        code.add_forward(self)
        
        return code
    
    def __topological_sort__(self, mode='khan') -> list:
        
        def khan(start_node: Node):
            """
            Kahn's algorithm for topological sorting of nodes in a directed acyclic graph (DAG).

            Returns:
            list: A list of nodes in topologically sorted order if the graph is a DAG.
                If the graph contains a cycle, the function will return None.
            """
            # L: List that will contain the sorted elements
            L = []
            # S: List of all nodes with no incoming edge
            S = []

            # Create a copy of in_degree to avoid modifying the original
            in_degree_copy = {node.id: node.in_degree for node in self.nodes}

            # Initialize S with start node
            S.append(start_node)

            # while S is not empty
            while S:
                # remove a node n from S
                n = S.pop()
                # add n to L
                L.append(n)
                
                # for each node m with an edge from n to m
                for m in n.next_nodes:
                    # decrement the in-degree of m in the copy
                    in_degree_copy[m.id] -= 1
                    # if m has no other incoming edges then
                    if in_degree_copy[m.id] == 0:
                        # insert m into S
                        S.append(self.node_hash_map[m.id])

            if len(L) == len(self.nodes):
                return L  # a topologically sorted order
            else:
                return None  # Graph has a cycle
        
        def dfs():
            pass
        
        if mode == 'khan':
            return khan(self.in_node)
        elif mode == 'dfs':
            return dfs(self.in_node)
        else:
            return None
    
    def __find_critical_path__(self) -> list:
        """
        Find the critical path in a directed acyclic graph (DAG) using the topological order of the nodes.
        
        Parameters:
        None
        
        Returns:
        list: A list of nodes that form the critical path in the graph.
        
        Description:
        The critical path is the longest path in the graph from the input node to the output node.
        This path is used to determine the maximum time it will take to complete the process.
        The critical path is calculated by finding the longest path from the input node to the output node.
        """
        
        # Initialize the critical path
        critical_path = []
        
        # Find the topological order of the nodes
        if self.topological_order == []:
            self.topological_order = self.topological_sort()
        
        # If the topological order is None, the graph contains a cycle
        if self.topological_order is None:
            return None
        
        # Initialize the distance to each node as 0
        distance = {node.id: 0 for node in self.nodes}
        predecessor = {node.id: None for node in self.nodes}
        
        # Iterate over the nodes in topological order
        for node in self.topological_order:
            # Iterate over the next nodes of the current node
            for next_node in node.next_nodes:
                # Update the distance to the next node
                if distance[next_node.id] < distance[node.id] + 1:
                    distance[next_node] = distance[node.id] + 1
                    predecessor[next_node] = node.id
        
        # Find the node with the maximum distance (end node of the critical path)
        end_node = max(distance, key=distance.get)
        
        # Backtrack to find the nodes that form the critical path
        while end_node is not None:
            critical_path.insert(0, self.node_hash_map[end_node.id])
            end_node = predecessor[end_node.id]
        
        return critical_path
    
    def set_model_code(self, model_code):
        self.model_code = model_code
      
    def __create_hash_map(self) -> dict:
        hash_map = {}
        for node_i in self.nodes:
            hash_map[node_i.id] = node_i
        
        return hash_map
    
    def __graphify__(self):
        for connection in self.connections:
            # Find the node with the ID of the from_node in the connection
            from_node = self.node_hash_map.get(connection.from_node)
            if from_node is None:
                print(f"Node with ID {connection.from_node} not found.")
                return
                
            # Find the node with the ID of the to_node in the connection
            to_node = self.node_hash_map.get(connection.to_node)
            if to_node is None:
                print(f"Node with ID {connection.to_node} not found.")
                return
            
            # Add the connection to the nodes
            from_node.next_nodes.append(to_node)
            from_node.out_degree += 1
            
            to_node.prev_nodes.append(from_node)
            to_node.in_degree += 1
    
    def __mark_critical_nodes__(self):
        for crit_node in self.critical_path:
            crit_node.set_critical(True)
            
    def __fill_variables__(self):
        # Add the critical variable to the input and output nodes
        for crit_node_i in self.critical_path:
            var_to_add = Variable("x", "x", is_critical=True)
            crit_node_i.in_vars.insert(0, var_to_add)
            crit_node_i.out_vars.insert(0, var_to_add)
        
        # Iterate over the nodes in topological order
        for node_i in self.topological_order:
            # Iterate over the next nodes of the current node
            for node_j in node_i.next_nodes:
                pass
    
    def __str__(self) -> str:
        return f"Model with {len(self.nodes)} nodes and {len(self.connections)} connections."
    
    def __get_in_node__(self):
        for node in self.nodes:
            if node.node_type_name == 'In':
                return node
            
    def __get_out_node__(self):
        for node in self.nodes:
            if node.node_type_name == 'Out':
                return node
            
