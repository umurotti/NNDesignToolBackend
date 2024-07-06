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
        
        code = model.generate_model_code()
        code.save_script()
        
        

    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    main()