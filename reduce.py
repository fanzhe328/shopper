## reduce transactions by category
from datetime import datetime

loc_offers = "data\\offers.csv"
loc_transactions = "data\\transactions.csv"
#loc_reduced = "shop\\reduced_category.csv" # will be created
loc_reduced = "data\\reduced_company.csv"

def reduce_data(loc_offers, loc_transactions, loc_reduced):
	start = datetime.now()
	# get all categories on offer in a dict, if company ,then
	# offers[line.split(",")[3] ] = 1   ## 1
	offers = {}
	for e, line in enumerate(open(loc_offers)):
		offers[line.split(",")[3] ] = 1
	#open output file
	with open(loc_reduced, "wb") as outfile:
		#go through transactions file and reduce
		reduced = 0
		for e, line in enumerate( open(loc_transactions) ):
			if e== 0:
				outfile.write(line) #print header
			else:
				# only write when category in offers dict, if company, then
				# if line.split(",")[4] in offers:  ## 3
				if line.split(",")[4] in offers:
					outfile.write(line)
					reduced += 1
				#progress
				if e % 5000000 == 0:
					print e,reduced, datetime.now() - start
		print e,reduced,datetime.now() - start


if __name__ == "__main__":
	reduce_data(loc_offers,loc_transactions,loc_reduced)