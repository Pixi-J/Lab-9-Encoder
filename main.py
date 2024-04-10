# Github is confusing asf
while True:
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")

    men_opt = int(input("Please enter an option: "))

    if men_opt == 1:
        password = input("Please enter your password to encode: ")
        encoded = ''
        for digit in list(password):
            encoded_digit = int(digit) + 3
            encoded += str(encoded_digit)
        print("Your password has been encoded and stored!\n")

    if men_opt == 2:
        pass

    if men_opt == 3:
        break
