from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_rendering_definition
from .part_definition import PartDefinition
if TYPE_CHECKING:
    from .rendering_usage import RenderingUsage


class RenderingDefinition(PartDefinition):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_rendering_definition()

    @property
    def rendering(self) ->'List["RenderingUsage"]':
        res = get_reference_value_by_name(self, 'rendering')
        return [(cast('RenderingUsage', r.referred) if r else None) for r in
            res]

    def add_to_rendering(self, new_element: '"RenderingUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('rendering'), ReferenceValue(
            new_element, new_element.name))
