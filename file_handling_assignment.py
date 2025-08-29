# Assignment Solution

# File Read & Write Challenge and Error Handling Lab

def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

def main():
    filename = input("Enter the filename to read: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        modified_content = modify_content(content)
        
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"File has been modified and saved as {new_filename}")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file cannot be read or written.")

if __name__ == "__main__":
    main()
