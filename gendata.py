import random


def gen_data(case, processList, percent_time, number_process):

    for i in range(3):
        for j in range(int(percent_time[case][i] * number_process[case] / 100)):
            if i == 0:
                processList.append(random.randrange(2, 9))
            if i == 1:
                processList.append(random.randrange(20, 31))
            if i == 2:
                processList.append(random.randrange(35, 41))

    random.shuffle(processList)
    return processList
