Glossary
==============

NEST-specific terms
-------------------
.. one refers to these things by putting the right quote into | | signs, like |model|
   these shortcuts are defined in the /glossary_include.rst file, which must be included in all files that use a glossary entry.
   
.. _glossary_model:

Model
~~~~~
An abstract representation of a neural network's component in NEST. NEST models comprise neuron models, synapse models, generators, and recording devices (models). TODO more?

Let's check if LaTeX is rendered: :math:`I(t) = I_mean + I_std*W(t)`

.. _glossary_status_dictionary:

Status dictionary
~~~~~~~~~~~~~~~~~
Also referred to by the name "parameter dictionary" (TODO change/unique name in doc), contains all parameters of the 

.. _glossary_model_dictionary:

Model dictionary
~~~~~~~~~~~~~~~~
NOT the status/parameter dictionary! TODO is/where is this used?

.. _glossary_kernel:

Kernel
~~~~~~
The component of NEST that performs the simulations. A user defining a neural simulation in Python interacts with it using the |PyNEST| API. Careful! In some model documentations, terms like "post-synaptic kernel" are used referring to integral kernels.

.. _glossary_pynest:

PyNEST
~~~~~~
A Python module allowing a Python script to interact with the NEST |kernel|. Documented in TODO reference to PyNEST tutorial, TODO reference to PyNEST API.

.. _glossary_sli:

SLI
~~~
Short for *Simulation Language Interpreter*, the low-level language (and interpreter of that language) to interact with the NEST kernel.

static synapse type

Common abbreviations in NEST
------------------------------
.. glossary::

 iaf
   integrate and fire

 gif
   generalized integrate and fire

 cond
   conductance-based

 psc
   post synaptic current (current-based)

 hh
   hodgkin huxley

 rng
   random number generator

 wfr
   waveform relaxation method

 aeif
   adaptive exponential integrate and fire

 ht
   hill and tononi

 pp
   point process

 in
   inhibitory

 ex
   excitatory

 MAM
   multi-area model

 mpi
   message passing interface

 stdp
   spike-timing dependent plasticity synapse

 st
   short term plasticity

 vp
   virtual process

Physical units and variable names used for NEST parameters
-------------------------------------------------------------

.. note::

   all parameters listed here are defined as `type double` in NEST

.. glossary::

 **time**
    milliseconds `ms`

 tau_m
    Membrane time constant in ms

 t_ref
    Duration of refractory period in ms

 t_spike
    point in time of last spike in

 **capacitance**
    picofarads `pF`

 C_m
    Capacitance of the membrane in pF

 **current**
    picoamperes `pA`

 I_e
    Constant input current in pA.

 **conductance**
    nanosiemens `nS`

   g_L
    Leak conductance in nS

   g_K
    Potassium peak conductance in nS.

   g_Na
    Sodium peak conductance in nS.

 **spike rates**
    spikes/s

 **modulation frequencies**
    herz `Hz`

 frequency
    frequncy in Hz

 **voltage**
   millivolts `mV`

 V_m
   Membrane potential in mV

 E_L
   Resting membrane potential in mV.

 V_th
   Spike threshold in mV.

 V_reset double
   Reset potential of the membrane in mV.

 V_min
   Absolute lower value for the membrane potential in mV

 E_ex
   Excitatory reversal potential in mV.

 E_in
    Inhibitory reversal potential in mV.

 E_Na
   Sodium reversal potential in mV.

 E_K
   Potassium reversal potential in mV.



