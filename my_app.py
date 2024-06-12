import random

def rock_paper_scissors_lizard_spock(choice: str) -> str:
    """
    Recieves a choice as a string: rock, paper, scissors, lizard, spock. 
    And the computer will choose, randomly, another play. The winner is given by the following rules:

    scissors cuts paper
    paper covers rock
    rock crushes lizard
    lizard poisons spock
    spock smashes scissors
    scissors decapitates lizard
    lizard eats paper
    paper disproves spock
    spock vaporizes rock
    (and as it always has) rock crushes scissors
    """
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    if choice not in choices:
        return "Invalid choice! Choose one of: rock, paper, scissors, lizard, spock."

    computer_choice = random.choice(choices)
    
    outcomes = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }
    
    if choice == computer_choice:
        result = "It's a tie!"
    elif computer_choice in outcomes[choice]:
        result = f"You win! {choice} beats {computer_choice}."
    else:
        result = f"You lose! {computer_choice} beats {choice}."
    
    return f"Player chose: {choice}\nComputer chose: {computer_choice}\n{result}"

# Tests:
# print("Executing tests...")
# print(rock_paper_scissors_lizard_spock("rock"))
# print(rock_paper_scissors_lizard_spock("spock"))
# print(rock_paper_scissors_lizard_spock("lizard"))


def Wordle():
    """
    (ESPAÑOL)
    Es un juego que consiste en adivinar la palabra de 5 letras, teniendo un número
    limitado de intentos para realizarlo, en este caso serán seis oportunidades.

    En cada ronda el juego pinta cada letra de un color indicando si esa letra
    se encuentra o no en la palabra y si se encuentra en la posición correcta.

    1. VERDE significa que la letra está en la palabra y en la posición CORRECTA.
    2. AMARILLO significa que la letra letra está presente en la palabra
       pero en la posición INCORRECTA.
    3. GRIS significa que la letra letra NO está presente en la palabra.


    (ENGLISH)
    [pronta traducción]
    """
    # listado de palabras de 5 letras
    palabras = [
    'barco', 'arbol', 'dulce', 'perro', 'sueño',
    'queso', 'piano', 'mujer', 'cielo', 'lavar',
    'aguas', 'polar', 'hojas', 'libro', 'plata',
    'hogar', 'fruta', 'carne', 'playa', 'suelo',
    'reloj', 'feliz', 'raton', 'niños', 'nubes',
    'marco', 'libre', 'verde', 'forma', 'sobre',
    'silla', 'talco', 'haber', 'menos', 'pared',
    'techo', 'gente', 'hojas', 'impar', 'ilusa',
    'joyas', 'carta', 'grupo', 'circo', 'koala',
    'danza', 'hielo', 'ñoqui', 'noche', 'miedo',
    'otoño', 'oliva', 'obvio', 'usted', 'unico',
    'watts', 'kiwis', 'nexos', 'torax', 'yerba',
    'yerno', 'yelmo', 'ayuda', 'mayor', 'zonas',
    'zurda', 'zumba', 'sorda', 'quita', 'lanza',
    'danza', 'quien', 'aquel', 'entre', 'calle',
    'flujo', 'sabor', 'plomo', 'clase', 'chile',
    'facil', 'dolor', 'denso', 'punto', 'preso',
    'copia', 'flota', 'metro', 'trigo', 'juego',
    'valor', 'nieto', 'cerca', 'feria', 'tarta',
    'grito', 'botin', 'mango', 'enano', 'fresa'
]

    palabra_oculta = random.choice(palabras) # selecciona una palabra al azar
    intentos = 6 # número de intentos
    letras_palabra = 5 # longitud de la palabra (contiene 5 letras)

    print("¡Bienvenido a <Wordle> en español!")
    print("Adivina la palabra oculta de 5 letras en un máximo de 6 intentos.")

    for intento in range(1, intentos + 1):
        while True:
            intento_palabra = input(f"Intento {intento}: ").lower()
            if intento_palabra.isalpha():
                break

            else:
                print("Por favor, introduzca una palabra válida.")

        # si encuentra la palabra,
        if intento_palabra == palabra_oculta:
            print(f"¡CORRECTOOO!👏 La palabra era {palabra_oculta}, lograste descubrirla en {intento} intentos.")
            return
        
            

        # con esto indicamos la cantidad de letras correctas/incorrectas para el usuario
        cuadritos = []
        for i in range(letras_palabra):
            if len(intento_palabra) == 5:
                if intento_palabra[i] in palabra_oculta:
                    if intento_palabra[i] == palabra_oculta[i]:
                        cuadritos.append('🟩')
                    elif intento_palabra[i] != palabra_oculta[i]:
                        cuadritos.append('🟨')
                else:
                    cuadritos.append('⬛')  # letra que no está en la palabra
            else:
                print("¡OJO! La palabra debe tener 5 letras. Perdiste un intento. 🤦‍♂️🤦‍♀️")
                break

        print("".join(cuadritos))

    print(f"La palabra era <{palabra_oculta}>, lamentablemente no la adivinaste.😔")
#Wordle()

# Let's define constant values for word chains that may repeat
menu_opt = "\n--- Game Menu ---\n1. Play Rock, Paper, Scissors, Lizard, Spock\n2. Play Wordle (in Spanish)\n3. Get out"
undefined_option = "Invalid input. Please, choose 1, 2 o 3."
bye_bye = "See you soon!"

def main_menu():
    """
    This function displays the main menu.
    Allows the user to choose between playing one of the two games or exiting the menu
    """
    while True:
        print(menu_opt)
        choice = input("Choose an option (1, 2, 3): ")
        if choice == '1':
            user_choice = input("Choose: rock, paper, scissors, lizard, spock: ").lower()
            try:
                result = rock_paper_scissors_lizard_spock(user_choice)
                print(result)
            except NameError:
                print("Undefined option, Try again.")
        elif choice == '2':
            wordle()
        except NameError:
            print("Undefined wordle option.")
        elif choice == '3':
            print(bye_bye)
            break
        else:
            print(undefined_option)

if __name__ == "__main__":
    main_menu()

