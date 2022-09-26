import math
import matplotlib.pyplot as plt

class Gaussian():
    """Create Gaussian class for calculation and visualization of a Gaussian distribution.

    Attributes
        mean : float
            The mean value of the distribution data.
        std : float
            The standard deviation of the distribution data.
        data : list of float
            List of float numbers extracted from the data file.
    """

    def __init__(self, mu=0, sigma=1):
        self.mean = mu
        self.std = sigma
        self.data = []

    def calculate_mean(self):
        """Function to calculate the mean of the data set.

        Returns:
            float: mean of the data set
        """
        avg = 1 * sum(self.data) / len(self.data)
        self.mean = avg
        return self.mean

    def calculate_std(self, sample=True):
        """Calculate the standard deviation of data set.

        Args:
            sample (bool): whether the data is a subset or population.
        Returns:
            The standard deviation of the data set.
        """
        mean = self.mean
        sigma = 0
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
        for x in self.data:
            sigma += (x - mean) ** 2
        self.std = math.sqrt(sigma / n)
        return self.std

    def read_data_file(self, filename, sample=True):
        """Read text file into a list.

        The file should contain one number (float) per line. The numbers are stored in the attribute data.
        Then the standard deviation and mean are calculated and stored in their attributes.

        Args:
            filename (string): The file path and name.
            sample (bool): whether the data is a subset or population.
        Returns:
            None
        """
        with open(filename, 'r') as file:
            numbers = file.read().strip().split('\n')
            numbers = list(map(int, numbers))
        file.close()

        self.data = numbers
        self.mean = self.calculate_mean()

    def plot_hist(self):
        """Function to output a histogram using the matplotlib module.

        Args:
            None
        Returns:
            Histogram plot
        """
        plt.hist(self.data)
        plt.ylabel("count")
        plt.xlabel("data")

    def pdf(self, x):
        """Probability Density function for calculating the Gaussian distribution.
        
        Args: 
            x (float): point for calculation the probality of the Gaussian distribution
        """
        return (1.0 / (self.std * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.std) ** 2)
    
     def plot_histogram_pdf(self, n_spaces=50):

        """Function to plot the normalized histogram of the data and a plot of the
        probability density function along the same range

        Args:
            n_spaces (int): number of data points

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        mu = self.mean
        sigma = self.std

        min_range = min(self.data)
        max_range = max(self.data)

        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density');
        plt.show()

        return x, y

