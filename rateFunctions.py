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
effect_worker_on_inoculation = 35 #number of people a worker can vacinate in one time step
effect_resistance_on_inoculation = 20
MAX_WORKERS_PER_PERSON = .01
MIN_WORKERS_PER_PERSON = .001

DOSES_PER_WORKER_PER_DAY = 50

keys = ('100-90','90-80','80-70', '70-60','60-50','50-40','40-30','30-20','20-10','10-0')

def getInfected(district):
    return districts[district]['infected']

def getVaccinated(district):
    return districts[district]['vaccinated']

def getNeighbors(district):
    return districts[district]['neighbors']

def supply(districts, doses):
    '''Calculate the effect of vaccination supply on:
        1. inoculation
    Supply is calculated in # of doses'''
    for district in districts:
        place = districts[district]
        place['supply'] = place['supply']- place['workers']*DOSES_PER_WORKER_PER_DAY+doses
        
def inoculation(districts):
    '''Calculate the effect of inoculation on:
        1. # of workers
        2. infection '''
    for district in districts:
        place = districts[district]
        '''increase the number of workers'''
        if (place['workers']< MAX_WORKERS_PER_PERSON* place['population']):
            sumrisk=place['vaccinated']['100-90']+place['vaccinated']['90-80']+place['vaccinated']['80-70']
            if (sumrisk > .2):
                place['workers'] = place['workers']+1

        if(place['workers'] > MIN_WORKERS_PER_PERSON *place['population']):
            place['workers'] = place['workers']-1

def workers(districts):
    '''Calculate the effect of the number of workers on: 
        1. inoculation
        2. Education'''
    for district in districts:
        place = districts[district]
        num_doses = place['workers']*DOSES_PER_WORKER_PER_DAY
        for i in range(len(keys)-1):
            if (place['population']*place['vaccinated'][keys[i]] < num_doses):
                num_doses = num_doses - place['population']*place['vaccinated'][keys[i]]
                place['vaccinated'][keys[i+1]] = place['vaccinated'][keys[i]]

        place['education'] = place['education'] + (place['workers']/400)
    
def resistance(districts):
    '''Calculate the effect of resistance of people to 
    receiving the drug on:
        1. infection
        2. inoculation
        3. Workers (???)'''
    for district in districts:
        place = districts[district]
        #Effect of human resistance to vacination on inoculation:
        for risk_level in place['vaccinated']:
            place['vaccinated'][risk_level] = place['vaccinated'][risk_level]*(1-place['resistance'])

        #
    
def education(districts):
    '''Calculate the effect of education on:
        1. RESISTANCE to being vacinated (less resistance)'''
    for district in districts:
        place = districts[district]
        place['resistance'] = place['resistance']*(place['education'])
    
    
def infection(districts): 
    '''Calculates the effect of infection on:
        1. Population'''
    for district in districts:
        place = districts[district]
        percent_infected = 0
        place['population'] = place['population']- place['infected']['100-90']*place['population']
        for i in range(0,len(keys)-2):
            place['infected'][keys[i]] = place['infected'][keys[i+1]]
            percent_infected = percent_infected + place['infected'][keys[i]]

        place['infected']['20-10'] = place['infected']['10-0'] * (percent_infected)-(place['vaccinated']['100-90'])
        percent_infected = percent_infected + place['infected']['20-10']

        place['infected']['10-0'] = 1 - percent_infected

    
def ProceedOneTimeStep():
    '''Advances the model by one time step'''
    global districts
    global dataOut

    
    #Call all the model functions!!!
    supply(districts, 100)
    inoculation(districts)
    workers(districts)
    resistance(districts)
    education(districts)
    infection(districts)
    dataOut.append(districts)
    pprint.pprint(dataOut)
    
    ###Test that the districts data is coming in correctly: 
#    for district in districts:
#        print 'Abreviation is: ', districts[district]['abbrev']
#        print 'Population is: ', districts[district]['population'], '\n'

def plotDatum(parameter, district):
    to_plot = []

    for day in dataOut:
        to_plot.append(day[district][parameter])

    return plt.plot(to_plot)
    #plt.show()

def plotDistricts(parameter):

    data = []
    names = []
    for district in districts:
        data.append(plotDatum(parameter, district))
        names.append(district)

    plt.figlegend(data,names,'upper right')
    plt.title(parameter)
    plt.xlabel("Days")
    plt.ylabel(parameter)
    plt.show()
    


    

if __name__ == '__main__':
    for _cycle in range(numberOfTimeCycles):
        ProceedOneTimeStep()
    
