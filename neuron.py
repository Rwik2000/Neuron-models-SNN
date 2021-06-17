import numpy as np
import matplotlib.pyplot as plt
from configs import LIFneuronConfig, IzhikevichConfig
import math
import time

class LIF():
    def __init__(self):
        LIFneuronConfig.__init__(self,)
        self.num=0
        self.isNoise = 0
        self.vprev = self.v_base

    def noiseTerm(self,dt):
        sigma = self.noise_amp

        y = np.random.normal(0,1,1)
        return sigma*math.sqrt(dt)*y

    def generateSpiking(self, I, t, dt):

        v = self.v_base
        if t >= self.initRefrac:
            noise = 0
            if self.isNoise:
                noise = self.noiseTerm(dt)

            v = self.vprev + (-self.vprev + I*self.R) / self.tau_m * dt +noise
            if v >= self.v_thresh:
                self.num+=1
                v += self.v_spike
                self.initRefrac = t + self.refracTime
        self.vprev = v 
        return v

class Izhikevich():
        def __init__(self,):
            izhikevichConfig.__init__(self,)
            # #parameters that define the neuron model
            self.uv = []

            #Initial conditions
            self.vprev = self.c #resting potential
            # self.u = self.u0 #recovery variable
            self.uprev = self.u0

        #integrate the model over one step
        def generateSpiking(self,input_current,t,dt):
            #find the next value of the membrane voltage
            # print(self.vprev)
            v = self.vprev + dt*((self.A*self.vprev**2 + self.B*self.vprev - self.uprev + self.C + (input_current/self.Cm)))
            
            #find the next value of the recovery variable
            u = self.uprev + dt*self.a*((self.b * self.vprev) - self.uprev)
            #spike event
            #if a spike is generated
            self.uv.append(u)
            if v >= 30:
                self.vprev = self.c #reset membrane voltage
                v = 31
                u = u + self.d #reset recovery variable
                self.uv.append(u)
            else:
                self.vprev = v
            self.uprev = u
            # print(self.vprev)
            # print(v)
            return v

def runNeuronSimple(model, t_span, dt, I):
    v = np.zeros_like(t_span)

    for i, t in enumerate(t_span):
        if i==0:
            v_prev = 0
        else:
            v_prev= v[i-1]
        v[i] = model.generateSpiking(I[i], t, dt)

    
    if model.isPlot:
        plt.plot(t_span,v, label = 'V')
        plt.plot(t_span,I, label = 'I')
        # plt.plot(t_span,Z, label = 'Z')

        plt.title('Leaky Integrate-and-Fire')
        plt.ylabel('Membrane Potential (V) and input current(I)')
        plt.xlabel('Time (msec)')
        plt.grid()
        plt.legend(loc="upper right")
        plt.show()
    return v

def runNeuronCustom(model, t_span, I,z ,ifSec = False):
    v = np.zeros_like(t_span)

    if ifSec:
        t_span = t_span*1000

    for i, t in enumerate(t_span):
        if i==0:
            v[i] = 0
            dt = t - 0
        else:
            dt = t - t_span[i-1]
            st = time.time()
            v[i] = model.generateSpiking(I[i], t, dt)
            print(time.time() - st)

    
    if model.isPlot:
        plt.plot(t_span,v, label = 'V')
        plt.plot(t_span,I, label = 'I')
        plt.plot(t_span,z, label = 'Z')

        plt.title('Leaky Integrate-and-Fire')
        plt.ylabel('Membrane Potential (V) and input current(I)')
        plt.xlabel('Time (msec)')
        plt.grid()
        plt.legend(loc="upper right")
        plt.show()
    return v

if __name__=='__main__':
    t_tot = 1000
    dt = 0.01
    t_span = np.arange(0, t_tot+dt, dt)
    I = [1 if 200/dt <= i <= 600/dt  else 10 for i in range(len(t_span))]
    neuron = izhikevich()
    v = runNeuronSimple(neuron, t_span, dt, I)
    