vowls = ['a','e','i','o','u']
words = input("input: ")
for i in words:
    if i.lower() in vowls:
        words = words.replace(i,'')
print('output: ',words)

