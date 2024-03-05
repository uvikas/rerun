# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/re_types/definitions/rerun/archetypes/line_strips3d.fbs".

# You can extend this class by creating a "LineStrips3DExt" class in "line_strips3d_ext.py".

from __future__ import annotations

from typing import Any

from attrs import define, field

from .. import components, datatypes
from .._baseclasses import Archetype
from ..error_utils import catch_and_log_exceptions

__all__ = ["LineStrips3D"]


@define(str=False, repr=False, init=False)
class LineStrips3D(Archetype):
    """
    **Archetype**: 3D line strips with positions and optional colors, radii, labels, etc.

    Example
    -------
    ### Many strips:
    ```python
    import rerun as rr

    rr.init("rerun_example_line_strip3d_batch", spawn=True)

    rr.log(
        "strips",
        rr.LineStrips3D(
            [
                [
                    [0, 0, 2],
                    [1, 0, 2],
                    [1, 1, 2],
                    [0, 1, 2],
                ],
                [
                    [0, 0, 0],
                    [0, 0, 1],
                    [1, 0, 0],
                    [1, 0, 1],
                    [1, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0],
                    [0, 1, 1],
                ],
            ],
            colors=[[255, 0, 0], [0, 255, 0]],
            radii=[0.025, 0.005],
            labels=["one strip here", "and one strip there"],
        ),
    )
    ```
    <center>
    <picture>
      <source media="(max-width: 480px)" srcset="https://static.rerun.io/line_strip3d_batch/102e5ec5271475657fbc76b469267e4ec8e84337/480w.png">
      <source media="(max-width: 768px)" srcset="https://static.rerun.io/line_strip3d_batch/102e5ec5271475657fbc76b469267e4ec8e84337/768w.png">
      <source media="(max-width: 1024px)" srcset="https://static.rerun.io/line_strip3d_batch/102e5ec5271475657fbc76b469267e4ec8e84337/1024w.png">
      <source media="(max-width: 1200px)" srcset="https://static.rerun.io/line_strip3d_batch/102e5ec5271475657fbc76b469267e4ec8e84337/1200w.png">
      <img src="https://static.rerun.io/line_strip3d_batch/102e5ec5271475657fbc76b469267e4ec8e84337/full.png" width="640">
    </picture>
    </center>

    """

    def __init__(
        self: Any,
        strips: components.LineStrip3DArrayLike,
        *,
        radii: components.RadiusArrayLike | None = None,
        colors: datatypes.Rgba32ArrayLike | None = None,
        labels: datatypes.Utf8ArrayLike | None = None,
        class_ids: datatypes.ClassIdArrayLike | None = None,
    ):
        """
        Create a new instance of the LineStrips3D archetype.

        Parameters
        ----------
        strips:
            All the actual 3D line strips that make up the batch.
        radii:
            Optional radii for the line strips.
        colors:
            Optional colors for the line strips.
        labels:
            Optional text labels for the line strips.
        class_ids:
            Optional `ClassId`s for the lines.

            The class ID provides colors and labels if not specified explicitly.

        """

        # You can define your own __init__ function as a member of LineStrips3DExt in line_strips3d_ext.py
        with catch_and_log_exceptions(context=self.__class__.__name__):
            self.__attrs_init__(strips=strips, radii=radii, colors=colors, labels=labels, class_ids=class_ids)
            return
        self.__attrs_clear__()

    def __attrs_clear__(self) -> None:
        """Convenience method for calling `__attrs_init__` with all `None`s."""
        self.__attrs_init__(
            strips=None,  # type: ignore[arg-type]
            radii=None,  # type: ignore[arg-type]
            colors=None,  # type: ignore[arg-type]
            labels=None,  # type: ignore[arg-type]
            class_ids=None,  # type: ignore[arg-type]
        )

    @classmethod
    def _clear(cls) -> LineStrips3D:
        """Produce an empty LineStrips3D, bypassing `__init__`."""
        inst = cls.__new__(cls)
        inst.__attrs_clear__()
        return inst

    strips: components.LineStrip3DBatch = field(
        metadata={"component": "required"},
        converter=components.LineStrip3DBatch._required,  # type: ignore[misc]
    )
    # All the actual 3D line strips that make up the batch.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    radii: components.RadiusBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.RadiusBatch._optional,  # type: ignore[misc]
    )
    # Optional radii for the line strips.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    colors: components.ColorBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.ColorBatch._optional,  # type: ignore[misc]
    )
    # Optional colors for the line strips.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    labels: components.TextBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.TextBatch._optional,  # type: ignore[misc]
    )
    # Optional text labels for the line strips.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    class_ids: components.ClassIdBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.ClassIdBatch._optional,  # type: ignore[misc]
    )
    # Optional `ClassId`s for the lines.
    #
    # The class ID provides colors and labels if not specified explicitly.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__
