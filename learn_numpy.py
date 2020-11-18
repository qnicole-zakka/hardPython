import numpy as np

# To create random floating-point values between 0.0 and 1.0, uniform distribution
# call np.random.random or np.random.random_sample or np.random.rand
rand01 = np.random.random((3, 4))
rand01 = np.random.rand(3, 4)
# starting from numpy 1.17, new API https://docs.scipy.org/doc/numpy/reference/random/generator.html
rng = np.random.default_rng()
rng.random(size=10)
rng.uniform(1, 10, size=10)
