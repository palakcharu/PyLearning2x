# Strings -> bunch of character -> represented by "" or ''

name = "Palak"
name2 = "Palak Jain"
print(name)
print(name2)

print(type(name))
print(type(name2))

#dir = "C://abc.de"
# dir = 'C://abc.de'
# dir = 'C:\abc.txt'
# \a for space
# dir = "C:\nbc.txt"
# \n for new line

# to use \a and \n in a dir path we can add r(r stand for raw) in the starting of dir path
dir = r"C:\nbc.txt"
print(dir)

# format String
first_name = "Palak"
last_name = "Jain"
print(f"your name is {first_name}{last_name}")

