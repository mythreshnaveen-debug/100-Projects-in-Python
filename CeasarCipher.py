# Day/Project 8 -- Ceaser Cipher
# Like Project/Day 7, this project originally was built up of 2 scripts (logo.py, main.py) and was combined into 1 for GitHub convenience.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)


def ceasar(original_text, shift_amount, eord): #eord stands for encode or decode
    def encrypt(sA, t):
        newWord = ""
        for letter in original_text:
            accepted = "abcdefghijklmnopqrstuvwxyz"
            if letter not in accepted:
                newWord += letter
            else:
                index = alphabet.index(letter) + sA  # sA stands for shift amount
                index = index % 26
                newWord = newWord + alphabet[index]

        print(f"Here is the {t} text: {newWord}")
    def decrypt(): #The tutorial required me to use a decrypt function.
        encrypt(shift_amount * (0 - 1), "decrypted")
    if eord == "encode":
        encrypt(shift_amount, "encrypted")
    elif eord == "decode":
        decrypt()
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text, shift, direction)
    if input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n") == "no":
        print("Goodbye")
        break
