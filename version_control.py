# Ryan_Froug


def main():
    print_menu()
    encoded = ""

    # Menu loop
    while True:
        option = input("Please enter an option: ")
        if option == '1':
            # Takes password and stores encoded input
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
        elif option == '2':
            # Shows user encoded and decoded string
            print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}.")
        elif option == '3':
            break
        print_menu()


# Function to print menu text
def print_menu():
    print("Menu")
    print("-" * 13)
    print("1. Encode\n"
          "2. Decode\n"
          "3. Quit")


def encode(string):
    encoded_string = ""
    for c in string:
        # Takes char and adds 3 (modulo if number is greater than 10)
        encoded_string += str((int(c) + 3) % 10)
    return encoded_string


def decode(string):
    # TO-DO: create decode function
    pass


if __name__ == "__main__":
    main()
