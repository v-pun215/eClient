import os
with open('check.txt') as f:
    content = f.read()
    if content == '0':
        os.system("python main.py")
        f = open("check.txt", "w")
        f.write("1")
        f.close()
    else:
        pass
