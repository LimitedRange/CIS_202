# Chapter 3 Noninteractive Checkpoints Questions 3.18

# Get speed from user
speed = float(input('What is your current speed? '))

# Checking if speed is between 0-200 or not
if speed >= 0 and speed <= 200:
    print('The number is valid')
else:
    print('The number is invalid')
