""" Unicode values  of alphabates A-Z are 65 -90, 
Unicode values of alphabates a-z are 97-122"""
for alpha in range(65, 91):
    print(chr(alpha), end=',')
print()
for alpha in range(122, 96, -1):
    print(chr(alpha), end=',')
