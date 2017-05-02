from sys import exit

def get_dict(filename):
    try:
        bd_dict = {}
        
        with open(filename, "r") as file:
            for line in file:
                s = line.strip().split(" ")
                
                bd_dict[s[0]] = s[1]

        return bd_dict

    except:
        print("Error opening file.")
        return None

def print_names(dic):
    print("Currently we have the birthdays of: ")
    for n in dic.keys():
        print(' '.join([s.capitalize() for s in n.split("_")]))

def get_birthday(dic, name):
    try:
        s = '_'.join(name.strip().lower().split(" "))
        return dic[s]
    except:
        return None


if __name__ == "__main__":
    fname = "birthdays.txt"

    bd_dict = get_dict(fname)

    if (bd_dict == None):
        exit(1)

    print_names(bd_dict)
    print("Whose birthday would you like to see?")

    inp = input("> ")

    bd = get_birthday(bd_dict, inp)

    if (bd != None):
        print("{}'s Birthday is {}".format(inp, bd))
    else:
        print("Birthday not found.")