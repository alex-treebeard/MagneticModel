#-------------------------------------------------------------------------------
#
#  Coefficient loaders - tests
#
# Author: Martin Paces <martin.paces@eox.at>
#
#-------------------------------------------------------------------------------
# Copyright (C) 2018 EOX IT Services GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
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
# pylint: disable=missing-docstring

from unittest import TestCase, main
from numpy import inf
from numpy.testing import assert_allclose
from eoxmagmod.data import (
    CHAOS5_CORE, CHAOS5_CORE_V4, CHAOS5_STATIC,
    CHAOS6_CORE, CHAOS6_CORE_X3, CHAOS6_STATIC,
    IGRF11, IGRF12, SIFM, WMM_2010, WMM_2015,
    EMM_2010_STATIC, EMM_2010_SECVAR,
)
from eoxmagmod.magnetic_model.coefficients import (
    SparseSHCoefficientsTimeDependent,
    SparseSHCoefficientsConstant,
    CombinedSHCoefficients,
)
from eoxmagmod.magnetic_model.loader_shc import load_shc, load_shc_combined
from eoxmagmod.magnetic_model.loader_igrf import load_igrf
from eoxmagmod.magnetic_model.loader_wmm import load_wmm
from eoxmagmod.magnetic_model.loader_emm import load_emm
from eoxmagmod._pytimeconv import (
    decimal_year_to_mjd2000, mjd2000_to_decimal_year,
)


class CoefficietLoaderTestMixIn(object):
    is_internal = True
    class_ = None
    validity = None
    degree = 0

    @property
    def coeff(self):
        if not hasattr(self, "_coeff"):
            self._coeff = self.load()
        return self._coeff

    @classmethod
    def load(cls):
        raise NotImplementedError

    def test_validity(self):
        assert_allclose(self.coeff.validity, self.validity, rtol=1e-8, atol=1e-8)

    def test_class(self):
        self.assertIsInstance(self.coeff, self.class_)

    def test_degree(self):
        self.assertEqual(self.coeff.degree, self.degree)

    def test_model_type(self):
        self.assertEqual(self.coeff.is_internal, self.is_internal)


class ShcTestMixIn(CoefficietLoaderTestMixIn):
    path = None

    @classmethod
    def load(cls):
        return load_shc(cls.path)


class CombinedShcTestMixIn(CoefficietLoaderTestMixIn):
    class_ = CombinedSHCoefficients
    path_core = None
    path_static = None

    @classmethod
    def load(cls):
        return load_shc_combined(cls.path_core, cls.path_static)


class WmmTestMixIn(CoefficietLoaderTestMixIn):
    path = None

    @classmethod
    def load(cls):
        return load_wmm(cls.path)

#-------------------------------------------------------------------------------

class TestCoeffSIFM(TestCase, ShcTestMixIn):
    class_ = SparseSHCoefficientsTimeDependent
    path = SIFM
    degree = 70
    validity = decimal_year_to_mjd2000((2013.4976, 2015.4962))


class TestCoeffIGRF12(TestCase, ShcTestMixIn):
    class_ = SparseSHCoefficientsTimeDependent
    path = IGRF12
    degree = 13
    validity = decimal_year_to_mjd2000((1900.0, 2020.0))


class TestCoeffIGRF11(TestCase, CoefficietLoaderTestMixIn):
    class_ = SparseSHCoefficientsTimeDependent
    degree = 13
    validity = decimal_year_to_mjd2000((1900.0, 2015.0))

    @staticmethod
    def load():
        return load_igrf(IGRF11)

#-------------------------------------------------------------------------------

class TestCoeffCHAOS5Core(TestCase, ShcTestMixIn):
    class_ = SparseSHCoefficientsTimeDependent
    path = CHAOS5_CORE
    degree = 20
    validity = decimal_year_to_mjd2000((1997.0021, 2015.0007))


class TestCoeffCHAOS5CoreV4(TestCase, ShcTestMixIn):
    class_ = SparseSHCoefficientsTimeDependent
    path = CHAOS5_CORE_V4
    degree = 20
    validity = decimal_year_to_mjd2000((1997.1020, 2016.1027))


class TestCoeffCHAOS5Static(TestCase, ShcTestMixIn):
    class_ = SparseSHCoefficientsConstant
    path = CHAOS5_STATIC
    degree = 90
    validity = (-inf, inf)


class TestCoeffCHAOS5Combined(TestCase, CombinedShcTestMixIn):
    path_core = CHAOS5_CORE_V4
    path_static = CHAOS5_STATIC
    degree = 90
    validity = decimal_year_to_mjd2000((1997.1020, 2016.1027))

#-------------------------------------------------------------------------------

class TestCoeffCHAOS6Core(TestCase, ShcTestMixIn):
    class_ = SparseSHCoefficientsTimeDependent
    path = CHAOS6_CORE
    degree = 20
    validity = decimal_year_to_mjd2000((1997.102, 2016.6023))


class TestCoeffCHAOS6CoreX3(TestCase, ShcTestMixIn):
    class_ = SparseSHCoefficientsTimeDependent
    path = CHAOS6_CORE_X3
    degree = 20
    validity = decimal_year_to_mjd2000((1997.102, 2017.6016))


class TestCoeffCHAOS6Static(TestCase, ShcTestMixIn):
    class_ = SparseSHCoefficientsConstant
    path = CHAOS6_STATIC
    degree = 110
    validity = (-inf, inf)


class TestCoeffCHAOS6Combined(TestCase, CombinedShcTestMixIn):
    path_core = CHAOS6_CORE_X3
    path_static = CHAOS6_STATIC
    degree = 110 
    validity = decimal_year_to_mjd2000((1997.1020, 2017.6016))

#-------------------------------------------------------------------------------

class TestCoeffWMM2010(TestCase, WmmTestMixIn):
    class_ = SparseSHCoefficientsTimeDependent
    path = WMM_2010
    degree = 12
    validity = decimal_year_to_mjd2000((2010., 2015.))


class TestCoeffWMM2015(TestCase, WmmTestMixIn):
    class_ = SparseSHCoefficientsTimeDependent
    path = WMM_2015
    degree = 12
    validity = decimal_year_to_mjd2000((2015., 2020.))


class TestCoeffEMM2010(TestCase, CoefficietLoaderTestMixIn):
    class_ = CombinedSHCoefficients
    degree = 739
    validity = decimal_year_to_mjd2000((2010.0, 2015.0))

    @staticmethod
    def load():
        return load_emm(EMM_2010_STATIC, EMM_2010_SECVAR)

#-------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
