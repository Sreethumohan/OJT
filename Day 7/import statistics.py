import statistics

# Define your list of numbers
numbers = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 9, 10]

# Calculate the mean
mean = statistics.mean(numbers)
print("Mean:", mean)

# Calculate the median
median = statistics.median(numbers)
print("Median:", median)

# Calculate the mode
mode = statistics.mode(numbers)
print("Mode:", mode)