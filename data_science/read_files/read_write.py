with open("data.txt","r")as f1:
    with open("file1.txt","w") as f2:
        f2.write(f1.read())
