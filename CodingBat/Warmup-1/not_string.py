def not_string(str):
    if len(str) < 3 or str[0:3] != "not":
        return_string = "not " + str
        return return_string
    else:
        return str
