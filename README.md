# robo-advisors

hello friends
welcome to the robo-advisor project
to setup this project, there are a first few steps you need to take: 

First: 
Use your text editor or the command-line to create a new file called "requirements.txt", and then place the following contents inside:


requests
python-dotenv

Second:
Create and activate a new Anaconda virtual environment:

conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env

Third: 
From within the virtual environment, install the required packages specified in the "requirements.txt" file you created:

pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)

Fourth: 
From within the virtual environment, demonstrate your ability to run the Python script from the command-line by adding the below into your robo_advisor.py file:

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

Then from your command line run: python robo_advisor.py

If you get it back, you're all set to start!!

#todoIt also includes instructions for setting an environment variable named ALPHAVANTAGE_API_KEY (see "Security Requirements" section below).

import below:

import response - pull the data from the html
import json - parse the response text from a string into a dictionary
import datetime - find the request time
import csv - write data to csv file
import os - create a file path that can be used across mac / window
from dotenv import load_dotenv - to access your secret API


API Key setup: 
Create a file called .env after installing the dotenv package -  Example ".env" contents:

ALPHAVANTAGE_API_KEY="abc123"

You should be good to start!

