import matplotlib.pyplot as plt
from tensorflow import keras
import numpy as np

if __name__ == '__main__':
    model = keras.models.load_model('model.h5')

    (trainFeatures, trainLabels), (testFeatures, testLabels) = keras.datasets.mnist.load_data()

    predictions = model.predict(testFeatures)


    for i in range(len(testFeatures)):

        modelPrediction = np.argmax(predictions[i])
        actual = testLabels[i]

        print('Close the image to show the next one')

        plt.imshow(testFeatures[i], cmap=plt.cm.binary)
        plt.title('Model says: ' + str(modelPrediction) + ', Actual: ' + str(actual))
        plt.show()



