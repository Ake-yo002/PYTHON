# PART 1:FILE MODIFICATION
# Read from aboutnicole.txt and write modified version
try:
    # Open file in read mode (automatically closes when done)
    with open("aboutnicole.txt", "r") as file:
        data = file.read()

        #My simple modification will be adding stars around my texts and making them upper case.
        modification = f"** {data.upper()} **"
    # Create new file (or overwrite if exists) with modified content
    with open("modified_aboutnicole.txt" , "w") as file:
        file.write(modification)
    print("The file is modified successfully")


except FileNotFoundError:  # Specific error: missing file
    print("Error: aboutnicole.txt not found")
except Exception as e: # Catch-all for other errors like permission issues
    print(f"Error processing the file: {str(e)}")

# PART 2: USER FILE HANDLING
# Prompt user for filename and read its content
filename = input("Enter the name of file you want to read: ")

try:
     # Attempt to read and print the user-specified file
    with open(filename, "r") as file:
        print(file.read())# Display file content directly
        
except FileNotFoundError: # Specific error: missing file
    print(f"Error: {filename} doesn't exist")
except Exception as e:  # Other read errors like a corrupted file
    print(f"Error reading file: {str(e)}")