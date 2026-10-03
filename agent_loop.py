# agent_loop.py

def perceive():
    """Get information from the environment."""
    temperature = int(input("Enter current temperature: "))
    return temperature


def think(temperature, goal_temperature=72):
    """Decide what action to take."""
    if temperature > goal_temperature:
        return "Cool"
    elif temperature < goal_temperature:
        return "Heat"
    else:
        return "Idle"


def act(action):
    """Perform the selected action."""
    print("Agent Action:", action)


# Agent Loop
while True:
    temperature = perceive()

    action = think(temperature)

    act(action)

    if temperature == 72:
        print("Goal reached!")
        break