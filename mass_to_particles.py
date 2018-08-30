from molar_mass_calc import molar_mass
mass = input("How much mass is there in grams?")
molar_mass = molar_mass()
moles = int(mass) / molar_mass
print(str(moles * 6.02214 * 10 ** 23) + ' particles are present in the sample.')
