'''This code convert all word in a string into capitalize mode'''

s = "an inferior lawyer with dubious practices"
print(" ".join([x.capitalize() for x in s.split(" ")]))
