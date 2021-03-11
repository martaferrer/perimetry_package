import numpy as np
import pandas as pd
from .humphrey_perimetry import HumphreyPerimetry

from csv import reader

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

def ReadOriginalDataset():

    path = 'data/insel_data_exported_23_08_2017_anonymized.csv'

    # open file in read mode
    with open(path, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            columns = row[0].split(';')
            print(len(columns))
            # row variable is a list that represents a row in csv
            #print(row)



data = GetRotterdamDataset()
patient_id = data.loc[0]['patient_id']
total_deviation = data.iloc[0].drop(labels=['patient_id'])
print('Total deviation length', total_deviation.shape[0])

perimetry = HumphreyPerimetry(perimetry=total_deviation)
#perimetry.create_image(mask=0)
#perimetry.create_image(mask=0, height=10, width=10)
hemified = perimetry.glaucoma_hemifield_test()
perimetry.create_image(hemified)
