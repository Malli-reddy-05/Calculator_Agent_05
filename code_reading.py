# code_reading.py

def read_code(filename):
    try:
        with open(filename, "r") as file:
            code = file.read()

        print("Code read successfully!")
        print("\n--- Code ---")
        print(code)

        return code

    except FileNotFoundError:
        print("Error: File not found.")
        return None


# Example usage
filename = "example.py"

read_code(filename)