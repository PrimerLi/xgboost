import xgboost
def main():
    import os
    import sys
    if (len(sys.argv) != 3):
        print "trainFileName = sys.argv[1], testFileName = sys.argv[2]. "
        return -1
    trainFileName = sys.argv[1]
    testFileName = sys.argv[2]
    dtrain = xgboost.DMatrix(trainFileName)
    dtest = xgboost.DMatrix(testFileName)
    param = {"max_depth": 12, "eta": 0.1, "silent": 1, "objective": "binary:logistic"}
    number_of_rounds = 12
    bst = xgboost.train(param, dtrain, number_of_rounds)
    predictions = bst.predict(dtest)
    ofile = open("predicions.txt", "w")
    for i in range(len(predictions)):
        ofile.write(str(predictions[i]) + "\n")
    ofile.close()
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
