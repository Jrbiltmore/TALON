# visualization.py - Visualization Module

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class Visualization:
    def __init__(self):
        self.data = None
        self.labels = None

    def load_data(self, data, labels):
        # Placeholder for loading data and labels for visualization
        self.data = np.array(data)
        self.labels = np.array(labels)

    def scatter_plot(self):
        # Placeholder for creating a scatter plot
        sns.set(style="whitegrid", font_scale=1.2)
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=self.data[:, 0], y=self.data[:, 1], hue=self.labels, palette="viridis", s=100)
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.title("Scatter Plot with Class Labels")
        plt.legend(title="Class")
        plt.show()

    def histogram(self):
        # Placeholder for creating a histogram
        plt.figure(figsize=(8, 6))
        sns.histplot(self.data[:, 0], bins=20, color='skyblue', kde=True)
        plt.xlabel("Feature 1")
        plt.ylabel("Frequency")
        plt.title("Histogram of Feature 1")
        plt.show()

    def box_plot(self):
        # Placeholder for creating a box plot
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=self.labels, y=self.data[:, 1], palette="Set2")
        plt.xlabel("Class")
        plt.ylabel("Feature 2")
        plt.title("Box Plot of Feature 2 by Class")
        plt.show()

# Example usage:
if __name__ == "__main__":
    visualization = Visualization()

    # Load data and labels
    data = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]
    labels = [0, 0, 1, 1, 0, 1, 1, 0]
    visualization.load_data(data, labels)

    # Create scatter plot
    visualization.scatter_plot()

    # Create histogram
    visualization.histogram()

    # Create box plot
    visualization.box_plot()
