
# coding: utf-8

#the regulars.
import numpy as np
import pandas as pd

#import files
regional_factors = pd.read_excel('CostFactorsFormatted.xlsx', sheetname = 'Sheet2')
unlabled = pd.read_excel('unknown_factors.xlsx', sheetname='sites_latlong')


#-------------Attempt using sklearn
unlabled['PROV'].unique()
#prepare data for calculations.
regional_factors.index.names = ['state','statelong']
regional_factors['State'] = regional_factors.index
statelist = []

for x in regional_factors['State'].values:
    statelist.append(x[0])
statelist
regional_factors['StateShort'] = statelist
twentyfifteensites = regional_factors[regional_factors['StateShort'].isin(unlabled['PROV'].unique())]
twentyfifteensites['Factor ID'] = "TDUS_" + twentyfifteensites['StateShort'] + "_" + twentyfifteensites['TORONTO, ONTARIO']
twentyfifteensites
siteswithIDs = twentyfifteensites[twentyfifteensites['TOTAL'] == "TOTAL"][['Factor ID','TORONTO, ONTARIO','StateShort','Unnamed: 21','Unnamed: 23','Unnamed: 24']]
siteswithIDs

from sklearn.neighbors.nearest_centroid import NearestCentroid

y = regional_factors['No'].values
#print y
X = regional_factors[['Lat','Long']].values
#print X
clf = NearestCentroid()
clf.fit(X, y)
labels = {}
for label, position in zip(y,X):
    labels[label] = position
labels.values
unlabled.head()

index = 0
unlabled['factor'] = 0
unlabled_points = unlabled[['Latitude','Longitude']].values
#for x in unlabled_dict:
#    print clf.predict(x)
#    unlabled['factor'].loc[index] = clf.predict(x)
#   index +=1
    
#print unlabled

from pandas import ExcelWriter

writer = ExcelWriter('Factors_NearestNeighbour.xlsx')
unlabled.to_excel(writer,'Sheet1')
writer.save()
#----------------End sklearn Attempt

#from the failed sklearn attempt, used the labels dictionary and unlabeled_points lat,long coordinates. 

#Brute force algorithm.
def findclosestpoi(point,pois):
    smallest = 0
    """
    if passing in list use this
    for x in pois:
        d = ((point[0] - x[0])**2 + (point[1]-x[1])**2)**.5
        if d < smallest or smallest ==0:
            smallest = d
            closestpoi = x
    """
    #for passing in a dictionary use this
    for key, value in pois.iteritems():
        d = ((point[0] - value[0])**2 + (point[1]-value[1])**2)**.5
        if d < smallest or smallest ==0:
            smallest = d
            closestpoi = key
            
    return closestpoi

index = 0
for points in unlabled_points:
    #print points 
    #print findclosestpoi(points, labels)
    unlabled['factor'].loc[index] = findclosestpoi(points, labels) # append closest regional cost factor to end of each row.
    index +=1 #potentially dangerous, this assumed order of the unlabeled points array was same as the unlabled dataframe.

from pandas import ExcelWriter

writer = ExcelWriter('Factors_NearestNeighbour.xlsx')
unlabled.to_excel(writer,'Sheet1')
writer.save()
