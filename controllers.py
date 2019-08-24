#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 11:20:00 2019

@author: eadali
"""
from numpy import cos, linspace, pi, cumsum
from matplotlib import pyplot

class pid_controller:
    def __init__(self, k_p, k_i, k_d):
        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d

        self.first = True
        self.i = 0
        self.e_m1 = 0


    def update(self, e):
        if self.first:
            u = self.k_p*e + self.k_i*0 + self.k_d*0
            self.first = False

        else:
            de = e - self.e_m1
            u = self.k_p*e + self.k_i*self.i + self.k_d*de


        self.i = self.i + e
        self.e_m1 = e


        print(self.i)

        return u



if __name__ == '__main__':
    p_pid = pid_controller(k_p=1, k_i=0, k_d=0)
    i_pid = pid_controller(k_p=0, k_i=1/16, k_d=0)
    d_pid = pid_controller(k_p=0, k_i=0, k_d=8)
    e_signal = cos(linspace(0, 4*pi, 100))

    ss = cumsum(e_signal)


    p_signal = list()
    i_signal = list()
    d_signal = list()

    for e in e_signal:
        p_signal.append(p_pid.update(e))
        i_signal.append(i_pid.update(e))
        d_signal.append(d_pid.update(e))

    pyplot.subplot(2,1,1)
    pyplot.plot(e_signal)

    pyplot.subplot(2,1,2)
    pyplot.plot(p_signal, 'b')
    pyplot.plot(i_signal, 'g')
    pyplot.plot(d_signal, 'r')
    pyplot.plot(ss)
    pyplot.show()



