
def FCFS(FCFS_time, processList, numberProcess):
    temp = 0
    time_array = []
    process_array = []
    for i in range(len(processList)):
        FCFS_time += temp
        temp += processList[i]
        # process_array.append(i+1)
        # time_array.append(FCFS_time)

    # print(time_array)
    # print(process_array)
    FCFS_time = FCFS_time / numberProcess
    return FCFS_time


def SJF(SJF_time, processList, numberProcess):

    temp = 0
    time_array = []
    process_array = []
    for i in range(len(processList)):
        SJF_time += temp
        temp += min(processList)
        processList.remove(min(processList))
        # time_array.append(SJF_time)
        # process_array.append(i+1)
    # print(process_array)
    # print(time_array)
    SJF_time = SJF_time / numberProcess
    return SJF_time


def RR(RR_Time, processList, numberProcess):
    countTime = 0

    end_process = [0] * numberProcess
    timeQuantum = 8
    point = 0
    time_array = []
    process_array = []
    i = 0
    while len(processList) > 0:
        point = point % (len(processList))
        RR_Time += (countTime - end_process[point])
        if processList[point] > timeQuantum:
            processList[point] -= timeQuantum
            countTime += timeQuantum
            end_process[point] = countTime
        elif processList[point] <= timeQuantum:
            countTime += processList[point]
            processList.remove(processList[point])
            end_process.remove(end_process[point])
            point -= 1
            # time_array.append(RR_Time)
        point += 1
        i = i+1
        # process_array.append(len(processList))
    # print(process_array)
    # print(time_array)
    RR_Time = RR_Time/numberProcess

    return RR_Time
