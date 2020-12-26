from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from tkinter import ttk



    
# This object records the data in relation to the percentage difference from the previous close. Additionally
# this object will contain information related to the similarity between the most recent data and every day in the S&P 500.
class StockDifference(object):


    def __init__(self, dateParam):
        self.date = dateParam
        self.timeInterval0Prices = []
        self.timeInterval1Prices = []
        self.timeInterval2Prices = []
        self.timeInterval3Prices = []
        self.timeInterval4Prices = []
        self.ClosingPrice = 0
        self.timeInterval0Function = []
        self.timeInterval1Function = []
        self.timeInterval2Function = []
        self.timeInterval3Function = []
        self.timeInterval4Function = []
        self.areaBetweenInterval0Functions = 0
        self.areaBetweenInterval1Functions = 0
        self.areaBetweenInterval2Functions = 0
        self.areaBetweenInterval3Functions = 0
        self.areaBetweenInterval4Functions = 0
        self.totalAreaBetweenFunctions = (self.areaBetweenInterval0Functions + self.areaBetweenInterval1Functions
                                         + self.areaBetweenInterval2Functions + self.areaBetweenInterval3Functions
                                          + self.areaBetweenInterval4Functions)

    
    # get and set methods for the attributes of the Stock Difference class
    def updateClosingPrice(self, closingPrice):
        self.ClosingPrice = closingPrice

    def addTimeInterval0Price(self, timeInterval0Price):
        self.timeInterval0Prices.append(timeInterval0Price)

    def addTimeInterval1Price(self, timeInterval1Price):
        self.timeInterval1Prices.append(timeInterval1Price)

    def addTimeInterval2Price(self, timeInterval2Price):
        self.timeInterval2Prices.append(timeInterval2Price)

    def addTimeInterval3Price(self, timeInterval3Price):
        self.timeInterval3Prices.append(timeInterval3Price)

    def addTimeInterval4Price(self, timeInterval4Price):
        self.timeInterval4Prices.append(timeInterval4Price)

    def getDate(self):
        return self.date

    def getTimeInterval0Prices(self):
        return self.timeInterval0Prices

    def getTimeInterval1Prices(self):
        return self.timeInterval1Prices

    def getTimeInterval2Prices(self):
        return self.timeInterval2Prices

    def getTimeInterval3Prices(self):
        return self.timeInterval3Prices

    def getTimeInterval4Prices(self):
        return self.timeInterval4Prices

    def getClosingPrice(self):
        return self.ClosingPrice

    def updateTimeInterval0Function(self, function):
        self.timeInterval0Function = function

    def updateTimeInterval1Function(self, function):
        self.timeInterval1Function = function

    def updateTimeInterval2Function(self, function):
        self.timeInterval2Function = function

    def updateTimeInterval3Function(self, function):
        self.timeInterval3Function = function

    def updateTimeInterval4Function(self, function):
        self.timeInterval4Function = function

    def getTimeInterval0Function(self):
        return self.timeInterval0Function

    def getTimeInterval1Function(self):
        return self.timeInterval1Function

    def getTimeInterval2Function(self):
        return self.timeInterval2Function

    def getTimeInterval3Function(self):
        return self.timeInterval3Function

    def getTimeInterval4Function(self):
        return self.timeInterval4Function

    def updateAreaBetweenInterval0Functions(self, area):
        self.areaBetweenInterval0Functions = area

    def updateAreaBetweenInterval1Functions(self, area):
        self.areaBetweenInterval1Functions = area

    def updateAreaBetweenInterval2Functions(self, area):
        self.areaBetweenInterval2Functions = area

    def updateAreaBetweenInterval3Functions(self, area):
        self.areaBetweenInterval3Functions = area

    def updateAreaBetweenInterval4Functions(self, area):
        self.areaBetweenInterval4Functions = area

    def getAreaBetweenInterval0Functions(self):
        return self.areaBetweenInterval0Functions

    def getAreaBetweenInterval1Functions(self):
        return self.areaBetweenInterval1Functions

    def getAreaBetweenInterval2Functions(self):
        return self.areaBetweenInterval2Functions

    def getAreaBetweenInterval3Functions(self):
        return self.areaBetweenInterval3Functions

    def getAreaBetweenInterval4Functions(self):
        return self.areaBetweenInterval4Functions

    def getTotalAreaBetweenFunctions(self):
        return sum([self.areaBetweenInterval0Functions, self.areaBetweenInterval1Functions, self.areaBetweenInterval2Functions,
                   self.areaBetweenInterval3Functions, self.areaBetweenInterval4Functions])


    # This class stores all the information for three-day interval graphing purposes, including the date range, similarity between the most
    # recent three day interval, and all the prices for that range
class ThreeDayIntervalObject(object):

    def __init__(self):
        self.BeginningDay = ""
        self.FinalDay = ""

        self.Day1XCoords = []
        self.Day1YCoords = []
        self.Day2XCoords = []
        self.Day2YCoords = []
        self.Day3XCoords = []
        self.Day3YCoords = []
        self.Day1Area = 0
        self.Day2Area = 0
        self.Day3Area = 0

        # get and set methods for the three day interval object
    def updateBeginningDay(self, BeginningDay):
        self.BeginningDay = BeginningDay

    def updateFinalDay(self, FinalDay):
        self.FinalDay = FinalDay

    def updateDay1XCoords(self, Day1XCoords):
        self.Day1XCoords = Day1XCoords

    def updateDay1YCoords(self, Day1YCoords):
        self.Day1YCoords = Day1YCoords

    def updateDay2XCoords(self, Day2XCoords):
        self.Day2XCoords = Day2XCoords

    def updateDay2YCoords(self, Day2YCoords):
        self.Day2YCoords = Day2YCoords

    def updateDay3XCoords(self, Day3XCoords):
        self.Day3XCoords = Day3XCoords

    def updateDay3YCoords(self, Day3YCoords):
        self.Day3YCoords = Day3YCoords

    def updateDay1Area(self, Day1Area):
        self.Day1Area = Day1Area

    def updateDay2Area(self, Day2Area):
        self.Day2Area = Day2Area

    def updateDay3Area(self, Day3Area):
        self.Day3Area = Day3Area

    def getDayRange(self):
        return self.BeginningDay + " to " + self.FinalDay

    def getDay1XCoords(self):
        return self.Day1XCoords

    def getDay1YCoords(self):
        return self.Day1YCoords

    def getDay2XCoords(self):
        return self.Day2XCoords

    def getDay2YCoords(self):
        return self.Day2YCoords

    def getDay3XCoords(self):
        return self.Day3XCoords

    def getDay3YCoords(self):
        return self.Day3YCoords

    def getTotalArea(self):

        return abs(self.Day1Area) + abs(self.Day2Area) + abs(self.Day3Area)

    def getTotalYCoords(self):
        i = self.Day2YCoords + self.Day1YCoords[-1]
        j = self.Day3YCoords + i[-1]
        a = np.concatenate((self.Day1YCoords, i))
        b = np.concatenate((a, j))
        return b

    def getTotalXCoords(self):
        return (self.Day1XCoords + self.Day2XCoords + self.Day3XCoords)



# this class contains all the information needed to graph the single day infromation, including the title, line labels, and coordinates
class GraphObject(object):

    def __init__(self):
        self.xCoords1 = []
        self.yCoords1 = []
        self.xCoords2 = []
        self.yCoords2 = []
        self.title = ""
        self.label1 = ""
        self.label2 = ""

    def updatelabel1(self, label):
        self.label1 = label

    def updatelabel2(self, label):
        self.label2 = label

    def updatexCoords1(self, xCoords):
        self.xCoords1 = xCoords

    def updateyCoords1(self, yCoords):
        self.yCoords1 = yCoords

    def updatexCoords2(self, xCoords):
        self.xCoords2 = xCoords

    def updateyCoords2(self, yCoords):
        self.yCoords2 = yCoords

    def updateTitle(self, title):
        self.title = title

    def getxCoords1(self):
        return self.xCoords1

    def getyCoords1(self):
        return self.yCoords1

    def getxCoords2(self):
        return self.xCoords2

    def getyCoords2(self):
        return self.yCoords2

    def getTitle(self):
        return self.title

    def getlabel1(self):
        return self.label1

    def getlabel2(self):
        return self.label2


    # this class creates a GUI where the user can see the data for the five most similar performance when compared to the most recent one, and how the similar
    # prior performances did the day afterwards. This can be done for a one or three day interval, and any graph the user wants can be displayed, and the 
    # graphs can be reset at any point.
class GUI:



    def __init__(self, master, CurrentDayXData, CurrentDayYData,
                afterHistoricalAverageXData, afterHistoricalAverageYData,
                 graphObjects, graphObjectsDayAfter,
                 differenceFromPreviousCloseList, threeDayAfterHistoricalXData, threeDayAfterHistoricalYData,
                 threeDayIntervalsList, threeDayAreaList, threeDayAreaListAfter):
        self.my_notebook = ttk.Notebook(master)
        self.my_notebook.grid()
        self.my_frame1 = Frame(self.my_notebook, width=1500, height=1000)
        self.my_frame1.pack(fill="both", expand = 1)
        self.my_frame2 = Frame(self.my_notebook, width=1500, height=1000)
        self.my_frame2.pack(fill="both", expand=1)
        self.my_notebook.add(self.my_frame1, text="1-day interval")
        self.my_notebook.add(self.my_frame2, text="3-day interval")
        self.differenceFromPreviousCloseList = differenceFromPreviousCloseList
        self.CurrentDayLabel = Label(self.my_frame1, text="Current Day Options:", font='Helvetica 18 bold')
        self.CurrentDayLabel.grid(row=0, sticky= W, pady=10)
        self.NextDayLabel = Label(self.my_frame1, text="Next Day Options:", font='Helvetica 18 bold')
        self.NextDayLabel.grid(row=9, sticky=W, pady=10)

        self.CurrentDayCheck = Button(self.my_frame1, text= "Display most recent S&P 500 performance (" + self.differenceFromPreviousCloseList[-1].getDate() + ")", command= self.GraphCurrentDay, font='Helvetica 12 bold', height= 2)
        self.CurrentDayCheck.grid(row= 2, sticky=W, pady=10)
        self.FirstSimilarDayCheck = Button(self.my_frame1, text="Display performance most similar to " + self.differenceFromPreviousCloseList[-1].getDate(), command= self.GraphFirstSimilarDay, font='Helvetica 12 bold', height= 2)
        self.FirstSimilarDayCheck.grid(row=3, sticky=W, pady=10)
        self.SecondSimilarDayCheck = Button(self.my_frame1, text="Display second performance most similar to " + self.differenceFromPreviousCloseList[-1].getDate(), command= self.GraphSecondSimilarDay, font='Helvetica 12 bold', height= 2)
        self.SecondSimilarDayCheck.grid(row=4, sticky=W, pady=10)
        self.ThirdSimilarDayCheck = Button(self.my_frame1, text="Display third performance most similar to " + self.differenceFromPreviousCloseList[-1].getDate(), command= self.GraphThirdSimilarDay, font='Helvetica 12 bold', height= 2)
        self.ThirdSimilarDayCheck.grid(row=5, sticky=W, pady=10)
        self.FourthSimilarDayCheck = Button(self.my_frame1, text= "Display fourth performance most similar to " + self.differenceFromPreviousCloseList[-1].getDate(), command= self.GraphFourthSimilarDay, font='Helvetica 12 bold', height= 2)
        self.FourthSimilarDayCheck.grid(row=6, sticky=W, pady=10)
        self.FifthSimilarDayCheck = Button(self.my_frame1, text= "Display fifth performance most similar to " + self.differenceFromPreviousCloseList[-1].getDate(), command= self.GraphFifthSimilarDay, font='Helvetica 12 bold', height= 2)
        self.FifthSimilarDayCheck.grid(row=7, sticky=W, pady=10)
        self.afterFirstSimilarDayCheck = Button(self.my_frame1, text="Display day after performance most similar to " + self.differenceFromPreviousCloseList[-1].getDate(),
                                                command=self.GraphAfterFirstSimilarDay, font='Helvetica 12 bold', height= 2)
        self.afterFirstSimilarDayCheck.grid(row=10, sticky=W, pady=10)
        self.afterSecondSimilarDayCheck = Button(self.my_frame1, text="Display day after second performance most similar to " + self.differenceFromPreviousCloseList[-1].getDate(),
                                                 command=self.GraphAfterSecondSimilarDay, font='Helvetica 12 bold', height= 2)
        self.afterSecondSimilarDayCheck.grid(row=11, sticky=W, pady=10)
        self.afterThirdSimilarDayCheck = Button(self.my_frame1, text="Display day after third performance most similar to " + self.differenceFromPreviousCloseList[-1].getDate(),
                                                command=self.GraphAfterThirdSimilarDay, font='Helvetica 12 bold', height= 2)
        self.afterThirdSimilarDayCheck.grid(row=12, sticky=W, pady=10)
        self.afterFourthSimilarDayCheck = Button(self.my_frame1, text="Display day after fourth performance most similar to " + self.differenceFromPreviousCloseList[-1].getDate(),
                                                 command=self.GraphAfterFourthSimilarDay, font='Helvetica 12 bold', height= 2)
        self.afterFourthSimilarDayCheck.grid(row=13, sticky=W, pady=10)
        self.afterFifthSimilarDayCheck = Button(self.my_frame1, text="Display day after fifth performance most similar to " + self.differenceFromPreviousCloseList[-1].getDate(),
                                                command=self.GraphAfterFifthSimilarDay, font='Helvetica 12 bold', height= 2)
        self.afterFifthSimilarDayCheck.grid(row=14, sticky=W, pady=10)
        self.NextDayAverageCheck = Button(self.my_frame1,
                                                     text="Display historical average for day after performances similar to " + self.differenceFromPreviousCloseList[-1].getDate(),
                                                     command=self.GraphNextDayAverage, font='Helvetica 12 bold', height= 2)
        self.NextDayAverageCheck.grid(row=15, sticky=W, pady=10)
        self.CurrentDayGraphLabel = Label(self.my_frame1, text="Graph of S&P 500 on " + self.differenceFromPreviousCloseList[-1].getDate() + " and Historically Similar Performances", font='Helvetica 18 bold')
        self.CurrentDayGraphLabel.grid(row=0, column= 19, pady=10)
        self.NextDayGraphLabel = Label(self.my_frame1, text="Graph of S&P 500 on day after performances historically similar to " + self.differenceFromPreviousCloseList[-1].getDate(), font='Helvetica 18 bold')
        self.NextDayGraphLabel.grid(row=9, column=19, pady=10)
        self.CurrentDayXData = CurrentDayXData
        self.CurrentDayYData = CurrentDayYData
        self.master = self.my_frame1
        self.afterHistoricalAverageXData = afterHistoricalAverageXData
        self.afterHistoricalAverageYData = afterHistoricalAverageYData

        self.fig = plt.Figure(figsize=(9, 3.25), tight_layout=True)
        self.ax = self.fig.add_subplot(111)
        self.ax.spines["top"].set_visible(False)
        self.ax.spines["bottom"].set_visible(False)
        self.ax.spines["right"].set_visible(False)
        self.ax.spines["left"].set_visible(False)
        self.ax.axhline(y=0, color='k', linestyle='dashed')
        self.fig.gca().set_xlabel("Minutes after 9:30 AM EST")
        self.fig.gca().set_ylabel("Percent Difference from Previous Close")
        chart1 = FigureCanvasTkAgg(self.fig, self.master)
        chart1.get_tk_widget().grid(row=2, rowspan=7, column=19)
        self.legendList = ["0 Line"]
        self.ResetButton = Button(self.master, text="Reset Graph", command= self.Reset, height= 2)
        self.ResetButton.grid(row=0, column=1, sticky=E, pady=10)

        self.fig1 = plt.Figure(figsize=(9, 3.25), tight_layout=True)
        self.ax1 = self.fig1.add_subplot(111)
        self.ax1.spines["top"].set_visible(False)
        self.ax1.spines["bottom"].set_visible(False)
        self.ax1.spines["right"].set_visible(False)
        self.ax1.spines["left"].set_visible(False)
        self.ax1.axhline(y=0, color='k', linestyle='dashed')
        self.fig1.gca().set_xlabel("Minutes after 9:30 AM EST")
        self.fig1.gca().set_ylabel("Percent Difference from Previous Close")
        chart2 = FigureCanvasTkAgg(self.fig1, self.master)
        chart2.get_tk_widget().grid(row=10, rowspan=7, column=19)
        self.ResetButton2 = Button(self.master, text="Reset Graph", command=self.Reset2, height= 2)
        self.ResetButton2.grid(row=9, column=1, sticky= E, pady=10)
        self.legendList1 = ["0 line"]
        self.graphObjects = graphObjects
        self.graphObjectsDayAfter = graphObjectsDayAfter
        self.counter1 = 0
        self.counter2 = 0
        self.counter3 = 0
        self.counter4 = 0
        self.counter5 = 0
        self.counter6 = 0
        self.counter7 = 0
        self.counter8 = 0
        self.counter9 = 0
        self.counter10 = 0
        self.counter11 = 0
        self.counter12 = 0
        #––––––––––––––––––––––––––––––––––––––––––––––––––––
        # 3-Day Interval layout
        self.threeDayIntervalsList = threeDayIntervalsList
        self.threeDayAreaList = threeDayAreaList
        self.ThreeDayCurrentDayLabel = Label(self.my_frame2, text="Current Day Options:", font='Helvetica 18 bold')
        self.ThreeDayCurrentDayLabel.grid(row=0, sticky=W, pady=10)
        self.ThreeDayNextDayLabel = Label(self.my_frame2, text="Next Day Options:", font='Helvetica 18 bold')
        self.ThreeDayNextDayLabel.grid(row=9, sticky=W, pady=10)

        self.ThreeDayCurrentDayCheck = Button(self.my_frame2, text="Display most recent S&P 500 performance (" +
                                                           self.threeDayIntervalsList[-1].getDayRange() + ")",
                                      command=self.ThreeDayGraphCurrentDay, font='Helvetica 12 bold', height=2)
        self.ThreeDayCurrentDayCheck.grid(row=2, sticky=W, pady=10)
        self.ThreeDayFirstSimilarDayCheck = Button(self.my_frame2, text="Display performance most similar to " +
                                                                self.threeDayIntervalsList[-1].getDayRange(),
                                           command=self.ThreeDayGraphFirstSimilarDay, font='Helvetica 12 bold', height=2)
        self.ThreeDayFirstSimilarDayCheck.grid(row=3, sticky=W, pady=10)
        self.ThreeDaySecondSimilarDayCheck = Button(self.my_frame2, text="Display second performance most similar to " +
                                                                 self.threeDayIntervalsList[-1].getDayRange(),
                                            command=self.ThreeDayGraphSecondSimilarDay, font='Helvetica 12 bold', height=2)
        self.ThreeDaySecondSimilarDayCheck.grid(row=4, sticky=W, pady=10)
        self.ThreeDayThirdSimilarDayCheck = Button(self.my_frame2, text="Display third performance most similar to " +
                                                                self.threeDayIntervalsList[-1].getDayRange(),
                                           command=self.ThreeDayGraphThirdSimilarDay, font='Helvetica 12 bold', height=2)
        self.ThreeDayThirdSimilarDayCheck.grid(row=5, sticky=W, pady=10)
        self.ThreeDayFourthSimilarDayCheck = Button(self.my_frame2, text="Display fourth performance most similar to " +
                                                                 self.threeDayIntervalsList[-1].getDayRange(),
                                            command=self.ThreeDayGraphFourthSimilarDay, font='Helvetica 12 bold', height=2)
        self.ThreeDayFourthSimilarDayCheck.grid(row=6, sticky=W, pady=10)
        self.ThreeDayFifthSimilarDayCheck = Button(self.my_frame2, text="Display fifth performance most similar to " +
                                                                self.threeDayIntervalsList[-1].getDayRange(),
                                           command=self.ThreeDayGraphFifthSimilarDay, font='Helvetica 12 bold', height=2)
        self.ThreeDayFifthSimilarDayCheck.grid(row=7, sticky=W, pady=10)
        self.ThreeDayafterFirstSimilarDayCheck = Button(self.my_frame2, text="Display interval after performance most similar to " +
                                                                     self.threeDayIntervalsList[-1].getDayRange(),
                                                command=self.ThreeDayGraphAfterFirstSimilarDay, font='Helvetica 12 bold',
                                                height=2)
        self.ThreeDayafterFirstSimilarDayCheck.grid(row=10, sticky=W, pady=10)
        self.ThreeDayafterSecondSimilarDayCheck = Button(self.my_frame2,
                                                 text="Display interval after second performance most similar to " +
                                                      self.threeDayIntervalsList[-1].getDayRange(),
                                                 command=self.ThreeDayGraphAfterSecondSimilarDay, font='Helvetica 12 bold',
                                                 height=2)
        self.ThreeDayafterSecondSimilarDayCheck.grid(row=11, sticky=W, pady=10)
        self.ThreeDayafterThirdSimilarDayCheck = Button(self.my_frame2,
                                                text="Display interval after third performance most similar to " +
                                                     self.threeDayIntervalsList[-1].getDayRange(),
                                                command=self.ThreeDayGraphAfterThirdSimilarDay, font='Helvetica 12 bold',
                                                height=2)
        self.ThreeDayafterThirdSimilarDayCheck.grid(row=12, sticky=W, pady=10)
        self.ThreeDayafterFourthSimilarDayCheck = Button(self.my_frame2,
                                                 text="Display interval after fourth performance most similar to " +
                                                      self.threeDayIntervalsList[-1].getDayRange(),
                                                 command=self.ThreeDayGraphAfterFourthSimilarDay, font='Helvetica 12 bold',
                                                 height=2)
        self.ThreeDayafterFourthSimilarDayCheck.grid(row=13, sticky=W, pady=10)
        self.ThreeDayafterFifthSimilarDayCheck = Button(self.my_frame2,
                                                text="Display interval after fifth performance most similar to " +
                                                     self.threeDayIntervalsList[-1].getDayRange(),
                                                command=self.ThreeDayGraphAfterFifthSimilarDay, font='Helvetica 12 bold',
                                                height=2)
        self.ThreeDayafterFifthSimilarDayCheck.grid(row=14, sticky=W, pady=10)
        self.ThreeDayNextDayAverageCheck = Button(self.my_frame2,
                                          text="Display historical average for interval after performances similar to " +
                                               self.threeDayIntervalsList[-1].getDayRange(),
                                          command=self.ThreeDayGraphNextDayAverage, font='Helvetica 12 bold', height=2)
        self.ThreeDayNextDayAverageCheck.grid(row=15, sticky=W, pady=10)
        self.ThreeDayCurrentDayGraphLabel = Label(self.my_frame2,
                                          text="Graph of S&P 500 on " + self.threeDayIntervalsList[-1].getDayRange() + " and Historically Similar Performances",
                                          font='Helvetica 18 bold')
        self.ThreeDayCurrentDayGraphLabel.grid(row=0, column=19, pady=10)
        self.ThreeDayNextDayGraphLabel = Label(self.my_frame2,
                                       text="Graph of S&P 500 on day after performances historically similar to " +
                                            self.threeDayIntervalsList[-1].getDayRange(),
                                       font='Helvetica 18 bold')
        self.ThreeDayNextDayGraphLabel.grid(row=9, column=19, pady=10)
        self.ThreeDayCurrentDayXData =  threeDayIntervalsList[-1].getTotalXCoords()
        self.ThreeDayCurrentDayYData = threeDayIntervalsList[-1].getTotalYCoords()
        self.master2 = self.my_frame2
        self.ThreeDayafterHistoricalAverageXData = threeDayAfterHistoricalXData 
        self.ThreeDayafterHistoricalAverageYData = threeDayAfterHistoricalYData 

        self.fig3 = plt.Figure(figsize=(8.2, 3.25), tight_layout=True)
        self.ax3 = self.fig3.add_subplot(111)
        self.ax3.spines["top"].set_visible(False)
        self.ax3.spines["bottom"].set_visible(False)
        self.ax3.spines["right"].set_visible(False)
        self.ax3.spines["left"].set_visible(False)
        self.ax3.axhline(y=0, color='k', linestyle='dashed')
        self.ax3.axvline(x=390, linestyle='dashed')
        self.ax3.axvline(x=780, linestyle='dashed', color="darkgray")
        self.fig3.gca().set_xlabel("Minutes after 9:30 AM EST from First Day")
        self.fig3.gca().set_ylabel("Percent Difference from Previous Close")
        chart3 = FigureCanvasTkAgg(self.fig3, self.master2)
        chart3.get_tk_widget().grid(row=2, rowspan=7, column=19)
        self.ThreeDaylegendList = ["0 Line", "Start of Second Day", "Start of Third Day"]
        self.ThreeDayResetButton = Button(self.master2, text="Reset Graph", command=self.ThreeDayReset, height=2)
        self.ThreeDayResetButton.grid(row=0, column=1, sticky=E, pady=0)

        self.fig4 = plt.Figure(figsize=(8.2, 3.25), tight_layout=True)
        self.ax4 = self.fig4.add_subplot(111)
        self.ax4.spines["top"].set_visible(False)
        self.ax4.spines["bottom"].set_visible(False)
        self.ax4.spines["right"].set_visible(False)
        self.ax4.spines["left"].set_visible(False)
        self.ax4.axhline(y=0, color='k', linestyle='dashed')
        self.ax4.axvline(x=390, linestyle='dashed')
        self.ax4.axvline(x=780, linestyle='dashed', color="darkgray")
        self.fig4.gca().set_xlabel("Minutes after 9:30 AM EST from First Day")
        self.fig4.gca().set_ylabel("Percent Difference from Previous Close")
        chart4 = FigureCanvasTkAgg(self.fig4, self.master2)
        chart4.get_tk_widget().grid(row=10, rowspan=7, column=19)
        self.ThreeDayResetButton2 = Button(self.master2, text="Reset Graph", command=self.ThreeDayReset2, height=2)
        self.ThreeDayResetButton2.grid(row=9, column=1, sticky=E, pady=0)
        self.ThreeDaylegendList1 = ["0 line", "Start of Second Day", "Start of Third Day"]
        self.ThreeDaygraphObjects = threeDayIntervalsList
        self.ThreeDaygraphObjectsDayAfter = threeDayAreaListAfter
        self.counter13 = 0
        self.counter14 = 0
        self.counter15 = 0
        self.counter16 = 0
        self.counter17 = 0
        self.counter18 = 0
        self.counter19 = 0
        self.counter20 = 0
        self.counter21 = 0
        self.counter22 = 0
        self.counter23 = 0
        self.counter24 = 0
        self.counter25 = 0




    def Reset(self):
        self.ax.get_legend().set_visible(False)
        self.fig.delaxes(self.ax)
        self.legendList = ["0 line"]
        self.fig.legend(self.legendList, bbox_to_anchor=(1.05, 1))
        self.ax = self.fig.add_subplot(111)
        self.ax.spines["top"].set_visible(False)
        self.ax.spines["bottom"].set_visible(False)
        self.ax.spines["right"].set_visible(False)
        self.ax.spines["left"].set_visible(False)
        self.ax.axhline(y=0, color='k', linestyle='dashed')
        self.fig.gca().set_xlabel("Minutes after 9:30 AM EST")
        self.fig.gca().set_ylabel("Percent Difference from Previous Close")
        chart1 = FigureCanvasTkAgg(self.fig, self.master)
        chart1.get_tk_widget().grid(row=2, rowspan=7, column=19)
        self.counter1 = 0
        self.counter2 = 0
        self.counter3 = 0
        self.counter4 = 0
        self.counter5 = 0
        self.counter6 = 0

    def Reset2(self):
        self.ax1.get_legend().set_visible(False)
        self.fig1.delaxes(self.ax1)
        self.legendList1 = ["0 line"]
        self.fig1.legend(self.legendList1, bbox_to_anchor=(1.05, 1))
        self.ax1 = self.fig1.add_subplot(111)
        self.ax1.spines["top"].set_visible(False)
        self.ax1.spines["bottom"].set_visible(False)
        self.ax1.spines["right"].set_visible(False)
        self.ax1.spines["left"].set_visible(False)
        self.ax1.axhline(y=0, color='k', linestyle='dashed')
        self.fig1.gca().set_xlabel("Minutes after 9:30 AM EST")
        self.fig1.gca().set_ylabel("Percent Difference from Previous Close")
        chart1 = FigureCanvasTkAgg(self.fig1, self.master)
        chart1.get_tk_widget().grid(row=10, rowspan=7, column=19)
        self.counter7 = 0
        self.counter8 = 0
        self.counter9 = 0
        self.counter10 = 0
        self.counter11 = 0
        self.counter12 = 0

    def GraphCurrentDay(self):
        if self.counter1 == 0:
            self.ax.plot(self.CurrentDayXData, self.CurrentDayYData, linewidth=0.75)
            self.legendList.append(self.graphObjects[0].getlabel1())
            self.ax.legend(self.legendList, bbox_to_anchor=(1.05, 1))
            chart1 = FigureCanvasTkAgg(self.fig, self.master)
            chart1.get_tk_widget().grid(row= 2, rowspan=7, column=19)
            self.counter1 += 1



    def GraphFirstSimilarDay(self):
        if self.counter2 == 0:
            self.ax.plot(self.graphObjects[0].getxCoords2(), self.graphObjects[0].getyCoords2(), linewidth=0.75)
            self.legendList.append(self.graphObjects[0].getlabel2())
            self.ax.legend(self.legendList, bbox_to_anchor=(1.05, 1))
            chart1 = FigureCanvasTkAgg(self.fig, self.master)
            chart1.get_tk_widget().grid(row= 2, rowspan=7, column=19)
            self.counter2 += 1


    def GraphSecondSimilarDay(self):
        if self.counter3 == 0:
            self.ax.plot(self.graphObjects[1].getxCoords2(), self.graphObjects[1].getyCoords2(), linewidth=0.75)
            self.legendList.append(self.graphObjects[1].getlabel2())
            self.ax.legend(self.legendList, bbox_to_anchor=(1.05, 1))
            chart1 = FigureCanvasTkAgg(self.fig, self.master)
            chart1.get_tk_widget().grid(row=2, rowspan=7, column=19)
            self.counter3 += 1


    def GraphThirdSimilarDay(self):
        if self.counter4 == 0:
            self.ax.plot(self.graphObjects[2].getxCoords2(), self.graphObjects[2].getyCoords2(), linewidth=0.75)
            self.legendList.append(self.graphObjects[2].getlabel2())
            self.ax.legend(self.legendList, bbox_to_anchor=(1.05, 1))
            chart1 = FigureCanvasTkAgg(self.fig, self.master)
            chart1.get_tk_widget().grid(row=2, rowspan=7, column=19)
            self.counter4 += 1

    def GraphFourthSimilarDay(self):
        if self.counter5 == 0:
            self.ax.plot(self.graphObjects[3].getxCoords2(), self.graphObjects[3].getyCoords2(), linewidth=0.75)
            self.legendList.append(self.graphObjects[3].getlabel2())
            self.ax.legend(self.legendList, bbox_to_anchor=(1.05, 1))
            chart1 = FigureCanvasTkAgg(self.fig, self.master)
            chart1.get_tk_widget().grid(row=2, rowspan=7, column=19)
            self.counter5 += 1

    def GraphFifthSimilarDay(self):
        if self.counter6 == 0:
            self.ax.plot(self.graphObjects[4].getxCoords2(), self.graphObjects[4].getyCoords2(), linewidth=0.75)
            self.legendList.append(self.graphObjects[4].getlabel2())
            self.ax.legend(self.legendList, bbox_to_anchor=(1.05, 1))
            chart1 = FigureCanvasTkAgg(self.fig, self.master)
            chart1.get_tk_widget().grid(row=2, rowspan=7, column=19)
            self.counter6 += 1

    def ThreeDayGraphCurrentDay(self):
        if self.counter13 == 0:
            self.ax3.plot(np.linspace(0, len(self.ThreeDayCurrentDayYData), len(self.ThreeDayCurrentDayYData)), self.ThreeDayCurrentDayYData, linewidth=0.75)
            self.ThreeDaylegendList.append(self.threeDayIntervalsList[-1].getDayRange())
            self.ax3.legend(self.ThreeDaylegendList, bbox_to_anchor=(1.05, 1))
            chart3 = FigureCanvasTkAgg(self.fig3, self.master2)
            chart3.get_tk_widget().grid(row=2, rowspan=7, column=19)
            self.counter13 += 1

    def ThreeDayGraphFirstSimilarDay(self):
        if self.counter14 == 0:
            self.ax3.plot(np.linspace(0, len(self.threeDayAreaList[0].getTotalYCoords()), len(self.threeDayAreaList[0].getTotalYCoords())), self.threeDayAreaList[0].getTotalYCoords(), linewidth=0.75)
            self.ThreeDaylegendList.append(self.threeDayAreaList[0].getDayRange())
            self.ax3.legend(self.ThreeDaylegendList, bbox_to_anchor=(1.05, 1))
            chart3 = FigureCanvasTkAgg(self.fig3, self.master2)
            chart3.get_tk_widget().grid(row= 2, rowspan=7, column=19)
            self.counter14 += 1

    def ThreeDayGraphSecondSimilarDay(self):
        if self.counter15 == 0:
            self.ax3.plot(np.linspace(0, len(self.threeDayAreaList[1].getTotalYCoords()), len(self.threeDayAreaList[1].getTotalYCoords())), self.threeDayAreaList[1].getTotalYCoords(), linewidth=0.75)
            self.ThreeDaylegendList.append(self.threeDayAreaList[1].getDayRange())
            self.ax3.legend(self.ThreeDaylegendList, bbox_to_anchor=(1.05, 1))
            chart3 = FigureCanvasTkAgg(self.fig3, self.master2)
            chart3.get_tk_widget().grid(row= 2, rowspan=7, column=19)
            self.counter15 += 1


    def ThreeDayGraphThirdSimilarDay(self):
        if self.counter16 == 0:
            self.ax3.plot(np.linspace(0, len(self.threeDayAreaList[2].getTotalYCoords()), len(self.threeDayAreaList[2].getTotalYCoords())), self.threeDayAreaList[2].getTotalYCoords(), linewidth=0.75)
            self.ThreeDaylegendList.append(self.threeDayAreaList[2].getDayRange())
            self.ax3.legend(self.ThreeDaylegendList, bbox_to_anchor=(1.05, 1))
            chart3 = FigureCanvasTkAgg(self.fig3, self.master2)
            chart3.get_tk_widget().grid(row= 2, rowspan=7, column=19)
            self.counter16 += 1


    def ThreeDayGraphFourthSimilarDay(self):
        if self.counter17 == 0:
            self.ax3.plot(np.linspace(0, len(self.threeDayAreaList[3].getTotalYCoords()), len(self.threeDayAreaList[3].getTotalYCoords())), self.threeDayAreaList[3].getTotalYCoords(), linewidth=0.75)
            self.ThreeDaylegendList.append(self.threeDayAreaList[3].getDayRange())
            self.ax3.legend(self.ThreeDaylegendList, bbox_to_anchor=(1.05, 1))
            chart3 = FigureCanvasTkAgg(self.fig3, self.master2)
            chart3.get_tk_widget().grid(row= 2, rowspan=7, column=19)
            self.counter17 += 1


    def ThreeDayGraphFifthSimilarDay(self):
        if self.counter18 == 0:
            self.ax3.plot(np.linspace(0, len(self.threeDayAreaList[4].getTotalYCoords()), len(self.threeDayAreaList[4].getTotalYCoords())), self.threeDayAreaList[4].getTotalYCoords(), linewidth=0.75)
            self.ThreeDaylegendList.append(self.threeDayAreaList[4].getDayRange())
            self.ax3.legend(self.ThreeDaylegendList, bbox_to_anchor=(1.05, 1))
            chart3 = FigureCanvasTkAgg(self.fig3, self.master2)
            chart3.get_tk_widget().grid(row= 2, rowspan=7, column=19)
            self.counter18 += 1


    def ThreeDayGraphAfterFirstSimilarDay(self):
        if self.counter19 == 0:
            self.ax4.plot(np.linspace(0, len(self.ThreeDaygraphObjectsDayAfter[0].getTotalYCoords()), len(self.ThreeDaygraphObjectsDayAfter[0].getTotalYCoords())), self.ThreeDaygraphObjectsDayAfter[0].getTotalYCoords(), linewidth=0.75)

            self.ThreeDaylegendList1.append(self.ThreeDaygraphObjectsDayAfter[0].getDayRange())
            self.ax4.legend(self.ThreeDaylegendList1, bbox_to_anchor=(1.05, 1))
            chart4 = FigureCanvasTkAgg(self.fig4, self.master2)
            chart4.get_tk_widget().grid(row=10, rowspan=7, column=19)
            self.counter19 += 1

    def ThreeDayGraphAfterSecondSimilarDay(self):
        if self.counter20 == 0:
            self.ax4.plot(np.linspace(0, len(self.ThreeDaygraphObjectsDayAfter[1].getTotalYCoords()), len(self.ThreeDaygraphObjectsDayAfter[1].getTotalYCoords())), self.ThreeDaygraphObjectsDayAfter[1].getTotalYCoords(), linewidth=0.75)
            self.ThreeDaylegendList1.append(self.ThreeDaygraphObjectsDayAfter[1].getDayRange())
            self.ax4.legend(self.ThreeDaylegendList1, bbox_to_anchor=(1.05, 1))
            chart4 = FigureCanvasTkAgg(self.fig4, self.master2)
            chart4.get_tk_widget().grid(row=10, rowspan=7, column=19)
            self.counter20 += 1


    def ThreeDayGraphAfterThirdSimilarDay(self):
        if self.counter21 == 0:
            self.ax4.plot(np.linspace(0, len(self.ThreeDaygraphObjectsDayAfter[2].getTotalYCoords()), len(self.ThreeDaygraphObjectsDayAfter[2].getTotalYCoords())), self.ThreeDaygraphObjectsDayAfter[2].getTotalYCoords(), linewidth=0.75)
            self.ThreeDaylegendList1.append(self.ThreeDaygraphObjectsDayAfter[2].getDayRange())
            self.ax4.legend(self.ThreeDaylegendList1, bbox_to_anchor=(1.05, 1))
            chart4 = FigureCanvasTkAgg(self.fig4, self.master2)
            chart4.get_tk_widget().grid(row=10, rowspan=7, column=19)
            self.counter21 += 1


    def ThreeDayGraphAfterFourthSimilarDay(self):
        if self.counter22 == 0:
            self.ax4.plot(np.linspace(0, len(self.ThreeDaygraphObjectsDayAfter[3].getTotalYCoords()), len(self.ThreeDaygraphObjectsDayAfter[3].getTotalYCoords())), self.ThreeDaygraphObjectsDayAfter[3].getTotalYCoords(), linewidth=0.75)
            self.ThreeDaylegendList1.append(self.ThreeDaygraphObjectsDayAfter[3].getDayRange())
            self.ax4.legend(self.ThreeDaylegendList1, bbox_to_anchor=(1.05, 1))
            chart4 = FigureCanvasTkAgg(self.fig4, self.master2)
            chart4.get_tk_widget().grid(row=10, rowspan=7, column=19)
            self.counter22 += 1

    def ThreeDayGraphAfterFifthSimilarDay(self):
        if self.counter23 == 0:
            self.ax4.plot(np.linspace(0, len(self.ThreeDaygraphObjectsDayAfter[4].getTotalYCoords()), len(self.ThreeDaygraphObjectsDayAfter[4].getTotalYCoords())), self.ThreeDaygraphObjectsDayAfter[4].getTotalYCoords(), linewidth=0.75)

            self.ThreeDaylegendList1.append(self.ThreeDaygraphObjectsDayAfter[4].getDayRange())
            self.ax4.legend(self.ThreeDaylegendList1, bbox_to_anchor=(1.05, 1))
            chart4 = FigureCanvasTkAgg(self.fig4, self.master2)
            chart4.get_tk_widget().grid(row=10, rowspan=7, column=19)
            self.counter23 += 1


    def ThreeDayGraphNextDayAverage(self):
        if self.counter24 == 0:
            self.ax4.plot(np.linspace(0, len(self.ThreeDayafterHistoricalAverageYData), len(self.ThreeDayafterHistoricalAverageYData)), self.ThreeDayafterHistoricalAverageYData, linewidth=0.75)
            self.ThreeDaylegendList1.append("Historical next 3-Day Interval Average")
            self.ax4.legend(self.ThreeDaylegendList1, bbox_to_anchor=(1.05, 1))
            chart4 = FigureCanvasTkAgg(self.fig4, self.master2)
            chart4.get_tk_widget().grid(row=10, rowspan=7, column=19)
            self.counter24 += 1


    def ThreeDayReset(self):
        self.ax3.get_legend().set_visible(False)
        self.fig3.delaxes(self.ax3)
        self.ThreeDaylegendList = ["0 line", "Start of Second Day", "Start of Third Day"]
        self.fig3.legend(self.ThreeDaylegendList, bbox_to_anchor=(1.05, 1))
        self.ax3 = self.fig3.add_subplot(111)
        self.ax3.spines["top"].set_visible(False)
        self.ax3.spines["bottom"].set_visible(False)
        self.ax3.spines["right"].set_visible(False)
        self.ax3.spines["left"].set_visible(False)
        self.ax3.axhline(y=0, color='k', linestyle='dashed')
        self.ax3.axvline(x=390, linestyle='dashed')
        self.ax3.axvline(x=780, linestyle='dashed', color="darkgray")
        self.fig3.gca().set_xlabel("Minutes after 9:30 AM EST from First Day")
        self.fig3.gca().set_ylabel("Percent Difference from Previous Close")
        chart3 = FigureCanvasTkAgg(self.fig3, self.master2)
        chart3.get_tk_widget().grid(row=2, rowspan=7, column=19)
        self.counter13 = 0
        self.counter14 = 0
        self.counter15 = 0
        self.counter16 = 0
        self.counter17 = 0
        self.counter18 = 0

    def ThreeDayReset2(self):
        self.ax4.get_legend().set_visible(False)
        self.fig4.delaxes(self.ax4)
        self.ThreeDaylegendList1 = ["0 line", "Start of Second Day", "Start of Third Day"]
        self.fig4.legend(self.ThreeDaylegendList1, bbox_to_anchor=(1.05, 1))
        self.ax4 = self.fig4.add_subplot(111)
        self.ax4.spines["top"].set_visible(False)
        self.ax4.spines["bottom"].set_visible(False)
        self.ax4.spines["right"].set_visible(False)
        self.ax4.spines["left"].set_visible(False)
        self.ax4.axhline(y=0, color='k', linestyle='dashed')
        self.ax4.axvline(x=390, linestyle='dashed')
        self.ax4.axvline(x=780, linestyle='dashed', color="darkgray")
        self.fig4.gca().set_xlabel("Minutes after 9:30 AM EST from First Day")
        self.fig4.gca().set_ylabel("Percent Difference from Previous Close")
        chart4 = FigureCanvasTkAgg(self.fig4, self.master2)
        chart4.get_tk_widget().grid(row=10, rowspan=7, column=19)
        self.counter19 = 0
        self.counter20 = 0
        self.counter21 = 0
        self.counter22 = 0
        self.counter23 = 0
        self.counter24 = 0






