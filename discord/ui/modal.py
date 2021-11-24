from __future__ import annotations
from typing import Any, Dict, List, Optional

import os
from .item import Item
from itertools import groupby

from .view import _ViewWeights as _ModalWeights

__all__ = ("Modal",)


class Modal:
    """Represents a UI Modal.

    This object must be inherited to create a UI within Discord.

    .. versionadded:: 2.0
    """

    def __init__(self, title: str, custom_id: Optional[str] = None) -> None:

        self.title = title
        self.custom_id = custom_id
        self.children = []

        if not custom_id:
            self.custom_id = os.urandom(16).hex()

        self.__weights = _ModalWeights(self.children)

    def add_item(self, item: Item):
        if not isinstance(item, Item):
            raise TypeError(f"expected Item not {item.__class__!r}")

        if len(self.children) > 5:
            raise ValueError("Modal can only have a maximum of 5 items")

        self.__weights.add_item(item)
        self.children.append(item)

    def remove_item(self, item: Item):

        try:
            self.children.remove(item)
        except ValueError:
            pass
        else:
            self.__weights.remove_item(item)

    def to_components(self) -> List[Dict[str, Any]]:
        def key(item: Item) -> int:
            return item._rendered_row or 0

        children = sorted(self.children, key=key)
        components: List[Dict[str, Any]] = []
        for _, group in groupby(children, key=key):
            children = [item.to_component_dict() for item in group]
            if not children:
                continue

            components.append(
                {
                    "type": 1,
                    "components": children,
                }
            )

        return components

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "custom_id": self.custom_id,
            "components": self.to_components(),
        }
