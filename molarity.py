from mass_to_moles import mass_to_moles
from input_is import *
while True:
    print("Starting with grams or moles?(grams/moles)")
    ask_1 = input()
    if ask_1.lower() == "grams":
        moles = mass_to_moles()
        break
    elif ask_1.lower() == "moles":
        print("Input moles:")
        moles = input()
        moles = input_is_decimal(moles)
        break
print("How much solution in Liters is present?")
volume = input()
volume = input_is_decimal(volume)
molarity = float(moles) / float(volume)
print(molarity)
