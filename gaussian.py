import math
import matplotlib.pyplot as plt

class Gaussian():
    """
    Create Gaussian class for calculation and visualization of a Gaussian distribution.

    Attributes
    ----------
    mean : float
        The mean value of the distribution data.
    stdev : float
        The standard deviation of the distribution data.
    data : list of float
        List of float numbers extracted from the data file.
    """
    def __init__(self, mu=0, sigma=1):
        self.mean = mu
        self.stdev = sigma
        self.data = []
