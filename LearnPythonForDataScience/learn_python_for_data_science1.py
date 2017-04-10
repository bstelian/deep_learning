# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn import svm

clf1 = tree.DecisionTreeClassifier()
clf2 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                   hidden_layer_sizes=(5, 2), random_state=1)
clf3 = svm.SVC()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# CHALLENGE - ...and train them on our data
clf1 = clf1.fit(X, Y)
clf2 = clf2.fit(X, Y)
clf3 = clf3.fit(X, Y)

prediction1 = clf1.predict([[190, 70, 43]])

prediction2 = clf2.predict([[190, 70, 43]])

prediction3 = clf3.predict([[190, 70, 43]])
# CHALLENGE compare their reusults and print the best one!

print(prediction1)
print(prediction2)
print(prediction3)