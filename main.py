import sys
from parser.JSONparser import JSONparser

def main():
    input_file_path = "test_json/test1.1_edit.json"

    try:
        # Parse the JSON data from the input file
        parser = JSONparser(input_file_path)

        # Process the JSON data as needed
        # TODO: Add your code here to process the JSON data
        
        # Print the parsed JSON data
        print(parser.parse())
        
        model = parser.create_model()
        print(model)
        
        topological_sort = model.topological_sort('khan')
        model.set_topological_order(topological_sort)
        print(model.topological_order)
        
        code = model.generate_model_code()
        code.save_script()
        
        

    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    main()