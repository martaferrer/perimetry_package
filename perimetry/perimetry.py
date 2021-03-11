import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Visual function assessment is integral to the evaluation and management of glaucoma.
# https://eyewiki.aao.org/Standard_Automated_Perimetry#Target_size_and_luminance
# https://www.reviewofoptometry.com/article/sharpen-your-visual-field-interpretation-skills
class Perimetry:
    def __init__(self, total_deviation=None, eye='OS', patient_id = 0, pattern_deviation=None):
        self.eye = eye
        self.patient_id = patient_id
        self.num_positions = len(total_deviation)

        # “raw data” in decibels (dB)
        #  visual field that are different from a “normal” patient’s field of the same age.
        if total_deviation is not None:
            self.total_deviation = total_deviation

        if pattern_deviation is not None:
            self.pattern_deviation = pattern_deviation


    def set_patient_id(self, patient_id):
        self.patient_id = patient_id

    def TransformRightToLeftEye(self):
        '''
        Left eyes were converted to a right eye format.
        :return:
        '''

    def CalculateMeanDeviation(self):
        '''
        The average of these deviations across all test locations is referred to as the Mean Deviation (MD).
        Subjects, who are able to see dimmer stimuli than others of similar age and race will have positive values
        for their MD, while subjects who require brighter stimuli will have negative MD values. MD values for reliable
        tests typically range from +2 dB to -30 dB.
        :return:
        '''
        mean_deviation = self.total_deviation.mean(axis=1)

        return mean_deviation

    def GetDiseaseSeverity(self):
        '''

        :return:
        '''
        mean_deviation = self.CalculateMeanDeviation()

        glaucoma_type = []
        for i in range(len(mean_deviation)):
            if mean_deviation.loc[i] <= -12:
                glaucoma_type.append('Advanced')
            elif -12 < mean_deviation.loc[i] < -6:
                glaucoma_type.append('Moderate')  # early glaucoma
            elif mean_deviation.loc[i] >= -6:
                glaucoma_type.append('Mild')  # mild??

        return glaucoma_type

