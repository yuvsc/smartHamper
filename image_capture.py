# get common labels
# consider combining api calls and limiting maxResults
# sort by fraction instead of score

from google.cloud import vision
from google.cloud.vision import types
import io
import os

API_KEY =  "AIzaSyDyp0yvPqn1MrJDGNpHkCSQCek5RsSW8oM"
LABEL_WEIGHT = 100
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/smartHamper/Smartwatch-001b7770899b.json'

def detect_colors(path):
    """Detects image properties in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    
    # print('Properties:')

    # for color in props.dominant_colors.colors:
    #     print('fraction: {}'.format(color.pixel_fraction))
    #     print('\tr: {}'.format(color.color.red))
    #     print('\tg: {}'.format(color.color.green))
    #     print('\tb: {}'.format(color.color.blue))
    #     print('\ta: {}'.format(color.color.alpha))

    colors = []
    for color in props.dominant_colors.colors[:2]:
        # colors.append([[color.color.red, color.color.green, color.color.blue], color.pixel_fraction])
        colors.append([color.color.red, color.color.green, color.color.blue])
    return colors

def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    label_names = []
    for label in labels:
        label_names.append(str(label.description))

    return label_names

def get_feature_vector(path):
    labels = detect_labels(path)
    colors = detect_colors(path)

    # feature_vector = [label_val, R, G, B]

    # Get label_val
    if 't shirt' in labels or 'shirt' in labels or 'sleeve' in labels or 'top' in labels:
        label_val = 1*LABEL_WEIGHT 
    elif 'trousers' in labels or 'denim' in labels or 'jeans' in labels:
        label_val = 2*LABEL_WEIGHT
    elif 'brand' in labels or 'text' in labels or 'font' in labels:
        label_val = 3*LABEL_WEIGHT
    else:
        label_val = 0

    r, g, b = colors[0]

    return [label_val, r, g, b]


"""
Label Results:
['plaid', 'tartan', 'pattern', 'maroon', 'textile', 'design', 'outerwear', 'material']
['t shirt', 'red', 'pink', 'sleeve', 'maroon', 'magenta', 'product', 'outerwear', 'shirt', 'font']
['red', 't shirt', 'text', 'maroon', 'font', 'product', 'outerwear', 'textile', 'sleeve', 'product']
['outerwear', 'dress', 'velvet', 'coat', 'sleeve']
['dress', 'outerwear', 'trousers']
['purple', 'pink', 'violet', 'lilac', 'lavender', 'textile', 'outerwear', 'button', 'sleeve']
['outerwear', 'jacket', 'shoulder', 'textile', 'girl', 'top', 'neck']
['bag', 'shoulder', 'fashion', 'product', 'outerwear', 'jacket']
['denim', 'jeans', 'shoulder', 'outerwear', 'textile', 'pocket', 'trousers', 'button', 'pattern', 'plaid']
['t shirt', 'sleeve', 'product', 'outerwear', 'product', 'shirt', 'font', 'hoodie', 'top', 'brand']

Good ones:
t shirt, shirt, sleeve
font, text, brand
trousers, denim, jeans

hoodie?
"""


