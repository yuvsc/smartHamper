- Install Google Vision API
	sudo pip install --upgrade google-cloud-vision

- Install urequests
	sudo pip install urequests

- Get JSON with API key from
	https://console.cloud.google.com/iam-admin/serviceaccounts/project?project=buoyant-arcanum-151300
	Options
	Create key
	JSON

- Set env var to find JSON from prev step
export GOOGLE_APPLICATION_CREDENTIALS="/Users/jonathanherman/Desktop/IoT/SmartHamper/Smartwatch-001b7770899b.json"

- Enable API key
	https://console.developers.google.com/apis/api/vision.googleapis.com/overview?project=buoyant-arcanum-151300
