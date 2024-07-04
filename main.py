import sys
from parser.JSONparser import JSONparser

def main():
    #input_file_path = "test_json/test1.1_edit.json"
    #input_file_path = "test_json/test_old.json"
    input_file_path = "test_json/crit0.json"
    
    try:
        # Parse the JSON data from the input file
        parser = JSONparser(input_file_path, use_facade=True)
        
        # Print the parsed JSON data
        print(parser.parse())
        
        model = parser.create_model()
        print(model)
        
        topological_order = model.topological_sort('khan')
        model.set_topological_order(topological_order)
        print("topological order:", model.topological_order)
        
        critical_path = model.find_critical_path()
        model.set_critical_path(critical_path)
        print("critical path:", model.critical_path)
        
        code = model.generate_model_code()
        code.save_script()
        
        

    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    main()