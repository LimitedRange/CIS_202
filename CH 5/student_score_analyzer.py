# This program calculates the average quiz score
# and determines the correct letter grade.

# Function to collect scores and calculate the average.
def calculate_average(number_of_scores):
    total = 0

    for score in range(number_of_scores):
        test_score = float(input(f"Enter score {score + 1}: "))
        total += test_score

    average = total / number_of_scores
    return average

# Function to determine the letter grade.
def determine_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Main program.
def main():

    # Ask the teacher how many scores to enter.
    number_of_scores = int(input("How many test scores do you have?"))

    if number_of_scores > 0:

        # Call the function to calculate the average.
        average = calculate_average(number_of_scores)

        # Call the function to determine the letter grade.
        letter_grade = determine_grade(average)

        # Display the results.
        print("\n----- Student Score Results -----")
        print(f"Number of Scores: {number_of_scores}")
        print(f"Average Score: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")

    else:
        print("Please enter a number greater than zero.")

# Call the main function.
main()