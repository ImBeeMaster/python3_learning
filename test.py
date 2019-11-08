def pangram_test(arg1):
    test_str = arg1
    pan_list = []
    for s in range(len(test_str)-1, -1, -1):
        pan_list += test_str[s]
        pan_str = ''.join(pan_list)
    if pan_str.lower() == test_str.lower():
        print("It is a pangram")
    else:
        print("It is not! a pangram")
a = input("Enter a string:> ")
pangram_test(a)


    if set(b).issubset(a):