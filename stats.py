#!/usr/bin/env python

def getStats(inputFileName):
    import os
    assert(os.path.exists(inputFileName))
    data = []
    ifile = open(inputFileName, "r")
    for (index, string) in enumerate(ifile):
        data.append(float(string.strip()))
    ifile.close()
    stats = {}
    for i in range(len(data)):
        if (not data[i] in stats.keys()):
            stats[data[i]] = 1
        else:
            stats[data[i]] += 1
    return stats

def main():
    import os
    import sys

    if (len(sys.argv) != 2):
        print "input file name = sys.argv[1]. "
        return -1

    inputFileName = sys.argv[1]
    stats = getStats(inputFileName)
    ofile = open("stats.txt", "w")
    for key in stats.keys():
        ofile.write(str(key) + "  " + str(stats[key]) + "\n")
    ofile.close()

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
