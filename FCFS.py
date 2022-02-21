class FCFS():
    def __init__(self,arrival_time,burst_time) -> None:
        self.arrval_time = arrival_time
        self.burst_time = burst_time
        self.dict = self.create_dict(arrival_time,burst_time)
        self.waiting_time = []  # waiting time
        self.turnaround_time = [] # turnaround time
        self.completion_time = []  # completion time
        self.compute_time()

    def compute_time(self):
        self.calculate_completion_time()
        self.calculate_waiting_time()
        self.calcualte_turnaround_time()

    def create_dict(self,arrival_time,burst_time):
        dict = {}
        for i in range(len(arrival_time)):
            dict[i] = [arrival_time[i],burst_time[i]]
        return dict

    def calculate_completion_time(self):
        for i in range(len(self.dict)):
            if i == 0:
                self.completion_time.append(self.dict[i][1])
            else:
                self.completion_time.append(self.completion_time[i-1] + self.dict[i][1])
    
    def calculate_waiting_time(self):
        for i in range(len(self.dict)):
            if i == 0:
                self.waiting_time.append(0)
            else:
                self.waiting_time.append(self.completion_time[i-1] - self.dict[i][0])
    
    def calcualte_turnaround_time(self):
        for i in range(len(self.dict)):
            self.turnaround_time.append(self.completion_time[i] - self.dict[i][0])

    
    def print_results(self):
        print("Process\t\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time")
        for i in range(len(self.dict)):
            print(f"P{i}\t\t{self.dict[i][0]}\t\t{self.dict[i][1]}\t\t{self.waiting_time[i]}\t\t{self.turnaround_time[i]}\t\t{self.completion_time[i]}")
        print("Average Waiting Time: ",sum(self.waiting_time)/len(self.waiting_time))
        print("Average Turnaround Time: ",sum(self.turnaround_time)/len(self.turnaround_time))


# main function
if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    arrival_time = []
    burst_time = []
    for i in range(n):
        arrival_time.append(int(input(f"Enter arrival time of process {i+1}: ")))
        burst_time.append(int(input(f"Enter burst time of process {i+1}: ")))
    fcfs = FCFS(arrival_time,burst_time)
    fcfs.print_results()

        

        