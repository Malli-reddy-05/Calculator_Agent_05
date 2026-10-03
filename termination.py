# termination.py

def should_terminate(state, goal_reached):
    if state == "completed":
        return True

    if goal_reached:
        return True

    return False


# Example usage
state = "completed"
goal_reached = True

if should_terminate(state, goal_reached):
    print("Agent terminated.")
else:
    print("Agent is still running.")