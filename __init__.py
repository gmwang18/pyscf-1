'''
*****************************************************
PySCF Python-based simulations of chemistry framework
*****************************************************

How to use
----------
There are two ways to access the documentation: the docstrings come with
the code, and an online program reference, available from
http://www.sunqm.net/pyscf/index.html

We recommend the enhanced Python interpreter `IPython <http://ipython.org>`_
and the web-based Python IDE `Ipython notebook <http://ipython.org/notebook.html>`_
to try out the package::

    >>> from pyscf import gto, scf
    >>> mol = gto.M(atom='H 0 0 0; H 0 0 1.2', basis='cc-pvdz')
    >>> mol.apply(scf.RHF).run()
    converged SCF energy = -1.06111199785749
    -1.06111199786


Submodules
----------
In pyscf, most submodules requires explict import::

    >>> from pyscf import gto, scf

:mod:`gto`
    Molecular structure and basis sets.
scf
    Non-relativistic and relativistic Hartree-Fock.
mcscf
    CASCI, 1-step and 2-step CASSCF
ao2mo
    General 2-electron AO to MO integral transformation
dft
    Non-relativistic DFT
df
    Density fitting
fci
    Full CI
cc
    Coupled Cluster
dmrgscf
    DMRGCI, 1-step and 2-step DMRG-CASSCF
fciqmcscf
    2-step FCIQMC-CASSCF
grad
    Gradients
lo
    Localization and orbital orthogonalization
lib
    Basic functions and C extensions
nmr
    NMR
mp
    Moller-Plesset perturbation theory
symm
    Symmetry
pbc
    A complete tool sets for periodic boundary condition.
tools
    fcidump, molden etc


Pure function and Class
-----------------------
Class are designed to hold only the final results and the control parameters
such as maximum number of iterations, convergence threshold, etc.
The intermediate status are not saved in the class.  If the .kernel() function
is finished without any errors,  the solution will be saved in the class (see
documentation).

Most useful functions are implemented at module level, and can be accessed in
both class or module,  e.g.  ``scf.hf.get_jk(mol, dm)`` and
``SCF(mol).get_jk(mol, dm)`` have the same functionality.  As a result, most
functions and class are **pure**, i.e. no status are saved, and the argument
are not changed inplace.  Exceptions (destructive functions and methods) are
suffixed with underscore in the function name,  eg  ``mcscf.state_average_(mc)``
changes the attribute of its argument ``mc``


Stream functions
----------------
For most methods, there are three stream functions to pipe computing stream:

1 ``.set`` function to update object attributes, eg
``mf = scf.RHF(mol).set(conv_tol=1e-5)`` is identical to proceed in two steps
``mf = scf.RHF(mol); mf.conv_tol=1e-5``

2 ``.run`` function to execute the kernel function (the function arguments
are passed to kernel function).  If keyword arguments is given, it will first
call ``.set`` function to update object attributes then execute the kernel
function.  Eg
``mf = scf.RHF(mol).run(dm_init, conv_tol=1e-5)`` is identical to three steps
``mf = scf.RHF(mol); mf.conv_tol=1e-5; mf.kernel(dm_init)``

3 ``.apply`` function to apply the given function/class to the current object
(function arguments and keyword arguments are passed to the given function).
Eg
``mol.apply(scf.RHF).run().apply(mcscf.CASSCF, 6, 4, frozen=4)`` is identical to
``mf = scf.RHF(mol); mf.kernel(); mcscf.CASSCF(mf, 6, 4, frozen=4)``

'''

__version__ = '1.3b'

import os
from distutils.version import LooseVersion
import numpy
if LooseVersion(numpy.__version__) <= LooseVersion('1.8.0'):
    raise SystemError("You're using an old version of Numpy (%s). "
                      "It is recommended to upgrad numpy to 1.8.0 or newer. \n"
                      "You still can use all features of PySCF with the old numpy by removing this warning msg. "
                      "Some modules (DFT, CC, MRPT) might be affected because of the bug in old numpy." %
                      numpy.__version__)
from pyscf import gto
from pyscf import lib
from pyscf import scf
from pyscf import ao2mo

__path__.append(os.path.join(os.path.dirname(__file__), 'future'))
__path__.append(os.path.join(os.path.dirname(__file__), 'tools'))

DEBUG = False

