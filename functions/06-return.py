# Para hacer que una función entregue un valor de retorno utilizamos la palabra reservada return

def hero_phrase(hero_name):
    phrase = f"Soy el súper heroe {hero_name}"
    return phrase

superman = " Super man"
aquaman = "Aqua man"

super_phrase = hero_phrase(superman)
aqua_phrase = hero_phrase(aquaman)

print(super_phrase)
print(aqua_phrase)