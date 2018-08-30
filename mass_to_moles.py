def print_mass_to_moles():
    from molar_mass_calc import molar_mass
    mass = input("How much mass is there in grams?")
    molar_mass = molar_mass()
    print()
    print("The moles of the substance are {}".format(int(mass) / molar_mass))


def mass_to_moles():
    from molar_mass_calc import molar_mass
    print("How much mass is there in grams?")
    mass = input()
    molar_mass = molar_mass()
    moles = float(mass) / molar_mass
    return moles
