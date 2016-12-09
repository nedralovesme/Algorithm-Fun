## Write an algorithm that takes in a string and reverses all the characters in that string

#define the string
my_string = "My spoon is too big"

#split it up
splitz = my_string.split()
print splitz

#flip it
reverse = splitz[::-1]
print reverse

#put it back together
string_reversed = " ".join(reverse)

print my_string
print string_reversed
