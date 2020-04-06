word = 'диван'  # Искомое слово

inp = open('11.txt').readlines()
with open('file.txt', 'r') as file:
    filedata = file.read()

for i in iter(inp):
    if word in i:
        inp = inp.replace('диван', 'говно')
        with open('11.txt', 'w') as file:
            file.write(i)