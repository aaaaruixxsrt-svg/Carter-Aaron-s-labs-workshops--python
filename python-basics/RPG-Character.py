def create_character(name, strength, intelligence, charisma):
    # Validate name
    if not isinstance(name, str):
        return "The character name should be a string."
    if name == "":
        return "The character should have a name."
    if len(name) > 10:
        return "The character name is too long."
    if " " in name:
        return "The character name should not contain spaces."


    # Validate stats are integers
    stats = [strength, intelligence, charisma]
    if not all(isinstance(s, int) for s in stats):
        return "All stats should be integers."
    
    # Validate stats range
    if not all(s >= 1 for s in stats):
        return "All stats should be no less than 1."
    if not all(s <= 4 for s in stats):
        return "All stats should be no more than 4."
    
    # Validate total points
    if sum(stats) != 7:
        return "The character should start with 7 points."


    # Create stats lines
    def format_stat(label, value):
        return f"{label} " + "●" * value + "○" * (10 - value)


    result = f"{name}\n"
    result += format_stat("STR", strength) + "\n"
    result += format_stat("INT", intelligence) + "\n"
    result += format_stat("CHA", charisma)


    return result



print(create_character('carter', 4, 2, 1))

