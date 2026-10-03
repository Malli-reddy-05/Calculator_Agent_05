# safety_limit.py

MAX_ACTIONS = 5


def safety_limit(action_count):
    if action_count >= MAX_ACTIONS:
        return False
    return True


# Example usage
action_count = 0

for i in range(8):
    if safety_limit(action_count):
        action_count += 1
        print(f"Action {action_count}: Allowed")
    else:
        print("Safety limit reached. Action stopped.")
        break