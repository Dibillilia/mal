import reader, printer

def READ():
    return reader.read_str(input("user> "))

def EVAL(user_string):
    return user_string

def PRINT(output):
    print(printer.pr_str(output))

def rep():
    PRINT(EVAL(READ()))

while True:
    try:
        rep()
    except (KeyboardInterrupt, EOFError):
        print("")
        break