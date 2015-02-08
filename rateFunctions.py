import data
import pprint
import math
import numpy 
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import random
import copy

#import the massive district dictionary from Emily's Magick
numberOfTimeCycles = 360

global districts
#global dataOut

#Global variables used as such:
districts = data.returnDistricsDictionary()
dataOut = [] #array to store the data about the system



#Global variables that aren't really global:
effect_worker_on_inoculation = 400 #number of people a worker can vacinate in one time step
MAX_WORKERS_PER_PERSON = .01
DAILY_SUPPLY_PER_DISTRICT = 600000
THRESHOLD_FOR_MORE_WORKERS = .75

keys=('10-0','20-10','30-20','40-30','50-40','60-50','70-60','80-70','90-80','100-90')
rev_keys = tuple(reversed(keys))

def supply(districts, doses=DAILY_SUPPLY_PER_DISTRICT):
    '''Calculate the effect of vaccination supply on:
        1. inoculation
    Supply is calculated in # of doses'''
    for district in districts:
        place = districts[district]
        place['supply'] = place['supply']- (place['workers']*effect_worker_on_inoculation) +doses
        if place['supply'] < 0:
            place['supply'] = 0
        # print 'supply is:', place['supply']
    #TODO: Check that supply is actually correct. Changes but is more or less uniform across districts. 
        
def inoculation(districts):
    '''Calculate the effect of inoculation on:
        2. infection'''
    for district in districts:
        place = districts[district]
        av_vac = 0
        for i in range(0, len(keys)):
            av_vac = av_vac + ((i+1)/10)*place['vaccinated'][keys[i]]

        for i in range(1, len(keys)):
            percent_change = place['infected'][keys[i]]*(1-av_vac)
            place['infected'][keys[i-1]] = place['infected'][keys[i-1]]+percent_change
            place['infected'][keys[i]]= place['infected'][keys[i]]-percent_change

def workers(districts):
    '''Calculate the effect of the number of workers on: 
        1. inoculation'''
    for district in districts:
        place = districts[district]

        num_doses = supply
        if num_doses > place['workers']*effect_worker_on_inoculation:
            num_doses = place['workers']*effect_worker_on_inoculation

        change = [0,0,0,0,0,0,0,0,0,0]

        for i in range(0,len(keys)-1):
            if (place['population']*place['vaccinated'][rev_keys[i]] <= num_doses):
                num_doses = num_doses - place['population']*place['vaccinated'][rev_keys[i]]

                change[i] = change[i]-(place['vaccinated'][rev_keys[i]])
                change[i+1] = place['vaccinated'][rev_keys[i]]

            else:
                change[i] = change[i]-(num_doses/(place['population']*place['vaccinated'][rev_keys[i]]))
                change[i+1] = ((num_doses/(place['population']*place['vaccinated'][rev_keys[i]]))*place['vaccinated'][rev_keys[i]])
                num_doses = 0

        for i in range(0, len(keys)):
            place['vaccinated'][rev_keys[i]] = place['vaccinated'][rev_keys[i]]+change[i]
            if place['vaccinated'][rev_keys[i]] < 0:
                place['vaccinated'][rev_keys[i]] = 0
        
def infection(districts): 
    '''Calculates the effect of infection on:
        1. Population
        2. Infection
        3. Workers'''
    for district in districts:
        place = districts[district]
        prev_pop = place['population']
        total_infected = 0
        avg_inf = 0

        change = [0,0,0,0,0,0,0,0,0,0,0]

        for i in range(0, len(keys)):
            change[i+1]= place['infected'][keys[i]]*(float(numpy.random.randint(int(i*10),int((i+1)*10)))/100)
            change[i] = change[i] - change[i+1]

        for i in range(0, len(keys)):
            place['infected'][keys[i]] = place['infected'][keys[i]] + change[i]

        place['population'] = place['population'] - place['population']*change[10]

        if place['population'] > 0:
            for i in range(0,len(keys)):
                place['infected'][keys[i]] = place['infected'][keys[i]]*prev_pop/place['population']
                avg_inf = avg_inf + (i+1)/10*place['infected'][keys[i]]

            if (avg_inf > THRESHOLD_FOR_MORE_WORKERS):
                place['workers'] = place['workers']+1
  
def ProceedOneTimeStep():
    #Call all the model functions!!!
    supply(districts, DAILY_SUPPLY_PER_DISTRICT)
    inoculation(districts)
    workers(districts)
    infection(districts)
    dataOut.append(copy.deepcopy(districts))
#    pprint.pprint(dataOut)
    print 'New Cycle!!!'

def plotData():
    '''Plots the infection and vaccination rates for all districts over the time the model has been running'''

    toPlot = ('kai', 'western_urban','koinadugu')
    for district in toPlot:

        vaccination_list = []
        infection_list = []

        
        for i in range(0, len(dataOut)):
            #print i
            #print dataOut[i]['kai']['vaccinated']
            district_list = dataOut[i]
            risk_avg = 0
            inf_avg = 0

            for i in range(0,len(keys)):
                risk_avg = risk_avg + district_list[district]['vaccinated'][keys[i]]*(float(i+1)/10) 
                inf_avg = inf_avg + district_list[district]['infected'][keys[i]]*(float(i+1)/10)

            vaccination_list.append(risk_avg)
            infection_list.append(inf_avg)

        plt.plot(vaccination_list, label = 'Average infection risk in '+ district)
        plt.plot(infection_list, label = 'Average death risk in ' +district)

    plt.legend()
    plt.xlabel('Days')
    plt.ylabel('% of district population')
    plt.show()

if __name__ == '__main__':
    for _cycle in range(numberOfTimeCycles):
        ProceedOneTimeStep()
    plotData()

   
    
