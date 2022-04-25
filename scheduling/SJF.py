class SJF():
    def __init__(self,arrival_time,burst_time) -> None:
        self.arrval_time = arrival_time
        self.burst_time = burst_time
        self.data = self.create_array(arrival_time,burst_time)
        self.waiting_time = []  # waiting time
        self.turnaround_time = [] # turnaround time
        self.completion_time = []  # completion time
        self.average_turnaround_time = 0
        self.average_waiting_time = 0
        self.schedulingProcesse()
        self.compute_time()
    

    def schedulingProcesse(self):
        start_time = []
        exit_time = []
        s_time = 0
        
        self.data.sort(key=lambda x: x[1])

        for i in range(len(self.data)):
            ready_queue = []
            temp = []
            normal_queue = []

            for j in range(len(self.data)):
                if (self.data[j][1] <= s_time) and (self.data[j][3] == 0):
                    temp.extend([self.data[j][0], self.data[j][1], self.data[j][2]])
                    ready_queue.append(temp)
                    temp = []
                elif self.data[j][3] == 0:
                    temp.extend([self.data[j][0], self.data[j][1], self.data[j][2]])
                    normal_queue.append(temp)
                    temp = []

            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(self.data)):
                    if self.data[k][0] == ready_queue[0][0]:
                        break
                self.data[k][3] = 1
                self.data[k].append(e_time)

            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(self.data)):
                    if self.data[k][0] == normal_queue[0][0]:
                        break
                self.data[k][3] = 1
                self.data[k].append(e_time)

    def compute_time(self):
        self.calcualte_turnaround_time()
        self.calculate_waiting_time()

    def create_array(self,arrival_time,burst_time):
        data = []
        for i in range(len(arrival_time)):
            data.append([i+1 , arrival_time[i],burst_time[i],0])
        return data

    
    def calculate_waiting_time(self):
        total_waiting_time = 0
        for i in range(len(self.data)):
            waiting_time = self.data[i][5] - self.data[i][2]
            total_waiting_time = total_waiting_time + waiting_time
            self.data[i].append(waiting_time)
        self.average_waiting_time = total_waiting_time / len(self.data)
    
    def calcualte_turnaround_time(self):
        total_turnaround_time = 0
        for i in range(len(self.data)):
            turnaround_time = self.data[i][4] - self.data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            self.data[i].append(turnaround_time)
        self.average_turnaround_time = total_turnaround_time / len(self.data)

    
    def print_results(self):
        self.data.sort(key=lambda x: x[0])
        print("Process\t\tArrival Time\tBurst Time\tCompletionTime\tWaitingTime\tTurnaround Time")

        for i in range(len(self.data)):
            print(self.data[i][0], "\t\t", self.data[i][1], "\t\t", self.data[i][2], "\t\t", self.data[i][4], "\t\t", self.data[i][5], "\t\t", self.data[i][6])

        print(f'Average Turnaround Time: {self.average_turnaround_time}')

        print(f'Average Waiting Time: {self.average_waiting_time}')


# main function
if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    arrival_time = []
    burst_time = []
    for i in range(n):
        arrival_time.append(int(input(f"Enter arrival time of process {i+1}: ")))
        burst_time.append(int(input(f"Enter burst time of process {i+1}: ")))
    fcfs = SJF(arrival_time,burst_time)
    fcfs.print_results()

        

        