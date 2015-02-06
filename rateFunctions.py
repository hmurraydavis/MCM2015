#import the massive district dictionary from Emily's Magick
numberOfTimeCycles = 4

districts = {}
dataOut = [] #array to store the data about the system

def supply(districts):
    '''Calculate the effect of vacination supply on:
        1. innoculation
    Supply is caluclated in # of doses'''
    supply = 96
        
        
def innoculation(districts):
    '''Calculate the effect of innoculation on:
        1. # of workers
        2. infection '''
    
def workers(districts):
    '''Calculate the effect of the number of workers on: 
        1. innoculation
        2. Infection
        3. Education'''
    
def resistance(districts):
    '''Calculate the effect of resistance of people to 
    receiving the drug on:
        1. infection
        2. vacination
        3. Workers (???)'''
    
    
def education(districts):
    '''Calculate the effect of education on:
        1. RESISTANCE to being vacinated (less resistance), and
        2. VACINATION (increase in # of shots)'''
    
    
def infection(districts): 
    '''Calculates the effect of infection on:
        1. Population'''
        
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
    
