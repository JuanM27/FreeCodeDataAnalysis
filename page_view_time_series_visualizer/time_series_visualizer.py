import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR,"fcc-forum-pageviews.csv")

df = pd.read_csv(csv_path,parse_dates=['date'])

#Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset
lower = df['value'].quantile(0.025)
upper = df['value'].quantile(0.975)

df = df[(df['value'] >= lower) & (df['value'] <= upper)]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(18,6))
    plt.plot(df['date'],df['value'])
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')

    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy(deep=True)
    df_bar['year'] = df_bar['date'].dt.year

    months = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]
    
    df_bar['month'] = df_bar['date'].dt.month_name()
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=months)


    df_bar_pivot = pd.pivot_table(
        df_bar,
        values="value",
        index="year",
        columns="month",
        aggfunc=np.mean
    )   

    fig = df_bar_pivot.plot(kind='bar').get_figure()

    fig.set_figheight(6)
    fig.set_figwidth(8)

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')

    fig.savefig('bar_plot.png')

    return fig

#def draw_box_plot():
