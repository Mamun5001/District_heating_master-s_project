#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[19]:


# -*- coding: utf-8 -*-
from tespy.components import Source, Sink, HeatExchangerSimple, Pipe
from tespy.connections import Connection, Bus, Ref
from tespy.networks import Network
from tespy.tools import document_model

from sub_consumer import (LinConsumClosed as lc,
                          LinConsumOpen as lo,
                          Fork as fo)

# %% network

nw = Network(fluids=['water'], T_unit='C', p_unit='bar', h_unit='kJ / kg')

# %% components

# sources and sinks

so = Source('source')
si = Sink('sink')


# %% construction part

# pipe_feed

pif1 = Pipe('pipe1_feed', ks=7e-5, L=50, D=0.15, offdesign=['kA_char'])
pif2 = Pipe('pipe2_feed', ks=7e-5, L=200, D=0.15, offdesign=['kA_char'])

pif4 = Pipe('pipe4_feed', ks=7e-5, L=50, D=0.15, offdesign=['kA_char'])
pif7 = Pipe('pipe7_feed', ks=7e-5, L=175, D=0.15, offdesign=['kA_char'])

pif8 = Pipe('pipe8_feed', ks=7e-5, L=75, D=0.15, offdesign=['kA_char'])
pif10 = Pipe('pipe10_feed', ks=7e-5, L=450, D=0.1, offdesign=['kA_char'])

pif11 = Pipe('pipe11_feed', ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
pif16 = Pipe('pipe16_feed', ks=7e-5, L=30, D=0.065, offdesign=['kA_char'])

pif17 = Pipe('pipe17_feed', ks=7e-5, L=250, D=0.065, offdesign=['kA_char'])
pif18 = Pipe('pipe18_feed', ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])

pif19 = Pipe('pipe19_feed', ks=7e-5, L=250, D=0.065, offdesign=['kA_char'])
pif20 = Pipe('pipe20_feed', ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
pif21 = Pipe('pipe21_feed', ks=7e-5, L=250, D=0.065, offdesign=['kA_char'])
pif22 = Pipe('pipe22_feed', ks=7e-5, L=250, D=0.065, offdesign=['kA_char'])

# pipe_back

pib1 = Pipe('pipe1_back', ks=7e-5, L=50, D=0.15, offdesign=['kA_char'])
pib2 = Pipe('pipe2_back', ks=7e-5, L=200, D=0.15, offdesign=['kA_char'])

pib4 = Pipe('pipe4_back', ks=7e-5, L=50, D=0.15, offdesign=['kA_char'])
pib7 = Pipe('pipe7_back', ks=7e-5, L=175, D=0.15, offdesign=['kA_char'])

pib8 = Pipe('pipe8_back', ks=7e-5, L=75, D=0.15, offdesign=['kA_char'])
pib10 = Pipe('pipe10_back', ks=7e-5, L=450, D=0.1, offdesign=['kA_char'])

pib11 = Pipe('pipe11_back', ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
pib16 = Pipe('pipe16_back', ks=7e-5, L=30, D=0.065, offdesign=['kA_char'])

pib17 = Pipe('pipe17_back', ks=7e-5, L=250, D=0.065, offdesign=['kA_char'])
pib18 = Pipe('pipe18_back', ks=7e-5, L=30, D=0.05, offdesign=['kA_char'])
pib19 = Pipe('pipe19_back', ks=7e-5, L=40, D=0.04, offdesign=['kA_char'])
pib20 = Pipe('pipe20_back', ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
pib21 = Pipe('pipe21_back', ks=7e-5, L=40, D=0.04, offdesign=['kA_char'])
pib22 = Pipe('pipe22_back', ks=7e-5, L=40, D=0.04, offdesign=['kA_char'])

# %% subsystems for forks

k1 = fo('K1', 2)
k2 = fo('K2', 2)
k3 = fo('K3', 2)
k4 = fo('K4', 2)
k5 = fo('K5', 2)
k6 = fo('K6', 2)

nw.add_subsys(k1, k2, k3, k4,k5,k6)

# %% subsystems for consumers

h1 = lc('housing area 1', 2)
ia = lo('industrial area', 3)
sc = lc('sport center', 2)
h2 = lc('housing area 2', 5)
h3 = lc('housing area 3', 3)
h4 = lc('housing area 4', 4)
h5 = lc('housing area 5', 4)
h6 = lc('housing area 6', 4)


# consumers of subsystems

h1.comps['consumer_0'].set_attr(Q=5e4, pr=0.99)
h1.comps['consumer_1'].set_attr(Q=5e4, pr=0.99)

ia.comps['consumer_0'].set_attr(Q=6.15e5, pr=0.99)
ia.comps['consumer_1'].set_attr(Q=2.23e5, pr=0.99)
ia.comps['consumer_2'].set_attr(Q=4e5, pr=0.99)

sc.comps['consumer_0'].set_attr(Q=5.8e5, pr=0.99)
sc.comps['consumer_1'].set_attr(Q=1e6, pr=0.99)

h2.comps['consumer_0'].set_attr(Q=18e3, pr=0.99)
h2.comps['consumer_1'].set_attr(Q=4e3, pr=0.99)
h2.comps['consumer_2'].set_attr(Q=4e3, pr=0.99)
h2.comps['consumer_3'].set_attr(Q=4e3, pr=0.99)
h2.comps['consumer_4'].set_attr(Q=4e3, pr=0.99)

h3.comps['consumer_0'].set_attr(Q=1.4e5, pr=0.99)
h3.comps['consumer_1'].set_attr(Q=5.2e4, pr=0.99)
h3.comps['consumer_2'].set_attr(Q=5e4, pr=0.99)

h4.comps['consumer_0'].set_attr(Q=5e4, pr=0.99)
h4.comps['consumer_1'].set_attr(Q=5e4, pr=0.99)
h4.comps['consumer_2'].set_attr(Q=5e4, pr=0.99)
h4.comps['consumer_3'].set_attr(Q=5e4, pr=0.99)

h5.comps['consumer_0'].set_attr(Q=5e4, pr=0.99)
h5.comps['consumer_1'].set_attr(Q=5e4, pr=0.99)
h5.comps['consumer_2'].set_attr(Q=5e4, pr=0.99)
h5.comps['consumer_3'].set_attr(Q=5e4, pr=0.99)


h6.comps['consumer_0'].set_attr(Q=5e4, pr=0.99)
h6.comps['consumer_1'].set_attr(Q=5e4, pr=0.99)
h6.comps['consumer_2'].set_attr(Q=5e4, pr=0.99)
h6.comps['consumer_3'].set_attr(Q=5e4, pr=0.99)



# pipes of subsystems
# feed flow

h1.comps['feed_0'].set_attr(ks=7e-5, L=150, D=0.15, offdesign=['kA_char'])

ia.comps['feed_0'].set_attr(ks=7e-5, L=100, D=0.15, offdesign=['kA_char'])
ia.comps['feed_1'].set_attr(ks=7e-5, L=100, D=0.15, offdesign=['kA_char'])

sc.comps['feed_0'].set_attr(ks=7e-5, L=100, D=0.15, offdesign=['kA_char'])

h2.comps['feed_0'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
h2.comps['feed_1'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
h2.comps['feed_2'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
h2.comps['feed_3'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])

h3.comps['feed_0'].set_attr(ks=7e-5, L=335, D=0.05, offdesign=['kA_char'])
h3.comps['feed_1'].set_attr(ks=7e-5, L=100, D=0.04, offdesign=['kA_char'])

h4.comps['feed_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
h4.comps['feed_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
h4.comps['feed_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])

h5.comps['feed_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
h5.comps['feed_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
h5.comps['feed_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])

h6.comps['feed_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
h6.comps['feed_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
h6.comps['feed_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])


# return flow

h1.comps['return_0'].set_attr(ks=7e-5, L=150, D=0.15, offdesign=['kA_char'])

ia.comps['return_0'].set_attr(ks=7e-5, L=100, D=0.15, offdesign=['kA_char'])
ia.comps['return_1'].set_attr(ks=7e-5, L=100, D=0.15, offdesign=['kA_char'])

sc.comps['return_0'].set_attr(ks=7e-5, L=100, D=0.15, offdesign=['kA_char'])

h2.comps['return_0'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
h2.comps['return_1'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
h2.comps['return_2'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
h2.comps['return_3'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])

h3.comps['return_0'].set_attr(ks=7e-5, L=335, D=0.05, offdesign=['kA_char'])
h3.comps['return_1'].set_attr(ks=7e-5, L=100, D=0.04, offdesign=['kA_char'])

h4.comps['return_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
h4.comps['return_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
h4.comps['return_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])

h5.comps['return_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
h5.comps['return_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
h5.comps['return_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])

h6.comps['return_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
h6.comps['return_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
h6.comps['return_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])


# temperature difference factor for pipes:

dT_feed = 100
dT_return = 200
# return temperatures of consumers

for sub in [h1, ia, sc, h2, h3, h4, h5,h6]:
    for i in range(sub.num_consumer):
        sub.conns['cova_' + str(i)].set_attr(T=52)

    # temperature differences over subsystem pipes

    if isinstance(sub, lc):

        for i in range(sub.num_consumer - 1):

            # feed
            dT_feed_ref = Ref(
                sub.conns['spfe_' + str(i)], 1,
                -sub.comps['feed_' + str(i)].L.val / dT_feed)
            # return
            if i == sub.num_consumer - 1:
                dT_return_ref = Ref(
                    sub.conns['mere_' + str(i + 1)], 1,
                    -sub.comps['return_' + str(i)].L.val / dT_return)
            else:
                dT_return_ref = Ref(
                    sub.conns['cova_' + str(i + 1)], 1,
                    -sub.comps['return_' + str(i)].L.val / dT_return)

            if i == sub.num_consumer - 2:
                sub.conns['spco_' + str(i + 1)].set_attr(
                    T=dT_feed_ref, design=['T'])
            else:
                sub.conns['fesp_' + str(i + 1)].set_attr(
                    T=dT_feed_ref, design=['T'])
            sub.conns['reme_' + str(i)].set_attr(T=dT_return_ref, design=['T'])

    elif isinstance(sub, lo):

        for i in range(sub.num_consumer - 1):

            # feed
            dT_feed_ref = Ref(
                sub.conns['spfe_' + str(i)], 1,
                -sub.comps['feed_' + str(i)].L.val / dT_feed)
            # return
            dT_return_ref = Ref(
                sub.conns['mere_' + str(i + 1)], 1,
                -sub.comps['return_' + str(i)].L.val / dT_return)

            sub.conns['fesp_' + str(i + 1)].set_attr(
                T=dT_feed_ref, design=['T'])
            sub.conns['reme_' + str(i)].set_attr(
                T=dT_return_ref, design=['T'])

# %% connections

# %% starting area & housing area 1

# feed
so_pif1 = Connection(so, 'out1', pif1, 'in1', T=90, p=15, fluid={'water': 1})
pif1_k1f = Connection(pif1, 'out1', k1.comps['splitter'], 'in1', T=Ref(so_pif1, 1, -pif1.L.val / dT_feed), design=['T'])
k1f_pif2 = Connection(k1.comps['splitter'], 'out1', pif2, 'in1')
pif2_h1 = Connection(pif2, 'out1', h1.comps['splitter_0'], 'in1', T=Ref(pif1_k1f, 1, -pif2.L.val / dT_feed), design=['T'])

# back
h1_pib2 = Connection(h1.comps['merge_0'], 'out1', pib2, 'in1')
pib2_k1 = Connection(pib2, 'out1', k1.comps['valve_0'], 'in1', T=Ref(h1_pib2, 1, -pib2.L.val / dT_return), design=['T'])
k1_pib1 = Connection(k1.comps['merge'], 'out1', pib1, 'in1', p=11)
pib1_si = Connection(pib1, 'out1', si, 'in1', T=Ref(k1_pib1, 1, -pib1.L.val / dT_return), design=['T'])

nw.add_conns(so_pif1, pif1_k1f, k1f_pif2, pif2_h1)
nw.add_conns(h1_pib2, pib2_k1, k1_pib1, pib1_si)
nw.add_subsys(h1)


# %%industrial area

# feed
k1_pif4 = Connection(k1.comps['splitter'], 'out2', pif4, 'in1')
pif4_v = Connection(pif4, 'out1', ia.comps['splitter_0'], 'in1', T=Ref(k1_pif4, 1, -pif4.L.val / dT_feed), design=['T'])
v_pif7 = Connection(ia.comps['splitter_2'], 'out2', pif7, 'in1')
pif7_k2 = Connection(pif7, 'out1', k2.comps['splitter'], 'in1', T=Ref(v_pif7, 1, -pif7.L.val / dT_feed), design=['T'])

# back
k2_pib7 = Connection(k2.comps['merge'], 'out1', pib7, 'in1', p=12)
pib7_v = Connection(pib7, 'out1', ia.comps['merge_2'], 'in1', T=Ref(k2_pib7, 1, -pib7.L.val / dT_return), design=['T'])
v_pib4 = Connection(ia.comps['merge_0'], 'out1', pib4, 'in1')
pib4_k1 = Connection(pib4, 'out1', k1.comps['valve_1'], 'in1', T=Ref(v_pib4, 1, -pib4.L.val / dT_return), design=['T'])

nw.add_conns(k1_pif4, pif4_v, v_pif7, pif7_k2)
nw.add_conns(k2_pib7, pib7_v, v_pib4, pib4_k1)
nw.add_subsys(ia)

# %% sport center

# feed
k2_pif8 = Connection(k2.comps['splitter'], 'out1', pif8, 'in1')
pif8_sc = Connection(pif8, 'out1', sc.comps['splitter_0'], 'in1', T=Ref(k2_pif8, 1, -pif8.L.val / dT_feed), design=['T'])

# back
sc_pib8 = Connection(sc.comps['merge_0'], 'out1', pib8, 'in1')
pib8_k2 = Connection(pib8, 'out1', k2.comps['valve_0'], 'in1', T=Ref(sc_pib8, 1, -pib8.L.val / dT_return), design=['T'])

nw.add_conns(k2_pif8, pif8_sc)
nw.add_conns(sc_pib8, pib8_k2)
nw.add_subsys(sc)

# %% pipe10 & housing area 2

# feed
k2_pif10 = Connection(k2.comps['splitter'], 'out2', pif10, 'in1')
pif10_k3 = Connection(pif10, 'out1', k3.comps['splitter'], 'in1', T=Ref(k2_pif10, 1, -pif10.L.val / dT_feed), design=['T'])
k3_pif11 = Connection(k3.comps['splitter'], 'out1', pif11, 'in1')
pif11_h2 = Connection(pif11, 'out1', h2.comps['splitter_0'], 'in1', T=Ref(k3_pif11, 1, -pif11.L.val / dT_feed), design=['T'])

# back
h2_pib11 = Connection(h2.comps['merge_0'], 'out1', pib11, 'in1')
pib11_k3 = Connection(pib11, 'out1', k3.comps['valve_0'], 'in1', T=Ref(h2_pib11, 1, -pib11.L.val / dT_return), design=['T'])
k3_pib10 = Connection(k3.comps['merge'], 'out1', pib10, 'in1', p=12.5)
pib10_k2 = Connection(pib10, 'out1', k2.comps['valve_1'], 'in1', T=Ref(k3_pib10, 1, -pib10.L.val / dT_return), design=['T'])
#
nw.add_conns(k2_pif10, pif10_k3, k3_pif11, pif11_h2)
nw.add_conns(h2_pib11, pib11_k3, k3_pib10, pib10_k2)
nw.add_subsys(h2)

# %% pipe16 & housing area 3

# feed
k3_pif16 = Connection(k3.comps['splitter'], 'out2', pif16, 'in1')
pif16_k4 = Connection(pif16, 'out1', k4.comps['splitter'], 'in1', T=Ref(k3_pif16, 1, -pif16.L.val / dT_feed), design=['T'])
k4_pif17 = Connection(k4.comps['splitter'], 'out1', pif17, 'in1')
pif17_h3 = Connection(pif17, 'out1', h3.comps['splitter_0'], 'in1', T=Ref(k4_pif17, 1, -pif17.L.val / dT_feed), design=['T'])


# back
h3_pib17 = Connection(h3.comps['merge_0'], 'out1', pib17, 'in1')
pib17_k4 = Connection(pib17, 'out1', k4.comps['valve_0'], 'in1',T=Ref(h3_pib17, 1, -pib17.L.val / dT_return), design=['T'])
k4_pib16 = Connection(k4.comps['merge'], 'out1', pib16, 'in1', p=12.75)
pib16_k3 = Connection(pib16, 'out1', k3.comps['valve_1'], 'in1', T=Ref(k4_pib16, 1, -pib16.L.val / dT_return), design=['T'])

nw.add_conns(k3_pif16, pif16_k4, k4_pif17, pif17_h3)
nw.add_conns(h3_pib17, pib17_k4, k4_pib16, pib16_k3)
nw.add_subsys(h3)

# %% housing area 4


# feed
k4_pif18 = Connection(k4.comps['splitter'], 'out2', pif18, 'in1')
pif18_k5 = Connection(pif18, 'out1', k5.comps['splitter'], 'in1', T=Ref(k4_pif18, 1, -pif18.L.val / dT_feed), design=['T'])
k5_pif19 = Connection(k5.comps['splitter'], 'out1', pif19, 'in1')
pif19_h4 = Connection(pif19, 'out1', h4.comps['splitter_0'], 'in1', T=Ref(k5_pif19, 1, -pif19.L.val / dT_feed), design=['T'])

# back

h4_pib19 = Connection(h4.comps['merge_0'], 'out1', pib19, 'in1')
pib19_k5 = Connection(pib19, 'out1', k5.comps['valve_0'], 'in1',T=Ref(h4_pib19, 1, -pib19.L.val / dT_return), design=['T'])
k5_pib18 = Connection(k5.comps['merge'], 'out1', pib18, 'in1', p=12.75)
pib18_k4 = Connection(pib18, 'out1', k4.comps['valve_1'], 'in1', T=Ref(k5_pib18, 1, -pib18.L.val / dT_return), design=['T'])

nw.add_conns(k4_pif18, pif18_k5, k5_pif19, pif19_h4)
nw.add_conns(h4_pib19, pib19_k5, k5_pib18, pib18_k4)
nw.add_subsys(h4)


# %% housing area 5

# feed
k5_pif20 = Connection(k5.comps['splitter'], 'out2', pif20, 'in1')
pif20_k6 = Connection(pif20, 'out1', k6.comps['splitter'], 'in1', T=Ref(k5_pif20, 1, -pif20.L.val / dT_feed), design=['T'])
k6_pif21 = Connection(k6.comps['splitter'], 'out1', pif21, 'in1')
pif21_h5 = Connection(pif21, 'out1', h5.comps['splitter_0'], 'in1', T=Ref(k6_pif21, 1, -pif21.L.val / dT_feed), design=['T'])


# back

h5_pib21 = Connection(h5.comps['merge_0'], 'out1', pib21, 'in1')
pib21_k6 = Connection(pib21, 'out1', k6.comps['valve_0'], 'in1',T=Ref(h5_pib21, 1, -pib21.L.val / dT_return), design=['T'])
k6_pib20 = Connection(k6.comps['merge'], 'out1', pib20, 'in1', p=12.75)
pib20_k5 = Connection(pib20, 'out1', k5.comps['valve_1'], 'in1', T=Ref(k6_pib20, 1, -pib20.L.val / dT_return), design=['T'])

nw.add_conns(k5_pif20, pif20_k6, k6_pif21, pif21_h5)
nw.add_conns(h5_pib21, pib21_k6, k6_pib20, pib20_k5)
nw.add_subsys(h5)

# %% housing area 6


# feed
k6_pif22 = Connection(k6.comps['splitter'], 'out2', pif22, 'in1')
pif22_h6 = Connection(pif22, 'out1', h6.comps['splitter_0'], 'in1', T=Ref(k6_pif22, 1, -pif22.L.val / dT_feed), design=['T'])

# back
h6_pib22 = Connection(h6.comps['merge_0'], 'out1', pib22, 'in1')
pib22_k6 = Connection(pib22, 'out1', k6.comps['valve_1'], 'in1', T=Ref(h6_pib22, 1, -pib22.L.val / dT_return), design=['T'])

nw.add_conns(k6_pif22, pif22_h6)
nw.add_conns(h6_pib22, pib22_k6)
nw.add_subsys(h6)



# %% busses

heat_losses = Bus('network losses')
heat_consumer = Bus('network consumer')
nw.check_network()

for comp in nw.comps['object']:
    if isinstance(comp, Pipe):
        comp.set_attr(Tamb=0)

        heat_losses.add_comps({'comp': comp})

    if (isinstance(comp, HeatExchangerSimple) and
            not isinstance(comp, Pipe)):
        heat_consumer.add_comps({'comp': comp})

nw.add_busses(heat_losses, heat_consumer)


# %% solve

# design case: 0 °C ambient temperature
nw.solve('design')
nw.save('grid')
document_model(nw)

heat_loss_value = heat_losses.P.val

# List of all subsystems
subsystems = [h1, ia, sc, h2, h3, h4, h5, h6]

# Initialize total heat demand
total_heat_generated = 0

# Loop through each subsystem to sum up the heat demand
for subsys in subsystems:
    for consumer in subsys.comps.values():
        if hasattr(consumer, 'Q'):
            total_heat_generated += consumer.Q.val

print('Heat demand consumer:', heat_consumer.P.val)
print('network losses at 0 °C outside temperature (design):', heat_losses.P.val)
print("Total heat generated in the network:", total_heat_generated, "W")
print('Efficiency :',(heat_consumer.P.val/total_heat_generated) * 100)

# Define temperature and other constant parameters
T_supply = [60,70,80,90,100]  # in °C
ambient_temperature = 20  # in °C


# Initialize dictionaries to store results
efficiency_results = {}
heat_losses_values = {}
total_generated_heat_values = {}
total_consumed_heat_values = {}


# Loop through each supply temperature
for temp in T_supply:
    
    
    # Set the ambient temperature for all pipe components
    for comp in nw.comps['object']:
        if isinstance(comp, Pipe):
            so_pif1.set_attr(T=T_supply)
            comp.set_attr(Tamb=ambient_temperature)
            
    
    # Perform off-design simulation for the current temperature
    nw.solve('offdesign', design_path='grid')
    

    # Calculate heat demand and losses (adapt these calculations to your specific case)
    heat_demand_consumer = abs(heat_consumer.P.val)
    network_losses = abs(heat_losses.P.val)
    total_generated_heat=(heat_demand_consumer+network_losses)
    
    # Calculate efficiency
    efficiency = abs(heat_demand_consumer) / (abs(heat_demand_consumer) + abs(network_losses))
    
    
    # Store the results for the current temperature
    efficiency_results[temp] = efficiency
    heat_losses_values[temp] = network_losses
    total_generated_heat_values[temp] = total_generated_heat
    total_consumed_heat_values[temp] = heat_demand_consumer
    
    # Extract values for plotting
    efficiencies = list(efficiency_results.values())
    total_heat_losses = list(heat_losses_values.values())
    total_generated_heat_list = list(total_generated_heat_values.values())
    total_consumed_heat_list = list(total_consumed_heat_values.values())
    
print(total_consumed_heat_list)
    
import csv

# Define the filename for the CSV file
csv_filename = 'dh_supply_temp.csv'

# Open the CSV file for writing
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(['Supply Temperature (°C)', 'Efficiency (%)', 'Heat Loss (W)', 'Generated Heat (W)', 'Consumed Heat (W)'])

    # Write the data
    for temp in T_supply:
        writer.writerow([
            temp,
            efficiency_results[temp] * 100,
            heat_losses_values[temp],
            total_generated_heat_values[temp],
            total_consumed_heat_values[temp]
        ])

print(f'Results have been saved to {csv_filename}')


# In[2]:


import csv

# Define the filename for the CSV file
csv_filename = 'dh_supply_temp.csv'

# Open the CSV file for writing
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(['Supply Temperature (°C)', 'Efficiency (%)', 'Heat Loss (W)', 'Generated Heat (W)', 'Consumed Heat (W)'])

    # Write the data
    for temp in T_supply:
        writer.writerow([
            temp,
            efficiency_results[temp] * 100,
            heat_losses_values[temp],
            total_generated_heat_values[temp],
            total_consumed_heat_values[temp]
        ])

print(f'Results have been saved to {csv_filename}')


# In[14]:


import matplotlib.pyplot as plt

# Graph 1: Supply Temperature vs Heat Loss
plt.figure(figsize=(8, 6))
plt.plot(T_supply, total_heat_losses, linestyle='-', marker='o', color='red')
plt.title('Supply Temperature vs Heat Loss')
plt.xlabel('Supply Temperature (°C)')
plt.ylabel('Heat Loss (W)')
plt.grid(True)
plt.savefig('Supply_Temperature_ST_vs_Heat_Loss.png')  # Save the figure
plt.show()

# Graph 2: Supply Temperature vs Efficiency
plt.figure(figsize=(8, 6))
plt.plot(T_supply, efficiencies, linestyle='-', marker='o', color='blue')
plt.title('Supply Temperature vs Efficiency')
plt.xlabel('Supply Temperature (°C)')
plt.ylabel('Efficiency (%)')
plt.grid(True)
plt.savefig('Supply_Temperature_ST_vs_Efficiency.png')  # Save the figure
plt.show()

# Graph 3: Supply Temperature vs Total Heat Generated
plt.figure(figsize=(8, 6))
plt.plot(T_supply, list(total_generated_heat_values.values()), linestyle='-', marker='o', color='green')
plt.title('Supply Temperature vs Total Heat Generated')
plt.xlabel('Supply Temperature (°C)')
plt.ylabel('Generated Heat (W)')
plt.grid(True)
plt.savefig('Supply_Temperature_ST_vs_Total_Heat_Generated.png')  # Save the figure
plt.show()

# Graph 4: Supply Temperature vs Total Heat Consumed
plt.figure(figsize=(8, 6))
plt.plot(T_supply, list(total_consumed_heat_values.values()), linestyle='-', marker='o', color='purple')
plt.title('Supply Temperature vs Total Heat Consumed')
plt.xlabel('Supply Temperature (°C)')
plt.ylabel('Consumed Heat (W)')
plt.grid(True)
plt.savefig('Supply_Temperature_ST_vs_Total_Heat_Consumed.png')  # Save the figure
plt.show()


# In[3]:


import matplotlib.pyplot as plt
import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('dh_supply_temp.csv')

# Plotting
plt.figure(figsize=(10, 6))

# Create the first Y-axis (left side) for heat loss, generated heat, and consumed heat
plt.plot(df['Supply Temperature (°C)'], df['Heat Loss (W)'], label='Heat Loss (W)', color='red')
plt.plot(df['Supply Temperature (°C)'], df['Generated Heat (W)'], label='Generated Heat (W)', color='green')
plt.plot(df['Supply Temperature (°C)'], df['Consumed Heat (W)'], label='Consumed Heat (W)', color='blue')
plt.xlabel('Supply Temperature (°C)')
plt.ylabel('Heat Metrics (W)')
plt.title('Supply Temperature vs Various Heat Metrics and Efficiency')
plt.grid(True)

# Create the second Y-axis (right side) for efficiency
ax2 = plt.gca().twinx()
ax2.plot(df['Supply Temperature (°C)'], df['Efficiency (%)'], label='Efficiency (%)', color='purple')
ax2.set_ylabel('Efficiency (%)')

# Adding legends
plt.gca().legend(loc='upper left')
ax2.legend(loc='upper right')

plt.savefig('Combined_Graph.png')
plt.show()




# In[4]:


import matplotlib.pyplot as plt
import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('dh_supply_temp.csv')

# Plotting
plt.figure(figsize=(10, 6))

# Create the first Y-axis (left side) for heat loss, generated heat, and consumed heat
# Plotting heat loss
plt.plot(df['Supply Temperature (°C)'], df['Heat Loss (W)'], label='Heat Loss (W)', color='red', marker='o')
plt.xlabel('Supply Temperature (°C)')
plt.ylabel('Heat Metrics (W)')
plt.title('Supply Temperature vs Various Heat Metrics and Efficiency')
plt.grid(True)

# Plotting generated heat
plt.plot(df['Supply Temperature (°C)'], df['Generated Heat (W)'], label='Generated Heat (W)', color='green', marker='x')

# Plotting consumed heat
plt.plot(df['Supply Temperature (°C)'], df['Consumed Heat (W)'], label='Consumed Heat (W)', color='blue', marker='^')

# Create the second Y-axis (right side) for efficiency
# Plotting efficiency on a secondary Y-axis
ax2 = plt.gca().twinx()
ax2.plot(df['Supply Temperature (°C)'], df['Efficiency (%)'], label='Efficiency (%)', color='purple', linestyle='--')
ax2.set_ylabel('Efficiency (%)')

# Adding legends for both Y-axes
plt.gca().legend(loc='upper left')
ax2.legend(loc='upper right')

# Saving and showing the figure
plt.savefig('Combined_Graph.png')
plt.show()


# In[16]:


get_ipython().system('pip install --upgrade tespy')
get_ipython().system('pip install --upgrade CoolProp')


# In[45]:


# -*- coding: utf-8 -*-
import os
from tespy.components import Source, Sink, HeatExchangerSimple, Pipe
from tespy.connections import Connection, Bus, Ref
from tespy.networks import Network
from tespy.tools import document_model
import csv
import pandas as pd
from sub_consumer import (LinConsumClosed as lc,
                          LinConsumOpen as lo,
                          Fork as fo)

# %% network

nw = Network(fluids=['water'], T_unit='C', p_unit='bar', h_unit='kJ / kg')

# %% components

# sources and sinks

so = Source('source')
si = Sink('sink')


# %% construction part

# pipe_feed

pif1 = Pipe('pipe1_feed', ks=7e-5, L=50, D=0.15, offdesign=['kA_char'])
pif2 = Pipe('pipe2_feed', ks=7e-5, L=200, D=0.15, offdesign=['kA_char'])

pif4 = Pipe('pipe4_feed', ks=7e-5, L=50, D=0.15, offdesign=['kA_char'])
pif7 = Pipe('pipe7_feed', ks=7e-5, L=175, D=0.15, offdesign=['kA_char'])

pif8 = Pipe('pipe8_feed', ks=7e-5, L=75, D=0.15, offdesign=['kA_char'])
pif10 = Pipe('pipe10_feed', ks=7e-5, L=450, D=0.1, offdesign=['kA_char'])

pif11 = Pipe('pipe11_feed', ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
pif16 = Pipe('pipe16_feed', ks=7e-5, L=30, D=0.065, offdesign=['kA_char'])

pif17 = Pipe('pipe17_feed', ks=7e-5, L=250, D=0.065, offdesign=['kA_char'])
pif18 = Pipe('pipe18_feed', ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])

pif19 = Pipe('pipe19_feed', ks=7e-5, L=250, D=0.065, offdesign=['kA_char'])
pif20 = Pipe('pipe20_feed', ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
pif21 = Pipe('pipe21_feed', ks=7e-5, L=250, D=0.065, offdesign=['kA_char'])
pif22 = Pipe('pipe22_feed', ks=7e-5, L=250, D=0.065, offdesign=['kA_char'])

pif23 = Pipe('pipe23_feed', ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
pif24 = Pipe('pipe24_feed', ks=7e-5, L=250, D=0.065, offdesign=['kA_char'])
pif25 = Pipe('pipe25_feed', ks=7e-5, L=250, D=0.065, offdesign=['kA_char'])

pif25 = Pipe('pipe25_feed', ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
pif26 = Pipe('pipe26_feed', ks=7e-5, L=250, D=0.065, offdesign=['kA_char'])
pif27 = Pipe('pipe27_feed', ks=7e-5, L=250, D=0.065, offdesign=['kA_char'])



# pipe_back

pib1 = Pipe('pipe1_back', ks=7e-5, L=50, D=0.15, offdesign=['kA_char'])
pib2 = Pipe('pipe2_back', ks=7e-5, L=200, D=0.15, offdesign=['kA_char'])

pib4 = Pipe('pipe4_back', ks=7e-5, L=50, D=0.15, offdesign=['kA_char'])
pib7 = Pipe('pipe7_back', ks=7e-5, L=175, D=0.15, offdesign=['kA_char'])

pib8 = Pipe('pipe8_back', ks=7e-5, L=75, D=0.15, offdesign=['kA_char'])
pib10 = Pipe('pipe10_back', ks=7e-5, L=450, D=0.1, offdesign=['kA_char'])

pib11 = Pipe('pipe11_back', ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
pib16 = Pipe('pipe16_back', ks=7e-5, L=30, D=0.065, offdesign=['kA_char'])

pib17 = Pipe('pipe17_back', ks=7e-5, L=250, D=0.065, offdesign=['kA_char'])
pib18 = Pipe('pipe18_back', ks=7e-5, L=30, D=0.05, offdesign=['kA_char'])
pib19 = Pipe('pipe19_back', ks=7e-5, L=40, D=0.04, offdesign=['kA_char'])
pib20 = Pipe('pipe20_back', ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
pib21 = Pipe('pipe21_back', ks=7e-5, L=40, D=0.04, offdesign=['kA_char'])
pib22 = Pipe('pipe22_back', ks=7e-5, L=40, D=0.04, offdesign=['kA_char'])

pib23 = Pipe('pipe23_back', ks=7e-5, L=40, D=0.04, offdesign=['kA_char'])
pib24 = Pipe('pipe24_back', ks=7e-5, L=40, D=0.04, offdesign=['kA_char'])
pib25 = Pipe('pipe25_back', ks=7e-5, L=40, D=0.04, offdesign=['kA_char'])

pib26 = Pipe('pipe26_back', ks=7e-5, L=40, D=0.04, offdesign=['kA_char'])
pib27 = Pipe('pipe27_back', ks=7e-5, L=40, D=0.04, offdesign=['kA_char'])
pib28 = Pipe('pipe28_back', ks=7e-5, L=40, D=0.04, offdesign=['kA_char'])

# %% subsystems for forks

k1 = fo('K1', 2)
k2 = fo('K2', 2)
k3 = fo('K3', 2)
k4 = fo('K4', 2)
k5 = fo('K5', 2)
k6 = fo('K6', 2)
k7 = fo('K7', 2)
k8 = fo('K8', 2)


nw.add_subsys(k1, k2, k3, k4,k5,k6,k7,k8)

# %% subsystems for consumers

h1 = lc('housing area 1', 2)
ia1 = lo('industrial area 1', 3)
sc = lc('sport center', 2)
h2 = lc('housing area 2', 5)
h3 = lc('housing area 3', 3)
h4 = lc('housing area 4', 4)
h5 = lc('housing area 5', 4)
h7 = lc('housing area 6', 4)
ia3 = lc('industrial area 3',4)
ia2= lc('industrial area 2',4)

# consumers of subsystems

h1.comps['consumer_0'].set_attr(Q=5e4, pr=0.99)
h1.comps['consumer_1'].set_attr(Q=5e4, pr=0.99)

ia1.comps['consumer_0'].set_attr(Q=3e5, pr=0.99)
ia1.comps['consumer_1'].set_attr(Q=3e5, pr=0.99)
ia1.comps['consumer_2'].set_attr(Q=3e5, pr=0.99)

sc.comps['consumer_0'].set_attr(Q=2e4, pr=0.99)
sc.comps['consumer_1'].set_attr(Q=2e4, pr=0.99)

h2.comps['consumer_0'].set_attr(Q=5e4, pr=0.99)
h2.comps['consumer_1'].set_attr(Q=5e4, pr=0.99)
h2.comps['consumer_2'].set_attr(Q=5e4, pr=0.99)
h2.comps['consumer_3'].set_attr(Q=5e4, pr=0.99)
h2.comps['consumer_4'].set_attr(Q=5e4, pr=0.99)

h3.comps['consumer_0'].set_attr(Q=1e5, pr=0.99)
h3.comps['consumer_1'].set_attr(Q=1e5, pr=0.99)
h3.comps['consumer_2'].set_attr(Q=1e5, pr=0.99)

h4.comps['consumer_0'].set_attr(Q=5e4, pr=0.99)
h4.comps['consumer_1'].set_attr(Q=5e4, pr=0.99)
h4.comps['consumer_2'].set_attr(Q=5e4, pr=0.99)
h4.comps['consumer_3'].set_attr(Q=5e4, pr=0.99)

h5.comps['consumer_0'].set_attr(Q=5e4, pr=0.99)
h5.comps['consumer_1'].set_attr(Q=5e4, pr=0.99)
h5.comps['consumer_2'].set_attr(Q=5e4, pr=0.99)
h5.comps['consumer_3'].set_attr(Q=5e4, pr=0.99)


h7.comps['consumer_0'].set_attr(Q=6e4, pr=0.99)
h7.comps['consumer_1'].set_attr(Q=6e4, pr=0.99)
h7.comps['consumer_2'].set_attr(Q=6e4, pr=0.99)
h7.comps['consumer_3'].set_attr(Q=6e4, pr=0.99)

ia2.comps['consumer_0'].set_attr(Q=3e5, pr=0.99)
ia2.comps['consumer_1'].set_attr(Q=3e5, pr=0.99)
ia2.comps['consumer_2'].set_attr(Q=3e5, pr=0.99)
ia2.comps['consumer_3'].set_attr(Q=3e5, pr=0.99)

ia3.comps['consumer_0'].set_attr(Q=5e5, pr=0.99)
ia3.comps['consumer_1'].set_attr(Q=5e5, pr=0.99)
ia3.comps['consumer_2'].set_attr(Q=5e5, pr=0.99)
ia3.comps['consumer_3'].set_attr(Q=5e5, pr=0.99)



# pipes of subsystems
# feed flow

h1.comps['feed_0'].set_attr(ks=7e-5, L=150, D=0.15, offdesign=['kA_char'])

ia1.comps['feed_0'].set_attr(ks=7e-5, L=100, D=0.15, offdesign=['kA_char'])
ia1.comps['feed_1'].set_attr(ks=7e-5, L=100, D=0.15, offdesign=['kA_char'])

sc.comps['feed_0'].set_attr(ks=7e-5, L=100, D=0.15, offdesign=['kA_char'])

h2.comps['feed_0'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
h2.comps['feed_1'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
h2.comps['feed_2'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
h2.comps['feed_3'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])

h3.comps['feed_0'].set_attr(ks=7e-5, L=335, D=0.05, offdesign=['kA_char'])
h3.comps['feed_1'].set_attr(ks=7e-5, L=100, D=0.04, offdesign=['kA_char'])

h4.comps['feed_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
h4.comps['feed_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
h4.comps['feed_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])

h5.comps['feed_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
h5.comps['feed_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
h5.comps['feed_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])


h7.comps['feed_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
h7.comps['feed_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
h7.comps['feed_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])

ia3.comps['feed_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
ia3.comps['feed_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
ia3.comps['feed_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])

ia2.comps['feed_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
ia2.comps['feed_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
ia2.comps['feed_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])


# return flow

h1.comps['return_0'].set_attr(ks=7e-5, L=150, D=0.15, offdesign=['kA_char'])

ia1.comps['return_0'].set_attr(ks=7e-5, L=100, D=0.15, offdesign=['kA_char'])
ia1.comps['return_1'].set_attr(ks=7e-5, L=100, D=0.15, offdesign=['kA_char'])

sc.comps['return_0'].set_attr(ks=7e-5, L=100, D=0.15, offdesign=['kA_char'])

h2.comps['return_0'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
h2.comps['return_1'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
h2.comps['return_2'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])
h2.comps['return_3'].set_attr(ks=7e-5, L=60, D=0.04, offdesign=['kA_char'])

h3.comps['return_0'].set_attr(ks=7e-5, L=335, D=0.05, offdesign=['kA_char'])
h3.comps['return_1'].set_attr(ks=7e-5, L=100, D=0.04, offdesign=['kA_char'])

h4.comps['return_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
h4.comps['return_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
h4.comps['return_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])

h5.comps['return_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
h5.comps['return_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
h5.comps['return_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])


h7.comps['return_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
h7.comps['return_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
h7.comps['return_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])

ia3.comps['return_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
ia3.comps['return_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
ia3.comps['return_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])

ia2.comps['return_0'].set_attr(ks=7e-5, L=30, D=0.04, offdesign=['kA_char'])
ia2.comps['return_1'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])
ia2.comps['return_2'].set_attr(ks=7e-5, L=10, D=0.04, offdesign=['kA_char'])

# temperature difference factor for pipes:

dT_feed = 100
dT_return = 200
# return temperatures of consumers

for sub in [h1, ia1, sc, h2, h3, h4, h5,h7,ia3,ia2]:
    for i in range(sub.num_consumer):
        sub.conns['cova_' + str(i)].set_attr(T=52)

    # temperature differences over subsystem pipes

    if isinstance(sub, lc):

        for i in range(sub.num_consumer - 1):

            # feed
            dT_feed_ref = Ref(
                sub.conns['spfe_' + str(i)], 1,
                -sub.comps['feed_' + str(i)].L.val / dT_feed)
            # return
            if i == sub.num_consumer - 1:
                dT_return_ref = Ref(
                    sub.conns['mere_' + str(i + 1)], 1,
                    -sub.comps['return_' + str(i)].L.val / dT_return)
            else:
                dT_return_ref = Ref(
                    sub.conns['cova_' + str(i + 1)], 1,
                    -sub.comps['return_' + str(i)].L.val / dT_return)

            if i == sub.num_consumer - 2:
                sub.conns['spco_' + str(i + 1)].set_attr(
                    T=dT_feed_ref, design=['T'])
            else:
                sub.conns['fesp_' + str(i + 1)].set_attr(
                    T=dT_feed_ref, design=['T'])
            sub.conns['reme_' + str(i)].set_attr(T=dT_return_ref, design=['T'])

    elif isinstance(sub, lo):

        for i in range(sub.num_consumer - 1):

            # feed
            dT_feed_ref = Ref(
                sub.conns['spfe_' + str(i)], 1,
                -sub.comps['feed_' + str(i)].L.val / dT_feed)
            # return
            dT_return_ref = Ref(
                sub.conns['mere_' + str(i + 1)], 1,
                -sub.comps['return_' + str(i)].L.val / dT_return)

            sub.conns['fesp_' + str(i + 1)].set_attr(
                T=dT_feed_ref, design=['T'])
            sub.conns['reme_' + str(i)].set_attr(
                T=dT_return_ref, design=['T'])

# %% connections

# %% starting area & housing area 1

# feed
so_pif1 = Connection(so, 'out1', pif1, 'in1', T=90, p=15, fluid={'water': 1})
pif1_k1f = Connection(pif1, 'out1', k1.comps['splitter'], 'in1', T=Ref(so_pif1, 1, -pif1.L.val / dT_feed), design=['T'])
k1f_pif2 = Connection(k1.comps['splitter'], 'out1', pif2, 'in1')
pif2_h1 = Connection(pif2, 'out1', h1.comps['splitter_0'], 'in1', T=Ref(pif1_k1f, 1, -pif2.L.val / dT_feed), design=['T'])

# back
h1_pib2 = Connection(h1.comps['merge_0'], 'out1', pib2, 'in1')
pib2_k1 = Connection(pib2, 'out1', k1.comps['valve_0'], 'in1', T=Ref(h1_pib2, 1, -pib2.L.val / dT_return), design=['T'])
k1_pib1 = Connection(k1.comps['merge'], 'out1', pib1, 'in1', p=11)
pib1_si = Connection(pib1, 'out1', si, 'in1', T=Ref(k1_pib1, 1, -pib1.L.val / dT_return), design=['T'])

nw.add_conns(so_pif1, pif1_k1f, k1f_pif2, pif2_h1)
nw.add_conns(h1_pib2, pib2_k1, k1_pib1, pib1_si)
nw.add_subsys(h1)


# %%industrial area

# feed
k1_pif4 = Connection(k1.comps['splitter'], 'out2', pif4, 'in1')
pif4_v = Connection(pif4, 'out1', ia1.comps['splitter_0'], 'in1', T=Ref(k1_pif4, 1, -pif4.L.val / dT_feed), design=['T'])
v_pif7 = Connection(ia1.comps['splitter_2'], 'out2', pif7, 'in1')
pif7_k2 = Connection(pif7, 'out1', k2.comps['splitter'], 'in1', T=Ref(v_pif7, 1, -pif7.L.val / dT_feed), design=['T'])

# back
k2_pib7 = Connection(k2.comps['merge'], 'out1', pib7, 'in1', p=12)
pib7_v = Connection(pib7, 'out1', ia1.comps['merge_2'], 'in1', T=Ref(k2_pib7, 1, -pib7.L.val / dT_return), design=['T'])
v_pib4 = Connection(ia1.comps['merge_0'], 'out1', pib4, 'in1')
pib4_k1 = Connection(pib4, 'out1', k1.comps['valve_1'], 'in1', T=Ref(v_pib4, 1, -pib4.L.val / dT_return), design=['T'])

nw.add_conns(k1_pif4, pif4_v, v_pif7, pif7_k2)
nw.add_conns(k2_pib7, pib7_v, v_pib4, pib4_k1)
nw.add_subsys(ia1)

# %% sport center

# feed
k2_pif8 = Connection(k2.comps['splitter'], 'out1', pif8, 'in1')
pif8_sc = Connection(pif8, 'out1', sc.comps['splitter_0'], 'in1', T=Ref(k2_pif8, 1, -pif8.L.val / dT_feed), design=['T'])

# back
sc_pib8 = Connection(sc.comps['merge_0'], 'out1', pib8, 'in1')
pib8_k2 = Connection(pib8, 'out1', k2.comps['valve_0'], 'in1', T=Ref(sc_pib8, 1, -pib8.L.val / dT_return), design=['T'])

nw.add_conns(k2_pif8, pif8_sc)
nw.add_conns(sc_pib8, pib8_k2)
nw.add_subsys(sc)

# %% pipe10 & housing area 2

# feed
k2_pif10 = Connection(k2.comps['splitter'], 'out2', pif10, 'in1')
pif10_k3 = Connection(pif10, 'out1', k3.comps['splitter'], 'in1', T=Ref(k2_pif10, 1, -pif10.L.val / dT_feed), design=['T'])
k3_pif11 = Connection(k3.comps['splitter'], 'out1', pif11, 'in1')
pif11_h2 = Connection(pif11, 'out1', h2.comps['splitter_0'], 'in1', T=Ref(k3_pif11, 1, -pif11.L.val / dT_feed), design=['T'])

# back
h2_pib11 = Connection(h2.comps['merge_0'], 'out1', pib11, 'in1')
pib11_k3 = Connection(pib11, 'out1', k3.comps['valve_0'], 'in1', T=Ref(h2_pib11, 1, -pib11.L.val / dT_return), design=['T'])
k3_pib10 = Connection(k3.comps['merge'], 'out1', pib10, 'in1', p=12.5)
pib10_k2 = Connection(pib10, 'out1', k2.comps['valve_1'], 'in1', T=Ref(k3_pib10, 1, -pib10.L.val / dT_return), design=['T'])
#
nw.add_conns(k2_pif10, pif10_k3, k3_pif11, pif11_h2)
nw.add_conns(h2_pib11, pib11_k3, k3_pib10, pib10_k2)
nw.add_subsys(h2)

# %% pipe16 & housing area 3

# feed
k3_pif16 = Connection(k3.comps['splitter'], 'out2', pif16, 'in1')
pif16_k4 = Connection(pif16, 'out1', k4.comps['splitter'], 'in1', T=Ref(k3_pif16, 1, -pif16.L.val / dT_feed), design=['T'])
k4_pif17 = Connection(k4.comps['splitter'], 'out1', pif17, 'in1')
pif17_h3 = Connection(pif17, 'out1', h3.comps['splitter_0'], 'in1', T=Ref(k4_pif17, 1, -pif17.L.val / dT_feed), design=['T'])


# back
h3_pib17 = Connection(h3.comps['merge_0'], 'out1', pib17, 'in1')
pib17_k4 = Connection(pib17, 'out1', k4.comps['valve_0'], 'in1',T=Ref(h3_pib17, 1, -pib17.L.val / dT_return), design=['T'])
k4_pib16 = Connection(k4.comps['merge'], 'out1', pib16, 'in1', p=12.75)
pib16_k3 = Connection(pib16, 'out1', k3.comps['valve_1'], 'in1', T=Ref(k4_pib16, 1, -pib16.L.val / dT_return), design=['T'])

nw.add_conns(k3_pif16, pif16_k4, k4_pif17, pif17_h3)
nw.add_conns(h3_pib17, pib17_k4, k4_pib16, pib16_k3)
nw.add_subsys(h3)

# %% housing area 4


# feed
k4_pif18 = Connection(k4.comps['splitter'], 'out2', pif18, 'in1')
pif18_k5 = Connection(pif18, 'out1', k5.comps['splitter'], 'in1', T=Ref(k4_pif18, 1, -pif18.L.val / dT_feed), design=['T'])
k5_pif19 = Connection(k5.comps['splitter'], 'out1', pif19, 'in1')
pif19_h4 = Connection(pif19, 'out1', h4.comps['splitter_0'], 'in1', T=Ref(k5_pif19, 1, -pif19.L.val / dT_feed), design=['T'])

# back

h4_pib19 = Connection(h4.comps['merge_0'], 'out1', pib19, 'in1')
pib19_k5 = Connection(pib19, 'out1', k5.comps['valve_0'], 'in1',T=Ref(h4_pib19, 1, -pib19.L.val / dT_return), design=['T'])
k5_pib18 = Connection(k5.comps['merge'], 'out1', pib18, 'in1', p=12.75)
pib18_k4 = Connection(pib18, 'out1', k4.comps['valve_1'], 'in1', T=Ref(k5_pib18, 1, -pib18.L.val / dT_return), design=['T'])

nw.add_conns(k4_pif18, pif18_k5, k5_pif19, pif19_h4)
nw.add_conns(h4_pib19, pib19_k5, k5_pib18, pib18_k4)
nw.add_subsys(h4)


# %% housing area 5

# feed
k5_pif20 = Connection(k5.comps['splitter'], 'out2', pif20, 'in1')
pif20_k6 = Connection(pif20, 'out1', k6.comps['splitter'], 'in1', T=Ref(k5_pif20, 1, -pif20.L.val / dT_feed), design=['T'])
k6_pif21 = Connection(k6.comps['splitter'], 'out1', pif21, 'in1')
pif21_h5 = Connection(pif21, 'out1', h5.comps['splitter_0'], 'in1', T=Ref(k6_pif21, 1, -pif21.L.val / dT_feed), design=['T'])


# back

h5_pib21 = Connection(h5.comps['merge_0'], 'out1', pib21, 'in1')
pib21_k6 = Connection(pib21, 'out1', k6.comps['valve_0'], 'in1',T=Ref(h5_pib21, 1, -pib21.L.val / dT_return), design=['T'])
k6_pib20 = Connection(k6.comps['merge'], 'out1', pib20, 'in1', p=12.75)
pib20_k5 = Connection(pib20, 'out1', k5.comps['valve_1'], 'in1', T=Ref(k6_pib20, 1, -pib20.L.val / dT_return), design=['T'])

nw.add_conns(k5_pif20, pif20_k6, k6_pif21, pif21_h5)
nw.add_conns(h5_pib21, pib21_k6, k6_pib20, pib20_k5)
nw.add_subsys(h5)



# %% housing area 6

# feed
k6_pif23 = Connection(k6.comps['splitter'], 'out2', pif23, 'in1')
pif23_k7 = Connection(pif23, 'out1', k7.comps['splitter'], 'in1', T=Ref(k6_pif23, 1, -pif23.L.val / dT_feed), design=['T'])
k7_pif24 = Connection(k7.comps['splitter'], 'out1', pif24, 'in1')
pif24_h7 = Connection(pif24, 'out1', h7.comps['splitter_0'], 'in1', T=Ref(k7_pif24, 1, -pif24.L.val / dT_feed), design=['T'])


# back

h7_pib24 = Connection(h7.comps['merge_0'], 'out1', pib24, 'in1')
pib24_k7 = Connection(pib24, 'out1', k7.comps['valve_0'], 'in1',T=Ref(h7_pib24, 1, -pib24.L.val / dT_return), design=['T'])
k7_pib23 = Connection(k7.comps['merge'], 'out1', pib23, 'in1', p=12.75)
pib23_k6 = Connection(pib23, 'out1', k6.comps['valve_1'], 'in1', T=Ref(k7_pib23, 1, -pib23.L.val / dT_return), design=['T'])

nw.add_conns(k6_pif23, pif23_k7, k7_pif24, pif24_h7)
nw.add_conns(h7_pib24, pib24_k7, k7_pib23, pib23_k6)
nw.add_subsys(h7)

# %% industrial area 2


# feed
k8_pif27 = Connection(k8.comps['splitter'], 'out2', pif27, 'in1')
pif27_ia2 = Connection(pif27, 'out1', ia2.comps['splitter_0'], 'in1', T=Ref(k8_pif27, 1, -pif27.L.val / dT_feed), design=['T'])

# back
ia2_pib27 = Connection(ia2.comps['merge_0'], 'out1', pib27, 'in1')
pib27_k8 = Connection(pib27, 'out1', k8.comps['valve_1'], 'in1', T=Ref(ia2_pib27, 1, -pib27.L.val / dT_return), design=['T'])

nw.add_conns(k8_pif27, pif27_ia2)
nw.add_conns(ia2_pib27, pib27_k8)
nw.add_subsys(ia2)

# %% industrial area 3

# feed
k7_pif25 = Connection(k7.comps['splitter'], 'out2', pif25, 'in1')
pif25_k8 = Connection(pif25, 'out1', k8.comps['splitter'], 'in1', T=Ref(k7_pif25, 1, -pif25.L.val / dT_feed), design=['T'])
k8_pif26 = Connection(k8.comps['splitter'], 'out1', pif26, 'in1')
pif26_ia3 = Connection(pif26, 'out1', ia3.comps['splitter_0'], 'in1', T=Ref(k8_pif26, 1, -pif26.L.val / dT_feed), design=['T'])


# back

ia3_pib26 = Connection(ia3.comps['merge_0'], 'out1', pib26, 'in1')
pib26_k8 = Connection(pib26, 'out1', k8.comps['valve_0'], 'in1',T=Ref(ia3_pib26, 1, -pib26.L.val / dT_return), design=['T'])
k8_pib25 = Connection(k8.comps['merge'], 'out1', pib25, 'in1', p=12.75)
pib25_k7 = Connection(pib25, 'out1', k7.comps['valve_1'], 'in1', T=Ref(k8_pib25, 1, -pib25.L.val / dT_return), design=['T'])

nw.add_conns(k7_pif25, pif25_k8, k8_pif26, pif26_ia3)
nw.add_conns(ia3_pib26, pib26_k8, k8_pib25, pib25_k7)
nw.add_subsys(ia3)






# %% busses

heat_losses = Bus('network losses')
heat_consumer = Bus('network consumer')
nw.check_network()

for comp in nw.comps['object']:
    if isinstance(comp, Pipe):
        comp.set_attr(Tamb=0)

        heat_losses.add_comps({'comp': comp})

    if (isinstance(comp, HeatExchangerSimple) and
            not isinstance(comp, Pipe)):
        heat_consumer.add_comps({'comp': comp})

nw.add_busses(heat_losses, heat_consumer)


# %% solve

# design case: 0 °C ambient temperature
nw.solve('design')
nw.save('grid')
document_model(nw)

heat_loss_value = heat_losses.P.val

# List of all subsystems
subsystems = [h1, ia1, sc, h2, h3, h4,h5,h7,ia2,ia3]

# Initialize total heat demand
total_heat_generated = 0

# Loop through each subsystem to sum up the heat demand
for subsys in subsystems:
    for consumer in subsys.comps.values():
        if hasattr(consumer, 'Q'):
            total_heat_generated += consumer.Q.val

print('Heat demand consumer:', heat_consumer.P.val)
print('network losses at 0 °C outside temperature (design):', heat_losses.P.val)
print("Total heat generated in the network:", total_heat_generated, "W")
print('Efficiency :',(heat_consumer.P.val/total_heat_generated) * 100)
            

# Define temperature and other constant parameters
T_supply = [60,70,80,90,100]  # in °C 74.51578565

ambient_temperature = 10  # in °C


# Initialize dictionaries to store results
efficiency_results = {}
heat_losses_values = {}
total_generated_heat_values = {}
total_consumed_heat_values = {}


# Loop through each supply temperature
for temp in T_supply:
    
    
    # Set the ambient temperature for all pipe components
    for comp in nw.comps['object']:
        if isinstance(comp, Pipe):
            so_pif1.set_attr(T=temp)
            comp.set_attr(Tamb=ambient_temperature)
         
    
    # Perform off-design simulation for the current temperature
    try:
        nw.solve('offdesign', design_path='grid')
    except Exception as e:
        print(f"Error setting temperatures for temp={temp}: {e}") 

    # Calculate heat demand and losses (adapt these calculations to your specific case)
    heat_demand_consumer = abs(heat_consumer.P.val)
    network_losses = abs(heat_losses.P.val)
    total_generated_heat=(heat_demand_consumer+network_losses)
    
    # Calculate efficiency
    efficiency = abs(heat_demand_consumer) / (abs(heat_demand_consumer) + abs(network_losses))
    
    
    # Store the results for the current temperature
    efficiency_results[temp] = efficiency
    heat_losses_values[temp] = network_losses
    total_generated_heat_values[temp] = total_generated_heat
    total_consumed_heat_values[temp] = heat_demand_consumer
    
    # Extract values for plotting
    efficiencies = list(efficiency_results.values())
    total_heat_losses = list(heat_losses_values.values())
    total_generated_heat_list = list(total_generated_heat_values.values())
    total_consumed_heat_list = list(total_consumed_heat_values.values())
    
excel_filename = 'dh_supply_temp.xlsx'

# Prepare the data
data = []
for temp in T_supply:
    data.append([
        temp,
        efficiency_results[temp] * 100,
        heat_losses_values[temp],
        total_generated_heat_values[temp],
        total_consumed_heat_values[temp]
    ])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Supply Temperature (°C)', 'Efficiency (%)', 'Heat Loss (W)', 'Generated Heat (W)', 'Consumed Heat (W)'])

# Write to an Excel file
df.to_excel(excel_filename, index=False)

print(f'Results have been saved to {excel_filename}')


# In[46]:


import csv

# List of ambient temperatures to check
ambient_temperatures = [-10,-5,0, 5, 10,20]

# Initialize dictionaries to store results
efficiency_results = {}
heat_losses_values = {}
consumer_heat_loads = {}
total_heat_generated_values = {}


# Loop through each ambient temperature
for temp in ambient_temperatures:
    # Set the ambient temperature for all pipe components
    for comp in nw.comps['object']:
        if isinstance(comp, Pipe):
            comp.set_attr(Tamb=temp)

    # Perform off-design simulation for the current temperature
    nw.solve('offdesign', design_path='grid')
    
    # Calculate the heat demand from consumers (negative values)
    heat_demand_consumer = abs(heat_consumer.P.val)
    
    # Calculate the network losses (negative values)
    network_losses = abs(heat_losses.P.val)
    total_generated_heat = abs(heat_demand_consumer+network_losses)
    
    # Calculate the efficiency as the ratio of useful output to input
    efficiency = abs(heat_demand_consumer) / (abs(heat_demand_consumer) + abs(network_losses))*100
    
    # Store the results for the current temperature
    efficiency_results[temp] = efficiency
    heat_losses_values[temp] = network_losses
    consumer_heat_loads[temp] = heat_demand_consumer
    total_heat_generated_values[temp] = total_generated_heat


import pandas as pd

# Prepare data for Excel
headers = ['Ambient Temperature', 'Efficiency', 'Heat Losses', 'Consumer Heat Load', 'Total Generated Heat']
data = []

# Populate data with rows
for temp in ambient_temperatures:
    data.append([
        temp,
        efficiency_results[temp],
        heat_losses_values[temp],
        consumer_heat_loads[temp],
        total_heat_generated_values[temp]
    ])

# Create a DataFrame
df = pd.DataFrame(data, columns=headers)

# Write to Excel
excel_filename = 'Ambient_temperature_ST.xlsx'
df.to_excel(excel_filename, index=False)

print(f"Data saved to {excel_filename}")


# In[ ]:




