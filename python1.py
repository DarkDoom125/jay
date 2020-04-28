weight = int(input("Weight: "))
unit = int(input("lbs or kg: "))
if unit.lower == "lbs":
    calc = weight * 0.45
    print(calc)
else:
    calc = weight / 0.45
    print(calc)

