# Name: Midnight Riders
# Author: Matt Wong
# Date: Feb 20, 2019

# Inspired by a text only game


import time
import math
import random

# Welcome
print(f"""-------Welcome To Midnight Rider!-------
We've stolen a car. We need to get to the home base. The car is special. 
It has some sort of mystical power. The gorvernment wants it.
It's chasing us down and won't stop until they have it. 
Your goal is to survive. Reach the end before the man gonna getchu!
""")

time.sleep(5)

# Main game variables
done = False
km_traveled = 0         # 100km travelled is a win
hunger = 0              # 0 is no hunger
fuel = 50               # 50 fuel max
agents_distance = 20    # If an agent catches you, you lose

# Give user base stats
print(f"""---Stats---
Km's traveled: 0
Hunger = 0/5
Fuel = 50/50
Agents are 20km behind you
""")

time.sleep(3)

# Main game loop
while not done:
    # Main Instructions
    print(""" 
-----Options-----
A. Eat a tofu (Remember to eat! If you get too hungry you'll starve)
B. Drive at a moderate speed.
C. Drive full throttle!
D. Stop at a gas station. (Doesn't have food)
E. Status check.
F. Quit
""")

    choice = input("What do you want to do? ")
    print("")

    if choice.lower().strip("!. ,?") == "f":
        done = True

    elif choice.lower().strip("!. ,?") == "e":
        print(f"""------Stats------
Km's traveled: {km_traveled} (At 100km you'll win!)
Fuel left: {fuel} (If you run outta fuel, the agents will catch you!)
Agents are {math.fabs(agents_distance)} km behind you.
Hunger = {hunger} (Try not to get to five hunger, you'll starve!)
""")
    
    elif choice.lower().strip("!. ,?") == "d":
        fuel = 50 
        agents_distance -= random.randrange(7,15)
        hunger += random.randrange(1,3)
        print(f"""You get more gas because you're running low. 
You now have {fuel} fuel. But, the agents are now {agents_distance} km 
away and you got hungry({hunger}) while filling up the tank.

-----Updated Stats-----
Agents are {agents_distance} km away
Fuel: {fuel}/50
Hunger: {hunger}/5
""")

    elif choice.lower().strip("!. ,?") == "c": 
        distance_traveled = random.randrange(10,20)
        km_traveled += distance_traveled
        agents_distance += random.randrange(7,15)
        fuel -= float(distance_traveled) * 1.5
        hunger += 2 
        print(f"""You travelled {distance_traveled} km, and {km_traveled} km in total. 
Agents are now {agents_distance} km away. And your fuel is now at {fuel}/50.
You got a little hungry({hunger}) during the drive.

-----Updated Stats-----
Km: {km_traveled} km
Agents are {agents_distance} km away
Fuel: {fuel}/50
Hunger: {hunger}/5
""")

    elif choice.lower().strip("!. ,?") == "b":
        distance_traveled = random.randrange(5,15)
        km_traveled += distance_traveled
        agents_distance -= random.randrange(0,5)
        fuel -= float(distance_traveled) * 1.5
        hunger += 1 
        print(f"""You travelled {distance_traveled} km, and {km_traveled} km total. 
Agents are now {agents_distance} km away. And your fuel is now at {fuel}/50. 
You got a little hungry({hunger}) during the drive.

-----Updated Stats-----
Km: {km_traveled} km
Agents are {agents_distance} km away
Fuel: {fuel}/50
Hunger: {hunger}/5
""")

    elif choice.lower().strip("!. ,?") == "a":    
        hunger = 0 
        agents_distance -= random.randrange(0,3)
        print(f"""You're not hungry({hunger}) anymore. 
The agents are {agents_distance} km away, better get a move on! 
""")
    if fuel < 0:
        print(f"""You ran out of gas and the agents caught up to you. They took
everything from you, the car, the kids, your house, EVERYTHING.

---------GAME OVER---------
""")
         
    if hunger > 5:
        print(f"""You passed out from starvation, the agents caught up to you. 
They took everything from you, the car, the kids, your house, EVERYTHING.

---------GAME OVER---------
""")
        
    if agents_distance <= 0:
        print(f"""The agents caught up to you. They took everything from you, 
the car, the kids, your house, EVERYTHING.

---------GAME OVER---------
""")
        
    if km_traveled > 100:
        print(f"""You crossed the border and escaped the agents! You got 
everything you ever wanted because of the car, you got kids, a house, EVERYTHING.

Congratulations! (っ◕‿◕)っ You get this EPIC prize because of winning....
""")
        print(f"""
            ⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⢸⡇⠄⠄
    ⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
    ⠄⠄⢀⡋⣡⣴⣶⣶⡀      ⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
    ⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
    ⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍      ⢀⣤⣄⠉⠋⣰
    ⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
    ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
   ⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
    ⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
    ⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
    ⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
    ⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
    ⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
    ⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿
 """)
        