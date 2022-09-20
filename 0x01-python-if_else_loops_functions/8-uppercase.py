#!usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) > 65 and ord(letter) < 91:
            print(letter, end="")
        elif letter == " ":
            print(letter, end="")
        else:
            print((chr(ord(letter)-32)), end="")
