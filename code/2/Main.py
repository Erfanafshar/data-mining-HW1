import numpy as np
import pandas as pd

LR = 0.0000045


def create_data():
    f = pd.read_csv("student.csv", delimiter=';')
    file = f.to_numpy()
    dat = []
    for i in file:
        lst = [1]
        for j in i:
            if type(j) is int:
                lst.append(j)
        dat.append(lst)

    train_data = np.array(dat[0:319])
    test_data = np.array(dat[319:])

    return train_data, test_data


def create_a():
    a = []
    for i in range(16):
        a.append(np.random.random())

    A = np.array(a)
    A = A.transpose()
    return A


def calculate_cost(train_data, A):
    sum = 0
    for sam in train_data:
        sum += (np.dot(sam[0:16], A) - sam[16]) ** 2
    return sum


def calculate_gradian(train_data, A):
    gradian = []
    sum = 0
    for sam in train_data:
        sum += 2 * (np.dot(sam[0:16], A) - sam[16])
    gradian.append(sum)
    for iter in range(15):
        sum = 0
        for sam in train_data:
            sum += 2 * sam[iter + 1] * (np.dot(sam[0:16], A) - sam[16])
        gradian.append(sum)
    return gradian


def training():
    train_data, test_data = create_data()
    A = create_a()
    for sample in train_data:
        cost = calculate_cost(train_data, A)
        # print(cost)

        gradian = calculate_gradian(train_data, A)
        A -= np.multiply(LR, gradian)
    return test_data, A


def testing(test_data, A):
    true_1 = 0
    false_1 = 0
    true_2 = 0
    false_2 = 0
    true0_1 = 0
    false0_1 = 0
    true0_2 = 0
    false0_2 = 0

    for test in test_data:
        pre_y = np.dot(test[0:16], A)
        if abs(pre_y - test[16]) < 1:
            true_1 += 1
        else:
            false_1 += 1
            # print("actual grade : ", test[16], " ## predicted grade : ", pre_y)

        if abs(pre_y - test[16]) < 2:
            true_2 += 1
        else:
            false_2 += 1
            # print("actual grade : ", test[16], " ## predicted grade : ", pre_y)

        if test[16] != 0:
            if abs(pre_y - test[16]) < 1:
                true0_1 += 1
            else:
                false0_1 += 1
                # print("actual grade : ", test[16], " ## predicted grade : ", pre_y)

            if abs(pre_y - test[16]) < 2:
                true0_2 += 1
            else:
                false0_2 += 1
                # print("actual grade : ", test[16], " ## predicted grade : ", pre_y)

    accuracy_1 = true_1 / (true_1 + false_1)
    accuracy_2 = true_2 / (true_2 + false_2)
    accuracy0_1 = true0_1 / (true0_1 + false0_1)
    accuracy0_2 = true0_2 / (true0_2 + false0_2)
    print("accuracy(delta < 1) : ", accuracy_1)
    print("accuracy(delta < 2) : ", accuracy_2)
    print("accuracy(delta < 1)(no 0) : ", accuracy0_1)
    print("accuracy(delta < 2)(no 0) : ", accuracy0_2)


def main():
    test_data, A = training()
    testing(test_data, A)


main()
