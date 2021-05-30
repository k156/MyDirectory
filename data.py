#2016-08-01부터 2018-07-31까지.
#20161001 ~ 20180630

import csv, codecs
from pprint import pprint
import numpy as np

fp = codecs.open("train.csv", "r", encoding = "MS949")
reader = csv.reader(fp, delimiter=',', quotechar='"')
data = []
for cells in reader:
    if cells[0] == "store_id":
        pass
	# data.append([cells[1], cells[4]])
    else:
        data.append([int(cells[1].replace('-','')), int(cells[4])])


for d in data:
    if d[0] 