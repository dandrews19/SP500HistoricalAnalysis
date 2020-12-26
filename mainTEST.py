import numpy as np
from datetime import date, time, datetime
import scipy.integrate as integrate
import statistics
from tkinter import *

from StockClass import StockDifference
from StockClass import GraphObject
from StockClass import GUI
from StockClass import ThreeDayIntervalObject


# input: none
# output: a list of objects, with each object in the list representing data from a single day in the stock market
# description: The purpose of this function is to parse through the data containing data from the S&P 500 from 2007 to
# 2020 and split up the data into an object so that it can be used more easily later. Specifically, each day of the
# stock market is being split up into 5, 77-78 minute time intervals, those being from (in EST) 9:30 AM - 10:48 AM,
# 10:49 AM - 12:06 PM, 12:07 PM - 1:24 PM, 1:25 PM - 2:42 PM, and 2:42 PM - 4:00 PM. The reason the data is being
# split up is because later on, I associate a piece-wise function with each day of the stock market, with a function
# being prescribed to each interval of the day. The data is in a CSV file, that contains data for each minute of
# # every day for the stock market, and from that I record the closing price for each minute, which is located in the
# # 5th column of the file. Additionally, rather than storing each value of the stock market, this function records
# the difference from the previous close in percentage to yield better comparisons
# Modules used: datetime to help go through the function in terms of the time it gives
def dataFrom2007to2020():
    listOfCSVs = ["SPX_2000_2009.csv", "SPX_2010_2019.csv", "SPX_2020_2020.csv"]
    listOfStocks1 = []
    print("Parsing through data from 2007 to 2020...")
    previousClose = 1.0
    for file in listOfCSVs:
        fileIn = open(file, "r")

        for line in fileIn:
            info = line.strip().split(",")
            if info[0][10] == " ":
                datetime_object = datetime.strptime(info[0][10:], ' %H:%M:%S').time()
            else:
                datetime_object = datetime.strptime(info[0][10:], '%H:%M:%S').time()
            i = datetime_object
            if i == time(hour= 9, minute= 30, second= 00):
                stock = StockDifference(dateParam=info[0][:10])

                stock.addTimeInterval0Price(float("{:.2f}".format(((((float(info[4]) - (previousClose))/(previousClose))*100)))))
            if time(hour= 9, minute= 30, second= 00) < i <= time(hour= 10, minute= 48, second= 00):

                stock.addTimeInterval0Price(
                    float("{:.2f}".format(((((float(info[4]) - (previousClose)) / (previousClose)) * 100)))))
            if time(hour= 10, minute= 48, second= 00) < i <= time(hour= 12, minute= 6, second= 00):

                stock.addTimeInterval1Price(
                    float("{:.2f}".format(((((float(info[4]) - (previousClose)) / (previousClose)) * 100)))))
            if time(hour= 12, minute= 6, second= 00) < i <= time(hour= 13, minute= 24, second= 00):

                stock.addTimeInterval2Price(
                    float("{:.2f}".format(((((float(info[4]) - (previousClose)) / (previousClose)) * 100)))))
            if time(hour= 13, minute= 24, second= 00) < i <= time(hour= 14, minute= 42, second= 00):

                stock.addTimeInterval3Price(
                    float("{:.2f}".format(((((float(info[4]) - (previousClose)) / (previousClose)) * 100)))))
            if time(hour= 14, minute= 42, second= 00) < i < time(hour= 16, minute= 00, second= 00):
                stock.addTimeInterval4Price(
                    float("{:.2f}".format(((((float(info[4]) - (previousClose)) / (previousClose)) * 100)))))
            if i == time(hour= 16, minute= 00, second= 00):
                stock.updateClosingPrice(closingPrice=float(info[4]))
                stock.addTimeInterval4Price(float("{:.2f}".format(((((float(info[4]) - (previousClose))/(previousClose))*100)))))
                previousClose = float(info[4])
                listOfStocks1.append(stock)
            if time(hour= 16, minute= 00, second= 00) < i < time(hour= 17, minute= 00, second= 00):
                stock.updateClosingPrice(closingPrice=float(info[4]))
                previousClose = float(info[4])
        fileIn.close()

    return listOfStocks1


# input: a list of objects containing data associated with the difference from the previous close (in points) for each
# minute of the day
# output: none
# Description: using a set of for loops, this function goes through each interval of each day, and assigns each interval
# a function fitted to a degree 12 polynomial (12 was chosen because of limited computing power, but it could be changed
# to any desired number), These functions will be used later on to calculate the area between the most recent data's
# piecewise functions and every other day from 2007 to now's assigned piecewise function.
# Modules used: numpy to fit each set of data to a polynomial of degree 12
def differenceToFunction(differenceFromPreviousCloseList):
    print("Converting each day into a piecewise function of five functions...")

    for day in differenceFromPreviousCloseList:
        length = len(day.getTimeInterval0Prices())
        x = np.linspace(0, length, length)
        y = np.array(day.getTimeInterval0Prices())
        coefficients = np.polyfit(x, y, 12)
        day.updateTimeInterval0Function(function=coefficients)

    for day in differenceFromPreviousCloseList:
        length = len(day.getTimeInterval1Prices())
        x = np.linspace(0, length, length)
        y = np.array(day.getTimeInterval1Prices())
        coefficients = np.polyfit(x, y, 12)
        day.updateTimeInterval1Function(function=coefficients)

    for day in differenceFromPreviousCloseList:
        length = len(day.getTimeInterval2Prices())
        x = np.linspace(0, length, length)
        y = np.array(day.getTimeInterval2Prices())
        coefficients = np.polyfit(x, y, 12)
        day.updateTimeInterval2Function(function=coefficients)

    for day in differenceFromPreviousCloseList:
        length = len(day.getTimeInterval3Prices())
        x = np.linspace(0, length, length)
        y = np.array(day.getTimeInterval3Prices())
        coefficients = np.polyfit(x, y, 12)
        day.updateTimeInterval3Function(function=coefficients)

    for day in differenceFromPreviousCloseList:
        length = len(day.getTimeInterval4Prices())
        x = np.linspace(0, length, length)
        y = np.array(day.getTimeInterval4Prices())
        coefficients = np.polyfit(x, y, 12)
        day.updateTimeInterval4Function(function=coefficients)

# inputs: a list of objects containing data associated with the difference from the previous close (in points) for each
# minute of the day
# output: none
# description: This function goes through every interval of every day of the S&P 500 data and finds the area between the
# historical curves and the most recent curves to measure the similarity between them.
# modules used: numpy to compute integrals between historical intervals and the most recent interval provided.
def areaBetweenRecentCurveAndEveryOtherCurve(differenceFromPreviousCloseList):
    print("Calculating which S&P 500 days are most similar to " + differenceFromPreviousCloseList[-1].getDate() + "...")

    counter0 = 0
    for day in differenceFromPreviousCloseList:
        if counter0 == len(differenceFromPreviousCloseList)-1:
            break
        length = len(day.getTimeInterval0Prices())
        recentCoefficients = differenceFromPreviousCloseList[len(differenceFromPreviousCloseList)-1].getTimeInterval0Function()
        historicalCoefficients = day.getTimeInterval0Function()
        z = np.poly1d(recentCoefficients)
        h = np.poly1d(historicalCoefficients)
        zdu = integrate.quad(z, 0, length)[0]
        hdu = integrate.quad(h, 0, length)[0]
        if (zdu > 0 and hdu > 0) or (zdu < 0 and hdu < 0):
            area_between_curves = abs(abs(zdu) - abs(hdu))
        else:
            area_between_curves = abs(abs(zdu) + abs(hdu))
        day.updateAreaBetweenInterval0Functions(area_between_curves)
        counter0 += 1


    counter1 = 0
    for day in differenceFromPreviousCloseList:
        if counter1 == len(differenceFromPreviousCloseList)-1:
            break
        length = len(day.getTimeInterval1Prices())
        recentCoefficients = differenceFromPreviousCloseList[len(differenceFromPreviousCloseList)-1].getTimeInterval1Function()
        historicalCoefficients = day.getTimeInterval1Function()
        z = np.poly1d(recentCoefficients)
        h = np.poly1d(historicalCoefficients)
        zdu = integrate.quad(z, 0, length)[0]
        hdu = integrate.quad(h, 0, length)[0]
        if (zdu > 0 and hdu > 0) or (zdu < 0 and hdu < 0):
            area_between_curves = abs(abs(zdu) - abs(hdu))
        else:
            area_between_curves = abs(abs(zdu) + abs(hdu))
        day.updateAreaBetweenInterval1Functions(area_between_curves)
        counter1 += 1


    counter2 = 0
    for day in differenceFromPreviousCloseList:
        if counter2 == len(differenceFromPreviousCloseList)-1:
            break
        length = len(day.getTimeInterval2Prices())
        recentCoefficients = differenceFromPreviousCloseList[len(differenceFromPreviousCloseList)-1].getTimeInterval2Function()
        historicalCoefficients = day.getTimeInterval2Function()
        z = np.poly1d(recentCoefficients)
        h = np.poly1d(historicalCoefficients)
        zdu = integrate.quad(z, 0, length)[0]
        hdu = integrate.quad(h, 0, length)[0]
        if (zdu > 0 and hdu > 0) or (zdu < 0 and hdu < 0):
            area_between_curves = abs(abs(zdu) - abs(hdu))
        else:
            area_between_curves = abs(abs(zdu) + abs(hdu))
        day.updateAreaBetweenInterval2Functions(area_between_curves)
        counter2 += 1


    counter3 = 0
    for day in differenceFromPreviousCloseList:
        if counter3 == len(differenceFromPreviousCloseList)-1:
            break
        length = len(day.getTimeInterval3Prices())
        recentCoefficients = differenceFromPreviousCloseList[len(differenceFromPreviousCloseList)-1].getTimeInterval3Function()
        historicalCoefficients = day.getTimeInterval3Function()
        z = np.poly1d(recentCoefficients)
        h = np.poly1d(historicalCoefficients)
        zdu = integrate.quad(z, 0, length)[0]
        hdu = integrate.quad(h, 0, length)[0]
        if (zdu > 0 and hdu > 0) or (zdu < 0 and hdu < 0):
            area_between_curves = abs(abs(zdu) - abs(hdu))
        else:
            area_between_curves = abs(abs(zdu) + abs(hdu))
        day.updateAreaBetweenInterval3Functions(area_between_curves)
        counter3 += 1

    counter4 = 0
    for day in differenceFromPreviousCloseList:
        if counter4 == len(differenceFromPreviousCloseList)-1:
            break
        length = len(day.getTimeInterval4Prices())
        recentCoefficients = differenceFromPreviousCloseList[len(differenceFromPreviousCloseList)-1].getTimeInterval4Function()
        historicalCoefficients = day.getTimeInterval4Function()
        z = np.poly1d(recentCoefficients)
        h = np.poly1d(historicalCoefficients)
        zdu = integrate.quad(z, 0, length)[0]
        hdu = integrate.quad(h, 0, length)[0]
        if (zdu > 0 and hdu > 0) or (zdu < 0 and hdu < 0):
            area_between_curves = abs(abs(zdu) - abs(hdu))
        else:
            area_between_curves = abs(abs(zdu) + abs(hdu))
        day.updateAreaBetweenInterval4Functions(area_between_curves)
        counter4 += 1


# input: a list of objects containing data associated with the difference from the previous close (in points) for each
# minute of the day
# output: a list of objects containing data from the historical three day intervals compared to the most recent three-day interval
# description: this function creates an object for each historical three-day interval, takes the area of each day with
# reespect to the most recent three-day interval, and creates a list containing data for all three day intervals
def ThreeDayIntervalAreas(differenceFromPreviousCloseList):
    print("Compiling a List of Three Day Intervals...")
    i = 2
    listofThreeDayIntervals = []
    while i < len(differenceFromPreviousCloseList):
        threeDayInterval = ThreeDayIntervalObject()
        threeDayInterval.updateBeginningDay(differenceFromPreviousCloseList[i-2].getDate())
        threeDayInterval.updateFinalDay(differenceFromPreviousCloseList[i].getDate())
        threeDayInterval.updateDay3Area(differenceFromPreviousCloseList[i].getTotalAreaBetweenFunctions())
        interval0Length = len(differenceFromPreviousCloseList[i].getTimeInterval0Prices())
        interval1Length = len(differenceFromPreviousCloseList[i].getTimeInterval1Prices())
        interval2Length = len(differenceFromPreviousCloseList[i].getTimeInterval2Prices())
        interval3Length = len(differenceFromPreviousCloseList[i].getTimeInterval3Prices())
        interval4Length = len(differenceFromPreviousCloseList[i].getTimeInterval4Prices())
        length3 = sum([interval0Length, interval1Length, interval2Length, interval3Length, interval4Length])
        x = np.linspace(0, length3, length3)
        threeDayInterval.updateDay3XCoords(x)
        interval0Prices = differenceFromPreviousCloseList[i].getTimeInterval0Prices()
        interval1Prices = differenceFromPreviousCloseList[i].getTimeInterval1Prices()
        interval2Prices = differenceFromPreviousCloseList[i].getTimeInterval2Prices()
        interval3Prices = differenceFromPreviousCloseList[i].getTimeInterval3Prices()
        interval4Prices = differenceFromPreviousCloseList[i].getTimeInterval4Prices()
        y = np.array(interval0Prices + interval1Prices + interval2Prices + interval3Prices + interval4Prices)
        threeDayInterval.updateDay3YCoords(y)


        closeInterval0Length0 = len(differenceFromPreviousCloseList[i-1].getTimeInterval0Prices())
        closeInterval1Length0 = len(differenceFromPreviousCloseList[i-1].getTimeInterval1Prices())
        closeInterval2Length0 = len(differenceFromPreviousCloseList[i-1].getTimeInterval2Prices())
        closeInterval3Length0 = len(differenceFromPreviousCloseList[i-1].getTimeInterval3Prices())
        closeInterval4Length0 = len(differenceFromPreviousCloseList[i-1].getTimeInterval4Prices())
        length2 = sum(
            [closeInterval0Length0, closeInterval1Length0, closeInterval2Length0, closeInterval3Length0,
             closeInterval4Length0])
        x2 = np.linspace(0, length2, length2)
        closeInterval0Prices0 = differenceFromPreviousCloseList[i-1].getTimeInterval0Prices()
        closeInterval1Prices0 = differenceFromPreviousCloseList[i-1].getTimeInterval1Prices()
        closeInterval2Prices0 = differenceFromPreviousCloseList[i-1].getTimeInterval2Prices()
        closeInterval3Prices0 = differenceFromPreviousCloseList[i-1].getTimeInterval3Prices()
        closeInterval4Prices0 = differenceFromPreviousCloseList[i-1].getTimeInterval4Prices()
        y2 = np.array(
            closeInterval0Prices0 + closeInterval1Prices0 + closeInterval2Prices0 + closeInterval3Prices0 + closeInterval4Prices0)
        threeDayInterval.updateDay2XCoords(x2)
        threeDayInterval.updateDay2YCoords(y2)
        closeInterval0Length1 = len(differenceFromPreviousCloseList[i - 1].getTimeInterval0Prices())
        closeInterval1Length1 = len(differenceFromPreviousCloseList[i - 1].getTimeInterval1Prices())
        closeInterval2Length1 = len(differenceFromPreviousCloseList[i - 1].getTimeInterval2Prices())
        closeInterval3Length1 = len(differenceFromPreviousCloseList[i - 1].getTimeInterval3Prices())
        closeInterval4Length1 = len(differenceFromPreviousCloseList[i - 1].getTimeInterval4Prices())
        length1 = sum(
            [closeInterval0Length1, closeInterval1Length1, closeInterval2Length1, closeInterval3Length1,
             closeInterval4Length1])
        x1 = np.linspace(0, length1, length1)
        closeInterval0Prices1 = differenceFromPreviousCloseList[i - 2].getTimeInterval0Prices()
        closeInterval1Prices1 = differenceFromPreviousCloseList[i - 2].getTimeInterval1Prices()
        closeInterval2Prices1 = differenceFromPreviousCloseList[i - 2].getTimeInterval2Prices()
        closeInterval3Prices1 = differenceFromPreviousCloseList[i - 2].getTimeInterval3Prices()
        closeInterval4Prices1 = differenceFromPreviousCloseList[i - 2].getTimeInterval4Prices()
        y1 = np.array(
            closeInterval0Prices1 + closeInterval1Prices1 + closeInterval2Prices1 + closeInterval3Prices1 + closeInterval4Prices1)
        threeDayInterval.updateDay1XCoords(x1)
        threeDayInterval.updateDay1YCoords(y1)



        #starting day 2

        length = len(differenceFromPreviousCloseList[i-1].getTimeInterval0Prices())
        recentCoefficients = differenceFromPreviousCloseList[-2].getTimeInterval0Function()
        historicalCoefficients = differenceFromPreviousCloseList[i-1].getTimeInterval0Function()
        z = np.poly1d(recentCoefficients)
        h = np.poly1d(historicalCoefficients)
        zdu = integrate.quad(z, 0, length)[0]
        hdu = integrate.quad(h, 0, length)[0]
        if (zdu > 0 and hdu > 0) or (zdu < 0 and hdu < 0):
            area_between_curves0 = abs(abs(zdu) - abs(hdu))
        else:
            area_between_curves0 = abs(abs(zdu) + abs(hdu))

        day2Interval0Area = area_between_curves0

        length1 = len(differenceFromPreviousCloseList[i - 1].getTimeInterval1Prices())
        recentCoefficients1 = differenceFromPreviousCloseList[-2].getTimeInterval1Function()
        historicalCoefficients1 = differenceFromPreviousCloseList[i - 1].getTimeInterval1Function()
        z1 = np.poly1d(recentCoefficients1)
        h1 = np.poly1d(historicalCoefficients1)
        zdu1 = integrate.quad(z1, 0, length1)[0]
        hdu1 = integrate.quad(h1, 0, length1)[0]
        if (zdu1 > 0 and hdu1 > 0) or (zdu1 < 0 and hdu1 < 0):
            area_between_curves1 = abs(abs(zdu1) - abs(hdu1))
        else:
            area_between_curves1 = abs(abs(zdu1) + abs(hdu1))

        day2Interval1Area = area_between_curves1

        length2 = len(differenceFromPreviousCloseList[i - 1].getTimeInterval2Prices())
        recentCoefficients2 = differenceFromPreviousCloseList[-2].getTimeInterval2Function()
        historicalCoefficients2 = differenceFromPreviousCloseList[i - 1].getTimeInterval2Function()
        z2 = np.poly1d(recentCoefficients2)
        h2 = np.poly1d(historicalCoefficients2)
        zdu2 = integrate.quad(z2, 0, length2)[0]
        hdu2 = integrate.quad(h2, 0, length2)[0]
        if (zdu2 > 0 and hdu2 > 0) or (zdu2 < 0 and hdu2 < 0):
            area_between_curves2 = abs(abs(zdu2) - abs(hdu2))
        else:
            area_between_curves2 = abs(abs(zdu2) + abs(hdu2))

        day2Interval2Area = area_between_curves2

        length3 = len(differenceFromPreviousCloseList[i - 1].getTimeInterval3Prices())
        recentCoefficients3 = differenceFromPreviousCloseList[-2].getTimeInterval3Function()
        historicalCoefficients3 = differenceFromPreviousCloseList[i - 1].getTimeInterval3Function()
        z3 = np.poly1d(recentCoefficients3)
        h3 = np.poly1d(historicalCoefficients3)
        zdu3 = integrate.quad(z3, 0, length3)[0]
        hdu3 = integrate.quad(h3, 0, length3)[0]
        if (zdu3 > 0 and hdu3 > 0) or (zdu3 < 0 and hdu3 < 0):
            area_between_curves3 = abs(abs(zdu3) - abs(hdu3))
        else:
            area_between_curves3 = abs(abs(zdu3) + abs(hdu3))

        day2Interval3Area = area_between_curves3

        length4 = len(differenceFromPreviousCloseList[i - 1].getTimeInterval4Prices())
        recentCoefficients4 = differenceFromPreviousCloseList[-2].getTimeInterval4Function()
        historicalCoefficients4 = differenceFromPreviousCloseList[i - 1].getTimeInterval4Function()
        z4 = np.poly1d(recentCoefficients4)
        h4 = np.poly1d(historicalCoefficients4)
        zdu4 = integrate.quad(z4, 0, length4)[0]
        hdu4 = integrate.quad(h4, 0, length4)[0]
        if (zdu4 > 0 and hdu4 > 0) or (zdu4 < 0 and hdu4 < 0):
            area_between_curves4 = abs(abs(zdu4) - abs(hdu4))
        else:
            area_between_curves4 = abs(abs(zdu4) + abs(hdu4))

        day2Interval4Area = area_between_curves4

        day2totalArea = day2Interval0Area + day2Interval1Area + day2Interval2Area+ day2Interval3Area + day2Interval4Area

        threeDayInterval.updateDay2Area(day2totalArea)

        # starting day 1

        length = len(differenceFromPreviousCloseList[i - 2].getTimeInterval0Prices())
        recentCoefficients = differenceFromPreviousCloseList[-3].getTimeInterval0Function()
        historicalCoefficients = differenceFromPreviousCloseList[i - 2].getTimeInterval0Function()
        z = np.poly1d(recentCoefficients)
        h = np.poly1d(historicalCoefficients)
        zdu = integrate.quad(z, 0, length)[0]
        hdu = integrate.quad(h, 0, length)[0]
        if (zdu > 0 and hdu > 0) or (zdu < 0 and hdu < 0):
            area_between_curves0 = abs(abs(zdu) - abs(hdu))
        else:
            area_between_curves0 = abs(abs(zdu) + abs(hdu))

        day1Interval0Area = area_between_curves0

        length1 = len(differenceFromPreviousCloseList[i - 2].getTimeInterval1Prices())
        recentCoefficients1 = differenceFromPreviousCloseList[-3].getTimeInterval1Function()
        historicalCoefficients1 = differenceFromPreviousCloseList[i - 2].getTimeInterval1Function()
        z1 = np.poly1d(recentCoefficients1)
        h1 = np.poly1d(historicalCoefficients1)
        zdu1 = integrate.quad(z1, 0, length1)[0]
        hdu1 = integrate.quad(h1, 0, length1)[0]
        if (zdu1 > 0 and hdu1 > 0) or (zdu1 < 0 and hdu1 < 0):
            area_between_curves1 = abs(abs(zdu1) - abs(hdu1))
        else:
            area_between_curves1 = abs(abs(zdu1) + abs(hdu1))

        day1Interval1Area = area_between_curves1

        length2 = len(differenceFromPreviousCloseList[i - 2].getTimeInterval2Prices())
        recentCoefficients2 = differenceFromPreviousCloseList[-3].getTimeInterval2Function()
        historicalCoefficients2 = differenceFromPreviousCloseList[i - 2].getTimeInterval2Function()
        z2 = np.poly1d(recentCoefficients2)
        h2 = np.poly1d(historicalCoefficients2)
        zdu2 = integrate.quad(z2, 0, length2)[0]
        hdu2 = integrate.quad(h2, 0, length2)[0]
        if (zdu2 > 0 and hdu2 > 0) or (zdu2 < 0 and hdu2 < 0):
            area_between_curves2 = abs(abs(zdu2) - abs(hdu2))
        else:
            area_between_curves2 = abs(abs(zdu2) + abs(hdu2))

        day1Interval2Area = area_between_curves2

        length3 = len(differenceFromPreviousCloseList[i - 2].getTimeInterval3Prices())
        recentCoefficients3 = differenceFromPreviousCloseList[-3].getTimeInterval3Function()
        historicalCoefficients3 = differenceFromPreviousCloseList[i - 2].getTimeInterval3Function()
        z3 = np.poly1d(recentCoefficients3)
        h3 = np.poly1d(historicalCoefficients3)
        zdu3 = integrate.quad(z3, 0, length3)[0]
        hdu3 = integrate.quad(h3, 0, length3)[0]
        if (zdu3 > 0 and hdu3 > 0) or (zdu3 < 0 and hdu3 < 0):
            area_between_curves3 = abs(abs(zdu3) - abs(hdu3))
        else:
            area_between_curves3 = abs(abs(zdu3) + abs(hdu3))

        day1Interval3Area = area_between_curves3

        length4 = len(differenceFromPreviousCloseList[i - 2].getTimeInterval4Prices())
        recentCoefficients4 = differenceFromPreviousCloseList[-3].getTimeInterval4Function()
        historicalCoefficients4 = differenceFromPreviousCloseList[i - 2].getTimeInterval4Function()
        z4 = np.poly1d(recentCoefficients4)
        h4 = np.poly1d(historicalCoefficients4)
        zdu4 = integrate.quad(z4, 0, length4)[0]
        hdu4 = integrate.quad(h4, 0, length4)[0]
        if (zdu4 > 0 and hdu4 > 0) or (zdu4 < 0 and hdu4 < 0):
            area_between_curves4 = abs(abs(zdu4) - abs(hdu4))
        else:
            area_between_curves4 = abs(abs(zdu4) + abs(hdu4))

        day1Interval4Area = area_between_curves4

        day1totalArea = day1Interval0Area + day1Interval1Area + day1Interval2Area + day1Interval3Area + day1Interval4Area

        threeDayInterval.updateDay1Area(day1totalArea)

        listofThreeDayIntervals.append(threeDayInterval)

        i += 1

    return listofThreeDayIntervals



# input: a list of objects containing data associated with the difference from the previous close (in points) for each
# minute of the day
# output: a list of objects containing data from the five most similar days to the most recent data determined by the
# area between each interval
# description: this function paarse through all of the areas calculated between the most recent data and all the historical
# data and sorts it into a list of the 5 most similar historical days based on the area between the curves of each
# interval by replacing the values in the list if they are found to be less than the values already contained in the list
def listFromLeastToGreatestAreas(differenceFromPreviousCloseList):
    print("Compiling list of previous days most similar to " + differenceFromPreviousCloseList[-1].getDate() + "...")

    listofObjectsFromLeastToMostArea = [9999999,
                                       99999999,
                                       999999999,
                                       99999999999,
                                       999999999999]
    for day in differenceFromPreviousCloseList:
        area = day.getTotalAreaBetweenFunctions()
        if area == 0:
            area += 99999

        if str(listofObjectsFromLeastToMostArea[0])[1].isdigit():
            compArea1 = listofObjectsFromLeastToMostArea[0]
        else:
            compArea1 = listofObjectsFromLeastToMostArea[0].getTotalAreaBetweenFunctions()

        if str(listofObjectsFromLeastToMostArea[1])[1].isdigit():
            compArea2 = listofObjectsFromLeastToMostArea[1]
        else:
            compArea2 = listofObjectsFromLeastToMostArea[1].getTotalAreaBetweenFunctions()

        if str(listofObjectsFromLeastToMostArea[2])[1].isdigit():
            compArea3 = listofObjectsFromLeastToMostArea[2]
        else:
            compArea3 = listofObjectsFromLeastToMostArea[2].getTotalAreaBetweenFunctions()

        if str(listofObjectsFromLeastToMostArea[3])[1].isdigit():
            compArea4 = listofObjectsFromLeastToMostArea[3]
        else:
            compArea4 = listofObjectsFromLeastToMostArea[3].getTotalAreaBetweenFunctions()

        if str(listofObjectsFromLeastToMostArea[4])[1].isdigit():
            compArea5 = listofObjectsFromLeastToMostArea[4]
        else:
            compArea5 = listofObjectsFromLeastToMostArea[4].getTotalAreaBetweenFunctions()


        if area < compArea1:
            listofObjectsFromLeastToMostArea.insert(0, day)
            listofObjectsFromLeastToMostArea.pop()
        elif area < compArea2:
            listofObjectsFromLeastToMostArea.insert(1, day)
            listofObjectsFromLeastToMostArea.pop()
        elif area < compArea3:
            listofObjectsFromLeastToMostArea.insert(2, day)
            listofObjectsFromLeastToMostArea.pop()
        elif area < compArea4:
            listofObjectsFromLeastToMostArea.insert(3, day)
            listofObjectsFromLeastToMostArea.pop()
        elif area < compArea5:
            listofObjectsFromLeastToMostArea.insert(4, day)
            listofObjectsFromLeastToMostArea.pop()

    return listofObjectsFromLeastToMostArea

# input: a list of objects containing data associated with the difference from the previous close (by percentage) for each
# minute of the day during a three day interval
# output: a list of objects containing data from the five most similar three-day intervals relatice to  the most recent data determined by the
# area between each interval
# description: this function paarse through all of the areas calculated between the most recent data and all the historical
# data and sorts it into a list of the 5 most similar historical days based on the area between the curves of each
# interval by replacing the values in the list if they are found to be less than the values already contained in the list
def ThreeDayIntervalListSort(threeDayIntervalsList):
    print("Compiling list of previous three day intervals most similar to " + threeDayIntervalsList[-1].getDayRange() + "...")

    listofObjectsFromLeastToMostArea1 = [9999999,
                                        99999999,
                                        999999999,
                                        99999999999,
                                        999999999999]
    for day in threeDayIntervalsList:
        area = day.getTotalArea()
        if area == 0.0:
            area += 99999

        if str(listofObjectsFromLeastToMostArea1[0])[1].isdigit():
            compArea1 = listofObjectsFromLeastToMostArea1[0]
        else:
            compArea1 = listofObjectsFromLeastToMostArea1[0].getTotalArea()

        if str(listofObjectsFromLeastToMostArea1[1])[1].isdigit():
            compArea2 = listofObjectsFromLeastToMostArea1[1]
        else:
            compArea2 = listofObjectsFromLeastToMostArea1[1].getTotalArea()

        if str(listofObjectsFromLeastToMostArea1[2])[1].isdigit():
            compArea3 = listofObjectsFromLeastToMostArea1[2]
        else:
            compArea3 = listofObjectsFromLeastToMostArea1[2].getTotalArea()

        if str(listofObjectsFromLeastToMostArea1[3])[1].isdigit():
            compArea4 = listofObjectsFromLeastToMostArea1[3]
        else:
            compArea4 = listofObjectsFromLeastToMostArea1[3].getTotalArea()

        if str(listofObjectsFromLeastToMostArea1[4])[1].isdigit():
            compArea5 = listofObjectsFromLeastToMostArea1[4]
        else:
            compArea5 = listofObjectsFromLeastToMostArea1[4].getTotalArea()

        if area < compArea1:
            listofObjectsFromLeastToMostArea1.insert(0, day)
            listofObjectsFromLeastToMostArea1.pop()
        elif area < compArea2:
            listofObjectsFromLeastToMostArea1.insert(1, day)
            listofObjectsFromLeastToMostArea1.pop()
        elif area < compArea3:
            listofObjectsFromLeastToMostArea1.insert(2, day)
            listofObjectsFromLeastToMostArea1.pop()
        elif area < compArea4:
            listofObjectsFromLeastToMostArea1.insert(3, day)
            listofObjectsFromLeastToMostArea1.pop()
        elif area < compArea5:
            listofObjectsFromLeastToMostArea1.insert(4, day)
            listofObjectsFromLeastToMostArea1.pop()

    return listofObjectsFromLeastToMostArea1


# input: a list of objects containing data associated with the difference from the previous close (in points) for each
# minute of the day, and a list of objects containing the data of the five most similar days found compared to the
# previous day
# output: A GUI where you are able to view the data in an organized manner, viewing which days are most similar to the
# most recent one and the similar days perfomed the next day in order to make a prediction on what will happen in the
# S&P 500 the next day
# description: this functions compiles the most recent day's data in the S&P 500, and the 5 previous days that were found to be
# similar to it from 2007 to now, and prepares the data to be graphed using a GUI where the user cn select what data they want to see.
# The graphs in the GUI include how the S&P performed in the most recent day's data, how the the 5 previous most similar days
# performed, how those 5 previous similar days performed the next day, and the average of how those 5 previous days
# performed the next day.
# modules used: tkinter for powering the GUI and making it simple for users to use
def Graph(differenceFromPreviousCloseList, areaList, threeDayAreaList, threeDayIntervalsList):
    print("Graphing days similar to " + differenceFromPreviousCloseList[-1].getDate() + "...")

    # Creating the info needed to graph the most recent day of the stock market
    interval0Length = len(differenceFromPreviousCloseList[-1].getTimeInterval0Prices())
    interval1Length = len(differenceFromPreviousCloseList[-1].getTimeInterval1Prices())
    interval2Length = len(differenceFromPreviousCloseList[-1].getTimeInterval2Prices())
    interval3Length = len(differenceFromPreviousCloseList[-1].getTimeInterval3Prices())
    interval4Length = len(differenceFromPreviousCloseList[-1].getTimeInterval4Prices())
    length1 = sum([interval0Length, interval1Length, interval2Length, interval3Length, interval4Length])
    x1 = np.linspace(0, length1, length1)
    interval0Prices = differenceFromPreviousCloseList[-1].getTimeInterval0Prices()
    interval1Prices = differenceFromPreviousCloseList[-1].getTimeInterval1Prices()
    interval2Prices = differenceFromPreviousCloseList[-1].getTimeInterval2Prices()
    interval3Prices = differenceFromPreviousCloseList[-1].getTimeInterval3Prices()
    interval4Prices = differenceFromPreviousCloseList[-1].getTimeInterval4Prices()
    y1 = np.array(interval0Prices + interval1Prices + interval2Prices + interval3Prices + interval4Prices)



    graphObjects = []

    # the five most similar days are made into objects which contain all the info needed for graphing
    i = 0
    while i < len(areaList):
        graph = GraphObject()
        closeInterval0Length0 = len(areaList[i].getTimeInterval0Prices())
        closeInterval1Length0 = len(areaList[i].getTimeInterval1Prices())
        closeInterval2Length0 = len(areaList[i].getTimeInterval2Prices())
        closeInterval3Length0 = len(areaList[i].getTimeInterval3Prices())
        closeInterval4Length0 = len(areaList[i].getTimeInterval4Prices())
        length2 = sum(
            [closeInterval0Length0, closeInterval1Length0, closeInterval2Length0, closeInterval3Length0, closeInterval4Length0])
        x2 = np.linspace(0, length2, length2)
        closeInterval0Prices0 = areaList[i].getTimeInterval0Prices()
        closeInterval1Prices0 = areaList[i].getTimeInterval1Prices()
        closeInterval2Prices0 = areaList[i].getTimeInterval2Prices()
        closeInterval3Prices0 = areaList[i].getTimeInterval3Prices()
        closeInterval4Prices0 = areaList[i].getTimeInterval4Prices()
        y2 = np.array(
            closeInterval0Prices0 + closeInterval1Prices0 + closeInterval2Prices0 + closeInterval3Prices0 + closeInterval4Prices0)

        graph.updatexCoords1(x1)
        graph.updateyCoords1(y1)
        graph.updatexCoords2(x2)
        graph.updateyCoords2(y2)
        graph.updateTitle("S&P 500 on " + differenceFromPreviousCloseList[-1].getDate() + " and " + areaList[i].getDate())
        graph.updatelabel1("S&P 500 on " + differenceFromPreviousCloseList[-1].getDate())
        graph.updatelabel2("S&P 500 on " + areaList[i].getDate())
        graphObjects.append(graph)

        i += 1


    # then, another list is made of how the days that were found to be similar performed the day after
    graphObjectsDayAfter = []
    listOfGraphsDayAfter = []
    print("Graphing day after...")
    c = 0
    while c < len(areaList):
        h = 0
        while h < len(differenceFromPreviousCloseList):
            if areaList[c] == differenceFromPreviousCloseList[h]:
                listOfGraphsDayAfter.append(differenceFromPreviousCloseList[h + 1])
            h += 1
        c += 1

    # creates a list objects containing info on how the similar days performed on their next day
    z = 0
    while z < len(listOfGraphsDayAfter):
        graph = GraphObject()
        aftercloseInterval0Length0 = len(listOfGraphsDayAfter[z].getTimeInterval0Prices())
        aftercloseInterval1Length0 = len(listOfGraphsDayAfter[z].getTimeInterval1Prices())
        aftercloseInterval2Length0 = len(listOfGraphsDayAfter[z].getTimeInterval2Prices())
        aftercloseInterval3Length0 = len(listOfGraphsDayAfter[z].getTimeInterval3Prices())
        aftercloseInterval4Length0 = len(listOfGraphsDayAfter[z].getTimeInterval4Prices())
        length3 = sum(
            [aftercloseInterval0Length0, aftercloseInterval1Length0, aftercloseInterval2Length0, aftercloseInterval3Length0,
             aftercloseInterval4Length0])
        x3 = np.linspace(0, length3, length3)
        aftercloseInterval0Prices0 = listOfGraphsDayAfter[z].getTimeInterval0Prices()
        aftercloseInterval1Prices0 = listOfGraphsDayAfter[z].getTimeInterval1Prices()
        aftercloseInterval2Prices0 = listOfGraphsDayAfter[z].getTimeInterval2Prices()
        aftercloseInterval3Prices0 = listOfGraphsDayAfter[z].getTimeInterval3Prices()
        aftercloseInterval4Prices0 = listOfGraphsDayAfter[z].getTimeInterval4Prices()
        y3 = np.array(
            aftercloseInterval0Prices0 + aftercloseInterval1Prices0 + aftercloseInterval2Prices0 + aftercloseInterval3Prices0 + aftercloseInterval4Prices0)

        graph.updatexCoords1(x3)
        graph.updateyCoords1(y3)
        graph.updateTitle(
            ("S&P 500 on day after days similar to " + differenceFromPreviousCloseList[-1].getDate()))
        graph.updatelabel1(("S&P 500 on " + listOfGraphsDayAfter[z].getDate()))
        graphObjectsDayAfter.append(graph)

        z += 1


    # finds the average of the five most similar days on the day after so it can be used to see how, on average,
    # the S&P 500 under similar circumstances perfromed the next day
    average = [statistics.mean(k) for k in zip(graphObjectsDayAfter[0].getyCoords1(), graphObjectsDayAfter[1].getyCoords1(),
                                               graphObjectsDayAfter[2].getyCoords1(), graphObjectsDayAfter[3].getyCoords1(),
                                               graphObjectsDayAfter[4].getyCoords1())]

    threeDayAreaListAfter = []
    d = 0
    while d < len(threeDayAreaList):
        u = 0
        while u < len(threeDayIntervalsList):
            if threeDayAreaList[d] == threeDayIntervalsList[u]:
                threeDayAreaListAfter.append(threeDayIntervalsList[u+3])
            u += 1
        d += 1


    averageThreeDayInterval = [statistics.mean(k) for k in zip(threeDayAreaListAfter[0].getTotalYCoords(), threeDayAreaListAfter[1].getTotalYCoords(),
                                               threeDayAreaListAfter[2].getTotalYCoords(), threeDayAreaListAfter[3].getTotalYCoords(),
                                               threeDayAreaListAfter[4].getTotalYCoords())]

    # sending all the infromation to the GUI, where its is taken and used to create a UI which can display all the graphs
    root = Tk()
    root.geometry("1500x1000")
    root.title("S&P 500 Historical Analysis")
    b = GUI(root, CurrentDayXData=x1, CurrentDayYData=y1,
            afterHistoricalAverageXData= graphObjectsDayAfter[0].getxCoords1(),
            afterHistoricalAverageYData = np.array(average),
            graphObjects= graphObjects,
            graphObjectsDayAfter= graphObjectsDayAfter, differenceFromPreviousCloseList= differenceFromPreviousCloseList,
            threeDayAfterHistoricalXData= np.linspace(0, 1173, 1173),
            threeDayAfterHistoricalYData=np.array(averageThreeDayInterval), threeDayIntervalsList= threeDayIntervalsList,
            threeDayAreaList= threeDayAreaList, threeDayAreaListAfter= threeDayAreaListAfter)



    root.mainloop()






def main():
    # creating a big list of all stock market data from each spreadsheet
    bigListofStocks = dataFrom2007to2020()


    # first turns all the data to be viewed as the difference from the previous close instead of the total value of
    # the S&P 500, then calculates the area between all the historical curves and the most recent one, then sent to a
    # function where the 5 most similar curves based on area between the curves are made into a list, and then finally
    # displayed on the GUI
    differenceToFunction(bigListofStocks)
    areaBetweenRecentCurveAndEveryOtherCurve(bigListofStocks)
    threeDayIntervalsList = ThreeDayIntervalAreas(bigListofStocks)

    areaList = listFromLeastToGreatestAreas(bigListofStocks)

    threeDayAreaList = ThreeDayIntervalListSort(threeDayIntervalsList)

    Graph(bigListofStocks, areaList, threeDayAreaList, threeDayIntervalsList)


main()