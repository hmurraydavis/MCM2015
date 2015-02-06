#import the massive district dictionary from Emily's Magick
numberOfTimeCycles = 4

#Global variables used as such:
districts = {}
dataOut = [] #array to store the data about the system

#Global variables that aren't really global:
effect_worker_on_innoculation = 35 #number of people a worker can vacinate in one time step
effect_resistance_on_innoculation = 20

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
        '''increase the number of workers'''
        if (district[workers]< .6* district[population]):
            if (district[vaccinated["0-10"]] > district[population]*.01){
                district[workers] = district[workers]+1

        if(district[workers] > .1 *district[population]):
            district[workers] = district[workers]-1

def workers(districts):
    '''Calculate the effect of the number of workers on: 
        1. innoculation
        2. Education'''
    for district in districts:
        innoculation = (effect_worker_on_innoculation*district['workers'])
        education = education + workers/4/100
    
def resistance(districts):
    '''Calculate the effect of resistance of people to 
    receiving the drug on:
        1. infection
        2. innoculation
        3. Workers (???)'''
    for _cycle in range(numberOfTimeCycles):
        for district in districts:
            innoculation = district['innoculation'] - effect_resistance_on_innoculation #not right!
    
    
def education(districts):
    '''Calculate the effect of education on:
        1. RESISTANCE to being vacinated (less resistance)'''
        for district in districts:
            district[resistance] = district[resistance]*(1-log(district[education]))
    
    
def infection(districts): 
    '''Calculates the effect of infection on:
        1. Population'''
    for district in districts:
        population = population - district[infection[90-100]]*population
        district[infection[90-100]] = 0'''assume nobody else dies'''
        
def ProceedOneTimeStep():
    '''Advances the model by one time step'''
    global districts
    global dataOut
    
    #Call all the model functions!!!
    supply(districts)
    innoculation(districts)
    workers(districts)
    resistance(districts)
    education(districts)
    infection(districts)
    dataOut.append(districts)
    print dataOut
    

if __name__ == '__main__':
    for _cycle in range(numberOfTimeCycles):
        ProceedOneTimeStep()
    
