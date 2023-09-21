
from random import randint
from math import ceil
class RunAlgorithm(object):
    """ This class will contain the schedule on both of the sets"""
    
    #Receiving the input from the user
    def __init__(self,print_option):
        self.cnt_amount_of_moves=0
        self.print_option=print_option
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
        
        self.schedule_on_both_sets=[]
        self.summation_of_both_sets=[]
        for x in range (0,self.parameter):
            for y in range(0,3):
                self.schedule_on_both_sets.append({})
                self.summation_of_both_sets.append(0)
        self.greedy_algorithm()
        self.local_search()
        self.print_final_schedule()
    
    #Scheduling the jobs on the machines using the greedy algorithm - for each job, take the minimal cost of scheduling between the sets, then schedule it on the minimal machine at that set.
    #if both values are equal, preferablly schedule the job on the second set (the bigger set)
    def greedy_algorithm(self):
        for key,value in self.list_of_jobs.items():
            min_val=float('inf')
            min_index=0
            if(value[0]<value[1]):
                for x in range(0,self.parameter):
                    if(self.summation_of_both_sets[x]<min_val):
                        min_val=self.summation_of_both_sets[x]
                        min_index=x
                self.schedule_on_both_sets[min_index][key]=value
                self.summation_of_both_sets[min_index]+=value[0]
            elif (value[0]>value[1]):
                for x in range(self.parameter,3*self.parameter):
                    if(self.summation_of_both_sets[x]<min_val):
                        min_val=self.summation_of_both_sets[x]
                        min_index=x
                self.schedule_on_both_sets[min_index][key]=value
                self.summation_of_both_sets[min_index]+=value[1]
            else:
                min_val2=float('inf')
                min_index2=0
                for x in range(0,self.parameter):
                    if(self.summation_of_both_sets[x]<min_val):
                        min_val=self.summation_of_both_sets[x]
                        min_index=x
                for x in range (self.parameter,3*self.parameter):
                    if(self.summation_of_both_sets[x]<min_val2):
                        min_val2=self.summation_of_both_sets[x]
                        min_index2=x
                if (min_val<min_val2):
                    self.schedule_on_both_sets[min_index][key]=value
                    self.summation_of_both_sets[min_index]+=value[0]
                else:
                    self.schedule_on_both_sets[min_index2][key]=value
                    self.summation_of_both_sets[min_index2]+=value[1]
            

    def local_search(self):
        moving_job_bool=True
        switching_jobs_bool=True
        while(moving_job_bool or switching_jobs_bool):
            moving_job_bool=self.moving_job()
            if(moving_job_bool):
                self.cnt_amount_of_moves+=1
                continue
            switching_jobs_bool=self.switching_two_jobs()
            if(switching_jobs_bool):
                self.cnt_amount_of_moves+=1
                continue
           
           

    def moving_job(self):
        for x in range(0,3*self.parameter):
            for key,value in self.schedule_on_both_sets[x].items():
                #try to move a job from set 1 to a machine in the same set
                for y in range(0,3*self.parameter):
                    maximum_between_the_machines=max(self.summation_of_both_sets[x],self.summation_of_both_sets[y])
                    case_value=0 if (y<self.parameter) else 1
                    if(y!=x and (self.summation_of_both_sets[y]+value[case_value]< maximum_between_the_machines)):
                        if(x<self.parameter):
                            self.summation_of_both_sets[x]-=value[0]
                        else:
                            self.summation_of_both_sets[x]-=value[1]
                        self.summation_of_both_sets[y]+=value[case_value]
                        self.schedule_on_both_sets[y][key]=value
                        del self.schedule_on_both_sets[x][key]
                        return True
        return False
    
    def switching_two_jobs(self):
        for x in range(0,3*self.parameter):
            for key,value in self.schedule_on_both_sets[x].items():
                for y in range(0,3*self.parameter):
                    maximum_between_the_machines=max(self.summation_of_both_sets[x],self.summation_of_both_sets[y])
                    where_is_x = 0 if (x<self.parameter) else 1
                    where_is_y= 0 if (y<self.parameter) else 1
                    for key2,value_of_y in self.schedule_on_both_sets[y].items():
                        if(x!=y and (self.summation_of_both_sets[x]-value[where_is_x]+value_of_y[where_is_x] < maximum_between_the_machines) and (self.summation_of_both_sets[y]+value[where_is_y]-value_of_y[where_is_y]<maximum_between_the_machines)):
                            self.summation_of_both_sets[x]+= (value_of_y[where_is_x]-value[where_is_x])
                            self.summation_of_both_sets[y]+= (value[where_is_y]-value_of_y[where_is_y])
                            self.schedule_on_both_sets[x][key2]=value_of_y
                            self.schedule_on_both_sets[y][key]=value
                            del self.schedule_on_both_sets[x][key]
                            del self.schedule_on_both_sets[y][key2]
                            return True
        return False
                        
                    
    
    def print_final_schedule(self):
        print("The schedule on the first set is ")
        print(self.schedule_on_both_sets[0:self.parameter])
        print(self.summation_of_both_sets[0:self.parameter])
        print("\n\n the schedule on the second set is ")
        print(self.schedule_on_both_sets[self.parameter:3*self.parameter])
        print(self.summation_of_both_sets[self.parameter:3*self.parameter])
        maximum_value_on_sets=0
        sum=0
        for x in range(0,3*self.parameter):
            sum+=self.summation_of_both_sets[x]
            if(self.summation_of_both_sets[x]>maximum_value_on_sets):
                maximum_value_on_sets=self.summation_of_both_sets[x]
        print("Total amount of moves is " + str(self.cnt_amount_of_moves))
        print("The makespan is " + str(maximum_value_on_sets))
        print("OPT is bound by " + str(ceil(sum/(3*self.parameter))))
        
        


        

            


                    



                
                
            
        
            
            
                