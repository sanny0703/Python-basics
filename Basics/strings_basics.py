# Here, we learn the basics of strings in python


#  Multiline Strings
multiline_string = """Hello
This is a multiline string
Also, notice that line breaks are exactly like in code"""

# Let's try to print it to see the line breaks
print(multiline_string)

# Strings as arrays
array_string = "SanjayKumar"

print("First Element", array_string[0])
print("Last Element", array_string[len(array_string) - 1])

# Now, let's loop through
for ch in array_string:
    print(type(ch))
    print(ch)

# we can search for a part or pattern in a string
pattern_string = "Sanjay Kumar Uppala"
# check for presence
print("Kum" in pattern_string)

# check for absence
print("San" not in pattern_string)

# string slicing
slice_string = "Hello, How are you doing these days"

# from n to m-1
print(slice_string[2:5])
# from 0 to m-1
print(slice_string[:5])
# from n to len-1
print(slice_string[2:])
# from n th last to m+1 th last
print(slice_string[-5:-1])