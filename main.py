from range_sensor import *
from subprocess import call
import image_capture

def main():
    range_init()
    while(1):
        dist = get_dist()
        print dist
        if dist < 30:
            print 'Interrupt'
            clss = classify_laundry()
            # <MOVE MOTORS>
            print 'sleeping...'
            break
            time.sleep(5)

    # Never gets called
    GPIO.cleanup()

def classify_laundry():
    # Take picture
    call(['./take_pic.sh'])

    feature_vector = image_capture.get_feature_vector('image.jpg')
    print feature_vector

    # Pass into SVM
    clss = 0
    return clss 
# Call main()
main()
