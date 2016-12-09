## Write a function that takes in a sentence and reverses the sentence

#define the string
my_string = "My spoon is too big"

#split it up
splitz = my_string.split()
# print splitz

#flip it
reverse = splitz[::-1]
# print reverse

#put it back together
string_reversed = " ".join(reverse)

print my_string
print string_reversed
