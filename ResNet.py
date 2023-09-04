import tensorflow as tf

def identity_block(x,filter):
    x_skip = x
    x = tf.keras.layers.Conv2D(filter,(3,3), padding = 'Same')(x)
    x = tf.keras.layers.BatchNormalization(axis = 3)(x)
    x = tf.keras.layers.Activation('relu')(x)
    x = tf.keras.layers.Conv2D(filter,(3,3), padding = 'Same')(x)
    x = tf.keras.layers.BatchNormalization(axis = 3)(x)
    x = tf.keras.layers.Add()([x,x_skip])
    return x

def convolutional_block(x,filter):
    x_skip = x
    x = tf.keras.layers.Conv2D(filter,(3,3), padding = 'Same', strides = (2,2))(x)
    x = tf.keras.layers.BatchNormalization(axis = 3)(x)
    x = tf.keras.layers.Activation('relu')(x)
    x = tf.keras.layers.Conv2D(filter,(3,3), padding = 'Same')(x)
    x = tf.keras.layers.BatchNormalization(axis = 3)(x)
    x_skip = tf.keras.layers.Conv2D(filter,(1,1),strides = (2,2))(x_skip)
    x = tf.keras.layers.Add()([x,x_skip])
    x = tf.keras.layers.Activation('relu')(x)
    return x
    
def ResNet34(input_shape):
    x_input = tf.keras.layers.Input(input_shape)
    x = tf.keras.layers.ZeroPadding2D((3,3))(x_input)
    x = tf.keras.layers.Conv2D(64,(7,7),strides = 2,padding = 'Same')(x)
    x = tf.keras.layers.BatchNormalization(axis = 3)(x)
    x = tf.keras.layers.Activation('relu')(x)
    x = tf.keras.layers.MaxPool2D(padding = 'Same',strides = 2, pool_size = 3)(x)
    block = (3,4,6,3)
    filter_size = 64
    for r in range(4):
        if r == 0:
            for j in range(block[r]-1):
                x = identity_block(x,filter_size)
        else:
            filter_size = 2*filter_size
            x = convolutional_block(x,filter_size)
            for j in range(block[r]-1):
                x = identity_block(x,filter_size)
    x = tf.keras.layers.AveragePooling2D((2,2),padding = 'Same')(x)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(512,activation = 'relu')(x)
    x = tf.keras.layers.Dense(11,activation = 'softmax')(x)
    model = tf.keras.models.Model(inputs= x_input, outputs = x , name = 'ResNet34')
    return model


