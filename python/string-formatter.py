version = "1.0.0"
print("Welcome to PyCliUtils - Formatter, " + version)
print("To exit, press Ctrl+C at any time.")
formatter = input(R"Please type in your formatter string - use {} for placeholder: ")

keepAsking = True

while keepAsking == True:
    string = input("Now, enter the data that you want to format, splitted by comma: ")
    strList = string.split(",")
    strListStripped = map(str.strip,strList)
    print(formatter.format(*strListStripped))
    askAgain = input("Do you want to format any other data? [yn] ")
    if askAgain == "n":
        keepAsking = False

exit