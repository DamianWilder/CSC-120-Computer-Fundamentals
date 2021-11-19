

def main():
    letter_dict = {}
    string = input('Enter a string: ').upper()
    for i in string:
        if i not in letter_dict and i != " " and i != ",":
            letter_dict[i] = string.count(i)
    print(letter_dict)
    chosen_letter = input('Choose a letter: ').upper()
    if chosen_letter in letter_dict:
        print(f'Frequency count of that letter: {letter_dict[chosen_letter]}')
        del(letter_dict[chosen_letter])
        print(f'Dictionary after {chosen_letter} removed: {letter_dict}')
    else:
        print(f'The letter {chosen_letter} is not in the dictionary')
    letter_list = list(letter_dict)
    letter_list.sort()
    print(f'Letters sorted: {letter_list}')


main()
