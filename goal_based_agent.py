def goal_based_agent(current_temperature, goal_temperature=72):

    if current_temperature > goal_temperature:
        return "Cool"

    elif current_temperature < goal_temperature:
        return "Heat"

    else:
        return "Idle"


# Test temperatures
temperatures = [90, 80, 72, 60, 50]

for temp in temperatures:
    action = goal_based_agent(temp)

    print("Temperature:", temp, "F")
    print("Agent Action:", action)
    print()