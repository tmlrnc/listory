"""
BALL TREE

n_samples is the number of points in the data set, and n_features is the dimension of the parameter space.
Note: if X is a C-contiguous array of doubles then data will not be copied. Otherwise, an internal copy will be made.

 trains the scikit-learn  python machine learning algorithm library function
 https://scikit-learn.org

 then passes the trained algorithm the features set and returns the
 predicted y test values form, the function

 then compares the y_test values from scikit-learn predicted to
 y_test values passed in

 then returns the accuracy
 """
# pylint: disable=duplicate-code
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

from sklearn.neighbors import KNeighborsClassifier
from axn.ml.predict.predictor import OneHotPredictor, Commandline
from axn.ml.predict.config import get_ohe_config


@Commandline("BALL_TREE")
class BALL_TREE_OHP(OneHotPredictor):

    def __init__(self, target, X_test, X_train, y_test, y_train):
        """
        initializes the training and testing features and labels

        :param target: string - label to be predicted or classified
        :param X_test: array(float) - testing features
        :param X_train: array(float) - training features
        :param y_test: array(float) - testing label
        :param y_train: array(float) - testing label
        """
        super().__init__(target, X_test, X_train, y_test, y_train)
        self.model_name = 'BALL TREE'

    def predict(self):
        """
        trains the scikit-learn  python machine learning algorithm library function
        https://scikit-learn.org

        then passes the trained algorithm the features set and returns the
        predicted y test values form, the function

        then compares the y_test values from scikit-learn predicted to
        y_test values passed in

        then returns the accuracy
        """
        algorithm = KNeighborsClassifier(algorithm='ball_tree')
        algorithm.fit(self.X_train.toarray(), self.y_train)
        y_pred = list(algorithm.predict(self.X_test.toarray()))
        self.acc = OneHotPredictor.get_accuracy(y_pred, self.y_test)
        return self.acc
