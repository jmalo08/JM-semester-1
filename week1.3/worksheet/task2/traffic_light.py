"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: James Malone
"""
states = { "red":4, "red_amber":3, "green":5, "amber":3 } #dictionary, used to look up the time which should be spent in each state
keys = ["red", "red_amber", "green", "amber"]
maxtime = int(input("")) # user input 
systime = 0 #variable won't reset, indicator for overall program length other than maxtime
time_in_state = 0 #variable will reset

state = "red"
n = 0 
print(f"Time {systime:03} State {state}")


while systime < maxtime:
    systime = systime + 1
    time_in_state = time_in_state + 1
    if time_in_state >= states.get(state) and n + 1 > len(keys) - 1:
        n = 0
        state = keys[n]
        time_in_state = 0
    if time_in_state >= states.get(state):
        n = n + 1
        state = keys[n]
        time_in_state = 0
    
    print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14