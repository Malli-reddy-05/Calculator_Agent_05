# error_handling.py

def safe_action(action):
    try:
        result = action()
        print("Action successful:", result)
        return result

    except Exception as e:
        print("Error occurred:", e)
        return None


# Example function
def divide_numbers():
    a = 10
    b = 0
    return a / b


# Example usage
safe_action(divide_numbers)