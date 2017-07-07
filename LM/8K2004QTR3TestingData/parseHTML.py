from bs4 import BeautifulSoup
import os
Path = '/home/traugerjacob/researchNCSABrunner/LM/2004QTR3/htmlTags/'
filelist = os.listdir(Path)
for i in filelist:
	with open(Path + i, 'r') as f:
		lines = f.readlines()
		html = ''
		for j in lines:
			html = html + j
		soup = BeautifulSoup(html, 'lxml')
		text = soup.findAll(text = True)
		with open('/home/traugerjacob/researchNCSABrunner/LM/2004QTR3/textOnly/' + i, 'w') as f:
			f.write(str(text))

