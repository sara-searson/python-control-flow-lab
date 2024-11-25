def print_heading(data): 
    print('--------------------')
    print(data)
    print('--------------------')





print_heading('Exercise 0: Example')
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()





print_heading('Exercise 1: Vowel or Consonant')
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    letter = input('Enter a letter: ').lower()
    if(letter == 'a' or 'e' or 'i' or 'o' or 'u'):
        print(f'The letter {letter} is a vowel')
    else:
        print(f'The letter {letter} is a consonant')

# Call the function
# check_letter()





print_heading('Exercise 2: Old enough to vote?')
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    age = input('Please enter your age: ')
    try: 
        if(int(age) >= 18): 
            print(f'{age} is old enough to vote.')
        else: 
            print(f'{age} is not old enough to vote')
    except ValueError:
        print('Please enter a number')

# Call the function
# check_voting_eligibility()





print_heading('Exercise 3: Calculate Dog Years')
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    dog_age = input('Please enter your dogs age: ')
    try: 
        dog_age_int = int(dog_age)
        if(dog_age_int <= 2):
            dog_age_int *= 10
        else: 
            dog_age_int -= 2
            dog_age_int *= 7
            dog_age_int += 20
        print(f'In dog years, your dogs age is {dog_age_int}')
    except ValueError:
        print('Please enter a number')


# Call the function
# calculate_dog_years()





print_heading('Exercise 4: Weather Advice')
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    temp = input('Is it cold? (yes/no)')
    percip = input('Is it raining? (yes/no)')
    if((temp == 'yes') and (percip == 'yes')):
        print('Wear a waterproof coat.')
    elif((temp =='yes') and (percip == 'no')):
        print('Wear a warm coat.')
    elif((temp == 'no') and (percip == 'yes')):
        print('Carry an umbrella')
    elif((temp == 'no') and (percip == 'no')):
        print('Wear light clothing.')
    else:
        print('Please type yes or no for the weather categories.')

# Call the function
# weather_advice()





print_heading('Exercise 5: Whats the Season?')
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    month = input('Please enter the month (Jan - Dec): ').lower()
    day = input('Please enter the day of the month: ')
    try:
        day = int(day)
        if month in ['jan', 'feb'] or (month == 'dec' and day >= 21) or (month == 'mar' and day <= 19):
            print(f'{month.capitalize()} {day} is winter.')
        elif month in ['apr', 'may'] or (month == 'mar' and day >= 20) or (month == 'jun' and day <= 20):
            print(f'{month.capitalize()} {day} is spring.')
        elif month in ['jul', 'aug'] or (month == 'jun' and day >= 21) or (month == 'sep' and day <= 21):
            print(f'{month.capitalize()} {day} is summer.')
        elif month in ['oct', 'nov'] or (month == 'sep' and day >= 22) or (month == 'dec' and day <= 20):
            print(f'{month.capitalize()} {day} is autumn.')
        else:
            print("Invalid date or out of range.")
    except ValueError:
        print("Please enter a valid numeric day.")

# Call the function
determine_season()
