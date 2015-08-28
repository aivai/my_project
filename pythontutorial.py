# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:16:17 2015

@author: Aiva
"""

def distance_between_points_2d(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (dx**2 + dy**2)**.5

p1 = (1,2)
p2 = (3,4)

print distance_between_points_2d(p1,p2)

p3 = (4,5)
p4 = (2,3)

print distance_between_points_2d(p3,p4)

