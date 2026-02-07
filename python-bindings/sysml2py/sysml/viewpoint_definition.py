from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_viewpoint_definition
from .requirement_definition import RequirementDefinition
if TYPE_CHECKING:
    from .i_part_usage import IPartUsage


class ViewpointDefinition(RequirementDefinition):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_viewpoint_definition()

    @property
    def viewpointStakeholder(self) ->'List["IPartUsage"]':
        res = get_reference_value_by_name(self, 'viewpointStakeholder')
        return [(cast('IPartUsage', r.referred) if r else None) for r in res]

    def add_to_viewpoint_stakeholder(self, new_element: '"IPartUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('viewpointStakeholder'),
            ReferenceValue(new_element, new_element.name))
