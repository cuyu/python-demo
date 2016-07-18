from demo_global_variables_A import funA, funB

if __name__ == '__main__':
    # The called method will only find variables in its python file(modular
    # scope), it cannot see the variable defined in another file.
    # Question is how can i make it see?
    out_a = 1
    funA()
    funB()
