# utils.py

def add_ingredient_quantities(instructions, ingredients):
    """
    Takes a list of instructions and ingredients.
    Searches the instruction text for ingredient names and appends the quantity.
    """
    updated_instructions = []
    
    for instruction in instructions:
        instruction_text = instruction.text  # Start with the raw instruction text

        # Search and replace ingredient names with quantity in parentheses
        for ingredient in ingredients:
            if ingredient.name.lower() in instruction_text.lower():
                # Case-insensitive replacement and appending the amount
                instruction_text = instruction_text.replace(
                    ingredient.name,
                    f"{ingredient.name} ({ingredient.unit_text})"
                )

        # Store the updated instruction text
        updated_instructions.append({
            'step': instruction.step,
            'text': instruction_text
        })
    
    return updated_instructions
