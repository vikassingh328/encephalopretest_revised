# Encephalo Investments Coding Pre-Test - Revised April 2020

import pandas as pd
import numpy as np
import math


def cleanse_data(df):
    # Your task here is to remove data from any ticker that isn't XXY, sort chronologically and return a dataframe
    # whose only column is 'Adj Close'
    dfclean = df
    dfclean = dfclean[dfclean.Ticker == 'XXY']
    dfclean.sort_values(by=['Date'], ascending = True)
    dfclean = dfclean.drop(columns = ['Date','Ticker'])
    return dfclean


import statistics
def Average(lst): 
    return sum(lst) / len(lst)
def mc_sim(sims, days, df):
    # The code for a crude monte carlo simulation is given below. Your job is to extract the mean expected price
    # on the last day, as well as the 95% confidence interval.
    # Note that the z-score for a 95% confidence interval is 1.960
    returns = df.pct_change()
    last_price = df.iloc[-1]

    simulation_df = pd.DataFrame()

    for x in range(sims):
        count = 0
        daily_vol = returns.std()

        price_series = []

        price = last_price * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)

        for y in range(days):
            price = price_series[count] * (1 + np.random.normal(0, daily_vol))
            price_series.append(price)
            count += 1

        simulation_df[x] = [float(n) for n in price_series]
      price_series_updated = [float(n) for n in price_series]
      mean_closing_value = Average(price_series_updated
      std_dev = statistics.pstdev(price_series_updated)
      #x is the list of values with +/- 1 Stv dev from the mean last day price
      #y is the range of values for a 95% confidence interval                             
      x = [mean_closing_value - std_dev,mean_closing_value + std_dev]
      y = [mean_closing_value - (2*std_dev),mean_closing_value + (2*std_dev)]
      return x                    

def main():
    filename = '20192020histdata.csv'
    rawdata = pd.read_csv(filename)
    cleansed = cleanse_data(rawdata)
    simnum = 1  # change this number to one that you deem appropriate
    days = 25
    mc_sim(simnum, days, cleansed)
    return


if __name__ == '__main__':
    main()
