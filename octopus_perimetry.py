from perimetry import Perimetry

# Octopus perimeter (OP)
# SAP with the OP (Haag-Streit International; TOP test strategy).
# Test positions: G-pattern, containing 59
class OctopusPerimetry:
    def __init__(self, perimetry, eye='OS'):

        Perimetry.__init__(self, perimetry, eye)