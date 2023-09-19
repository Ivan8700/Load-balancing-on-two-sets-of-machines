
from random import randint

class RunAlgorithm(object):
    """ This class will contain the schedule on both of the sets"""
    
    #Receiving the input from the user
    def __init__(self):
        self.list_of_jobs=[]
        input_option=int(input("Enter how would you like to receive the input? 0 - .txt file, 1 - manual insertion, 2 - randomization : "))
        if(input_option==0):
            input_from_text=open("inputs/input1.txt") #change the file name to read different input
            self.parameter=int(input_from_text.readline())
            amount_of_jobs=int(input_from_text.readline())
        else:
            self.parameter=int(input("Enter how many machines will be in the first set, the second set will contain twice as much machines : "))
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
        self.list_of_jobs=dict(zip(indecies,jobs_values))
        
        self.schedule_first_set=[]
        self.summation_array_first_set=[]
        self.schedule_second_set=[]
        self.summation_array_second_set=[]
        for x in range (0,self.parameter):
            self.schedule_first_set.append({})
            self.summation_array_first_set.append(0)
            self.schedule_second_set.append({})
            self.schedule_second_set.append({})
            self.summation_array_second_set.append(0)
            self.summation_array_second_set.append(0)
        self.greedy_algorithm()
    
    #Scheduling the jobs on the machines using the greedy algorithm - for each job, take the minimal cost of scheduling between the sets, then schedule it on the minimal machine at that set.
    #if both values are equal, preferablly schedule the job on the second set (the bigger set)
    def greedy_algorithm(self):
        for key,value in self.list_of_jobs.items():
            min_val=float('inf')
            min_index=0
            if(value[0]<value[1]):
                for x in range(0,self.parameter):
                    if(self.summation_array_first_set[x]<min_val):
                        min_val=self.summation_array_first_set[x]
                        min_index=x
                self.schedule_first_set[min_index][key]=value
                self.summation_array_first_set[min_index]+=value[0]
            elif (value[0]>value[1]):
                for x in range(0,self.parameter*2):
                    if(self.summation_array_second_set[x]<min_val):
                        min_val=self.summation_array_second_set[x]
                        min_index=x
                self.schedule_second_set[min_index][key]=value
                self.summation_array_second_set[min_index]+=value[1]
            else:
                min_val2=float('inf')
                min_index2=0
                for x in range(0,self.parameter):
                    if(self.summation_array_first_set[x]<min_val):
                        min_val=self.summation_array_first_set[x]
                        min_index=x
                for x in range (0,2*self.parameter):
                    if(self.summation_array_second_set[x]<min_val2):
                        min_val2=self.summation_array_second_set[x]
                        min_index2=x
                if (min_val<min_val2):
                    self.schedule_second_set[min_index][key]=value
                    self.summation_array_second_set[min_index]+=value[0]
                else:
                    self.schedule_second_set[min_index2][key]=value
                    self.summation_array_second_set[min_index2]+=value[1]
                    
                
                
            
        
            
            
                