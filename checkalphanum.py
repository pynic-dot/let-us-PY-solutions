# Count alpha and numeric in this string 'Nagput-440010'
s = 'Nagpur-4405854646010'
alpha, num = 0, 0
for x in range(len(s)):
    if s[x].isalpha():
        alpha += 1
    elif s[x].isdigit():
        num += 1
    else:
        pass
print("Total number of alpha is {}".format(alpha))
print("Total number of numeric in string is : {}".format(num))
