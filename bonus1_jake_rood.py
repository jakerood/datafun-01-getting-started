# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Import from Python Standard Library

import statistics
import functools

# get the number of runs from the user - input result is always a string
# Use \n to add a blank new line to the terminal before we ask for input
runs1_string = input("\nEnter the number of runs for game one: ")
runs2_string = input("\nEnter the number of runs for game two: ")
runs3_string = input("\nEnter the number of runs for game three: ")

# convert the runs_string to a number
runs1 = int(runs1_string)
runs2 = int(runs2_string)
runs3 = int(runs3_string)
results = (runs1, runs2, runs3)

# calculate the statistics using the numeric value (not the string) 
sum = sum(results)
average = statistics.mean(results)
product = runs1*runs2*runs3
min = min(results)
max = max(results)

# log the results
logger.info(f"The total runs scored over three games is {sum}.")
logger.info(f"The average runs scored over three games is {average}.")
logger.info(f"The product of the runs scored over three games is {product}.")
logger.info(f"The fewest runs scored over three games is {min}.")
logger.info(f"The most runs scored over three games is {max}.")
logger.info("Great job, team!")
