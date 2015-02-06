notes = {
	"population":"number of people in the district",
	"infected":"percent of people with n risk of death that day",
	"vaccinated":"percent of people at that risk level",
	"workers":"# of people actively vaccinating others",
	"resistance":"probability that someone will refuse vaccination",
	"education":"awareness of the drug and its effects",
	"supply": "# of doses available for that district"
}
kai_inf = { '100-90':0,
            '90-80':0,
            '80-70':0,
            '70-60':0,
            '60-50':0,
            '40-30':0,
            '30-20':0,
            '20-10':0,
            '10-0':0,}
	                
kai_vac = { '100-90':0,
            '90-80':0,
            '80-70':0,
            '70-60':0,
            '60-50':0,
            '40-30':0,
            '30-20':0,
            '20-10':0,
            '10-0':.088}
            
ken_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

ken_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':.07,
}
	                
	                
districts = {'kai': {
	            'abbrev':'kai',
	            'population':358190,	
	            'infected':kai_inf,
	            'vaccinated':kai_vac,
	            'workers':1,
	            'resistance':.25,
	            'education':.1,
	            'supply':4000
                },
                
            'ken': {
	                'abbrev':'ken',
	                'population':497948,
	                'infected': ken_inf,
	                'vaccinated':ken_vac,
	                'workers':1,
	                'resistance':.2,
	                'education':.2,
	                'supply':2000
                },
        }
'''
kono = {
	'abbrev':'kon',
	'population':497948,
	'infected': kon_inf,
	'vaccinated':kon_vac,
	'workers':1,
	'resistance':.2,
	'education':.2,
	'supply':2000
}

kon_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

kon_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':.123,
}

bombali = {
	'abbrev':'bom',
	'population':408390,
	'infected': bom_inf,
	'vaccinated':bom_vac,
	'workers':1,
	'resistance':.2,
	'education':.2,
	'supply':2000
}

bom_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

bom_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':.1,
}

kambia = {
	'abbrev':'kam',
	'population':497948,
	'infected': kam_inf,
	'vaccinated':kam_vac,
	'workers':1,
	'resistance':.2,
	'education':.2,
	'supply':2000
}

kam_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':.2,
}

kam_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

koinadugu = {
	'abbrev':'koi',
	'population':265758,
	'infected': koi_inf,
	'vaccinated':koi_vac,
	'workers':1,
	'resistance':.2,
	'education':.2,
	'supply':2000
}

koi_inf = {
	'100-90':2,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

koi_vac = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':.14,
}

port_loko = {
	'abbrev':'por',
	'population':497948,
	'infected': por_inf,
	'vaccinated':por_vac,
	'workers':1,
	'resistance':.2,
	'education':.2,
	'supply':2000
}

por_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
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
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

tonkolili = {
	'abbrev':'ton',
	'population':347197,
	'infected': kam_inf,
	'vaccinated':kam_vac,
	'workers':1,
	'resistance':.2,
	'education':.2,
	'supply':2000
}

ton_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
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
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':.07,
}

bo = {
	'abbrev':'bod',
	'population':463668,
	'infected': bod_inf,
	'vaccinated': bod_vac,
	'workers':1,
	'resistance':.2,
	'education':.2,
	'supply':2000
}

bod_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
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
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':07,
}

bonthe = {
	'abbrev':'bon',
	'population':139687,
	'infected': bon_inf,
	'vaccinated': bon_vac,
	'workers':1,
	'resistance':.2,
	'education':.2,
	'supply':2000
}

bon_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
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
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

moyamba = {
	'abbrev':'moy',
	'population':260190,
	'infected': moy_inf,
	'vaccinated': moy_vac,
	'workers':1,
	'resistance':.2,
	'education':.2,
	'supply':2000
}

moy_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
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
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

pujehun = {
	'abbrev':'puj',
	'population':228392,
	'infected': puj_inf,
	'vaccinated': puj_vac,
	'workers':1,
	'resistance':.2,
	'education':.2,
	'supply':2000
}

puj_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
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
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

western_rural = {
	'abbrev':'wer',
	'population':174249,
	'infected': wur_inf,
	'vaccinated': wur_vac,
	'workers':1,
	'resistance':.2,
	'education':.2,
	'supply':2000
}

wur_inf ={
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

wur_vac = { 
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}

western_urban = {
	'abbrev':'weu',
	'population':772873,
	'infected': weu_inf,
	'vaccinated': weu_vac,
	'workers':1,
	'resistance':.2,
	'education':.2,
	'supply':2000
}

weu_inf = {
	'100-90':0,
	'90-80':0,
	'80-70':0,
	'70-60':0,
	'60-50':0,
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
	'40-30':0,
	'30-20':0,
	'20-10':0,
	'10-0':0,
}
'''
#districts = {
#	'kai':kailahun,
#	'ken':kenema,}
''''kon':kono,
	'bom':bombali,
	'kam':kambia,
	'koi':koinadugu,
	'por':port_loko,
	'ton':tonkolili,
	'bod':bo,
	'bon':bonthe,
	'moy':moyamba,
	'puj':pujehun,
	'wer':western_rural,
	'weu':western_urban	
}
'''
#global districts

def returnDistricsDictionary():
    return districts
