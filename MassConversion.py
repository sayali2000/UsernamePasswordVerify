# -*- coding: utf-8 -*-
"""
Conversion of kg->tonne, kg->pound
"""

Unitkg='Kg'
Unitpound='Pounds'
Unittonne='Tonne'


def kgtotonne(x):
	#1 kg=0.001 Tonne
	return x * 0.001

def kgtopound(x):
	#1 kg= 2.20462 pound
	return x* 2.20462
