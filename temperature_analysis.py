# Name: Srividhya S
# Roll Number: IITP_AIMLTN_2601051
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

# Write your code here
if temperatures:
    max_temp,min_temp=temperatures[0],temperatures[0]
    for i in temperatures:
        if i < min_temp:
            min_temp = i 
        if i> max_temp:
            max_temp = i 
    print(f"\nHighest Temperature: {max_temp}°C")
    print(f"Lowest Temperature: {min_temp}°C")
else:
    print("Empty Temperature List")

#####Task 1 ends####

print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

# Write your code here

hot_days = 0
for i in temperatures:
    if i<=30:
        continue
    hot_days+=1

print(f"\nHot Days (>30°C): {hot_days}")

#####Task 2 ends####

print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

# Write your code here

hot_days_alert = 0
alert_triggered = False

for day in range(len(temperatures)):
    if temperatures[day] >= 40:
        print(f"Hot Days before alert: {hot_days_alert}")
        print(f"Alert! Extreme temperature {temperatures[day]}°C detected on Day {day+1}")
        alert_triggered = True
        break

    if temperatures[day] > 30:
        hot_days_alert += 1

if not alert_triggered:
    print(f"No extreme temperature detected.")
    print(f"Total Hot Days: {hot_days_alert}")

#####Task 3 ends####