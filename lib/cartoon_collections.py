def roll_call_dwarves(names):
    for i, name in enumerate(names, start=1):
        print(f"{i}. {name}")

def summon_captain_planet(planeteer_calls):
    new_list = [call.title() + "!" for call in planeteer_calls]
    return new_list

def long_planeteer_calls(call_list):
    if any(len(call) > 4 for call in call_list):
        return True
    return False

def find_the_cheese(string_list):
    for string in string_list:
        if string == "cheese" or string == "cheddar":
            return string
    return None
           
        
