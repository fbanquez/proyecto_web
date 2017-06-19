#!/usr/local/bin/python
# -*- coding: utf-8 -*-


def anio_bisiesto(anio):
    if(anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0):
        return True
    else:
        return False
