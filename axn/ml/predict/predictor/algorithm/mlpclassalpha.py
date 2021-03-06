"""
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

from sklearn.neural_network import MLPClassifier

from axn.ml.predict.predictor import OneHotPredictor, Commandline
from axn.ml.predict.config import get_ohe_config


@Commandline("MLPCLASSALPHA")
class MLPClassifierAlpha_OHP(OneHotPredictor):

    def __init__(self, target, X_test, X_train, y_test, y_train):
        super().__init__(target, X_test, X_train, y_test, y_train)
        self.model_name = 'MLPCLASSALPHA'

    def predict(self):
        algorithm = MLPClassifier(
            solver=get_ohe_config().mlp_solver,
            alpha=get_ohe_config().mlp_alpha,
            hidden_layer_sizes=(
                get_ohe_config().mlp_layers,
                get_ohe_config().mlp_neurons),
            random_state=get_ohe_config().mlp_random_state)
        algorithm.fit(self.X_train, self.y_train)
        y_pred = list(algorithm.predict(self.X_test))
        self.acc = OneHotPredictor.get_accuracy(y_pred, self.y_test)
        return self.acc
