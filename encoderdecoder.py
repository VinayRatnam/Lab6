#VinayRatnam

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
    return encoded


def main():
    while True:
        #menu for the encoder/decoder
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        current = ""
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            raw = input("Please enter your password to encode: ")
            current = encoder(raw) #stores encoded password
            print("Your password has been encoded and stored!")
        elif menu_option == 3:
            break


if __name__ == "__main__":
    main()
