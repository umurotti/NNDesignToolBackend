import json

class JSONFacade:
    def __init__(self, in_JSON_path: str):
        self.in_JSON_path = in_JSON_path
        
        self.complex_json = None
        self.out_JSON = None
        
    def __read_JSON(self):
        # Read the JSON file
        with open(self.in_JSON_path) as JSON_file:
            self.complex_json = json.load(JSON_file)

    def simplify_json(self):
        self.__read_JSON()
        # Perform the necessary operations to simplify the JSON object
        simplified_json = {
            "connections": [],
            "nodes": []
        }

        # Extract and simplify connections
        for connection in self.complex_json['connections']:
            simplified_json['connections'].append({
                "from_node": connection['from_node'],
                "from_port": connection['from_port'],
                "to_node": connection['to_node'],
                "to_port": connection['to_port']
            })

        # Extract and simplify nodes
        for node in self.complex_json['nodes']:
            simplified_node = {
                #"id": node.get('nodeid'),
                "id": node.get('godotname'),
                "node_full_class_name": node.get('nodefullclassname'),
                "node_type_name": node['nodetypename'],
                "node_params": node.get('zdata', {}).get('nodeparams', node.get('node_params', {}))
            }
            # remove "opt" including keys from node_params
            simplified_node["node_params"] = {k: v for k,v in
                                              simplified_node["node_params"].items() if "optname" not in k}
            simplified_json['nodes'].append(simplified_node)

        return simplified_json