CONVERSION_FACTOR = 0.3048


def main():
    display_title()
    running = 'y'
    while running == 'y':
        choice = display_menu()
        if choice == 'a':
            to_meters()
            running = convert_again()
        else:
            to_feet()
            running = convert_again()
    print('Thanks, bye!')


def display_title():
    print('Feet and Meters Converter')
    print()


def display_menu():
    print('Conversions Menu:')
    print('a. Feet to Meters')
    print('b. Meters to Feet')
    conversion = input('Select a Conversion (a/b): ')
    while conversion != 'a' and conversion != 'b':
        print('Invalid entry')
        conversion = input('Select a Conversion (a/b): ')
    print()
    return conversion


def to_meters():
    num_to_convert = int(input('Enter Feet: '))
    print(f'{round(num_to_convert * CONVERSION_FACTOR, 2)} meters')
    print()


def to_feet():
    num_to_convert = int(input('Enter Meters: '))
    print(f'{round(num_to_convert / CONVERSION_FACTOR, 2)} feet')
    print()


def convert_again():
    again = input('Would you like to perform another conversion? (y/n): ')
    while again != 'y' and again != 'n':
        print('Invalid answer')
        again = input('Would you like to perform another conversion? (y/n): ')
    print()
    return again


main()
