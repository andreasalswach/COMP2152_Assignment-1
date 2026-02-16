"""
Author: <Andrea Salswach Lopez>
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" #string
preferred_weight_kg = 20.5 #float
highest_reps = 25 #int
membership_active = True #boolean

# Step c: Create a dictionary named workout_stats

workout_stats = {
    "Alex" : (30, 45, 20),
    "Jamie" : (20, 35, 25),
    "Taylor" : (15, 30, 40)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary

totals = {}
for friend, minutes in workout_stats.items():
    total_minutes = sum(minutes)
    totals[friend + "_Total"] = total_minutes

workout_stats.update(totals)

  
# Step e: Create a 2D nested list called workout_list
# 2D nested list (list of lists) storing workout minutes for each friend

workout_list = []  
for friend in workout_stats:              
    minutes_tuple = workout_stats[friend] 
    minutes_list = list(minutes_tuple)   
    workout_list.append(minutes_list)
print("Workout List:", workout_list)


# Step f: Slice the workout_list

yoga_running = [row[:2] for row in workout_list]
print("Yoga and Running Minutes:", yoga_running)

weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting Minutes for Last Two Friends:", weightlifting_last_two)


# Step g: Check if any friend's total >= 120

for key, value in workout_stats.items():
    if key.endswith("_Total") and value >= 120:
        friend_name = key.replace("_Total", "")
        print(f"Great job staying active, {friend_name}!")

# Step h: User input to look up a friend

search_name = input("Enter a friend's name: ")

if search_name in workout_stats:
    minutes = workout_stats[search_name]
    total = workout_stats.get(search_name + "_Total", 0)
    print(f"{search_name}'s workout minutes (Yoga, Running, Weightlifting): {minutes}")
    print(f"Total Workout Minutes: {total}")
else:
    print(f"Friend {search_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes

highest_friend = None
lowest_friend = None
highest_total = -1
lowest_total = float('inf')

for key, value in workout_stats.items():
    if key.endswith("_Total"):
        if value > highest_total:
            highest_total = value
            highest_friend = key.replace("_Total", "")
        if value < lowest_total:
            lowest_total = value
            lowest_friend = key.replace("_Total", "")

print(f"Highest Total Workout Minutes: {highest_friend} with {highest_total} minutes")
print(f"Lowest Total Workout Minutes: {lowest_friend} with {lowest_total} minutes")