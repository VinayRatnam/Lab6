#VinayRatnam

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

def encoder(original):
    """encodes the original password into an encoded password"""
    encoded = ""
    for element in original:
        val = chr(ord(element) + 3)
        if val == ":":
            val = "0"
        elif val == ";":
            val = "1"
        elif val == "<":
            val = "2"
        encoded += val
    return

def decode(encoded_pw):
    if len(encoded_pw) != 8:
        return "Your encoded password is required to be 8 digits long."

    decoded_pw = ""

    for digit in encoded_pw:
            decoded_digit = str((int(digit) - 3) % 10)
            decoded_pw += decoded_digit

    return decoded_pw


def main():
    while True:
        #menu for the encoder/decoder
        menu()

        current = ""
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            raw = input("Please enter your password to encode: ")
            current = encoder(raw) #stores encoded password
            print("Your password has been encoded and stored!\n")

        elif menu_option == 3: #ends program
            break


if __name__ == "__main__":
    main()
