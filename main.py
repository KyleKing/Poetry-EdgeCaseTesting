"""Verify the NumPy version and make sure it installed correctly."""

import numpy as np

assert np.__version__ == '1.16.0'
assert np.zeros(1)//1 == [-0]  # Test NumPy (Fixed in 1.16.2)
