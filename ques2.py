with open("file.txt") as f:
    content = f.read()
    if("twinkle"in content):
        print("yes")
    else:
        print("no")    