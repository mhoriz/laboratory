#include <iostream>
using namespace std;

class FCFS {
public:
    void calculateEndTime(int endTime[], int burstTime[], int NoOfProcess) {
        endTime[0] = burstTime[0];

        for (int i = 1; i < NoOfProcess; i++) {
            endTime[i] = endTime[i - 1] + burstTime[i];
        }
    }

    void calculateTurnAroundTime(int endTime[], int arrivalTime[], int turnAroundTime[], int NoOfProcess) {
        for (int i = 0; i < NoOfProcess; i++) {
            turnAroundTime[i] = endTime[i] - arrivalTime[i];
        }
    }

    void calculateWaitingTime(int burstTime[], int turnAroundTime[], int waitingTime[], int NoOfProcess) {
        for (int i = 0; i < NoOfProcess; i++) {
            waitingTime[i] = turnAroundTime[i] - burstTime[i];
        }
    }
};

int main() {
    const int NoOfProcess = 5;
    float avgWaitingTime = 0.0, avgTurnAroundTime = 0.0;
    int burstTime[NoOfProcess], endTime[NoOfProcess], turnAroundTime[NoOfProcess], waitingTime[NoOfProcess], arrivalTime[NoOfProcess];

    cout << "Enter Arrival Time and Burst Time for 5 Jobs: \n";
    for (int i = 0; i < NoOfProcess; i++) {
        cout << "Job " << i + 1 << " Arrival Time: ";
        cin >> arrivalTime[i];
        cout << "Job " << i + 1 << " Burst Time: ";
        cin >> burstTime[i];
    }

    FCFS scheduler;
    scheduler.calculateEndTime(endTime, burstTime, NoOfProcess);
    scheduler.calculateTurnAroundTime(endTime, arrivalTime, turnAroundTime, NoOfProcess);
    scheduler.calculateWaitingTime(burstTime, turnAroundTime, waitingTime, NoOfProcess);

    cout << "\nID  AT  BT  ET  TAT WT\n";

    for (int i = 0; i < NoOfProcess; i++) {
        cout << i + 1 << "   "
             << arrivalTime[i] << "   "
             << burstTime[i] << "   "
             << endTime[i] << "   "
             << turnAroundTime[i] << "   "
             << waitingTime[i] << "\n";
    }

    for (int i = 0; i < NoOfProcess; i++) {
        avgWaitingTime += waitingTime[i];
        avgTurnAroundTime += turnAroundTime[i];
    }
    avgWaitingTime /= NoOfProcess;
    avgTurnAroundTime /= NoOfProcess;

    cout << "\nAverage Turn Around Time = " << avgTurnAroundTime;
    cout << "\nAverage Waiting Time = " << avgWaitingTime << endl;

    return 0;
}