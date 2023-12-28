n = 10
str = ""
for i in range(int(n/2), n, 2):
    for j in range(1, n - i, 2):
        str += " "
    for j in range(1, i + 1):
        str += "*"
    for j in range(1, n - i + 1):
        str += " "
    for j in range(1, i + 1):
        str += "*"
    str += "\n"
for i in range(n, 0, -1):
    for j in range(0, n - i):
        str += " "
    
    for j in range(1, i*2):
        str += "*"
    str += "\n"


print(str)

