import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    plt.scatter(x=df["Year"],y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    slope,intercept,r,p,se = linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
    years = pd.DataFrame(range(1880,2051))
    best_line = years*slope + intercept 
    plt.plot(years,best_line , 'r', label='fitted line')
    
    # Create second line of best fit
    df_new = df[df["Year"] >= 2000]
    slope1,intercept1,r1,p1,se1 = linregress(df_new["Year"],df_new["CSIRO Adjusted Sea Level"])
    years_new = pd.DataFrame(range(2000,2051))
    best_line_new = years_new*slope1 + intercept1 
    plt.plot(years_new,best_line_new , 'orange', label='new-fitted line')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
