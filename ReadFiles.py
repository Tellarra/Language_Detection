import glob
listText = []

def getTexts(inputUser) :
    #inputUser = input("Enter the name of the folder you want to search in: ")
    #print(inputUser)
    mypath = "DataSet/Train/" + inputUser + "/*.txt"
    #print(mypath)
    listText = glob.glob(mypath)

    count = 0
    for text in listText :
        textSplit = text.split("/")
        listText[count] = textSplit[3]
        count += 1

    return listText, inputUser

def getTextsTest() :
    #inputUser = input("Enter the name of the folder you want to search in: ")
    #print(inputUser)
    mypath = "DataSet/Test/*.txt"
    #print(mypath)
    listText = glob.glob(mypath)

    count = 0
    for text in listText :
        textSplit = text.split("/")
        listText[count] = textSplit[2]
        count += 1

    return listText
