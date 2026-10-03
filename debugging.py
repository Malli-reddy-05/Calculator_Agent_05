# debugging.py

DEBUG = True


def debug(message):
    if DEBUG:
        print("[DEBUG]", message)


# Example usage
debug("Agent started")

state = "thinking"
debug(f"Current state: {state}")

action = "search"
debug(f"Agent action: {action}")

state = "completed"
debug(f"Final state: {state}")