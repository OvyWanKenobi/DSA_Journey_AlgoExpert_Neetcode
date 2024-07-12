
#[3,6,2,1,2] <- these are time need to WAIT to perform some tasks
#we need to queue them in a order that that minimum waiting time to complete all tasks
#trick is to sort the input array and finish the lowest waiting time first.

#remember we need to know the minimum time of WAIT , not time processing, hence last tasks will not contribute to total waiting time

#total combine wating time is time needed to complete current task * the number of tasks left after the task,,, as the tasks left need to wait the time to complete its previous tasks

def minimumWaitingTime(queries):
    queries.sort()
    
    totalWaitingTime = 0
    for idx, duration in enumerate(queries):
        queriesLeft = len(queries) - (idx+1)
        totalWaitingTime = totalWaitingTime + (duration * queriesLeft) 
    return totalWaitingTime


#time complexity is O(nlogn) for sorting the array and o(n) for calculating totalwaiting time but it is insignificant to o(nlogn), hence totalwaitingtime is o(nlogn)


def main():
    print("Hello World!")
    
    
    queries = [3,6,2,1,2]
    
    minWaitingTime = minimumWaitingTime(queries)
    
    print("Min waiting time:", minWaitingTime)
    

if __name__ == "__main__":
    main()


