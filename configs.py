import numpy as np

class LIFneuronConfig():
    def __init__(self,):
        self.R = 5 # resistance (k-Ohm)
        self.C = 3 # capacitance (u-F)

        self.v_thresh = 30
        self.V_spike = 10

        self.tau_m = self.R*self.C # time constant (msec)
        self.refracTime = 50 # refractory time (msec)
        self.initRefrac = 0

        self.isPlot = 1



    


