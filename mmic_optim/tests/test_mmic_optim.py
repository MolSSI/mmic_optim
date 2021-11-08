"""
Unit and regression test for the mmic_optim package.
"""

# Import package, test suite, and other packages as needed
import mmic_optim
from mmelemental.models import Molecule, ForceField
from mmic.components import TacticComponent
from cmselemental.util.decorators import classproperty
import mm_data
import pytest
from typing import Tuple, Union
import sys
import json


mol_file = mm_data.mols["water-mol.json"]
ff_file = mm_data.ffs["water-ff.json"]


def test_mmic_optim_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_optim" in sys.modules


def test_mmic_optim_models():
    with open(mol_file, "r") as fp:
        mol_data = json.load(fp)
        mol = Molecule(**mol_data)

    with open(ff_file, "r") as fp:
        ff_data = json.load(fp)
        ff = ForceField(**ff_data)

    inputs = mmic_optim.InputOptim(
        schema_name="test",
        schema_version=1.0,
        system={mol: ff},
        boundary=(
            "periodic",
            "periodic",
            "periodic",
            "periodic",
            "periodic",
            "periodic",
        ),
        cell=(0, 0, 0, 1, 1, 1),
        short_forces={"method": "cut-off", "cutoff": 14.0},  # "dielectric": 0.0},
        long_forces={"method": "pme"},  # "dielectric": 0.0},
    )

    class OptimDummyComponent(TacticComponent):
        @classproperty
        def input(cls):
            return mmic_optim.InputOptim

        @classproperty
        def output(cls):
            return mmic_optim.OutputOptim

        @classmethod
        def strategy_comps(cls):
            return mmic_optim.OptimComponent

        @classproperty
        def version(cls):
            return None

        def execute(
            self, inputs: mmic_optim.InputOptim
        ) -> Tuple[bool, mmic_optim.OutputOptim]:

            return (
                True,
                mmic_optim.OutputOptim(
                    proc_input=inputs,
                    molecule=mol,
                    schema_name="test",
                    schema_version=1.0,
                    success=True,
                ),
            )

    outputs = OptimDummyComponent.compute(inputs)
