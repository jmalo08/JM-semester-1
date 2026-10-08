# Week 1.2, Session 2: Task 6

temp = int(input("Enter the machine's temperature (degrees celcius):"))
pressure = int(input("Enter the machine's pressure (PSI)"))
opstatus = int(input("Enter the machine's operational status"))
status = "stable"
if temp > 80:
    print("ALERT: Temperature is too high, please turn off the machine")
    status = "unstable"
elif temp <= 80 and temp >= 50:
    print("Temperature is within safe limits")
else:
    print("Machine temperature is low, no action required")

if pressure > 100:
    print("Pressure is too high, maintenence is recommended")
    status = "unstable"
elif pressure >= 70 and pressure >= 100:
    print("Pressure is stable")
else:
    print("Pressure is low")

if opstatus == 1 and status == "unstable":
    print("Machine is operating in unsafe condtions, please shut it down")
elif opstatus == 1 and status == "stable":
    print("Machine is running as intended")
else:
    print("Machine is stopped, no further action required")

