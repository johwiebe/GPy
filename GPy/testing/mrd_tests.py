# Copyright (c) 2013, Max Zwiessele
# Licensed under the BSD 3-clause license (see LICENSE.txt)
'''
Created on 10 Apr 2013

@author: maxz
'''

import unittest
import numpy as np
import GPy

class MRDTests(unittest.TestCase):

    def test_gradients(self):
        num_m = 3
        N, M, Q, D = 20, 8, 6, 20
        X = np.random.rand(N, Q)

        k = GPy.kern.linear(Q) + GPy.kern.bias(Q) + GPy.kern.white(Q)
        K = k.K(X)

        Ylist = [np.random.multivariate_normal(np.zeros(N), K, D).T for _ in range(num_m)]
        likelihood_list = [GPy.likelihoods.Gaussian(Y) for Y in Ylist]

        m = GPy.models.MRD(likelihood_list, Q=Q, kernels=k, M=M)
        m.ensure_default_constraints()

        self.assertTrue(m.checkgrad())

if __name__ == "__main__":
    print "Running unit tests, please be (very) patient..."
    unittest.main()
