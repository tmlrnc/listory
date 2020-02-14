from sklearn.linear_model import LogisticRegression

from ohe.predictor import OneHotPredictor, Commandline
from ohe.config import get_ohe_config

@Commandline("LR")
class LogisticRegression_OHP(OneHotPredictor):

    def __init__(self, target, X_test, X_train, y_test, y_train):
        super().__init__(target, X_test, X_train, y_test, y_train)
        self.model_name = "Logical Regression"

    def predict(self):
        algorithm = LogisticRegression(random_state=get_ohe_config().LR_random_state)
        algorithm.fit(self.X_train, self.y_train)
        y_pred = list(algorithm.predict(self.X_test))
        self.acc = OneHotPredictor.get_accuracy(y_pred, self.y_test)
        return self.acc