def encrypt(s, k):
    ls = list(s)

    aux = ""
    for letter in ls:
        if not letter.isalpha():
            aux += letter
        elif letter.isupper():
            aux += chr((ord(letter) + k-65) % 26 + 65)
        elif letter.islower():
            aux += chr((ord(letter) + k-97) % 26 + 97)
    
    print(aux)