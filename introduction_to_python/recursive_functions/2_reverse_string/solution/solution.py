def reverse(string):
    if len(string)==0:
        return ""
    return string[-1] + reverse(string[:-1])