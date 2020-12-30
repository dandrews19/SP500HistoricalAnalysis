# S&P 500 Historical Analysis Tool

#### This project is meant to be used as a tool to see if there are any recurring trends with the most recent performance/ performances of the S&P 500

###### * The code for this program can be applied to any stock/index/etf etc. if the data is in the correct format. However, the GUI is set up best for the S&P

# Motivation
#### The motivation behind this project was to see whether or not the phrase "Past performance is no guarantee of future results" holds up. Through this project, the goal is to look at performances of the S&P 500 in the past that are similar to the most recent performance of the S&P 500 (based on percentage difference from the previous close)


# How it works
#### The algorithm goes through a series of processes to parse through all of the data from the S&P 500 (dating back to April 2007). It uses intraday, 1- minute data from FirstRateData.com, where it is formatted by the following in a csv:  Date/Time, Open, High, Low, Close
#### First, the algorithm goes through all the data, which is contained in three csv files, and breaks up each day of the stock market into the following sections:
- Date: the date is recorded
- Time Interval 0 Prices: The first of five total time intervals, this one ranging from (in EST) 9:30 AM - 10:48 AM. This contains of list of all the closing prices by the minute in the interval 0 time period.
- Time Interval 1 Prices: The second time interval, ranging from 10:49 AM - 12:06 PM, containing a list of all closing prices by the minute in the interval 1 time period.
- Time Interval 2 Prices: The third time interval, ranging from 12:07 PM - 1:24 PM, containing a list of all closing prices by the minute in the interval 2 time period.
- Time Interval 3 Prices: The fourth time interval, ranging from 1:25 PM - 2:42 PM, containing a list of all closing prices by the minute in the interval 3 time period.
- Time Interval 4 Prices: The fifth and final time interval, ranging from 2:42 PM - 4:00 PM, containing a list of all closing prices by the minute in the interval 4 time period.
- Closing Price: Records the last known value of the S&P 500 for each day

#### Then, the algorithm goes through each day again, this time changing all the prices from the value of the S&P 500 at each day and time to the percent difference from the previous of the S&P 500 on that day. For example, if the closing price of the S&P 500 on the previous day was 100, and the first price of the S&P 500 on the current day was 99, the recorded value for that first price on the current day would be -1(%). Like the previous step, these values are broken up into 5 time intervals, which are the same as the ones from before. 

#### Next, the algorithm fits a polynomial of degree 12 to each time interval of each day using NumPy's polyfit function, essentially describing the performance of the S&P 500 on each day by a piecewise function composed of five functions. This was the original motivation behind breaking up each day into five intervals, as the polyfit function works best when it is fitting functions to less than degree 13, and it is more accurate with less data, hence five intervals each described by a 12 degree polynomial is more accurate than just each one day interval described by a 12 degree polynomial.

#### After that, using SciPy's integration function, the area between the most recent day's curves and every other day in the S&P 500's data is recorded, as that is the technique used to describe similarity between curves. Since each day is broken up into five intervals, the area between each curve is taken with their respective interval, and then the five areas are added up to describe the area between each curve.

#### Then, the five day's with the least area between the most recent day's performance are sorted into a list from least to greatest, so the data can be graphed.

###### * A similar process is used for the three day interval calculation as well, no significant differences.

#### Finally, the most recent day's data and the 5 most similar previous perfromances, alongside the data for how the similar previous day's performed afterward, are sent to a GUI where they can be displayed in any order the user wants (screenshots are below). 

# Screenshots
![Image of Blank Tool](https://github.com/dandrews19/SP500HistoricalAnalysis/blob/master/Blank-Tool.png)
#### This is a screenshot of the GUI with no graphs on it. At the top, there are tabs for a single-day and three day intervals. On the left, there are two lists of buttons, labeled Current Day Options and Next Day Options. The buttons under the current day options allow the user to dispay the most recent performance of the S&P 500, and then rest of the buttons are used to display the days that the algorithm found to be similar to the most recent day. Under Next Day options, the user has the option to display how the similsr performances in the past did the day after. This can be used to try and estimate how the market will perform in the future, if there is a pattern. Below is a screenshot of what it looks like when all the plots are displayed. The user can make the graphs blank whenever they wish using the respective Reset Graph buttons. The legend on the right automatically updates when the user selects an option to be displayed, and clears when the graph is reset.
![Image of Full Tool](https://github.com/dandrews19/SP500HistoricalAnalysis/blob/master/Full-Tool.png)
#### The user also has all of the same options for the three day interval, and when displaying the graphs, it displays graphs of three days rather than one, as shown below.
![Image Three Day Full](https://github.com/dandrews19/SP500HistoricalAnalysis/blob/master/Three-Day-Full.png)
#### Here is a gif running through all the options on the three-day interval:
![Gif of Demo](https://github.com/dandrews19/SP500HistoricalAnalysis/blob/master/StockDemo.gif)

# Modules Used

- Numpy, for fitting data into a polynomial and storing data in arrays
- Datetime, for having the ability to parse through data based on time
- SciPy, to integrate polynomials
- Statistics, to calculate the average value between lists
- Matplotlib, to graph all the data and display it
- Tkinter, to create a user-friendly interface with buttons that enable the plots to be shown


# How to use
#### To use this program, all you have to do is press run in mainTEST.py; make sure you have all the modules installed, StockClass.py is in your directory, and put the the provided CSV files in your directory. Additionally, the csv probably won't be updated, so you might have to somehow get data for the most current dates, or buy data from FirstRateData.com
