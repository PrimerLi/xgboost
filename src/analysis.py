#!/usr/bin/env python

def get_labels(inputFileName):
    import os
    assert(os.path.exists(inputFileName))
    labels = []
    ifile = open(inputFileName, "r")
    for (index, string) in enumerate(ifile):
        if (index == 0):
            continue
        else:
            labels.append(float(string.split(',')[-1]))
    ifile.close()
    return labels

def read_labels(inputFileName):
    import os
    import sys

    assert(os.path.exists(inputFileName))
    labels = []
    ifile = open(inputFileName, "r")
    for (index, string) in enumerate(ifile):
        a = string.split(',')
        labels.append(float(a[-1]))
    ifile.close()

    return labels

def get_confusion_matrix(labels, predictions, theta):
    import numpy as np
    assert(len(labels) == len(predictions))
    true_negative = 0.0
    false_negative = 0.0
    false_positive = 0.0
    true_positive = 0.0
    for i in range(len(labels)):
        if (labels[i] == 0 and predictions[i] < theta):
            true_negative += 1.0
        if(labels[i] == 0 and predictions[i] > theta):
            false_positive += 1.0
        if(labels[i] == 1 and predictions[i] < theta):
            false_negative += 1.0
        if(labels[i] == 1 and predictions[i] > theta):
            true_positive += 1.0
    confusion_matrix = np.zeros((2,2))
    confusion_matrix[0,0] = true_negative
    confusion_matrix[0,1] = false_negative
    confusion_matrix[1,0] = false_positive
    confusion_matrix[1,1] = true_positive
    return confusion_matrix

def get_stat(confusion_matrix):
    true_positive = confusion_matrix[1,1]
    false_negative = confusion_matrix[0,1]
    false_positive = confusion_matrix[1,0]
    true_negative = confusion_matrix[0,0]
    eps = 1.0e-10
    precision = (true_positive + eps)/(true_positive + false_positive + eps)
    tpr = true_positive/(true_positive + false_negative)
    fpr = false_positive/(false_positive + true_negative)
    recall = tpr
    return tpr, fpr, precision

def printFile(x, y, outputFileName):
    assert(len(x) == len(y))
    ofile = open(outputFileName, "w")
    for i in range(len(x)):
        ofile.write(str(x[i]) + "    " + str(y[i]) + "\n")
    ofile.close()

def matrixTOString(matrix):
    assert(len(matrix) == 2)
    assert(len(matrix[0]) == 2)
    return str(matrix[0,0]) + "   " + str(matrix[0,1]) + "\n" + str(matrix[1,0]) + "    " + str(matrix[1,1]) + "\n"

def printMatrix(thetas, matrices, fileName):
    assert(len(thetas) == len(matrices))
    ofile = open(fileName, "w")
    for i in range(len(thetas)):
        ofile.write("theta = " + str(thetas[i]) + "\n")
        ofile.write(matrixTOString(matrices[i]))
        ofile.write("\n")
    ofile.close()

def harmonic_mean(a, b):
    return 2*a*b/(a + b)

def get_ROC_PR(labels, predictions, theta_number):
    import numpy as np
    tpr_values = []
    fpr_values = []
    precision_values = []
    thetas = []
    scores = []
    confusion_matrices = []
    lower = 0.0
    upper = 1.0
    delta = (upper - lower)/theta_number
    for i in range(theta_number+1):
        theta = lower + i*delta
        thetas.append(theta)
        confusion_matrix = get_confusion_matrix(labels, predictions, theta)
        confusion_matrices.append(confusion_matrix)
        tpr, fpr, precision = get_stat(confusion_matrix)
        tpr_values.append(tpr)
        fpr_values.append(fpr)
        precision_values.append(precision)
        scores.append(harmonic_mean(precision, tpr))
    printFile(fpr_values, tpr_values, "ROC.txt")
    printFile(tpr_values, precision_values, "PR.txt")
    printFile(thetas, scores, "F1_theta.txt")
    printMatrix(thetas, confusion_matrices, "confusion_matrix.txt")
    opt_theta = thetas[0]
    max_score = scores[0]
    for i in range(1, len(thetas)):
        if (scores[i] > max_score):
            max_score = scores[i]
            opt_theta = thetas[i]
    integral = 0.0
    for i in range(len(thetas)-1):
        integral += 0.5*(scores[i] + scores[i+1])*(thetas[i+1] - thetas[i])
    print "optimal theta = ", opt_theta
    print "AUC for F1 vs. theta: ", integral
    penalty = np.sqrt(0.5*((opt_theta - 0.5)**2 + (integral - 1.0)**2))
    #print "penalty = ", penalty
    ofile = open("penalty.txt", "w")
    ofile.write("optimal theta = " + str(opt_theta) + "\n")
    ofile.write("AUC of F1 vs. theta = " + str(integral) + "\n")
    ofile.write("penalty = " + str(penalty) + "\n")
    ofile.close()

def main():
    import os
    import sys

    if (len(sys.argv) != 3):
        print "label file = sys.argv[1], prediction file = sys.argv[2]. "
        return -1

    label_file = sys.argv[1]
    prediction_file = sys.argv[2]
    assert(os.path.exists(label_file))
    assert(os.path.exists(prediction_file))
    labels = get_labels(label_file)
    predictions = read_labels(prediction_file)
    get_ROC_PR(labels, predictions, 40)
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
