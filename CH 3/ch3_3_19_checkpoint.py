# Chapter 3 Noninteractive Checkpoints Questions 3.19

# Get speed from user
speed = int(input('What is your current speed? '))

# Checking if speed is outside the range 0-200
if speed < 0 or speed > 200:
    print('The number is not valid')
else:
    print('The number is valid')
