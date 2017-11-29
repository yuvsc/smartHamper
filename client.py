import time
import socket
import requests
import json
import sys
import image_capture
		
vects = []

def take_snapshot():
        global vects
	print('Taking snapshot...')
        vect = image_capture.get_feature_vector('image.jpg')
        vects.append(vect)
	print('Snapshot received.\n')

def submitRecs():
	'''Send HTTP request to AWS server'''
        global imgs
	print('Submitting images to database...')

	# Send images
	#print(json.dumps(imgs), type(json.dumps(imgs)))
        test = {'test': 'hi'}
	url = 'http://34.210.106.90/train?msg=' + json.dumps(test)
	response = requests.get(url)

	print('Records submitted.')


def main():
        y = 'y'
	while(y.lower() == 'y'):
            print 'Getting sample...'
            take_pic.sh
            take_snapshot() 
	    y = raw_input("Input more samples? (Y/n)\t")
        print 'Submitting samples...'
        #submitRecs()
        global vects
        print vects
        print 'Done.'

if __name__ == '__main__':
    main()
