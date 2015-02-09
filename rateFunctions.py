import data
import pprint
import math
import numpy 
import matplotlib.pyplot as plt
import matplotlib.lines as lines

#import the massive district dictionary from Emily's Magick
numberOfTimeCycles = 2

#Global variables used as such:
districts = data.returnDistricsDictionary()
dataOut = [] #array to store the data about the system

#Global variables that aren't really global:
effect_worker_on_inoculation = 350000 #number of people a worker can vacinate in one time step
MAX_WORKERS_PER_PERSON = .01
DAILY_SUPPLY_PER_DISTRICT = 600000

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
            if (place['population']*place['vaccinated'][rev_keys[i]] < num_doses):
                num_doses = num_doses - place['population']*place['vaccinated'][rev_keys[i]]

                change[i] = change[i]-(place['vaccinated'][rev_keys[i]])
                change[i+1] = place['vaccinated'][rev_keys[i]]
            else:
                change[i] = change[i]-(num_doses/(place['population']*place['vaccinated'][rev_keys[i]]))
                print (num_doses/(place['population']*place['vaccinated'][rev_keys[i]]))
                change[i+1] = ((num_doses/(place['population']*place['vaccinated'][rev_keys[i]]))*place['vaccinated'][rev_keys[i]])


        for i in range(0, len(keys)):
            place['vaccinated'][rev_keys[i]] = place['vaccinated'][rev_keys[i]]+change[i]

        print place['vaccinated']
         
def infection(districts): 
    '''Calculates the effect of infection on:
        1. Population
        2. Infection'''
    for district in districts:
        place = districts[district]
        percent_infected = 0
        place['population'] = place['population']- place['infected']['100-90']*place['population']
        for i in range(0,len(keys)-2):
            place['infected'][keys[i]] = place['infected'][keys[i+1]]
            percent_infected = percent_infected + place['infected'][keys[i]]

        place['infected']['20-10'] = place['infected']['10-0'] * ((percent_infected)-(place['vaccinated']['100-90']))
        percent_infected = percent_infected + place['infected']['20-10']
        print percent_infected

        place['infected']['10-0'] = 1 - percent_infected

    
def ProceedOneTimeStep():
    '''Advances the model by one time step'''
    global districts
    global dataOut

    
    #Call all the model functions!!!
    supply(districts, DAILY_SUPPLY_PER_DISTRICT)
    inoculation(districts)
    workers(districts)
    # infection(districts)
    dataOut.append(districts)
#    pprint.pprint(dataOut)
    print 'New Cycle!!!'

def plotData():
    '''Plots the infection and vaccination rates for all districts over the time the model has been running'''

    toPlot = ('kai', 'western_urban','koinadugu')
    for district in toPlot:

        #vaccination_list = []
        infection_list = []
        #population_list = []
        l = []
        risk = 0
        pDeath = 0
        pop = 0

        for day in dataOut:

            for i in range(0, len(keys)-1):
                risk = risk + (1-i/10)*districts[district]['vaccinated'][keys[i]]
                pDeath = pDeath + i/10*districts[district]['infected'][keys[i]]

            #population_list.append(districts[district]['population'])
            #vaccination_list.append(risk)
            infection_list.append(pDeath)
            #l.append(districts[district]['workers'])


        #plt.plot(vaccination_list, label = 'Infection risk in ' + district)
        plt.plot(infection_list, label = 'Infection rate in ' + district)
        print(infection_list)
        #plt.plot(population_list)
        #plt.plot(l)

    plt.legend()
    plt.xlabel('Days')
    plt.ylabel('% of district population')
    plt.show()

if __name__ == '__main__':
    for _cycle in range(numberOfTimeCycles):
        ProceedOneTimeStep()
    #plotData()

   
    
