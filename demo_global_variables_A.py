global out_a


def funA():
    global inner_a
    inner_a = out_a
    private_a = "i'm private"


def funB():
    # Need to declare the variable as global in each scope where they are
    # being modified!
    global inner_a
    inner_a += 1
    print inner_a
    # No need to declare the variable when it is used as full path name
    GlobalA.class_a += '1'
    print GlobalA.class_a
    # Also no need to declare if you do not want to modify the value here
    print main_a


class GlobalA(object):
    # What's the meaning using global declare here, seems the same to local
    # variable when called by full path
    global class_a

if __name__ == "__main__":
    out_a = 1
    GlobalA.class_a = 'class_a'
    # It seems the same as declare the global variable `out_a', both are
    # modular scope
    main_a = 'main_a'
    funA()
    funB()
    funB()
