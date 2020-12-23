# S&P 500 Historical Analysis tool

#### This project is meant to be used as a tool to see if there are any recurring trends with the most recent performance/ performances of the S&P 500

# Motivation
#### The motivation behind this project was to see whether or not the phrase "Past performance is no guarantee of future results" holds up. Through this project, the goal is to look at performances of the S&P 500 in the past that are similar to the most recent performance of the S&P 500 (based on percentage difference from the previous close)


# How it works
#### The algorithm goes through a series of processes to parse through all of the data from the S&P 500. It uses intraday, 1- minute data from FirstRateData.com, where it is formatted by the following in a csv:  Date/Time, Open, High, Low, Close
#### First, the algorithm goes through all the data, which is contained in three csv files, and breaks up each day of the stock market into the following sections:
- Date: the date is recorded
- Time Interval 0 Prices: The first of five total time intervals, this one ranging from (in EST) 9:30 AM - 10:48 AM. This contains of list of all the closing prices by the minute in the interval 0 time period.
- Time Interval 1 Prices: The second time interval, ranging from 10:49 AM - 12:06 PM, containing a list of all closing prices by the minute in the interval 1 time period.
- Time Interval 2 Prices: The third time interval, ranging from 12:07 PM - 1:24 PM, containing a list of all closing prices by the minute in the interval 2 time period.
- Time Interval 3 Prices: The fourth time interval, ranging from 1:25 PM - 2:42 PM, containing a list of all closing prices by the minute in the interval 3 time period.
- Time Interval 4 Prices: The fifth and final time interval, ranging from 2:42 PM - 4:00 PM, containing a list of all closing prices by the minute in the interval 4 time period.
- Closing Price: Records the last known value of the S&P 500 for each day

#### Then, the algorithm goes through each day again, this time changing all the prices from the value of the S&P 500 at each day and time to the percent difference from the previous of the S&P 500 on that day. For example, if the closing price of the S&P 500 on the previous day was 100, and the first price of the S&P 500 on the current day was 99, the recorded value for that first price on the current day would be -0.01. Like the previous step, these values are broken up into 5 time intervals, which are the same as the ones from before. 

# Screenshots


# Modules Used


# Code Example


# How to use?
