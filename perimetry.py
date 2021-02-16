import pandas as pd

# Visual function assessment is integral to the evaluation and management of glaucoma.
# https://eyewiki.aao.org/Standard_Automated_Perimetry#Target_size_and_luminance
class Perimetry:
    def __init__(self, perimetry, eye='OS'):
        self.eye = eye
        self.perimetry = perimetry


    def CreateGlaucomaHemifield():
        print()

    def VisualFieldIndex():
        print()

    def CalculatePatternStandardDeviation():
        '''
        Visual field loss in glaucoma is frequently non-uniform, and thus a measure which quantifies irregularities
        is desirable. Pattern standard deviation (PSD) measures irregularity by summing the absolute value of the
        difference between the threshold value for each point and the average visual field sensitivity at each point
         (equal to the normal value for each point + the MD). Visual fields with the age-normal sensitivity at each
         point will have a PSD of 0, as will visual fields in which each point is uniformly depressed from the
         age-normal value. Thus, the largest PSD will be registered for focal, deep visual field defects.
         Near-normal and severely damaged visual fields will both have low PSD.


        :return:
        '''

    def CalculateMeanDeviation():
        '''
        The average of these deviations across all test locations is referred to as the Mean Deviation (MD).
        Subjects, who are able to see dimmer stimuli than others of similar age and race will have positive values
        for their MD, while subjects who require brighter stimuli will have negative MD values. MD values for reliable
        tests typically range from +2 dB to -30 dB.
        :return:
        '''

    def ConvertTo52TestLocations(linear_vector):
        # Remove two rows and one column of patching
        drop = [0,1,2,7,8,9,10,11,18,19,20,30,37,40,47,49,50,59,60,61,68,69,70,71,72,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
        linear_vector = linear_vector.drop(drop,  axis=1)

        return linear_vector

    def CreateImage10x10(data, value):
        patient_id = data['patient_id']
        modified_data = data.drop('patient_id', axis=1)

        # Add missing positions to create a 10x10 image
        AddEmptySpaces(modified_data, value)
        AddDummyRows(modified_data, value)
        AddDummyColumn(modified_data, value)

        # Print image to see if all is ok
        # DisplayImage(modified_data.loc[0],10,10)

        # Rename data frame header and insert patient ID
        modified_data.columns = range(modified_data.shape[1])
        modified_data.insert(loc=0, value=patient_id, column='patient_id')

        return modified_data


# path = 'insel_data_exported_23_08_2017_anonymized.csv'
#
# df = pd.read_csv('insel_data_exported_23_08_2017_anonymized.csv', sep='\t', encoding='unicode_escape')
#
# header = df.head()
# print(header)
# col = []
# for i in range(df.shape[0]):
#     col.append(str(df.values[i]).split(';'))
#
# pf2 = pd.DataFrame(col, header)
# print('Original dataset shape: ', df.shape)
# print(df.columns)
# print(df2.shape)