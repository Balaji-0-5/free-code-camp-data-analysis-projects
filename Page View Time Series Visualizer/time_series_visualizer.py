import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",index_col="date",parse_dates=True)

# Clean data
df = df.loc[(df["value"] > df["value"].quantile(.025)) & (df["value"] < df["value"].quantile(.975))]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(18,6))
    plt.plot(df,color="red")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["month"] = df_bar.index.month_name()
    df_bar["year"] = df_bar.index.year.values
    years = df_bar.year.unique().tolist()
    months = df_bar[df_bar["year"]==2017].month.unique().tolist()
    values = df_bar.groupby(["year","month"],sort=False).mean().values
    values = np.concatenate((np.zeros((4,1)),values))
    df_bar = pd.DataFrame(values.reshape((4,12)),index=years,columns=months)
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10,8))
    df_bar.plot(kind="bar",ax=ax)
    ax.set(xlabel="Years", ylabel="Average Page Views")
    plt.legend(title="Months")
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months = df_box[df_box["year"]==2017].month.unique().tolist()
    # Draw box plots (using Seaborn)
    fig,ax = plt.subplots(1,2,figsize=(20,8))
   
    sns.boxplot(data=df_box,x="year",y="value",hue="year",ax=ax[0],legend=False,palette="tab10",flierprops={"marker": "."})
    ax[0].set(xlabel="Year",ylabel="Page Views",title="Year-wise Box Plot (Trend)")
    
    sns.boxplot(data=df_box,x="month",y="value",order=months,hue="month",hue_order=months,ax = ax[1],palette="husl",flierprops={"marker": "."})
    ax[1].set(xlabel="Month",ylabel="Page Views",title="Month-wise Box Plot (Seasonality)")


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig