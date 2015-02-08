notes = {
	"population":"number of people in the district",
	"infected":"percent of people with n risk of death that day",
	"vaccinated":"percent of people at that vaccinated level", #1-susceptibility
	"workers":"# of people actively vaccinating others",
	"resistance":"probability that someone will refuse vaccination",
	"education":"awareness of the drug and its effects",
	"supply": "# of doses available for that district"
}

################################################################
####Vacination and Infection Dictionaries for all districts!####
################################################################
kai_inf = { 
    '100-90':0,
    '90-80':0,
    '80-70':0,
    '70-60':0,
    '60-50':0,
    '50-40':0,
    '40-30':0,
    '30-20':0,
    '20-10':0,
    '10-0':100,
}
	                
kai_vac = { 
    '100-90':0,
    '90-80':0,
    '80-70':0,
    '70-60':0,
    '60-50':0,
    '50-40':0,
    '40-30':0,
    '30-20':0,
    '20-10':0,
    '10-0':100
}

kai_neigh = {
	'kon':1,
	'ken':1
}
            
ken_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':100,
}

ken_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':1,}

ken_neigh = {
	'kai':1,
	'kon':1,
	'ton':1,
	'bod':1,
	'puj':1
}

kon_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':1,
}

kon_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':1,
}

kon_neigh = {
	'kai':1,
	'ken':1,
	'ton':1,
	'koi':1
}

bom_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':1,
}

bom_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':1,
}

bom_neigh = {
	'kam':1,
	'por':1,
	'ton':1,
	'koi':1
}
kam_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':1,
}

kam_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':1,
}

kam_neigh = {
	'por':1,
	'bom':1
}

koi_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':1,
}

koi_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':.14,
}

koi_neigh = {
	'bom':1,
	'ton':1,
	'kon':1
}

por_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

por_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

por_neigh = {
	'kam':1,
	'bom':1,
	'ton':1,
	'moy':1,
	'wer':1
}

ton_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

ton_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':.07,
}

ton_neigh = {
	'por':1,
	'bom':1,
	'koi':1,
	'kon':1,
	'ken':1,
	'bod':1,
	'moy':1,
	'por':1	
}

bod_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

bod_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':07,
}

bod_neigh = {
	'ton':1,
	'ken':1,
	'puj':1,
	'bon':1,
	'moy':1
}

bon_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

bon_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

bon_neigh = {
	'moy':1,
	'bod':1,
	'puj':1
}

moy_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

moy_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

moy_neigh = {
	'wer':1,
	'por':1,
	'ton':1,
	'bod':1,
	'bon':1
}

puj_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

puj_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

puj_neigh = {
	'bon':1,
	'bod':1,
	'ken':1
}

wer_inf ={
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

wer_vac = { 
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

wer_neigh = {
	'por':1,
	'moy':1,
	'weu':1
}

weu_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

weu_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'50-40':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

weu_neigh = {
	'wer':1
}
	                
#########################################
####Dictionary of ALL Dictionaries!!!####
#########################################	                
districts = {'kai': {'abbrev':'kai',
	            'population':358190,	
	            'infected':kai_inf,
	            'vaccinated':kai_vac,
	            'workers':1,
	            'education':.1,
	            'supply':4000,
	            'neighbors':kai_neigh,
                },
                
            'ken': {'abbrev':'ken',
	                'population':497948,
	                'infected': ken_inf,
	                'vaccinated':ken_vac,
	                'workers':1,
	                'education':.2,
	                'supply':2000,
	                'neighbors':ken_neigh
	                },
	                
            'kono' : {'abbrev':'kon',
	                'population':497948,
	                'infected': kon_inf,
	                'vaccinated':kon_vac,
	                'workers':1,
	                'education':.2,
	                'supply':2000,
	                'neighbors':kon_neigh
                },
                
            'bombali' : {
	                'abbrev':'bom',
	                'population':408390,
	                'infected': bom_inf,
	                'vaccinated':bom_vac,
	                'workers':1,
	                'education':.2,
	                'supply':2000,
	                'neighbors':bom_neigh
                },
                
            'kambia' : {
	                'abbrev':'kam',
	                'population':497948,
	                'infected': kam_inf,
	                'vaccinated':kam_vac,
	                'workers':1,
	                'education':.2,
	                'supply':2000,
	                'neighbors':kam_neigh
                },
                
            "koinadugu" : {
	                'abbrev':'koi',
	                'population':265758,
	                'infected': koi_inf,
	                'vaccinated':koi_vac,
	                'workers':1,
	                'education':.2,
	                'supply':2000,
	                'neighbors':koi_neigh
                },
                
            'port_loko' : {
	                'abbrev':'por',
	                'population':497948,
	                'infected': por_inf,
	                'vaccinated':por_vac,
	                'workers':1,
	                'education':.2,
	                'supply':2000,
	                'neighbors':por_neigh,
                },
                
            'tonkolili' : {
	                'abbrev':'ton',
	                'population':347197,
	                'infected': kam_inf,
	                'vaccinated':kam_vac,
	                'workers':1,
	                'education':.2,
	                'supply':2000,
	                'neighbors':ton_neigh
                },
                
                'bo' : {
	                'abbrev':'bod',
	                'population':463668,
	                'infected': bod_inf,
	                'vaccinated': bod_vac,
	                'workers':1,
	                'education':.2,
	                'supply':2000,
	                'neighbors':bod_neigh
                },

                'bonthe' : {
	                'abbrev':'bon',
	                'population':139687,
	                'infected': bon_inf,
	                'vaccinated': bon_vac,
	                'workers':1,
	                'education':.2,
	                'supply':2000,
	                'neighbors':bon_neigh
                },

                'moyamba' : {
	                'abbrev':'moy',
	                'population':260190,
	                'infected': moy_inf,
	                'vaccinated': moy_vac,
	                'workers':1,
	                'education':.2,
	                'supply':2000,
	                'neighbors':moy_neigh

                },

                'pujehun' : {
	                'abbrev':'puj',
	                'population':228392,
	                'infected': puj_inf,
	                'vaccinated': puj_vac,
	                'workers':1,
	                'education':.2,
	                'supply':2000,
	                'neighbors':puj_neigh
                },

                'western_rural' : {
	                'abbrev':'wer',
	                'population':174249,
	                'infected': wer_inf,
	                'vaccinated': wer_vac,
	                'workers':1,
	                'education':.2,
	                'supply':2000,
	                'neighbors':wer_neigh
                },

                'western_urban' : {
	                'abbrev':'weu',
	                'population':772873,
	                'infected': weu_inf,
	                'vaccinated': weu_vac,
	                'workers':1,
	                'education':.2,
	                'supply':2000,
	                'neighbors':weu_neigh
                }
        }

def returnDistricsDictionary():
    return districts
