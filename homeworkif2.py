def my_func(firstline, secondline):
    if type(firstline) != str or type(secondline) != str:
        return 0
    if firstline == secondline:
        return 1
    if len(firstline) > len(secondline):
        return 2
    if firstline != secondline and secondline == 'learn':
        return 3

print(my_func('segf', 'sa'))
print(my_func(4, 'python'))
print(my_func('python', 'savage'))
print(my_func('segf', 'learn'))

