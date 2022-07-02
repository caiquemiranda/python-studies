# reverse sorting of strings
# use in terminal

# numbers
x = [7, 8, 9, 4, 6, 5, 10]
x.sort(reverse=True)
print(x)
# [10, 9, 8, 7, 6, 5, 4]

# strings
x = 'abcd'
x.sort(x, reverse=True)
print(x)
# ['d', 'c', 'b', 'a']

x = 'abcd'
x = ''.join(sorted(x, reverse=True))
print(x)
# dbca