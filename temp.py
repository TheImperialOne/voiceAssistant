# Taking plain text from user
text = input("Please enter text: ")
# Taking key from user
key = input("Please enter key: ")


# To remove duplicates from key and convert it to small case
def removeduplicate(key):
    t = ""
    for i in key:
        if (i in t):
            pass
        else:
            t = t + i
    t.lower()
    return t


# For adding bogus x to text and if text is odd add z at the end
def addingxztotext(text):
    # Lower the input text
    text = text.lower()
    # remove space if any
    text = text.replace(" ", "")
    text1 = []
    x = 'x'
    z = 'z'
    group = 0
    i = 2
    while i < len(text):
        if text[group] == text[i - 1]:
            text1.append(text[group] + x)
            group = i - 1
            i -= 1
        else:
            text1.append(text[group:i])
            group = i
        i += 2

    if len(text[group:]) == 1:
        text1.append(text[group:] + z)
    else:
        text1.append(text[group:])
    # # Converting list to string
    # text = ""
    # for i in text1:
    #     text += i + ""
    return text1


keyinmatrix = removeduplicate(key)
keyinmatrix = keyinmatrix.lower()
textinmatrix = addingxztotext(text)

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
         'x', 'y', 'z']


# Function to construct matrix
def matrixconstructor(key, list):
    matrix = []
    matrix1 = []
    for i in key:
        matrix.append(i)
    for i in list:
        if i not in matrix:
            matrix.append(i)
    # for i in  range(0,25,5):
    #     print(matrix[i:i+5])
    # matrix
    for i in range(0, 25, 5):
        matrix1.append(matrix[i:i + 5])
    return matrix1


# Constructed Matrix
matrix = matrixconstructor(keyinmatrix, list1)

for i in range(0, 5):
    print(matrix[i])


def PlayfairCipher(matrix, text):
    CipherText = []
    for i in range(0, len(text)):
        c1 = 0
        c2 = 0
        ele1x, ele1y = search(matrix, text[i][0])
        ele2x, ele2y = search(matrix, text[i][1])

        if ele1x == ele2x:
            c1, c2 = Row(matrix, ele1x, ele1y, ele2x, ele2y)
        elif ele1y == ele2y:
            c1, c2 = Column(matrix, ele1x, ele1y, ele2x, ele2y)
        else:
            c1, c2 = Box(matrix, ele1x, ele1y, ele2x, ele2y)
        Cipher = c1 + c2
        CipherText.append(Cipher)
    return CipherText


def search(matrix, pairtext):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == pairtext:
                return i, j

    pass


def Row(matrix, ele1x, ele1y, ele2x, ele2y):
    char1 = ''
    if ele1y == 4:
        char1 = matrix[ele1x][0]
    else:
        char1 = matrix[ele1x][ele1y + 1]
    char2 = ''
    if ele2y == 4:
        char2 = matrix[ele2x][0]
    else:
        char2 = matrix[ele2x][ele2y + 1]
    return char1, char2


def Column(matrix, ele1x, ele1y, ele2x, ele2y):
    char1 = ''
    if ele1x == 4:
        char1 = matrix[0][ele1y]
    else:
        char1 = matrix[ele1x + 1][ele1y]

    char2 = ''
    if ele2x == 4:
        char2 = matrix[0][ele2y]
    else:
        char2 = matrix[ele2x + 1][ele2y]

    return char2, char1


def Box(matrix, ele1x, ele1y, ele2x, ele2y):
    char1 = ''
    char2 = ''
    if ele1x > ele2x:
        char2 = matrix[ele1x][ele2y]
        char1 = matrix[ele2x][ele1y]
    else:
        char1 = matrix[ele1x][ele2y]
        char2 = matrix[ele2x][ele1y]
    return char1, char2


print(textinmatrix)
print(keyinmatrix)
CipherText = PlayfairCipher(matrix, textinmatrix)
CipherText = "".join(CipherText)
print(f"Cipher Text is : {CipherText}")
