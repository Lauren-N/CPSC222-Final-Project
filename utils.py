import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Name: Lauren Nguyen
Course: CPSC 222
Assignment: Final Project
Date: 12/3/2022
Description: utility file to help with my project
"""

def read_file(filename):
    df = pd.read_csv(filename)
    return df

def delete_missing_data(df):
    df.dropna(axis=0, how='any', thresh=None, inplace=True)
    df.reset_index(inplace=True, drop=True)
    return df

def plot_data(x,y):
    plt.bar(x,y, width=0.25)
    plt.yticks(np.arange(0, len(x)+1, 5))
    plt.xlabel("Amount of tries")
    plt.ylabel("Day")
    plt.title("Amount of tries in 70 days")
    plt.show()

def computed_statistics(df):
    stats_list = []

    # Total Wordles
    total_wordles = len(df)
    stats_list.append(total_wordles)

    # creating two new df with pm and am times
    uncleaned_morning_df = df.copy()
    uncleaned_night_df = df.copy()
    for value in df["Time"]:
        if "AM" in value:
            uncleaned_night_df.replace(value, np.NaN, inplace=True)
        if "PM" in value:
            uncleaned_morning_df.replace(value, np.NaN, inplace=True)
    clean_morning_df = delete_missing_data(uncleaned_morning_df)
    clean_night_df = delete_missing_data(uncleaned_night_df)

    # Total Wordles completed in the morning
    total_morning = len(clean_morning_df)
    stats_list.append(total_morning)

    # Total Wordles completed in the night
    total_night = len(clean_night_df)
    stats_list.append(total_night)

    # Most common amount of tries
    most_common_tries = df["Tries"].mode().iloc[0]
    stats_list.append(most_common_tries)

    # Average amount of tries
    average_tries = df["Tries"].mean()
    stats_list.append(average_tries)

    # Standard deviation of tries
    std_tries = np.std(df["Tries"])
    stats_list.append(std_tries)

    # # Average tries in the morning
    average_tries_morning = clean_morning_df["Tries"].mean()
    stats_list.append(average_tries_morning)

    # # Standard deviation of tries in the morning
    std_tries_morning = np.std(clean_morning_df["Tries"])
    stats_list.append(std_tries_morning)

    # # Average tries in the night
    average_tries_night = clean_night_df["Tries"].mean()
    stats_list.append(average_tries_night)

    # # Standard deviation of tries in the night
    std_tries_night = np.std(clean_night_df["Tries"])
    stats_list.append(std_tries_night)

    return stats_list

def seperate_morning_night(df):
    uncleaned_morning_df = df.copy()
    uncleaned_night_df = df.copy()
    for value in df["Time"]:
        if "AM" in value:
            uncleaned_night_df.replace(value, np.NaN, inplace=True)
        if "PM" in value:
            uncleaned_morning_df.replace(value, np.NaN, inplace=True)
    clean_morning_df = delete_missing_data(uncleaned_morning_df)
    clean_night_df = delete_missing_data(uncleaned_night_df)
    return clean_morning_df, clean_night_df

