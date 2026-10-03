# state_tracking.py

class AgentState:
    def __init__(self):
        self.state = "start"
        self.action_count = 0

    def update_state(self, new_state):
        self.state = new_state

    def add_action(self):
        self.action_count += 1

    def show_state(self):
        print("Current State:", self.state)
        print("Action Count:", self.action_count)


# Example usage
agent = AgentState()

agent.show_state()

agent.update_state("thinking")
agent.add_action()
agent.show_state()

agent.update_state("acting")
agent.add_action()
agent.show_state()

agent.update_state("completed")
agent.show_state()