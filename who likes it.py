names = ['Jacob', 'Alex']


def likes(names):
    space = ' '
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return names[0] + space + 'likes this'
    elif len(names) == 2:
        return names[0] + space + 'and' + space + names[1] + space + 'like this'
    elif len(names) == 3:
        return names[0] + ',' + space + names[1] + space + 'and' + space + names[2] + space + 'like this'
    else:
        return names[0] + ',' + space + names[1] + space + 'and' + space + str(len(names) - 2) + space + 'others like this'
    pass


print(likes(names))