#Discription:This program analyzes a list of space missions using a for loop.
#It counts total missions,successful missions,calculate success rate,and lists missions launched before the year 2000.


#Data
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

#Variables
total_missions=0           #count of all missions
successful_missions=0      #count of successful missions
before_2000_list=[]        #list for missions before 2000

#for loop
#Go through each mission in the list
for i in range(len(mission_names)):
    total_missions+=1

    #check if mission was successful
    if mission_success[i] is True:
        successful_missions +=1   

    #check if mission year is before 2000
    if mission_years[i]<2000:
        before_2000_list.append(mission_names[i])

#calculate
success_rate=(successful_missions/total_missions)*100

#Output
print(f"Total number of missions :{total_missions}")  
print(f"Number of successful missions:{successful_missions}")
print(f"Success rate:{success_rate:.2f}%")
print(f"Missions launched before theyear 2000 :")

for mission in before_2000_list:
    print(f"-{mission}")


    


              
