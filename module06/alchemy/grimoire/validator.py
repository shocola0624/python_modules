def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = [
        "fire",
        "water",
        "earth",
        "air"
    ]
    ingredients_list = ingredients.split(" ")
    if len(ingredients_list) == 0:
        return f"{ingredients} - INVALID"
    for i in ingredients_list:
        if i not in valid_ingredients:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
