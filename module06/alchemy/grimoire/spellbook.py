def record_spell(spell_name: str, ingredients: str) -> str:
    try:
        import alchemy.grimoire.validator as validator
        validation_result = validator.validate_ingredients(ingredients)
        if validation_result[-7:] == "INVALID":
            return f"Spell rejected: {spell_name} ({validation_result})"
        return f"Spell recorded: {spell_name} ({validation_result})"
    except (ModuleNotFoundError, ImportError):
        return "An import error occured"
