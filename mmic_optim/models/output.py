from cmselemental.models.procedures import OutputProc
from .input import InputOptim
from mmelemental.models import Molecule, Trajectory
from pydantic import Field
from typing import Optional, Dict, List, Union

__all__ = ["OutputOptim"]


class OutputOptim(OutputProc):
    proc_input: InputOptim = Field(
        ..., description="Input schema used to run optimization"
    )
    molecule: Union[Molecule, List[Molecule]] = Field(
        ...,
        description="Molecule output object or list of objects. See the :class:``Molecule`` class..",
    )
    trajectory: Optional[Dict[str, Trajectory]] = Field(
        None,
        description="Trajectory output representing a series of snapshots of the system at "
        "different timesteps. See the :class:``Trajectory`` class.",
    )
    observable: Optional[Dict[str, List[float]]] = Field(
        None,
        description="Stores any observable or physical variable not accounted for in the schema. "
        "e.g. ligand scores used in docking simulations.",
    )
    observable_units: Optional[Dict[str, str]] = Field(
        None, description="Observable units. Any unit supported by pint is allowed."
    )
