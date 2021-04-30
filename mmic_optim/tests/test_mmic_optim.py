"""
Unit and regression test for the mmic_optim package.
"""

# Import package, test suite, and other packages as needed
import mmic_optim
from mmic.components.blueprints import TacticComponent
import mm_data
import pytest
from typing import Tuple
import sys
import json


mol_file = mm_data.mols["water-mol.json"]
ff_file = mm_data.ffs["water-ff.json"]


def test_mmic_optim_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_optim" in sys.modules


def test_mmic_optim_models():
    with open(mol_file, "r") as fp:
        mol = json.load(fp)

    with open(ff_file, "r") as fp:
        ff = json.load(fp)

    inputs = mmic_optim.OptimInput(
        component="mmic_optim", molecule={"mol": mol}, forcefield={"mol": ff}
    )

    class OptimDummyComponent(TacticComponent):
        @classmethod
        def input(cls):
            return mmic_optim.OptimInput

        @classmethod
        def output(cls):
            return mmic_optim.OptimOutput

        @classmethod
        def strategy_comp(cls):
            return mmic_optim.OptimComponent

        @classmethod
        def get_version(cls):
            return None

        def execute(
            self,
            inputs: mmic_optim.OptimInput,
        ) -> Tuple[bool, mmic_optim.OptimOutput]:

            return True, mmic_optim.OptimOutput(
                proc_input=inputs, molecule=inputs.molecule
            )

    outputs = OptimDummyComponent.compute(inputs)
