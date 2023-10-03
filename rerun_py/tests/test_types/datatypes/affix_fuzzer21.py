# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/testing/datatypes/fuzzy.fbs".

# You can extend this class by creating a "AffixFuzzer21Ext" class in "affix_fuzzer21_ext.py".

from __future__ import annotations

from typing import Any, Sequence, Union

import numpy as np
import numpy.typing as npt
import pyarrow as pa
from attrs import define, field
from rerun._baseclasses import BaseBatch, BaseExtensionType
from rerun._converters import (
    to_np_float16,
)

__all__ = ["AffixFuzzer21", "AffixFuzzer21ArrayLike", "AffixFuzzer21Batch", "AffixFuzzer21Like", "AffixFuzzer21Type"]


@define(init=False)
class AffixFuzzer21:
    def __init__(self: Any, single_half: float, many_halves: npt.ArrayLike):
        """Create a new instance of the AffixFuzzer21 datatype."""

        # You can define your own __init__ function as a member of AffixFuzzer21Ext in affix_fuzzer21_ext.py
        self.__attrs_init__(single_half=single_half, many_halves=many_halves)

    single_half: float = field(converter=float)
    many_halves: npt.NDArray[np.float16] = field(converter=to_np_float16)


AffixFuzzer21Like = AffixFuzzer21
AffixFuzzer21ArrayLike = Union[
    AffixFuzzer21,
    Sequence[AffixFuzzer21Like],
]


class AffixFuzzer21Type(BaseExtensionType):
    _TYPE_NAME: str = "rerun.testing.datatypes.AffixFuzzer21"

    def __init__(self) -> None:
        pa.ExtensionType.__init__(
            self,
            pa.struct(
                [
                    pa.field("single_half", pa.float16(), nullable=False, metadata={}),
                    pa.field(
                        "many_halves",
                        pa.list_(pa.field("item", pa.float16(), nullable=False, metadata={})),
                        nullable=False,
                        metadata={},
                    ),
                ]
            ),
            self._TYPE_NAME,
        )


class AffixFuzzer21Batch(BaseBatch[AffixFuzzer21ArrayLike]):
    _ARROW_TYPE = AffixFuzzer21Type()

    @staticmethod
    def _native_to_pa_array(data: AffixFuzzer21ArrayLike, data_type: pa.DataType) -> pa.Array:
        raise NotImplementedError  # You need to implement native_to_pa_array_override in affix_fuzzer21_ext.py
