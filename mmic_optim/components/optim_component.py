from ..models.input import InputOptim
from ..models.output import OutputOptim
from mmic.components.blueprints import StrategyComponent
from cmselemental.util.decorators import classproperty
from typing import Set


__all__ = ["OptimComponent"]


class OptimComponent(StrategyComponent):
    @classproperty
    def input(cls):
        return InputOptim

    @classproperty
    def output(cls):
        return OutputOptim

    @classproperty
    def version(cls) -> str:
        """Finds program, extracts version, returns normalized version string.
        Returns
        -------
        str
            Return a valid, safe python version string.
        """
        return ""

    @classproperty
    def tactic_comps(cls) -> Set[str]:
        """Returns the supported components e.g. set(['mmic_mda',...]).
        Returns
        -------
        Set[str]
        """
        return {"mmic_optim_openmm", "mmic_optim_gmx"}
