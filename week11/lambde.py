# Example 1

def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = []
    for fahr in fahr_temps:
        cels = cels_from_fahr(fahr)
        cels_temps.append(cels)

    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")


def cels_from_fahr(fahr):
    """Convert a Fahrenheit temperature to
    Celsius and return the Celsius temperature.
    """
    cels = (fahr - 32) * 5 / 9
    return round(cels, 1)


# Call main to start this program.
if __name__ == "__main__":
    main()

# Example 2

def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = list(map(cels_from_fahr, fahr_temps))

    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")


def cels_from_fahr(fahr):
    """Convert a Fahrenheit temperature to
    Celsius and return the Celsius temperature.
    """
    cels = (fahr - 32) * 5 / 9
    return round(cels, 1)


# Call main to start this program.
if __name__ == "__main__":
    main()

# Example 4

def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Define a lambda function that converts
    # a Fahrenheit temperature to Celsius and
    # returns the Celsius temperature.
    cels_from_fahr = lambda fahr: round((fahr - 32) * 5 / 9, 1)

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = list(map(cels_from_fahr, fahr_temps))
    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = list(map(
            lambda fahr: round((fahr - 32) * 5 / 9, 1),
            fahr_temps))

    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")


# Call main to start this program.
if __name__ == "__main__":
    main()