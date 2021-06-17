import numpy as np

class LIFneuronConfig():
    def __init__(self,):
        self.R = 5 # resistance (k-Ohm)
        self.C = 3 # capacitance (u-F)

        self.v_thresh = 30
        self.v_spike = 10
        self.v_base = -1
        
        self.tau_m = self.R*self.C # time constant (msec)
        self.refracTime = 50 # refractory time (msec)
        self.initRefrac = 0

        self.noise_amp = 0.1

        self.isPlot = 1

class izhikevichConfig():
    def __init__(self,):
            self.A = 0.04
            self.B = 5
            self.C = 140
            self.Cm = 1
            self.a = 0.02
            self.b = 0.2
            self.c = -65
            self.d = 2
            self.u0 = 0.0#(self.b * self.vprev) #global initial condition of recovery variable

            self.isPlot = 1

    


