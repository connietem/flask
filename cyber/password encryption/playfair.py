def matrix(key):
    mat= []
    for e in key.upper():
        if e not in mat:
            mat.append(e)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for e in alphabet:
        if e not in mat:
            mat.append(e)
    matrix_group = []
    for e in range(5):
        matrix_group.append('')
    matrix_group[0] = mat[0:5]
    matrix_group[1] = mat[5:10]
    matrix_group[2] = mat[10:15]
    matrix_group[3] = mat[15:20]
    matrix_group[4] = mat[20:25]
    return matrix_group

def pairing(message_o):
    message = []
    for e in message_o:
        message.append(e)
    for unused in range(len(message)):
        if " " in message:
            message.remove(" ")
    i = 0
    for e in range(int(len(message) / 2)):
        if message[i] == message[i + 1]:
            message.insert(i + 1, 'X')
        i = i + 2

    if len(message) % 2 == 1:
        message.append("X")

    i = 0
    new = []
    for x in range(1, int(len(message) / 2 + 1)):
        new.append(message[i:i + 2])
        i = i + 2
    return new


def find_pos(key_matrix, letter):
    x = y = 0
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                x = i
                y = j

    return x, y


def encrypt(message):
    message = pairing(message)
    key_matrix = matrix(key)
    cipher = []
    for e in message:
        p1, q1 = find_pos(key_matrix, e[0])
        p2, q2 = find_pos(key_matrix, e[1])
        if p1 == p2:
            if q1 == 4:
                q1 = -1
            if q2 == 4:
                q2 = -1
            cipher.append(key_matrix[p1][q1 + 1])
            cipher.append(key_matrix[p1][q2 + 1])
        elif q1 == q2:
            if p1 == 4:
                p1 = -1
            if p2 == 4:
                p2 = -1
            cipher.append(key_matrix[p1 + 1][q1])
            cipher.append(key_matrix[p2 + 1][q2])
        else:
            cipher.append(key_matrix[p1][q2])
            cipher.append(key_matrix[p2][q1])
    return cipher


def cpairing(cipher):
    i = 0
    new = []
    for x in range(int(len(cipher) / 2)):
        new.append(cipher[i:i + 2])
        i = i + 2
    return new


def decrypt(cipher):
    cipher = cpairing(cipher)
    key_matrix = matrix(key)
    text = []
    for e in cipher:
        p1, q1 = find_pos(key_matrix, e[0])
        p2, q2 = find_pos(key_matrix, e[1])
        if p1 == p2:
            if q1 == 0:
                q1 = 5
            if q2 == 0:
                q2 = 5
            text.append(key_matrix[p1][q1 - 1])
            text.append(key_matrix[p1][q2 - 1])
        elif q1 == q2:
            if p1 == 0:
                p1 = 5
            if p2 == 0:
                p2 = 5
            text.append(key_matrix[p1 - 1][q1])
            text.append(key_matrix[p2 - 1][q2])
        else:
            text.append(key_matrix[p1][q2])
            text.append(key_matrix[p2][q1])

    for unused in range(len(text)):
        if "X" in text:
            text.remove("X")

    output = ""
    for e in text:
        output += e
    return output.lower()

key = input("Please input the key : ")
message = input("Please input the message : ")
message=message.upper()
cipher=encrypt(message)
print("Encrypted message is:")
print(cipher)
decipher=decrypt(cipher)
print("The decrypted message is:")
print(decipher)