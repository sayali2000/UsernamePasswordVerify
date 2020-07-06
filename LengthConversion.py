# -*- coding: utf-8 -*-
"""
conversion functions mile ->km, feet->inch
"""
Unitkm='Km'
Unitfeet='Inches'
Unitmile='mile'

def mile_to_km(x):
	#1 mile=1.609344km
	return x * 1.609344
def feet_to_inch(x):
	#1 feet=12 inches
	return x* 12
