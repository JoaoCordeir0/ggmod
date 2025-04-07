with open("models/LGN.spt", "rb") as f:
    data = f.read()

text = data.decode('latin1')

print(text)
print()

array = text.split('56%')
array.pop()

for item in array:
    print(item + '56%')