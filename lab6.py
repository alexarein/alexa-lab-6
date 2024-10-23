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

def decode_password(password):
    encoded_password = ""
    for char in password:
        if char.isdigit():
            new_digit = (int(char) - 3) % 10
            encoded_password += str(new_digit)
        else:
            encoded_password += char
    return encoded_password

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
            password = input("Enter password to decode:")
            password = decode_password(password)
            print("\nYour password:" + password)


        elif menu_option == "3":
            break

        else:
            print("Please enter a valid option.")

if __name__ == "__main__":
    main()






