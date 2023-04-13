# Calibration and Welfare Analysis (30%)

# a)  - Tutorial 4 -> {Code Replication}
            # Update {Predicted} + {Differences} Column --> "Slide 36" "TOPIC 4"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Lecture 4 Code Notes:

#                                       ***MAIN PAGE DATA***
#                {Estimates the effects of taxes on hours worked in different countries}

# Reads the data from a CSV file that includes information about hours worked,
# consumption/output ratio, and effective tax rates for 7 countries in two time periods.

# Calibrates a preference parameter called alpha using a minimization routine and a loss function.

# Calculates the predicted hours worked using the calibrated alpha parameter
# and the consumption/output ratio and effective tax rate for each country.

# Plots the predicted hours worked versus the actual hours worked for each country in both time periods.

# Conducts a counterfactual analysis to estimate the effect of changing the tax rate in one country
# on the hours worked in another country.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#                                      ***Make Figures Data***
#                            {Creates a plot data model for Countries}

# The function takes in 5 inputs: the figure number, data vector of hours worked for the countries,
# model vector of hours worked for the countries, a character string for the title of the graph, and an empty output.

# It creates a figure with the given figure number.

# It plots the data versus model using a red diamond marker and a black solid line for the 45-degree line.

# It sets the title, x-label, and y-label of the plot using the given title and font settings.

# It adds text labels to the plot for each country, placed at the corresponding data and model points.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#                                            ***Loss Function Data***
#                   {Defines Loss function then takes the sum of squared residual using 3 input args}

# Calculate the model's solution for hours worked for a given alfa using the following equations

# Calculate the sum of the squared residuals between the
# observed data and the model's solution using the following equation

# Returns value of sum of squared residuals

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Loss Function
import numpy as np

def LossFcn1(alfa, theta, data):
    # This is the loss function for calibration calculating the sum of the squared residuals
    # input: calibrated preference parameter, alfa
    #        predetermined production parameter, theta
    #        data inputs (dictionary), data
    # output: sum of the squared residuals

    # Calculate the model's solution for hours worked for a given alpha
    hmodel9396 = 100. * (1 - theta) / (alfa / (1 - data['tau9396']) * data['c2y9396'] + (1 - theta));
    hmodel7074 = 100. * (1 - theta) / (alfa / (1 - data['tau7074']) * data['c2y7074'] + (1 - theta));

    # Calculate the sum of the squared residuals
    loss = np.sum((data['hdata9396'] - hmodel9396) ** 2) + np.sum((data['hdata7074'] - hmodel7074) ** 2);
    # Note that * multiplies one vector by another component-by-component.

    return loss

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Make Figures
import matplotlib.pyplot as plt

def makefigures(num, hdata, hmodel, country_name, heading):
    # This function makes a graph plotting the data versus model for the 7 countries
    # Input: Num is the figure number
    #        hdata is the data vector of hours worked for the countries
    #        hmodel is the same thing for the model
    #        heading is a character string giving the title for the graph
    # Note that output for the function is empty , or [ ]

    plt.figure(num)
    plt.plot(hdata, hmodel, 'rd', hdata, hdata, 'k-', linewidth=1,
             markeredgecolor='r', markerfacecolor='r', markersize=5)
    # The plot command asks Python to plot hdata versus hmodel using a red symbol.
    # There is no line for the first plot.
    # The second plot shows the 45 degree line, using a straight line.
    plt.title(heading, fontsize=12, fontname='Calibri')
    plt.xlabel('Data', fontsize=12, fontname='Calibri')
    plt.ylabel('Model', fontsize=20, fontname='Calibri')
    for i in range(7):
        plt.text(hdata[i], hmodel[i], country_name[i])

    plt.show()

hdata = [1, 2, 3, 4, 5, 6, 7]
hmodel = [2, 3, 4, 5, 6, 7, 8]
country_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
heading = 'Data versus Model'
makefigures(1, hdata, hmodel, country_name, heading)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# MAIN DATA


import numpy as np
import pandas as pd
from scipy.optimize import fmin
import seaborn as sns
import matplotlib.pyplot as plt
import pandas_datareader as pdr

def makefigures(fig_num, data, model, country, title):
    plt.figure(fig_num)
    plt.plot(data, '-o', label='Data')
    plt.plot(model, '-x', label='Model')
    plt.legend()
    plt.xticks(range(len(country)), country)
    plt.title(title)
    plt.xlabel('Country')
    plt.ylabel('Hours worked')
    plt.show()

# Step 1: Load data

import os
data = "data_prescott.csv"

data = pd.read_csv('data_prescott.csv')

# Filter the data by year for the years 1993-1996
data_9396 = data.loc[data['period'] == '1993-1996']

# Extract the desired columns for the years 1993-1996
data_country = data_9396['country']
data_c2y9396 = data_9396['c2y']
data_tau9396 = data_9396['tau']
data_hdata9396 = data_9396['h']

# Filter the data by year for the years 1970-1974
data_7074 = data.loc[data['period'] == '1970-1974']

# Extract the desired columns for the years 1970-1974
data_c2y7074 = data_7074['c2y']
data_tau7074 = data_7074['tau']
data_hdata7074 = data_7074['h']

data.columns = data.columns.str.strip()


# Define the loss function
def LossFcn(alfa, theta, data):
    # Calculate the model's solution for hours worked for a given alpha
    hmodel9396 = 100.*(1-theta) / (alfa/(1-data_tau9396) * data_c2y9396 + (1-theta))
    hmodel7074 = 100.*(1-theta) / (alfa/(1-data_tau7074) * data_c2y7074 + (1-theta))
    # Calculate the sum of the squared residuals
    loss = sum((data_hdata9396 - hmodel9396)**2) + sum((data_hdata7074 - hmodel7074)**2)

    return loss

# Step 2: Set predeteremined parameter(s)
theta = 0.32  # production parameter, capital share

# Step 3: Calibrate the preference parameter alpha
alfa = fmin(lambda a: LossFcn(a, theta, data), 1.54, disp=False)
print(f'The calibrated alpha is {alfa:.3f}\n')

# Step 4: Plot the results
# Calculate model hours
hmodel9396 = 100*(1-theta) / (alfa/(1-data_tau9396) * data_c2y9396 + (1-theta))
hmodel7074 = 100*(1-theta) / (alfa/(1-data_tau7074) * data_c2y7074 + (1-theta))

# Plot the data versus model for the 7 countries
makefigures(1, data_hdata9396, hmodel9396, data_country, 'Fit of Model: Hours, 1993-1996')
makefigures(2, data_hdata7074, hmodel7074, data_country, 'Fit of Model: Hours, 1970-1974')

# Counterfactual Analysis
# Remember G7 Countres: GER, FRA, ITA, CAN, GBR, JPN, USA
ID = 4   # Select your base country
counter_ID = 5  # Select the country to use counterfactual analysis

# Counterfactual Analysis
h_base = hmodel9396[ID]  # Hours worked of the base country predicted by the model
h_counter = 100*(1-theta) / (alfa/(1-data_tau9396[counter_ID]) * data_c2y9396[ID] + (1-theta))  # Hours prediction if the country with ID changed its tax rate to the one of the country with counter_ID
print(f'Hours worked for {data_country[ID]} predicted by the model: {h_base:.3f}')
print(f'Counterfactual hours for {data_country[ID]} using the tax system of {data_country[counter_ID]}: {h_counter:.3f}\n')


# Code error, Tau9396 -> code fails to capture data from csv file. tau9396 => 1993-96 tau data

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# b)



# Prescott in the 21st Century (35%)

# Generalisation of Preference (35%)