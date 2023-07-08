def temperature_scale():
    print("Celsius = 0C")
    print("Fahrenheit = 32F")
    print("kelvin = 273k")
    print("0C=32F=273K")

    celsius=float(input("Enter the celsius: "))
    fahrenhit=float(input("Enter the fahrenheit: "))
    kelvin=float(input("Enter the kelvin: "))

    cel=(fahrenhit - 32)*5/9
    print("The celsius is, ", cel"C")

    fahr=celsius*9/5 + 32
    print("The fahrenheit is, " , fahr"F")

    kel=celsius + 273
    print("The kelvin is, ",kel "K")


