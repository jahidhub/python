text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

# w = open("writeFile.txt", "a")
# print(w.write(lorem))
# w.close()

with open("writeFiles.txt", "x") as f:
    print(f.write(text))

with open("writeFile.txt", "r") as f:
    print(f.read())
