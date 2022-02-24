import numpy as np

def vector_magnitude(vec1):
    """Calculates the magnitude of a vector.
    INPUTS:
        vec1 - The vector. Expected to be a 1D numpy array.

    OUTPUTS:
        Outputs the magnitude of the input vector.
    """

    return np.sqrt(np.sum(np.power(vec1, 2)))
