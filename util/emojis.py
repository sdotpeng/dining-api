def get_emoji(dish_name):
    """Get a emoji of food that is related to the input name of dishes

    Parameters
    ----------
    dish_name : str
        the full name of the dish

    Returns
    -------
    str
        a emoji related to the input dish
    """
    # Main dishes
    if "chicken" in dish_name:
        return "🐓"
    if "beef" in dish_name:
        return "🥩"
    if "fish" in dish_name or "cod" in dish_name or "salmon" in dish_name:
        return "🐟"
    if "shrimp" in dish_name:
        return "🦐"
    if "lobster" in dish_name:
        return "🦞"
    if "pork" in dish_name:
        return "🐖"
    if "rice" in dish_name:
        return "🍚"
    if "pho" in dish_name or "noodle" in dish_name or "noodles" in dish_name:
        return "🍜"
    if "omelette" in dish_name:
        return "🍳"
    # Main dishes that contain veg
    if "broccoli" in dish_name or "cauliflower" in dish_name:
        return "🥦"
    if "bok choy" in dish_name or "spinach" in dish_name or "asparagus" in dish_name:
        return "🥬"
    if "carrot" in dish_name:
        return "🥕"
    if "mushroom" in dish_name or "shiitake" in dish_name:
        return "🍄"
    # Fast food
    if "toast" in dish_name:
        return "🍞"
    if "fries" in dish_name or "chip" in dish_name or "tot" in dish_name or "hash" in dish_name:
        return "🍟"
    if "scramble" in dish_name or "egg" in dish_name and not "eggplant" in dish_name:
        return "🍳"
    if "dog" in dish_name or "sausage" in dish_name or "brat" in dish_name:
        return "🌭"
    if "burger" in dish_name or "cheeseburger" in dish_name:
        return "🍔"
    if "taco" in dish_name or "tortilla" in dish_name:
        return "🌮"
    if "pancake" in dish_name:
        return "🥞"
    if "falafel" in dish_name:
        return "🧆"
    if "dumpling" in dish_name or "dumplings" in dish_name:
        return "🥟"
    if "pizza" in dish_name:
        return "🍕"
    if "waffle" in dish_name:
        return "🧇"
    # Side dieshes
    if "squash" in dish_name:
        return "🎃"
    if "corn" in dish_name:
        return "🌽"
    if "onion" in dish_name:
        return "🧅"
    if "potato" in dish_name:
        return "🥔"
    if "bacon" in dish_name:
        return "🥓"
    if "cucumber" in dish_name:
        return "🥒"
    if "eggplant" in dish_name:
        return "🍆"
    if "tomato" in dish_name:
        return "🍅"
    if "pretzels" in dish_name:
        return "🥨"

    return "🥡"