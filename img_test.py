import image_capture

def main():
    # for img in ['flannel.jpg', 'maroon.jpg', 'red.jpg', 'sweats2.jpg', 'sweats.jpg', 'purple.jpg', 'test.jpg', 'test2.jpg', 'jeans.jpg', 'sweatshirt.jpg']:
    for img in ['flannel.jpg', 'maroon.jpg']:
        feature_vector = image_capture.get_feature_vector('img/' + img)
        print feature_vector

        # consider combining api calls and limiting maxResults
        # sort by fraction instead of score


# Call main():
if __name__ == '__main__':
    main()