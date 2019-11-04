"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documentation builds.
"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.test.python.package


_g = globals()
_g.update(build_package_configs(
    project_name='test_python_package',
    version=lsst.test.python.package.version.__version__))
