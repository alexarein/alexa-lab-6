def print_menu(): #create menu list
    print("Menu")
    print("-" * 13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode_password(password):
    encoded = ""
    for digit in password: # add 3 to each digit
        new_digit = (int(digit) + 3) % 10
        encoded += str(new_digit)
    return encoded



def main():
    encoded_password = ""

    while True:
        print_menu()
        # prompt use for input
        menu_option = input("Please enter and option: ")

        if menu_option == "1":
            encoded_password = input("Please enter your password to encode: ")
            encoded_password = encode_password(encoded_password)
            print("Your password has been encoded and stored!")

        elif menu_option == "2":
            # my partner will fill the rest

        elif menu_option == "3":
            break

        else:
            print("Please enter a valid option.")

if __name__ == "__main__":
    main()






