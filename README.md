# Drone-stations-Python

# Q1: Drone stations
Weight: 15%

Last update: 14 Nov, 10:00pm

You have a drone that can fly for a distance of D before it runs out of battery. 

There are N charging stations that can fully charge up a drone.

Write a program to determine whether there is a way to fly a drone (initially fully charged) from your location to a target location via zero or more intermediate charging stations.

Input specification: 

The first line consists of two positive integers N (≤ 10) and D (≤ 10); where N is the number of charging stations, D is the distance that a fully charged drone can travel. 

The next N lines are the X-Y coordinates of the locations of the N charging stations.

The 2nd last line is the X-Y coordinate of your location (with a fully charged drone).

The last line is the X-Y coordinate of the target location.

Output specification: 

The (lower-case) character “y” if there is a way to fly a drone (initially fully charged) from your location to a target location via zero or more intermediate charge stations., or “n” if there is not.

Sample testcases (The bolded text are user input)


```

Case 1

3 7
0 3
5 1
8 6
0 1
13 3
y
Case 2

4 6
1 7
5 5
6 1
7 8
5 6
14 32
n

```
