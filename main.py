#**********************************************************************************
# #Discription:
# -This program analyzes a list of space missions using a for loop.
#-For each mission,we check the name,the year it was launched,
#-and ,whether the mission was successful or not.
#-The program then:
#1-Counts the total number of missions
#2-counts how many missions were successful
#3-Calculates the success rate as a percentage.
#4-Creates a list of missions launched before the year 2000.
#Finally,the program prints allthis information in a clean and formatted way
#________________________________________________________________________________


#Data,three parallel lists.
#Each index represents the same mission.
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

#__________________________________________________________________________________
#Variables for analysis
total_missions=0           #counts of all missions,increases in each loop
successful_missions=0      #counts only missions where success==True
before_2000_list=[]        #list for missions before 2000


#____________________________________________________________________________________
#for loop:
#Go through each mission in the list
#program use range(len(list)) to access index i
#This allows us to use all three lists with the same index

for i in range(len(mission_names)):
    #Count each mission once per loop
    total_missions+=1

    #check if mission was successful
    #mission_success[i] gives True or Flase
    if mission_success[i] is True:
        successful_missions +=1   

    #check if the mission happend before year 2000
    #If yes,add the mission name to the special list
    if mission_years[i]<2000:
        before_2000_list.append(mission_names[i])

#______________________________________________________________________________
#calculate the success rate
#Formula:(successful/total)*100
#Format with 2 decimal places using {:.2f}
success_rate=(successful_missions/total_missions)*100

#________________________________________________________________________________
#Output results
print(f"Total number of missions :{total_missions}")  
print(f"Number of successful missions:{successful_missions}")
print(f"Success rate:{success_rate:.2f}%")
print(f"Missions launched before theyear 2000 :")


for mission in before_2000_list:
    print(f"-{mission}")


    


              
