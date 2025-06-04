from tensorflow.keras.models import load_model as keras_load_model

def load_model(path = "C:\model\my_model_v2.h5" ):
    
    model = keras_load_model(path)
    
    return model