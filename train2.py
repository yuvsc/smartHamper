import time
import os
import socket
import requests
import json
import sys
import image_capture
from subprocess import call

fp = '/smartHamper/train/'
vects = []

def take_snapshot(img):
        global vects
        vect = image_capture.get_feature_vector(fp+img)
        vects.append(vect)
	print('Snapshot received.\n')

def submitRecs():
	'''Send HTTP request to AWS server'''
        global vects
	print('Submitting images to database...')

	# Send images
	#print(json.dumps(imgs), type(json.dumps(imgs)))
        #test = {'test': 'hi'}
	url = 'http://34.210.106.90/train?msg=' + json.dumps(vects)
	response = requests.get(url)

	print('Records submitted.')


def main():
    for img in os.listdir(fp):
        print img
        take_snapshot(img)
    submitRecs()
    global vects
    print vects
    print 'Done.'

if __name__ == '__main__':
    main()
