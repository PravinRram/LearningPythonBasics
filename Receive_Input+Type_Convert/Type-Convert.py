birth_year = input('What is your birth year? ')
print(type(birth_year))

age = 2023 - int(birth_year)
print(type(age))

print(age)


# int() --> convert str into int
# float() --> convert str into float
# bool() --> convert str into boolean
#
# input is a str, so cannot calculate with str and int together
# so need to convert type of input to int to be able to calculate
