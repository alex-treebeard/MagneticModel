#-------------------------------------------------------------------------------
#
#  World Magnetic Model 2010 / Geomagnetism Library
#
# Project: Earth magnetic field in Python.
# Author: Martin Paces <martin.paces@eox.at>
#
#-------------------------------------------------------------------------------
# Copyright (C) 2014 EOX IT Services GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all
# copies of this Software or works derived from this Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#-------------------------------------------------------------------------------

from .base import (
    MagneticModel,
    DATA_WMM_2010,
    DATA_EMM_2010_STATIC,
    DATA_EMM_2010_SECVAR,
    GEODETIC_ABOVE_WGS84,
    GEODETIC_ABOVE_EGM96,
    GEOCENTRIC_SPHERICAL,
    GEOCENTRIC_CARTESIAN,
)
from .wmm import GeomagWMM2010, read_model_wmm2010, convert
from .emm import read_model_emm2010

__all__ = [
    'MagneticModel',
    'GeomagWMM2010',
    'read_model_wmm2010',
    'read_model_emm2010',
    'convert',
    'DATA_WMM_2010',
    'DATA_EMM_2010_STATIC',
    'DATA_EMM_2010_SECVAR',
    'GEODETIC_ABOVE_WGS84',
    'GEODETIC_ABOVE_EGM96',
    'GEOCENTRIC_SPHERICAL',
    'GEOCENTRIC_CARTESIAN',
]

__version__ = '0.1.0dev'
__author__ = 'Martin Paces (martin.paces@eox.at)'
__copyright__ = 'Copyright (C) 2014 EOX IT Services GmbH'
__licence__ = 'EOX licence (MIT style)'