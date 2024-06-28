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
        simplified_json = {}

        # Extract the required data from the complex JSON object
        simplified_json['data'] = self.complex_json['data']
        simplified_json['metadata'] = self.complex_json['metadata']

        # Convert the simplified JSON object to a string
        simplified_json_str = json.dumps(simplified_json)

        return simplified_json_str