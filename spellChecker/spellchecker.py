from tqdm import tqdm
import sys

if len(sys.argv) > 1:
    fileInput = sys.argv[1]
else:
    fileInput = None

with open("words.txt", 'r') as wordsFile:
    words = wordsFile.read().splitlines()

inList = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c', 'r', 't', 'y', 'f', 'g', 'h', 'v', 'b', 'n', 'u', 'i', 'o', 'p', 'j', 'k', 'l', 'm', "'"]
outList = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13 ,14, 15 ,16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

def unconvertWord(word):
    output = []
    for letter in str(word):
        output.append(str(inList[outList.index(int(letter))]))

    return "".join(output)

def convertWord(word):
    output = []
    for letter in word:
        try:
            output.append(str(outList[inList.index(letter)]))
        except:
            pass

    return "".join(output)

def check(query):
    if not " " in query:
        if query in words:
            print(f"{query} is spelled correctly")
        else:
            queryNum = abs(int(convertWord(query)))
            minDiff = 10000000000000000  # set the initial minimum difference
            minWord = ""  # set the initial closest word
            for word, num in tqdm(wordsNumbers.items(), desc="find closest word"):  # loop over the dictionary items
                testDiff = abs(queryNum - int(num))
                if testDiff < minDiff:  # if found difference is less than the minimum difference
                    minDiff = testDiff
                    minWord = word
                    if minDiff == 0:
                        break  # if the difference is 0, found the closest word already and can exit the loop
            print(f"print {query} is actually spelled {minWord}")
    else:
        querys = query.split(" ")
        for query in querys:
            if query in words:
                print(f"{query} is spelled correctly")
                outList.append(query)
            else:
                try:
                    queryNum = abs(int(convertWord(query)))
                except:
                    pass
                minDiff = 10000000000000000  # set the initial minimum difference
                minWord = ""  # set the initial closest word
                for word, num in tqdm(wordsNumbers.items(), desc="find closest word"):  # loop over the dictionary items
                    testDiff = abs(queryNum - int(num))
                    if testDiff < minDiff:  # if found difference is less than the minimum difference
                        minDiff = testDiff
                        minWord = word
                        if minDiff == 0:
                            break  # if the difference is 0, found the closest word already and can exit the loop
                print(f"print {query} is actually spelled {minWord}")
                outputList.append(minWord)

wordsNumbers = {}
numbersWords = {}
numbers = []
for word in tqdm(words, desc="words completed"):
    converted = convertWord(word)
    wordsNumbers[word] = converted
    numbersWords[converted] = word
    numbers.append(converted)

outputFile = "output.txt"
outputList = []

if fileInput != None:
    query = "".join(open(fileInput, 'r').read().splitlines())
    check(query)

    with open(outputFile, "w") as outF:
        outF.write(" ".join(outputList))

else:
    while True:
        query = input("type a word wrong\n")
        check(query)


