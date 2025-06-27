# Exercise 1: Data Quality Check
# You are analyzing a sales dataset and need to ensure that all records have positive values for quantity and price.
# Write a program that checks these fields and prints "Valid data" if both are positive, or "Invalid data" otherwise.

quantity = float(input("Enter the quantity: "))
price = float(input("Enter the price: "))

if quantity > 0 and price > 0:
    print("Valid data")
else:
    print("Invalid data")


# Exercise 2: Sensor Data Classification
# Imagine you are working with IoT sensor data. The data includes temperature measurements.
# You need to classify each reading as 'Low', 'Normal', or 'High'. Given that:
# Temperature < 18°C is 'Low'
# Temperature >= 18°C and <= 26°C is 'Normal'
# Temperature > 26°C is 'High'

temperature = 22

if temperature < 18:
    print("Temperature is low.")
elif temperature >= 18 and temperature <= 26:
    print("Temperature is normal")
else:
    print("Temperature is high")


# Exercise 3: Log Filtering by Severity
# You are analyzing logs from an application and need to filter messages with severity 'ERROR'.
# Given a log record in dictionary format like log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Connection failed'},
# write a program that prints the message if the severity is 'ERROR'.

log = {
    'timestamp': '2021-06-23 10:00:00',
    'level': 'ERROR',
    'message': 'Connection failed'
}

if log['level'] == 'ERROR':
    print(log['message'])


# Exercise 4: Input Data Validation
# Before processing user data in a recommendation system,
# you need to ensure that each user is between 18 and 65 years old and has provided a valid email.
# Write a program to validate these conditions and print "Valid user data" or the specific error found.

user_age = 28
email = "joao.sgobero@gmail.com"

if user_age < 18 or user_age > 65:
    print("Your age is outside the company's guidelines.")
elif "@" not in email:
    print("The email is invalid because it doesn't contain '@'.")
elif "." not in email:
    print("The email is invalid because it doesn't contain '.'.")
else:
    print("The data is valid")


# Exercise 5: Transaction Anomaly Detection
# You are working on a fraud detection system and need to identify suspicious transactions.
# A transaction is considered suspicious if the amount is greater than R$ 10,000 or if it occurs outside business hours (before 9 am or after 6 pm).
# Given a transaction like transaction = {'value': 12000, 'hour': 20}, check if it is suspicious.

transaction = {'value': 12000, 'hour': 20}

if transaction['value'] > 10000 or (transaction['hour'] < 9 or transaction['hour'] > 18):
    print("This transaction is suspicious")
else:
    print("Transaction approved.")


# Exercise 6: Word Count in Texts
# Given a text, count how many times each unique word appears in it.

dirty_text = "Hello, world! The world is beautiful. Beautiful, beautiful world."
print(f"Original text: {dirty_text}")

# Clean and Prepare Data
clean_text = dirty_text.lower()
punctuations_to_remove = ",.!?;:"

for punctuation in punctuations_to_remove:
    # Replace the punctuation with nothing in our text.
    clean_text = clean_text.replace(punctuation, "")

print(f"Clean text: {clean_text}")

# Break the cleaned text into words
word_list = clean_text.split()

# Prepare the "counter"
word_count = {}

# The Counting Loop (stays exactly the same!)
for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the result
print("\nFinal word count (version 2.0):")
print(word_count)


# Exercise 7: Data Normalization
# Normalize a list of numbers to a scale from 0 to 1.

numbers = [10, 20, 30, 40, 50]
min_value = min(numbers)  # 10
max_value = max(numbers)  # 50

normalized = [(x - min_value) / (max_value - min_value) for x in numbers]
print(normalized)


# Exercise 8: Filtering Missing Data
# Given a list of dictionaries representing user data, filter those who have a missing specific field.

users = [
    {"name": "Ana", "age": 25, "email": "ana@email.com"},
    {"name": "Bruno", "age": 30},
    {"name": "Carla", "age": 28, "email": "carla@email.com"},
    {"name": "Diego"},
]

field = "email"

users_with_missing_field = []

for user in users:
    # Check if the field is missing
    if field not in user:
        users_with_missing_field.append(user)

print(users_with_missing_field)


# Exercise 9: Extracting Subsets of Data
# Given a list of numbers, extract only those that are even.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)


# Exercise 10: Data Aggregation by Category
# Given a set of sales records, calculate the total sales by category.

sales = [
    {"category": "Electronics", "value": 1000},
    {"category": "Clothing", "value": 500},
    {"category": "Electronics", "value": 1500},
    {"category": "Food", "value": 300},
    {"category": "Clothing", "value": 700},
    {"category": "Food", "value": 200}
]

# Dictionary to store total sales by category
total_by_category = {}

# Loop through sales records
for sale in sales:
    category = sale["category"]
    value = sale["value"]
    
    # If the category already exists in the dictionary, add the value
    if category in total_by_category:
        total_by_category[category] += value
    else:
        # If the category doesn't exist, add it to the dictionary with the sale value
        total_by_category[category] = value

# Display total sales by category
print(total_by_category)


### Exercises with WHILE

# Exercise 11: Reading Data until Flag
# Read input data until a specific keyword ("exit") is provided.

# List to store user inputs
inputs = []

# Loop to read data until the user types "exit"
while True:
    data = input("Type something (or 'exit' to finish): ")
    
    if data.lower() == "exit":
        break  # Exit the loop if the user types 'exit'
    
    # Add input to the list
    inputs.append(data)

# Display all inputs made by the user
print("Registered inputs:")
for entry in inputs:
    print(entry)


# Exercise 12: Input Validation
# Ask the user for a number within a specific range until the input is valid.

# Defining the range
min_value = 1
max_value = 10

# Loop to request input until it's valid
while True:
    try:
        # Ask the user for a number
        number = int(input(f"Enter a number between {min_value} and {max_value}: "))
        
        # Check if the number is within the range
        if min_value <= number <= max_value:
            print(f"You entered a valid number: {number}")
            break  # Exit the loop if the number is valid
        else:
            print(f"Error: The number must be between {min_value} and {max_value}. Try again.")
    
    except ValueError:
        print("Error: Please enter a valid number.")


# Exercise 13: Simulated API Consumption
# Simulate consuming a paginated API, where each "page" of data is processed in a loop until there are no more pages.

# Function to simulate paginated API consumption
def consume_paginated_api(total_pages, items_per_page):
    # Simulating API data (a total of items)
    total_items = total_pages * items_per_page
    data = [f"Item {i+1}" for i in range(total_items)]
    
    # Pages to be processed
    current_page = 0
    while current_page < total_pages:
        start = current_page * items_per_page
        end = start + items_per_page
        page = data[start:end]
        
        # Simulate processing the page
        print(f"Processing Page {current_page + 1}: {page}")
        
        # Move to the next page
        current_page += 1

# Defining the API configurations
total_pages = 5  # Total pages to consume
items_per_page = 3  # Number of items per page

# Calling the function to consume the API
consume_paginated_api(total_pages, items_per_page)


# Exercise 14: Connection Attempts
# Simulate attempts to reconnect to a service with a maximum number of attempts.

import random
import time

# Function to simulate a connection attempt
def connection_attempt(max_attempts):
    attempts = 0
    
    while attempts < max_attempts:
        attempts += 1
        print(f"Attempt {attempts} of {max_attempts}...")
        
        # Simulate success or failure of the connection (50% chance of success)
        if random.choice([True, False]):
            print("Connection successful!")
            break
        else:
            print("Connection failed. Retrying...")
            time.sleep(2)  # 2 seconds pause between attempts

    # If the maximum attempts are reached without success
    if attempts == max_attempts:
        print("Max attempts reached. Could not connect to the service.")

# Maximum number of attempts
max_attempts = 5

# Calling the function to try the connection
connection_attempt(max_attempts)


# Exercise 15: Data Processing with Stop Condition
# Process items in a list until a specific value indicating stop is found.

# List of items
items = [10, 20, 30, 40, 50, "stop", 60, 70]

# Value indicating stop
stop_value = "stop"

# Process items until the stop value is found
for item in items:
    if item == stop_value:
        print(f"Value '{stop_value}' found. Stopping the processing.")
        break  # Stop the loop when the stop value is found
    else:
        print(f"Processing item: {item}")
