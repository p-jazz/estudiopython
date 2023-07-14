recipe_to_search = input("Dime tu receta")

recipes = {
    "pollo arvejado": "lavar los trozos de pollo "
}

if recipe_to_search in recipes:
    print(f"Si está la receta de {recipe_to_search}")
    print(f"La rceta es {recipes[recipe_to_search]}")
else:
    print(f"Receta no encontrada {recipe_to_search}")