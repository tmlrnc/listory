from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

from ohe.predictor import OneHotPredictor, Commandline
from ohe.config import get_ohe_config

@Commandline("QDA")
class QDA_OHP(OneHotPredictor):

    def __init__(self, target, X_test, X_train, y_test, y_train):
        super().__init__(target, X_test, X_train, y_test, y_train)
        self.model_name = 'Quadratic Discriminant Analysis'

    def predict(self):
        algorithm = QuadraticDiscriminantAnalysis()
        algorithm.fit(self.X_train.toarray(), self.y_train)
        y_pred = list(algorithm.predict(self.X_test.toarray()))
        self.acc = OneHotPredictor.get_accuracy(y_pred, self.y_test)
        return self.acc