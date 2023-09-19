
from random import randint

class RunAlgorithm(object):
    """ This class will contain the schedule on both of the sets"""
    
    def __init__(self):
        self.list_of_jobs=[]
        input_option=int(input("Enter how would you like to receive the input? 0 - .txt file, 1 - manual insertion, 2 - randomization : "))
        if(input_option==0):
            input_from_text=open("inputs/input1.txt") #change the file name to read different input
            parameter=int(input_from_text.readline())
            amount_of_jobs=int(input_from_text.readline())
        else:
            parameter=int(input("Enter how many machines will be in the first set, the second set will contain twice as much machines : "))
            amount_of_jobs=int(input("Enter the total amount of jobs there will be in the input : "))
        indecies=[]
        jobs_values=[]
        for x in range(0,amount_of_jobs):
            jobs_values.append([])
        if(input_option==1):
            print("Enter the value of the jobs, first value for the cost for the first set and the second value for the cost on the second set : ")
        for x in range (1,(amount_of_jobs+1)):
            indecies.append(x)
            if(input_option==0):
                value=int(input_from_text.readline())
                jobs_values[(x-1)].append(value)
                value=int(input_from_text.readline())
                jobs_values[(x-1)].append(value)
            elif (input_option==1):
                jobs_values[(x-1)].append(int(input()))
                jobs_values[(x-1)].append(int(input()))
            else:
                jobs_values[(x-1)].append(randint(21,60))
                jobs_values[(x-1)].append(randint(21,60))
        list_of_jobs=dict(zip(indecies,jobs_values))
        print(list_of_jobs)
                
            
            
                