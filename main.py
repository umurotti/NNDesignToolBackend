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
        print(topological_sort)

    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    main()