#!/usr/bin/env python
# encoding: utf-8
"""
factorTheTime.py

Created by Ryan Matthew Balfanz on 2009-05-01.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import time
import sys

from factors import time_factors

def factor_the_time(time, thinkFast=True):
	"""Facotr the time ala XKCD #247 'Factoring The Time'.
	View the comic at http://xkcd.com/247/.
	
	time should be a 2-tuple like (hour, min), where
	hour is given in 24-hour format.
	
	Returns a list containing each factor and its multiplicity.
	"""
	if not thinkFast:
		sys.stderr.write("THINK FAST.")
	hour, min = time
	return time_factors[int(hour+min)]

if __name__ == '__main__':

	# time.ctime() returns something like: 'Fri May  1 14:40:36 2009'
	hour, min, sec = time.ctime().split()[3].split(':')
	print factor_the_time((hour, min))
