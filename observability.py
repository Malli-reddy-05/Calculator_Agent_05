# observability.py

def log_event(event, details):
    print(f"[LOG] {event}: {details}")


def show_agent_status(state, action_count):
    print("\n--- Agent Status ---")
    print("State:", state)
    print("Actions:", action_count)
    print("--------------------")


# Example usage
log_event("Agent Started", "Agent is running")

state = "thinking"
action_count = 1

show_agent_status(state, action_count)

log_event("Action Completed", "Agent completed one action")

state = "completed"
action_count = 2

show_agent_status(state, action_count)