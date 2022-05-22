students = {
    'kemi' : [54, 64, 88, 72, 65],
    'lukman' : [71, 82, 76, 59, 91],
    'femi' : [23, 32, 43, 84, 23],
    'johnson' : [32, 98, 67, 81, 77]
}

dict = {len(name): name for name in students.keys()}
maxlen = max(dict.keys())
print(maxlen)
print('{:<14}{:<12}{:<12}{:<12}{:<12}{:<12}'.format('name\n\subject', 'mathematics',
                               'chemistry', 'physics', 'biology', 'english' ))
for name, (a, b, c, d, e) in students.items():
    print('{:<14}{:<12}{:<12}{:<12}{:<12}{:<12}'.format(name, a, b, c, d, e))



