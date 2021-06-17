# Neuron Models 
This is a repository of simulating Neuron Models:
* Leaky integrate and fire model (LIF)
![alt text](https://github.com/Rwik2000/LIF-SNN/blob/master/images/LIF_equation.png)
* Izhekevich 
![alt text](https://github.com/Rwik2000/LIF-SNN/blob/master/images/Iz_equation.png)
Taken from https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1257420

Given an input current value the neuron gives the corresponding spikes. The data obtained can be used in various Spiking Neural Networks (SNN) architectures.

All parameters of the neuron can be changed in the [configs.py](https://github.com/Rwik2000/LIF-SNN/blob/master/configs.py). Note that the units of time is **milliseconds**.


## Usage:
From [neuron.py](https://github.com/Rwik2000/LIF-SNN/blob/master/neuron.py), call the function `runLIF()`. 
```python
def runNeuron(model, t_span, dt, I):
    v = np.zeros_like(t_span)

    for i, t in enumerate(t_span):
        v[i] = model.generateSpiking(I[i], t, dt)

    
    if model.isPlot:
        plt.plot(t_span,v, label = 'V')
        plt.plot(t_span,I, label = 'I')
        plt.title('Neuron Model')
        plt.ylabel('Membrane Potential (V) and input current(I)')
        plt.xlabel('Time (msec)')
        plt.grid()
        plt.legend(loc="upper right")
        plt.show()
    return v
```
Here, `t_span` is the the overall time duration, `dt` being the small time steps and `I` being the current function w.r.t time.

To get an idea just run the [neuron.py](https://github.com/Rwik2000/LIF-SNN/blob/master/neuron.py), and see the default example given at the end:
```python
t_tot = 1000
dt = 0.01
t_span = np.arange(0, t_tot+dt, dt)
I = [1 if 200/dt <= i <= 600/dt  else 10 for i in range(len(t_span))] # defining the current(time)
neuron = Izhikevich() #defining the neuron model
# passing the current through the neuron.
v = runNeuronSimple(neuron, t_span, dt, I)
```

**NOTE**: To plot the voltage and current data, turn ON the `isPLot` argument in the [configs.py](https://github.com/Rwik2000/LIF-SNN/blob/master/configs.py)

## Test Case:
![alt text](https://github.com/Rwik2000/LIF-SNN/blob/master/images/testCase_1.png)

## Some links:
* [MIT open courseware](https://ocw.mit.edu/resources/res-9-003-brains-minds-and-machines-summer-course-summer-2015/tutorials/tutorial-2.-matlab-programming/MITRES_9_003SUM15_fire.pdf)
* https://neuronaldynamics.epfl.ch/index.html
* https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1257420

## To-Do:
- [*] Add random salt-pepper noise to the output voltage.


