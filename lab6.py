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

def decode_password(encoded_password):
    decoded = ""
    for digit in encoded_password: # subtract 3 from each digit
        new_digit = (int(digit) - 3) % 10
        decoded += str(new_digit)
    return decoded

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
            decoded_password = decode_password(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        elif menu_option == "3":
            break

        else:
            print("Please enter a valid option.")

if __name__ == "__main__":
    main()






