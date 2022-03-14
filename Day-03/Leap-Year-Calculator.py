year = int(input("Which year do you want to check? "))

year_mod = year % 4
year_mod_hundo = year % 100
year_mod_fourhundo = year % 400

if year_mod == 0:
    if year_mod_hundo == 0 and year_mod_fourhundo == 0:
        print("Leap year.")
    elif year_mod_hundo == 0 and year_mod_fourhundo != 0:
        print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")