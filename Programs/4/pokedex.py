import string

# Pokemon class. Defines what makes a pokemon and allows the user to create said pokemon
class Pokemon:
    def __init__(self, name, number, cp, types):
        self.number = number # Pokedex number
        self.name = name
        self.cp = cp         # total combat points
        self.types = types   # list of all types

    # __str__ defines the string representation of a Pokemon
    def __str__(self):
        type_str = self.types[0]
        # for each additional type, add a separator
        for i in range(1, len(self.types)):
            type_str += " and " + self.types[i]
        return "Number: " + str(self.number) + ", Name: " + self.name + ", HP: " + str(self.cp) + ", types: " + type_str

# ---------------------------------------
# Pokedex functions
# ---------------------------------------

def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist[0])               # number
        name = pokelist[1]                      # name
        combat_points = int(pokelist[2])        # hit points
        types = []
        for position in range(3, len(pokelist)):
            types += [pokelist[position]]       # type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex

# how_many_combat_points outputs the total number of combat points in the Pokedex
def average_hit_points(pokedex):
    totCP = 0
    count = 0
    for pkmn in pokedex:
        count += 1
        totCP += pkmn.cp
    totCP = totCP / count
    totCP = round(totCP,2)
    print("Average Pokemon combat points = ", totCP)

# how_many_pokemon prints how many pokemon are in the pokedex
def total_by_type(pokedex, poke_type):
    count = 0
    for i in range(len(pokedex)):
        if(poke_type in pokedex[i].types):
            count+=1
    print('Number of Pokemon that contain type', poke_type, "=", count)

# lookup_name looks through the given pokedex for a pokemon named the given name
def lookup_by_name(pokedex, name):
    for pkmn in pokedex:
        if pkmn.name.lower() == name:
            print(pkmn)
            return
    print("No Pokemon named", name, "is in the Pokedex")

# lookup_number looks through the given pokedex for a pokemon logged at the given number
def lookup_by_number(pokedex, number):
    for pkmn in pokedex:
        if pkmn.number == number:
            print(pkmn)
            return
    print("Pokemon number", number, "is not in the Pokedex")

# print_pokedex prints each pokemon in the given pokedex
def print_pokedex(pokedex):
    print("\nThe Pokedex")
    print("-------------")
    for pokemon in pokedex:
        print(pokemon)
    print("-------------")

# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# print_menu outputs all the user's options
def print_menu():
    print()
    print("1. Print Pokedex")
    print("2. Print Pokemon by Name")
    print("3. Print Pokemon by Number")
    print("4. Count Pokemon with Type")
    print("5. Print Average Pokemon Combat Points")
    print("6. Quit")

# ---------------------------------------

def main():
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ").lower()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            pokemon_type = input("Enter a Pokemon type: ").lower()
            total_by_type(pokedex, pokemon_type)
        elif choice == 5:
            average_hit_points(pokedex)
        elif choice == 6:
            print("Thank you.  Goodbye!")
        print()


main()
