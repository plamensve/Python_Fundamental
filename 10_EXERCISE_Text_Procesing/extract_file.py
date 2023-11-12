line = input()
extension = ''
file = line.split('\\')

for index, char in enumerate(line):
    if char == ".":
        for x in range(len(line[index:])):
            extension += line[index:]
            break

for word in file:
    if extension in word:
        file_name, extension = word.split('.')
        print(f"File name: {file_name}\nFile extension: {extension}")
