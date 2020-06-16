from django.apps import AppConfig
from django.conf import settings
import os
import pickle

class PredictorConfig(AppConfig):
    name = 'predictor'

    # create path to models
    path = os.path.join(settings.MODELS, 'models.p')
 
    # load models into separate variables
    # these will be accessible via this class
    data = {}
    with open(path, 'rb') as pickled:
        # unpickler = pickle.Unpickler(pickled)
        # data = unpickler.load()
        data = pickle.load(pickled)
        
    regressor = data['regressor']
    vectorizer = data['vectorizer']