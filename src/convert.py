def listToString(myList):
    result = str(myList[-1]) + " "
    for i in range(len(myList)-1):
        result = result + str(i) + ":" + str(myList[i]) + " "
    return result

def main():
    import os
    import sys
    if (len(sys.argv) != 3):
        print "inputFileName = sys.argv[1], outputFileName = sys.argv[2]. "
        return -1
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    numberOfFeatures = 0
    ifile = open(inputFileName, "r")
    ofile = open(outputFileName, "w")
    for (index, string) in enumerate(ifile):
        string = string.strip()
        if (index == 0):
            a = string.split(",")
            numberOfFeatures = len(a)
        else:
            a = string.split(",")
            result = listToString(a)
            ofile.write(result + "\n")
    ofile.close()
    ifile.close()
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
