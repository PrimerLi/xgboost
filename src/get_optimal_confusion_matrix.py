#!/usr/bin/env python

def read_F1(inputFileName):
    import os
    assert(os.path.exists(inputFileName))
    theta = []
    F1 = []
    ifile = open(inputFileName, "r")
    for (index, string) in enumerate(ifile):
        tempArray = string.strip('\n').split()
        theta.append(float(tempArray[0]))
        F1.append(float(tempArray[1]))
    ifile.close()
    return theta, F1

def get_max_F1(F1):
    max_F1 = F1[0]
    max_index = 0
    for i in range(1, len(F1)):
        if (max_F1 < F1[i]):
            max_F1 = F1[i]
            max_index = i
    return max_index, max_F1

def get_optimal_confusion_matrix(F1_file_name, confusion_matrix_file_name):
    import os

    assert(os.path.exists(F1_file_name))
    assert(os.path.exists(confusion_matrix_file_name))

    theta, F1 = read_F1(F1_file_name)
    max_index, max_F1 = get_max_F1(F1)
    ifile = open(confusion_matrix_file_name, "r")
    for i in range(max_index):
        string1 = ifile.readline()
        string2 = ifile.readline()
        string3 = ifile.readline()
        null = ifile.readline()
    
    string1 = ifile.readline()
    string2 = ifile.readline()
    string3 = ifile.readline()
    max_theta = float(string1.split()[2])
    true_negative, false_negative = map(float, string2.split())
    false_positive, true_positive = map(float, string3.split())
    ifile.close()
    print "Optimal theta: ", max_theta
    print "Optimal F1: ", max_F1
    print "Optimal confusion matrix: "
    print true_negative, false_negative
    print false_positive, true_positive
    capture_rate = true_positive/(true_positive + false_negative)
    incorrect_slay_rate = false_positive/(false_positive + true_positive)
    print "Capture rate: ", capture_rate
    print "Incorrect slay rate: ", incorrect_slay_rate
    ofile = open("final_resuts.txt", "w")
    ofile.write("Optimal theta: " + str(max_theta) + "\n")
    ofile.write("Optimal F1: " + str(max_F1) + "\n")
    ofile.write(str(true_negative) + "  " + str(false_negative) + "\n")
    ofile.write(str(false_positive) + "  " + str(true_positive) + "\n")
    ofile.write("Capture rate: " + str(capture_rate) + "\n")
    ofile.write("Incorrect slay rate: " + str(incorrect_slay_rate) + "\n")
    ofile.close()
    return true_negative, false_negative, false_positive, true_positive

def main():
    import sys
    if (len(sys.argv) != 3):
        print "F1_file_name = sys.argv[1], confusion_matrix_file_name = sys.argv[2]. "
        return -1

    F1_file_name = sys.argv[1]
    confusion_matrix_file_name = sys.argv[2]
    get_optimal_confusion_matrix(F1_file_name, confusion_matrix_file_name)
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
