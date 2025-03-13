filename = input("Enter a file name: ")

try:
    with open(filename, "r") as file:
        for line in file:
            print(line.strip().upper())  # Convert to uppercase and remove extra spaces
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
