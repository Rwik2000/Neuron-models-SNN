import numpy as np
import matplotlib.pyplot as plt
from configs import LIFneuronConfig

class LIF():
    def __init__(self):
        LIFneuronConfig.__init__(self,)
        self.v = 0
    
    def generateSpiking(self, I, t, dt, vprev):

        self.v = 0
        if t >= self.initRefrac:
            self.v = vprev + (-vprev + I*self.R) / self.tau_m * dt            
            if self.v >= self.v_thresh:
                self.v += self.V_spike
                self.initRefrac = t + self.refracTime
        return self.v

def runLIF(model, t_span, dt, I):
    v = np.zeros_like(t_span)

    for i, t in enumerate(t_span):
        if i==0:
            v_prev = 0
        else:
            v_prev= v[i-1]
        v[i] = model.generateSpiking(I[i], t, dt, v_prev)

    
    if model.isPlot:
        plt.plot(t_span,v, label = 'V')
        plt.plot(t_span,I, label = 'I')
        plt.title('Leaky Integrate-and-Fire')
        plt.ylabel('Membrane Potential (V) and input current(I)')
        plt.xlabel('Time (msec)')
        plt.grid()
        plt.legend(loc="upper right")
        plt.show()
    return v

if __name__=='__main__':
    t_tot = 500
    dt = 0.01
    t_span = np.arange(0, t_tot+dt, dt)
    I = [0 if 200/dt <= i <= 300/dt  else 10 for i in range(len(t_span))]
    neuron = LIF()
    v = runLIF(neuron, t_span, dt, I)
    