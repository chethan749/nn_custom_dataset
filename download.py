import requests
import argparse
import os
import cv2
import glob

parser = argparse.ArgumentParser()

parser.add_argument('-u', type = str, required = True, help = 'Path to urls.txt')
parser.add_argument('-p', type = str, required = True, help = 'Path to folder for image download')

args = vars(parser.parse_args())

urls = open(args['u']).read().strip().split('\n')
total = 0

for url in urls:
	try:
		r = requests.get(url)
		
		p = os.path.sep.join([args['p'], 'img' + '{}.jpg'.format(total).zfill(8)])
		with open(p, 'wb') as fp:
			fp.write(r.content)
		
		print('Downloaded:', p)
		total += 1
	
	except:
		print('Error downloading:', p)

for image in glob.glob(args['p'] + '/*'):
	delete = False
	try:
		img = cv2.imread(image)
		
		if img is None:
			delete = True
	except:
		print('Error')
		delete = True
	
	if delete:
		print('Deleting:', image)
		os.remove(image)

