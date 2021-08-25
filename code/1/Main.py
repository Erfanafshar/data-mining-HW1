import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mean = 0
max = 0
std = 0
year_list = []
state_list = []
info_table = []


def main():
    global info_table
    file = open("covid.csv", "r")

    for line in file:
        info_table.append(line.split(","))

    info_table = info_table[1:176]


def mean_calc():
    global mean
    sum = 0
    num = 0
    for year in year_list:
        if year != '':
            sum += int(year)
            num += 1

    mean = sum / num
    print("mean = " + str(mean))


def max_calc():
    global max
    for year in year_list:
        if year != '':
            if int(year) > max:
                max = int(year)
    print("max = " + str(max))


def std_calc():
    global std
    sum = 0
    num = 0
    for year in year_list:
        if year != '':
            sum += (int(year) - mean) ** 2
            num += 1
    var = sum / (num - 1)
    std = math.sqrt(var)
    print("std = " + str(std))


def remove_null_values():
    info = pd.read_csv("covid.csv")
    # print(info.shape)
    # print(info.isnull().sum())
    new_info = info.dropna()
    # print(newInfo.shape)
    # print(newInfo.isnull().sum())
    return new_info


def histogram(new_info):
    plt.hist(new_info['birth_year'], bins=20)
    plt.show()


def scatter(new_info):
    plt.scatter(new_info['birth_year'], new_info['state'])
    plt.show()


def matrix(new_info):
    X = new_info.iloc[:, 0:20]
    y = new_info.iloc[:, -1]
    correlation = new_info.corr()
    top_corr_features = correlation.index
    plt.figure(figsize=(20, 20))
    g = sns.heatmap(new_info[top_corr_features].corr(), annot=True, cmap="RdYlGn")
    plt.show()


main()

# mean_calc()
# max_calc()
# std_calc()

new_info = remove_null_values()

# histogram(new_info)
# scatter(new_info)
# matrix(new_info)
