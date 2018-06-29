#Write a function that will convert a JSON-formatted string to a dictionary. 
# For instance, the function will take this string as a parameter:

def main():
    jsonFile = open('sample.json').read() #this is open the json file and reading it
    parse = eval(jsonFile) #this evaluates the json file and makes the string into different data types
    # print(jsonFile)
    result(**parse) #this is "parsing" the entered JSON-Formatted string and formating it in to

def result(**args):
    if len(args):
        for x in args:
            print('result["{}"] = "{}"'.format(x, args[x]))
    return result

if __name__ == '__main__': main()

####################################


# def main():
#     jsonFile = open('sample.json').read()
#     parse = eval(jsonFile)
#     # print(jsonFile)
#     newDictionary(parse)

# def newDictionary(o):
#     for x in o:
#         print('Result["{}"] = "{}"'.format(x, o[x]))

# if __name__ == '__main__': main()

####################################################

# def main():
#     jsonFile = {'totalCount':'1',
#                 'ID':'1029',
#                 'IP':'10.0.0.1'}
#     newDictionary(**jsonFile)

# def newDictionary(**kwargs):
#     if len(kwargs):
#         for k in kwargs:
#             print('Result["{}"] = "{}"'.format(k, kwargs[k]))
#     else: print('No result!')

# if __name__ == '__main__': main()
    