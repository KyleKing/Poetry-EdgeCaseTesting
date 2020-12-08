"""Verify the NumPy version and make sure it installed correctly."""

import numpy as np

assert np.__version__ == '1.16.0'
print('Result: {} (Expected: [-0.] for 1.16.0)'.format(np.zeros(1) // 1))  # Test NumPy
