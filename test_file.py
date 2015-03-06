#!/usr/bin/python

import sys
import math
import csv
import numpy

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

class fileOps(object):
	def __init__(self, arg):
		self.volume = [][]


		with open(arg, 'rb') as f:
			lineNum = 0
			for row in csv.reader(f, delimiter=',', skipinitialspace=True):
				if lineNum == 0:
					lineNum = 1
				else:
					count = 0
					for info in row:
						if count == 1:
							self.add_close(info)
						if count == 2:
							self.add_volume(info)
						if count == 3:
							self.add_open(info)
						if count == 4:
							self.add_high(info)
						if count == 5:
							self.add_low(info)
						count = count + 1

		self.min = 0
		self.max = 0
		self.diff = 0
		self.mean = 0
		self.std_dev = 0

	def add_volume(self, arg):
		self.volume.append(float(arg))

	def add_open(self, arg):
		self.open.append(float(arg))

	def add_close(self, arg):
		self.close.append(float(arg))

	def add_high(self, arg):
		self.high.append(float(arg))

	def add_low(self, arg):
		self.low.append(float(arg))

	def calc_min_vol(self):
		self.min = min(self.volume)

	def calc_max_vol(self):
		self.max = max(self.volume)

	def calc_diff_vol(self):
		self.calc_max_vol()
		self.calc_min_vol()
		self.diff = self.max - self.min

	def calc_mean(self):
		self.mean = numpy.mean(self.open)

	def calc_std_dev(self):
		self.std_dev = numpy.std(self.open)

	def homework2_part_a(self):
		self.calc_diff_vol()
		for number in self.volume:
			print(str(number) + "\t" + str((number-self.min)/self.diff))

	def homework2_part_b(self):
		self.calc_mean()
		self.calc_std_dev()
		for number in self.open:
			print(str(number) + "\t" + str((number-self.mean)/self.std_dev))

	def calc_high_low_diff(self):
		for x in xrange(0,len(self.high)):
			self.high_low.append(self.high[x]-self.low[x])

		
var1 = fileOps(sys.argv[1])
var2 = fileOps(sys.argv[2])

var1.homework2_part_a()
var2.homework2_part_b()
# part c
var1.calc_high_low_diff()
var2.calc_high_low_diff()
for x in xrange(0,len(var1.high)):
	print(str(var1.high_low[x]) + "\t" + str(var2.high_low[x]) + "\t" + str(var1.close[x]-var2.close[x]))

