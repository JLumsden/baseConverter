#Dictionary of values
decToRepValues = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
repToDecValues = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F": 15}
#Decimal to any base convert function
def decimalToRep(value, base):
    converted = ""
    remainder = 0
    while value > 0:
        remainder = value % base
        value = value // base
        converted = decToRepValues[remainder] +  converted
    print(converted)
    return(converted)
#Any base to decimal convert function
def repToDecimal(value, base):
    converted = 0
    exponent = len(value) - 1
    for ch in value:
        converted += repToDecValues[ch] * base ** exponent
        exponent -= 1
    print(converted)
    return converted
#User input
decision = int(input('Press "0" to convert a decimal value to any base.\nPress "1" to convert a value to decimal.'))
if decision == 0:
    decimalToRep(int(input("Enter the number you would like to convert: ")), int(input("Enter the base you would like to convert to: ")))
elif decision == 1:
    repToDecimal(input("Values may only contain 0-9 and CAPITAL A-F.\nInput your value: "),int(input("Base may only be digits.\nInput your base: ")))
else:
    print("You just had to make it difficult, huh?")
