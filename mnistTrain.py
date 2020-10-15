import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Flatten


if __name__ == '__main__':
    model = Sequential()
    model.add(Flatten())
    model.add(Dense(256, activation=tf.nn.relu))
    model.add(Dense(64, activation=tf.nn.relu))
    model.add(Dense(10, activation=tf.nn.softmax))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    (trainFeatures, trainLabels), (testFeatures, testLabels) = tf.keras.datasets.mnist.load_data()

    trainFeatures = tf.keras.utils.normalize(trainFeatures, axis=1)
    testFeatures = tf.keras.utils.normalize(testFeatures, axis=1)

    model.fit(trainFeatures, trainLabels, epochs=3)

    tf.keras.models.save_model(model, 'model.h5')
