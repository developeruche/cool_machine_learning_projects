from statistics import mean
import numpy as np
from matplotlib import pyplot as plt


# Stating the dataset
xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)

def  squared_error_calculator(y_dataset, y_best_fit_line):
    """ 
        The squared error is the difference between the 
        y_dataset and the y_best_fit_line 
    """
    return sum((y_best_fit_line-y_dataset) ** 2)

def coefficient_of_determination(y_dataset, y_best_fit_line):
    y_mean_line = [mean(y_dataset) for y in y_dataset]
    squared_errors_regression = squared_error_calculator(y_dataset, y_best_fit_line)
    squared_errors_y_mean = squared_error_calculator(y_dataset, y_mean_line)

    return 1 - (squared_errors_regression / squared_errors_y_mean)


# Defining a function that can determine slope of the best fit line
def best_fit_slope_and_intercept(xs, ys):
    """ 
        This is the formula(mathematical) for this experiment
        m = mean(x) * mean(y) - mean(x*y) / (mean(x))^2 - mean(x^2)
    """
    m =( ((mean(xs) * mean(ys))  - mean(xs * ys)) / 
            ((mean(xs) * mean(xs))  - mean(xs * xs)))
    
    b = mean(ys) - (m * mean(xs))

    # Now i gat the slope and intercept i can now go a head and get the list of regression variable

    regression_line = [(m*x)+b for x in xs]
    
    # Calculating the r**2 value
    """ 
        Thr r**2 value is the value the tells how good
        a dataset fits to the lineear model.
        it is represented by
        r**2 = 1 - 
    """

    print("Squared Error: ", coefficient_of_determination(ys, regression_line))
    return m, b, regression_line




m, b, regression_line = best_fit_slope_and_intercept(xs, ys)

print(m, b, regression_line)


