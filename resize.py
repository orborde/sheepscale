#!/usr/bin/env python

import sys
import xml.etree.ElementTree
t = xml.etree.ElementTree.parse(sys.argv[1])
flam = t.getroot()

target_width, target_height = map(int, sys.argv[2:])
current_width, current_height = map(int, flam.get('size').split())
scale_w = float(target_width) / current_width
scale_h = float(target_height) / current_height
scale_factor = min(scale_w, scale_h)

current_scale = float(flam.get('scale'))
final_scale = current_scale * scale_factor

flam.set('scale', str(final_scale))
flam.set('size', '{} {}'.format(target_width, target_height))

t.write(sys.stdout)
