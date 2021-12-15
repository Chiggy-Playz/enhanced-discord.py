from __future__ import annotations
from typing import TYPE_CHECKING, Any, Dict, List, Optional

import os
from .item import Item
from ..enums import InputTextStyle
from ..utils import MISSING
from ..components import InputText as InputTextComponent
from ..interactions import Interaction


__all__ = ("InputText",)

if TYPE_CHECKING:
    from ..types.components import InputText as InputTextPayload
    from ..types.interactions import (
        ComponentInteractionData,
    )


class InputText(Item):
    def __init__(
        self,
        label: str,
        placeholder: Optional[str] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        style: InputTextStyle = InputTextStyle.short,
        custom_id: Optional[str] = MISSING,
        row: Optional[int] = None,
        required: Optional[bool] = True,
        value: Optional[str] = None,
    ):

        super().__init__()
        custom_id = os.urandom(16).hex() if custom_id is MISSING else custom_id

        self._underlying = InputTextComponent._raw_construct(
            custom_id=custom_id,
            label=label,
            placeholder=placeholder,
            min_length=min_length,
            max_length=max_length,
            style=style,
            required=required,
            value=value,
        )
        self.row = row

    @property
    def width(self) -> int:
        return 5

    @property
    def custom_id(self) -> str:
        """:class:`str`: The ID of the input text that gets received during an interaction."""
        return self._underlying.custom_id

    @custom_id.setter
    def custom_id(self, value: str):
        if not isinstance(value, str):
            raise TypeError("custom_id must be None or str")

        self._underlying.custom_id = value

    @property
    def placeholder(self) -> Optional[str]:
        """Optional[:class:`str`]: The placeholder text that is shown if nothing is typed, if any."""
        return self._underlying.placeholder

    @placeholder.setter
    def placeholder(self, value: Optional[str]):
        if value is not None and not isinstance(value, str):
            raise TypeError("placeholder must be None or str")

        self._underlying.placeholder = value

    @property
    def label(self) -> str:
        """:class:`str`: The label of the input text."""
        return self._underlying.label

    @label.setter
    def label(self, value: str):
        if not isinstance(value, str):
            raise TypeError("label must be str")

        self._underlying.label = value

    @property
    def min_length(self) -> Optional[int]:
        """Optional[:class:`int`]: The minimum length of the input text. Defaults to `0`"""
        return self._underlying.min_length

    @min_length.setter
    def min_length(self, value: Optional[int]):
        if value is not None and not isinstance(value, int):
            raise TypeError("min_length must be None or int")

        self._underlying.min_length = value

    @property
    def max_length(self) -> Optional[int]:
        """Optional[:class:`int`]: The maximum length of the input text."""
        return self._underlying.max_length

    @max_length.setter
    def max_length(self, value: Optional[int]):
        if value is not None and not isinstance(value, int):
            raise TypeError("max_length must be None or int")

        self._underlying.max_length = value

    @property
    def style(self) -> InputTextStyle:
        """:class:`InputTextStyle`: The style of the input text."""
        return self._underlying.style

    @style.setter
    def style(self, value: InputTextStyle):
        if not isinstance(value, InputTextStyle):
            raise TypeError("style must be InputTextStyle")

        self._underlying.style = value

    @property
    def required(self) -> bool:
        """Optional[:class:`bool`] Whether the input text is required. Defaults to true."""
        return self._underlying.required

    @required.setter
    def required(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("required must be bool")

        self._underlying.required = value

    @property
    def value(self) -> Optional[str]:
        """Optional[:class:`str`] The pre filled value of the input text."""
        return self._underlying.value

    @value.setter
    def value(self, value: Optional[str]):
        if value is not None and not isinstance(value, str):
            raise TypeError("value must be None or str")

        self._underlying.value = value

    def to_component_dict(self) -> InputTextPayload:
        return self._underlying.to_dict()

    def refresh_state(self, interaction: Interaction) -> None:
        data: ComponentInteractionData = interaction.data  # type: ignore
