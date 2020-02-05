from gendata import gen_data
from Algorithm import FCFS, SJF, RR

number_process = {1: 60, 2: 40, 3: 20, 4: 200}
percent_time = {1: [70, 20, 10], 2: [50, 30, 20],
                3: [40, 40, 20], 4: [70, 10, 20]}

processList = []

case = int(input("Select case :  "))

FCFS_time = 0.0
SJF_time = 0.0
RR_time = 0.0


processList = gen_data(
    case, processList, percent_time, number_process)
print(processList)
FCFS_time = FCFS(FCFS_time, processList, number_process[case])

processList2 = processList.copy()

SJF_time = SJF(SJF_time, processList2, number_process[case])

processList3 = processList.copy()

RR_time = RR(RR_time, processList3, number_process[case])

print("First come first serve time = " + str(FCFS_time) + " milisecond")
print("Shortest-Job-First = " + str(SJF_time) + " milisecond")
print("Round Robin = " + str(RR_time) + " milisecond")
