str = "asdsadувуцвцувцууss"
str2 = "asdsadsdsadasdewdwedew"

if len(str) > 10:
    str = str[:6]
elif len(str) < 12:
    str += 'o'*(12-len(str))
print(str)