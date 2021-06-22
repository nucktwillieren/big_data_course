cm = float(input("cm: "))

inch = cm / 2.54 
inch_mod = inch % 12
feet = inch // 12

print(f"{cm}(cm) = {feet} feet and {inch_mod:.3} inch")