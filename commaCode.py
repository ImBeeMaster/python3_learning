def f_list (listArg):
    for i in range(len(listArg) - 1):
        listArg[i] = listArg[i] + ','
    listArg[-1] = "and " + listArg[-1]
    string_v = ''
    for i in range(len(listArg)):
        string_v += listArg[i]
        if i == len(listArg) - 1:
            break
        string_v += ' '
    return string_v

spam = ['apples', 'bananas', 'tofu', 'cats']
string_i = f_list(spam)

print (string_i)