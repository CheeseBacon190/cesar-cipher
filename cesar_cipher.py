# cesar cypher

def encrypt(message, key):
    nA, nZ, na, nz = ord('A'), ord('Z'), ord('a'), ord('z')
    encrypted = ""

    for character in message:
        #index
        ind = ord(character)
        if (nA <= ind <= nZ):
            new_letter = chr((ind + key) % (nZ + 1) + (
                (ind + key) // (nZ + 1)) * nA)
            # replace the letter with the new_letter in the message
            encrypted += new_letter

        elif (ind in range(na, nz + 1)):
            new_letter = chr((ind + key) % (nz + 1) + (
                (ind + key) // (nz + 1)) * na)
            encrypted += new_letter

        else:
            encrypted += character

    return encrypted


def decrypt(messagem, key):
    return encrypt(messagem, -key)


