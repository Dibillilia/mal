def READ():
    return input("user> ")

def EVAL(user_string):
    return user_string

def PRINT(output):
    print(output)

def rep():
    PRINT(EVAL(READ()))

while True:
    try:
        rep()
    except (KeyboardInterrupt, EOFError):
        print("")
        break