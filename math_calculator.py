print("Number Calculator / Converter")
print() ##INPUT YOUR INTEGERS/FLOATS ON NUM VALUES
num1 = 382
num2 = 5927
converter_num = 738
number2 = "Number two: "
print("inputted numbers:")
print(f"First input: {num1}")
print(f"Second input: {num2}")
print()
print("Converter Number:")
print(converter_num)
print()
math = num1 + num2
print("Addition Answer:")
print(f"{num1} + {num2} = {math}") ## * for multiplication / for division
print()
math = num1 * num2
print("Multiplication Answer:")
print(f"{num1} • {num2} = {math}")
print()
math = num1 / num2
print("Division Answer:")
print(f"{num1} ÷ {num2} = {math}")
print()
print("is number two higher than number one?")
print(num1 < num2)
print()
print("Are the numbers equal?")
print(num1 == num2)
print()
math = num1 * num1
print("To the power of 2:")
print(f"{num1}^2 = {math}")
print()
math = num1 * num1 * num1
print("To the the power of 3:")
print(f"{num1}^3 = {math}")
print()
math = num1 * num1 * num1 * num1
print("To the power of 4:")
print(f"{num1}^4 = {math}")
print()
math = num1 * num1 * num1 * num1 * num1
print("To the power of 5:")
print(f"{num1}^5 = {math}")
print()
print("!Next will only use converter input number!")
print()
cnvrt = converter_num / 1.609
print("Kilometer to mile")
print(f"{converter_num} -> {cnvrt}")
print()
cnvrt = converter_num * 1.609
print("Mile to kilometer")
print(f"{converter_num} -> {cnvrt}")
print()
cnvrt = converter_num * 5280
print("Mile to feet ")
print(f"{converter_num} -> {cnvrt}")
print()
cnvrt = converter_num / 2.54
print("Centimeter to inches")
print(f"{converter_num} -> {cnvrt}")
print()
cnvrt = converter_num / 5280
print("Feet to mile")
print(f"{converter_num} -> {cnvrt}")
print()
cnvrt = converter_num * 3281
print("Kilometer to feet")
print(f"{converter_num} -> {cnvrt}")
print()
cnvrt = converter_num / 3281
print("Feet to kilometer")
print(f"{converter_num} -> {cnvrt}")
print()
cnvrt = converter_num * 2.205
print("Kilogram to pound")
print(f"{converter_num} -> {cnvrt}")
print()
cnvrt = converter_num / 2.205
print("Pound to kilogram")
print(f"{converter_num} -> {cnvrt}")
print()
cnvrt = converter_num / 907.2
print("Kilogram to US ton")
print(f"{converter_num} -> {cnvrt}")
print()
cnvrt = converter_num * 907.2
print("US ton to kilogram")
print(f"{converter_num} -> {cnvrt}")