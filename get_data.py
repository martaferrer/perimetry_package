import numpy as np
import pandas as pd
from Perimetry import Perimetry

def GetRotterdamDataset():
    '''
    Visual fields were acquired on a Humphrey Visual Field Analyzer (Carl Zeiss Meditec) with a standard
    white-on-white 24-2 field with the full threshold program.

    :return: data set of 52 positions perimetry inclusing the patient id
    '''

    print('Loading Normal Rotterdam dataset')

    original_data = np.load('data/rotterdam_data.npz')

    data = pd.DataFrame(original_data.f.loc52)
    eye_id = np.asarray(original_data.f.eyeId)
    data.insert(0, column='patient_id', value=eye_id)

    return data


data = GetRotterdamDataset()
example = data.iloc[0].drop(labels=['patient_id'])

perimetry = Perimetry(example)