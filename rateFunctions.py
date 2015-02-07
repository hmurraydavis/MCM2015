import data
import pprint

#import the massive district dictionary from Emily's Magick
numberOfTimeCycles = 2

#Global variables used as such:
districts = data.returnDistricsDictionary()
dataOut = [] #array to store the data about the system

#Global variables that aren't really global:
effect_worker_on_innoculation = 35 #number of people a worker can vacinate in one time step
effect_resistance_on_innoculation = 20

keys = ('100-90','90-80','80-70', '70-60','60-50','50-40','40-30','30-20','20-10','10-0')

def getInfected(district):
    return districts[district]['infected']

def getVaccinated(district):
    return districts[district]['vaccinated']

def getNeighbors(district):
    return districts[district]['neighbors']

def supply(districts):
    '''Calculate the effect of vacination supply on:
        1. innoculation
    Supply is caluclated in # of doses'''
    supply = 96
        
        
def innoculation(districts):
    '''Calculate the effect of innoculation on:
        1. # of workers
        2. infection '''
    for district in districts:
        place = districts[district]
        '''increase the number of workers'''
        if (place['workers']< MAX_WORKERS_PER_PERSON* place['population']):
            if (place['vaccinated']["10-0"] > place['population']*.01):
                place[workers] = place[workers]+1

        if(place['workers'] > MIN_WORKERS_PER_PERSON *place['population']):
            place['workers'] = place['workers']-1

def workers(districts):
    '''Calculate the effect of the number of workers on: 
        1. innoculation
        2. Education'''
    for district in districts:
        place = districts[district]
        innoculation = (effect_worker_on_innoculation*place['workers'])
        place['education'] = place['education'] + (place['workers']/4/100)
    
def resistance(districts):
    '''Calculate the effect of resistance of people to 
    receiving the drug on:
        1. infection
        2. innoculation
        3. Workers (???)'''
    for district in districts:
        place = districts[district]
        #Effect of human resistance to vacination on innoculation:
        place['innoculation'] = place['innoculation'] - effect_resistance_on_innoculation #not right!
        
        #
    
    
def education(districts):
    '''Calculate the effect of education on:
        1. RESISTANCE to being vacinated (less resistance)'''
    for district in districts:
        place = district[districts]
        place['resistance'] = place['resistance']*(1-log(place['education']))
    
    
def infection(districts): 
    '''Calculates the effect of infection on:
        1. Population'''
    for district in districts:
        place = districts[district]
        population = population - place['infection']['100-90']*population
        place['infection']['90-100'] = 0 #'''assume nobody else dies'''
        
def ProceedOneTimeStep():
    '''Advances the model by one time step'''
    global districts
    global dataOut
    
    #Call all the model functions!!!
    supply(districts)
    innoculation(districts)
    workers(districts)
    resistance(districts)
    #education(districts)
    #infection(districts)
    dataOut.append(districts)
    pprint.pprint(dataOut)
    
    ###Test that the districts data is coming in correctly: 
#    for district in districts:
#        print 'Abreviation is: ', districts[district]['abbrev']
#        print 'Population is: ', districts[district]['population'], '\n'
    

if __name__ == '__main__':
    for _cycle in range(numberOfTimeCycles):
        ProceedOneTimeStep()
    
