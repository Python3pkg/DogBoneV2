# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:13:34 2015

@author: lvanhulle
"""
import numpy
import math
from parameters import constants as c
import matrixTrans as mt
class Point(object):
    
    COMPARE_PRECISION = 10000
    
    def __init__(self, x, y=None, z=0):
        try:
            len(x)
        except:
            if y is None:
                raise Exception('You did not initialize a Point correctly')            
            self.__normalVector = numpy.array([x, y, z, 1])            
            
        else:
            self.__normalVector = numpy.array([x[c.X], x[c.Y], x[c.Z], 1])
        
        self.__key = tuple(int(round(i*self.COMPARE_PRECISION))
                            for i in self.normalVector[:3])
        
    @property
    def x(self):
        return self.__normalVector[c.X]
        
    @property
    def y(self):
        return self.__normalVector[c.Y]
    
    @property
    def z(self):
        return self.__normalVector[c.Z]
        
    @property
    def normalVector(self):
        return numpy.array(self.__normalVector)
    
    def __iter__(self):
        return(i for i in self.__normalVector[:3])
    
    def get2DPoint(self):
        return self.__normalVector[:2]
    
    def mirror(self, axis):
        return self.transform(mt.mirrorMatrix(axis))
    
    def rotate(self, angle, point=None):
        return self.transform(mt.rotateMatrix(angle, point))
    
    def translate(self, shiftX, shiftY, shiftZ=0):
        return self.transform(mt.translateMatrix(shiftX, shiftY, shiftZ))
        
    def transform(self, transMatrix):
        nv = numpy.dot(transMatrix, self.normalVector)
        return Point(nv)
        
    def __getitem__(self, index):
        return self.normalVector[index]
    
    def __sub__(self, other):
        return numpy.linalg.norm(self.normalVector - other.normalVector)
        
    def __neg__(self):
        return Point(-self.x, -self.y, self.z)
    
    def squareDistance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def __lt__(self, other):
        return self.__key < other.__key
        
    def __gt__(self, other):
        return self.__key > other.__key

    def __eq__(self, other):
        return self.__key == other.__key
        
    def __ne__(self, other):
        return self.__key != other.__key
        
    def __hash__(self):
        return hash(self.__key)
    
    def CSVstr(self):
        return '{:.4f},{:.4f}'.format(self.x, self.y)
    
    def __str__(self):
        return 'X{:.4f} Y{:.4f} Z{:.4f}'.format(self.x, self.y, self.z)
    
#    def getNormalVector(self):
#        nv = [n for n in self.normalVector]
#        return nv
        
    