#Taking a temperature in Celsius and returning the corresponding temperature in Fahrenheit
def CelsiustoFahrenheit(Celsius):
    Fahrenheit = ((9/5) * Celsius) + 32
    return Fahrenheit

#Using the function and showing that the function works correctly
f = CelsiustoFahrenheit(0)
if f != 32:
    print("The function returned", f, "instead of 32 degrees.")
    exit()
else:
    f = CelsiustoFahrenheit(100)
    if f != 212:
        print("The function returned", f, "instead of 212 degrees.")
        exit()
    else:
        f = CelsiustoFahrenheit(-40)
        if f != -40:
            print("The function returned", f, "instead of -40 degrees.")
            exit()
        else:
            print("All the values worked.")


#Output when I ran the program:
            "All the values worked."



