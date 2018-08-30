from elements import ELEMENTS
from input_is import *
MMes = {}

while True:
    total_perc = 0
    print("Add an element?(no if done)")
    elem = input()
    if elem.isdigit():
        elem = int(elem)
    elif elem.lower() == "no" or elem.lower() == "n" or elem.lower() == "nope" or elem.lower() == "nah":
        break
    elem = ELEMENTS[elem]
    print('Percent by mass of {} present in sample:'.format(elem.name))
    while True:
        perc = input()
        perc = input_is_decimal(perc)
        if float(perc) <= 0:
            print("Tsk tsk try again:")
        elif float(perc) <= 1:
            perc = float(perc)
            break
        else:
            perc = float(perc) / 100
            break
    MMes.setdefault(elem.name, [elem.mass, perc])
    total_perc += perc
    if total_perc == 1:
        print("You are at 100%. Finishing calculation...")
        break
    elif total_perc > 1:
        print("You've exceeded 100%! Now you have to start over.")
        MMes = {}
print(MMes)
