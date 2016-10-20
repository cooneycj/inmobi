import re

gpid = re.compile('[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
idfa = re.compile('[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}')

ifile = open('tpr_inactive_maids.txt','r')
tenMB = 10*1000*1000
limit = int(tenMB/37) - 100
gpidindex = 0
idfaindex = 0
gpidcount = 0
idfacount = 0
gpidfile = open('output/validGPIDs-%i.txt' % gpidindex, 'w')
idfafile = open('output/validIDFAs-%i.txt' % idfaindex, 'w')
for line in ifile:
	if gpid.match(line):
		gpidfile.write(line)
		gpidcount+=1
		if gpidcount>limit:
			gpidfile.close()
			gpidindex+=1
			gpidfile=open('output/validGPIDs-%i.txt' % gpidindex, 'w')
			gpidcount=0
	if idfa.match(line):
		idfafile.write(line)
		idfacount+=1
		if idfacount>limit:
			idfafile.close()
			idfaindex+=1
			idfafile=open('output/validIDFAs-%i.txt' % idfaindex, 'w')
			idfacount=0
gpidfile.close()
idfafile.close()



