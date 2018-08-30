def print_molar_mass():
    from elements import ELEMENTS
    cont = True
    molecule = []
    print("""Hello and welcome to the Molar Mass Calculator. This program calculates the molar mass of any particle. 
    It asks you one by one for each element in the molecule. Give it an atomic number, symbol or direct name for the element you want to add. 
    It will then ask for the amount of that atom in the molecule. 
    It will keep asking until you tell it that you don't have another element to add.""")
    while cont:
        atom = input("Which atom do you want to add?")
        atom = ELEMENTS[atom]
        num_atom = input("How many of the {} atom are in the particle?".format(atom))
        condition = num_atom.isdigit()
        if not condition:
            while not condition:
                num_atom = input("Numeric integers only, please try again.")
                condition = num_atom.isdigit()
        tot_atom_mass = atom.mass * int(num_atom)
        molecule.append(tot_atom_mass)
        cont = input("Do you have another atom to add?(yes/no or y/n)")
        if cont.lower() == "yes" or cont.lower() == "y" or cont.lower() == "yea" or cont.lower() == "yeah" or cont.lower() == "yep":
            cont = True
        elif cont.lower() == "no" or cont.lower() == "n" or cont.lower() == "nope" or cont.lower() == "nah":
            cont = False

    final_value = sum(molecule)
    print()
    print("The total molar mass of the particle given is {} mol".format(final_value))

def molar_mass():
    from elements import ELEMENTS
    cont = True
    molecule = []
    print("""Now we need to find the molar mass of the substance.
    Follow the steps below.""")
    while cont:
        print("Which atom do you want to add?")
        atom = input()
        if atom.isdigit():
            atom = int(atom)
        atom = ELEMENTS[atom]
        print("How many of the {} atom are in the particle?".format(atom))
        num_atom = input()
        condition = num_atom.isdigit()
        if not condition:
            while not condition:
                print("Numeric integers only, please try again.")
                num_atom = input()
                condition = num_atom.isdigit()
        tot_atom_mass = atom.mass * int(num_atom)
        molecule.append(tot_atom_mass)
        print("Do you have another atom to add?")
        cont = input()
        if cont.lower() == "yes" or cont.lower() == "y" or cont.lower() == "yea" or cont.lower() == "yeah" or cont.lower() == "yep":
            cont = True
        elif cont.lower() == "no" or cont.lower() == "n" or cont.lower() == "nope" or cont.lower() == "nah":
            cont = False

    final_value = sum(molecule)
    return final_value
