#STEM 103, Fall 2025, Khatereh Banan Dargah,
 Level 2, For Loop

##Description:
This Python program analyzes a list of space missions using a for loop and three parallel lists.
For each mission, it checks the mission’s name, launch year, and whether the mission was successful or not.
The program then:
-Counts the total number of missions
-Counts how many missions were successful
-Calculates the success rate as a percentage
-Lists all missions that were launched before the year 2000

###Algorithm:

1.	Define three parallel lists for mission names, launch years, and success status.
2.	Initialize counters for total missions, successful missions, and an empty list for missions before 2000.
3.	Use a for loop with range(len(mission_names)) to process each mission by index.
4.	In each iteration:

-Increase the total mission counter.
-If the mission is successful, increase the successful mission counter.
-If the mission year is less than 2000, add the mission name to a special list.

5.	After the loop, calculate the success rate as a percentage.
6.	Print the total missions, successful missions, and success rate (formatted with two decimal places).
7.	Print the list of missions launched before the year 2000.
####Python Concepts Used:
-for loop with range(len(list)) to iterate over list indices
-Parallel lists (using the same index to access related data)
-if statements for decision making
-Counters to track totals
-List methods such as .append()
-Basic arithmetic and percentage calculation
-f-strings and numeric formatting ({value:.2f}) for clean output

#####Input and Output:
-Input:
There is no user input in this program. All data is stored in three predefined lists inside the code.
-Output:
The program prints:

-The total number of missions
-The number of successful missions
-The success rate as a percentage with two decimal places
-A list of mission names that were launched before the year 2000






