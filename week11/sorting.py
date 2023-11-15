# Example 6

def main():
    # Create a list that contains country names
    # and print the list.
    countries = [
        "Canada", "France", "Ghana", "Brazil", "Japan"
    ]
    print(countries)

    # Sort the list. Then print the sorted list.
    sorted_list = sorted(countries)
    print(sorted_list)


# Call main to start this program.
if __name__ == "__main__":
    main()
# Example 7

def main():
    # Create a list that contains data about countries.
    countries = [
        # [country_name, land_area, population, gdp_per_capita]
        ["Mexico", 1972550, 126014024, 21362],
        ["France",  640679,  67399000, 45454],
        ["Ghana",   239567,  31072940,  7343],
        ["Brazil", 8515767, 210147125, 14563],
        ["Japan",   377975, 125480000, 41634]
    ]

    # Print the unsorted list.
    print("Original unsorted list of countries")
    for country in countries:
        print(country)
    print()

    # Define a lambda function that will be used as the
    # key function by the sorted function. The lambda
    # function extracts the population data from a
    # country so that the population will be used for
    # sorting the list of countries.
    POPULATION_INDEX = 2
    popul_func = lambda country: country[POPULATION_INDEX]

    # Sort the list of countries by the population.
    sorted_list = sorted(countries, key=popul_func)

    # Print the sorted list.
    print("List of countries sorted by population")
    for country in sorted_list:
        print(country)


# Call main to start this program.
if __name__ == "__main__":
    main()

# Example 8

def main():
    # Create a list that contains data about young students.
    students = [
        # [given_name, surname, reading_level]
        ["Robert", "Smith", 6.7],
        ["Annie", "Smith", 6.2],
        ["Robert", "Lopez", 7.1],
        ["Sean", "Li", 5.6],
        ["Sofia", "Lopez", 5.3],
        ["Lily", "Harris", 6.7],
        ["Alex", "Harris", 5.8]
    ]

    GIVEN_INDEX = 0
    SURNAME_INDEX = 1

    # Define a lambda function that combines
    # a student's surname and given name.
    combine_names = lambda student_list: \
        f"{student_list[SURNAME_INDEX]}, {student_list[GIVEN_INDEX]}"

    # Sort the list by the combined key of surname, given_name.
    sorted_list = sorted(students, key=combine_names)

    # Print the list.
    for student in sorted_list:
        print(student)


# Call main to start this program.
if __name__ == "__main__":
    main()