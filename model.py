from tensorflow.keras.models import load_model as keras_load_model

def load_model(path = "my_model_v3.keras" ):
    
    model = keras_load_model(path)
    
    return model