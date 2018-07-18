#--------------------------------------------------
#  IMPORT MODULES
#--------------------------------------------------
import torch
from sklearn import linear_model
from sklearn.metrics import confusion_matrix
import numpy as np
from random import sample
from datetime import datetime

start_time = datetime.now()

#--------------------------------------------------
#  LOAD PREVIOUSLY STORED EMBEDDINGS
#--------------------------------------------------
embeddings = np.load('../dataset/startramp/embeddings.npy')
labels = np.loadtxt('../dataset/startramp/labels.txt')

#--------------------------------------------------
#  RUN LOGREG MODEL SEVERAL TIMES
#--------------------------------------------------
results = []
# Prepare confusion matrix
y_actual = []
y_pred = []

for i in range(10):

    loop_start = datetime.now()

    #--------------------------------------------------
    #  FIT LOGISTIC REGRESSION
    #--------------------------------------------------
    sample_index = sample(range(len(embeddings)), len(labels)-200) # choose random sample for fitting
    np_labels = np.array(labels)

    X = embeddings[sample_index, :]
    y = np_labels[sample_index]

    logreg = linear_model.LogisticRegression(penalty='l1', C=1e5)

    logreg.fit(X,y)     # FIT THE MODEL

    #--------------------------------------------------
    #  CHECK FIT
    #--------------------------------------------------
    test_index = [idx for idx in range(len(embeddings)) if idx not in sample_index]
    match_count = 0

    for idx in test_index:

        x_test = embeddings[idx, :].reshape(1,-1)
        y_hat = logreg.predict(x_test)

        y_actual.append(np_labels[idx])
        y_pred.append(y_hat)

        if y_hat == np_labels[idx]:
            match_count += 1

    results.append(match_count/200)
    loop_end = datetime.now()
    print('This loop took: ', loop_end - loop_start)
    print('Accurcay was: ', match_count/200)

#--------------------------------------------------
#  PRINT FINAL RESULTS
#--------------------------------------------------

end_time = datetime.now()
print('Average Accurcary: ', sum(results)/len(results))
print('Time for Total Script: ', end_time-start_time)
