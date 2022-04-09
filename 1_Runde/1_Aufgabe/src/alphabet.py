abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def a_():
    return abc

def c_(i):
    return abc[i]

def i_(c):
    try:
        return abc.index(c)
    except Exception as e:
        return None

def d_(d):
    if d:
        return "right"
    return "left"
