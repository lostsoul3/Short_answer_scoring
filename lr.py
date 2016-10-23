import numpy as np
import scipy.sparse
from scipy.optimize import fmin_l_bfgs_b

class LinearRegressionGD:
    def __init__(self, lambda_=1, **fmin_args):
        self.lambda_ = lambda_
        self.fmin_args = fmin_args

    def cost_grad(self, theta, X, y):
        m = X.shape[0]
        theta1 = theta[1:]

        t = X.dot(theta) - y
        j = (t.dot(t) + self.lambda_ * theta1.dot(theta1)) / (2.0 * m)

        grad = X.T.dot(t) / m
        grad[1:] += self.lambda_ * theta1 / m

        return j, grad

    def fit(self, X, y):
        theta = np.zeros(X.shape[1])
        self.theta, j, ret = fmin_l_bfgs_b(self.cost_grad, theta, args=(X, y),
            **self.fmin_args)

    def predict(self, X):
        return X.dot(self.theta)
