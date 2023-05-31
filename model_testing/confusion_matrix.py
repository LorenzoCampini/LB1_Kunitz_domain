#!/home/lorenzocam/anaconda3/bin/python3
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics



def confusionM(file, poslis, threshold):
    with open(poslis) as poli:                      # creating the list of positive ids
        pos_IDs=[]
        for linee in poli:
            pos_IDs.append(linee.strip())

    fp_list = []
    fn_list = []
    pred = []
    y = []

    with open(file) as f:

        tn, tp, fp, fn = 0, 0, 0, 0                #initializing all the values to 0
        for line in f:

            evalue = float(line.split()[1])
            ID = line.split()[0].split('|')[1]
            if ID in pos_IDs:

                y.append(1)                       # actual positives

                if evalue <= threshold:  # and (ID in pos_IDs):

                    tp += 1                       # TRUE POSITIVE
                    pred.append(1)                # predicted positives
                elif evalue > threshold:  # and (ID in pos_IDs):

                    fn += 1                       # FALSE NEGATIVE
                    fn_list.append(ID)
                    pred.append(0)                # predicted negatives

            if ID not in pos_IDs:
                y.append(0)                       # actual negatives

                if evalue > threshold:  # and (ID not in pos_IDs):

                    tn += 1                       # TRUE NEGATIVE
                    pred.append(0)                # predicted positives

                elif evalue <= threshold:  # and (ID not in pos_IDs):

                    fp += 1                       # FALSE POSITIVE
                    fp_list.append(ID)
                    pred.append(1)                # predicted positives

        cm = np.array([[tp, fp], [fn, tn]])
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        mcc=((tp*tn)-(fp*fn))/np.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
    return cm, mcc, fp_list, fn_list, precision, recall, y, pred

def roc_curve(y, pred):     # this function is to plot the roc curve, as displayed in sklearn
    fpr, tpr, thresholds = metrics.roc_curve(y, pred)
    roc_auc = metrics.auc(fpr, tpr)
    display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc,
                                      estimator_name="ROC curve")
    display.plot()

    plt.show()



if __name__ == '__main__':
    conf_file = sys.argv[1]                            # this file contains the cleaned result of hmmsearch + the other identifiers of uniprot that have not been mapped
    list_positives = sys.argv[2]                       # this file contains the list of positive IDs
    threshold = float(sys.argv[3])                     # this is the threshold I want to use to classify
    cm, mcc, fp_l, fn_l, precision, recall, y, pred = confusionM(conf_file, list_positives, threshold)


    print('THR:', threshold, 'MCC:', mcc, 'precision:', precision, 'recall:', recall)
    print(cm)
    print('false positives list:', fp_l)
    print('false negatives list:', fn_l)
    print('\n\n')
    roc_curve(y, pred)

