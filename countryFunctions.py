import math
import data

keys=('10-0','20-10','30-20','40-30','50-40','60-50','70-60','80-70','90-80','100-90')
MAX_SUPPLY = 6000000
BASE_WORKERS = 2400

districts = data.returnDistricsDictionary() 
days = 0

def supply():
	return 1 / (1 + math.exp(-days))*MAX_SUPPLY

def workers():
	return BASE_WORKERS + 100*30+days

def get_distribution():

	distribution_dict = {}

	for district in districts:	
		death_risk = 0
		for i in range(0, len(keys)):
			death_risk = death_risk + districts[district]['infected'][keys[i]]*float(i+1)/10
		distribution_dict[district] = death_risk

	factor=1.0/sum(distribution_dict.itervalues())
	normalised_d = {k: v*factor for k, v in distribution_dict.iteritems() }

	sorted_list = sorted(normalised_d.items(), key=lambda x:x[1])
	for key in sorted_list:
		if key[1] > .25:
			sorted_list.remove(key)

	sorted_list.sort(key = lambda x:abs(x[1]-.1))

	total = 0
	for key in sorted_list:
		key = list(key)
		key[1] = key[1]*districts[key[0]]['population']
		total = total + key[1]
		print key[1]

	factor = 1/total
	print factor

	final_dist = [[key[0],key[1]*factor] for key in sorted_list]
	print final_dist
	return final_dist

if __name__ == "__main__":
	total_supply = supply()
	total_workers = workers()
	distribution_list = get_distribution()
	for i in range(0, len(distribution_list)):
		districts[distribution_list[i][0]]['supply'] = total_supply*distribution_list[i][1]
	
	


		


			



