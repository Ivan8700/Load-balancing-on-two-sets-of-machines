# Load-balancing-on-two-sets-of-machines  
This repository explores a variation of the NP problem of Load balancing.  
Given a 2 sets of machines and list of jobs which can be allocated to any of the sets - find an optimal schedule for the jobs.  
Every job has 2 cost values, one cost for scheduling it on the first set and another cost for scheduling it on the second set.  
The amount of machines in every set is different, the first set contains "k" machines while the second set contains "2*k" machines.  
The parameter "k" is received by the user.  

The repository is implemented fully in the Python language and using the local-search method for finding the best schedule for the jobs.  

