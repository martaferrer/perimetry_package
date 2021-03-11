from perimetry import Perimetry
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

# Humphrey Field Analayzer perimeter (HFA)
# SAP with the HFA (Humphrey Zeiss Systems; 24-2 SITA Standard strategy)
# 24-2 pattern: 54 test locations
class HumphreyPerimetry(Perimetry):
    def __init__(self, perimetry, eye='OS', patient_id=0):

        Perimetry.__init__(self, total_deviation=perimetry, eye=eye,  patient_id=patient_id)


    def glaucoma_hemifield_test(self):
        '''
        Each hemifield was divided into 5 regions according to the Glaucoma Hemifield Test (GHT):
        central, paracentral, nasal, and peripheral arcuates 1 and 2.

        :return:
        '''
        # Divide the 24-2 pattern in 10 regions
        regions = []
        regions.append([0, 1, 4, 5, 6, 7])
        regions.append([2, 3, 8, 9])
        regions.append([10, 11, 18, 19, 20])
        regions.append([12, 13, 14, 15])
        regions.append([21, 22, 23])
        regions.append([26, 27, 28, 34, 35])
        regions.append([29, 30, 31])
        regions.append([36, 37, 38, 39])
        regions.append([42, 43, 44, 45, 48, 49])
        regions.append([46, 47, 50, 51])

        hemified = self.total_deviation.copy()
        for i in range(len(regions)):
            region_mean = self.total_deviation[regions[i]].mean()
            hemified.loc[regions[i]] = region_mean


        #hemified.insert(loc=0, column='patient_id', value=self.patient_id)
        print(hemified.shape)
        print(hemified)

        return hemified


    def create_image(self, mask=0, height=8, width=9):
        '''

        :param value:
        :param height:
        :param width:
        :param patient_id:
        :return:
        '''

        perimetry_array = pd.DataFrame(self.total_deviation).T

        if(height==8 and width==9):
            self._add_empty_spaces(perimetry_array, mask)
        elif(height==10 and width==10):
            # Add missing positions to create a 10x10 image
            self._add_empty_spaces(perimetry_array, mask)
            self._add_dummy_rows(perimetry_array, mask)
            self._add_dummy_columns(perimetry_array, mask)
        else:
            print('Image size not supported')
            sys.exit()

        # Print image to see if all is ok
        self._plot_image(perimetry_array.loc[0],height,width)

        # Rename data frame header and insert patient ID
        #perimetry_array.columns = range(perimetry_array.shape[1])
        #perimetry_array.insert(loc=0, value=patient_id, column='patient_id')

        #return perimetry_array

    def _add_empty_spaces(self, data, value):

        positions = [0, 1, 2, 7, 8, 9, 10, 17, 18, 34, 43, 45, 54, 55, 62, 63, 64, 65, 70, 71]
        column_name = ['0a', '1a', '2a', '7a', '8a', '9a', '10a', '17a', '18a', '34a', '43a', '45a', '54a', '55a',
                       '62a', '63a', '64a', '65a', '70a', '71a']

        for i in range(len(positions)):
            data.insert(column=column_name[i], loc=positions[i], value=value)

    def _add_dummy_rows(self, data, value):

        positions = [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]

        for pos in positions:
            data[pos] = value

        print('Add rows:', data.shape)

    def _add_dummy_columns(self, data, value):

        positions = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]
        column_name = ['9c', '19c', '29c', '39c', '49c', '59c', '69c', '79c', '89c', '99c']

        for i in range(len(positions)):
            data.insert(loc=positions[i], column=column_name[i], value=value)

        data = pd.DataFrame(data)

        print('Add columns:', data.shape)

    def _plot_image(self, vector, height, width):

        vector = np.asarray(vector)
        image_figure = vector.reshape(height, width)
        fig = plt.figure()

        img = plt.imshow(image_figure, interpolation='nearest', cmap='Blues')  # , norm=norm)
        plt.colorbar(img)

        plt.show()
