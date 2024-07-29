import cv2
import numpy as np


SIZE_IMAGE = 20
NUMBER_CLASSES = 10

def load_digits_and_labels(img_path):
    digits_img = cv2.imread(img_path)

    number_rows = digits_img.shape[1] / SIZE_IMAGE
    rows = np.vsplit(digits_img, digits_img.shape[0] / SIZE_IMAGE)
    
    digits = []
    for row in rows:
        row_cells = np.hsplit(row, row.shape[1]/SIZE_IMAGE)

        for digit in row_cells:
            digits.append(digit)

    
    digits = np.array(digits)
    labels = np.repeat(np.arange(NUMBER_CLASSES), len(digits)/NUMBER_CLASSES)
    return digits, labels


def raw_pixels(img):
    """Return raw pixels as feature from the image"""

    return img.flatten()

#create knn classifier
digits, labels = load_digits_and_labels("resources/digits.png")


# Shuffle data
# Constructs a random number generator:
rand = np.random.RandomState(1234)
# Randomly permute the sequence:
shuffle = rand.permutation(len(digits))
digits, labels = digits[shuffle], labels[shuffle]

raw_descriptors = []
for img in digits:
    raw_descriptors.append(np.float32(raw_pixels(img)))

raw_descriptors = np.squeeze(raw_descriptors)


partition = int(0.5*len(raw_descriptors))
print(partition)
raw_descriptors_train, raw_descriptors_test = np.split(raw_descriptors,[partition])
labels_train, labels_test = np.split(labels, [partition])

print(raw_descriptors.shape)

print('Training KNN model - raw pixels as features')
knn = cv2.ml.KNearest_create()
knn.train(raw_descriptors_train, cv2.ml.ROW_SAMPLE, labels_train)


k = 5
ret, result, neighbours, dist = knn.findNearest(raw_descriptors_test, k)




# Compute the accuracy:
def get_accuracy(predictions, labels):
    """Returns the accuracy based on the coincidences between predictions and labels"""

    accuracy = (np.squeeze(predictions) == labels).mean()
    return accuracy * 100


acc = get_accuracy(result, labels_test)
print("Accuracy: {}".format(acc))