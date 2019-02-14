# -*- coding: utf-8 -*-
import numpy as np

def NU():
    t_max = 12500
    tau = 0.04
    r = [[0 for j in range(3)] for i in range(int(t_max/tau))]
    r[0] = [1., 0., 500.]
    V = [[0 for j in range(3)] for i in range(int(t_max/tau))]
    V[0] = [250., 0., 0.]
    R = 6438000.
    return r, V, R, t_max, tau

def integrate(r, V, R, i, tau):
    '''
    Функция формирования данных движения изделия (координаты и скорости на текущем такте)
    :param r: координата объекта (широта, долгота, высота)
    :param V: скорость объекта
    :param R: радиус земли
    :param i: номер такта работы
    :param tau: шаг интегрирования
    :return:
    '''
    r[i][0] = r[i - 1][0] + (V[i-1][0] * tau)/R
    r[i][1] = r[i - 1][1] + (V[i-1][2] * tau)/(R*np.cos(r[i][0]))
    r[i][2] = r[i - 1][2] + V[i-1][1] * tau
    V[i][0] = V[i - 1][0]
    V[i][1] = V[i - 1][1]
    V[i][2] = V[i - 1][2]
    return r, V