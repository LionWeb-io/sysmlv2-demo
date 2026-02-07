from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_viewpoint_usage
from .requirement_usage import RequirementUsage
if TYPE_CHECKING:
    from .viewpoint_definition import ViewpointDefinition
    from .i_part_usage import IPartUsage


class ViewpointUsage(RequirementUsage):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_viewpoint_usage()

    @property
    def viewpointDefinition(self) ->'Optional["ViewpointDefinition"]':
        res = get_only_reference_value_by_reference_name(self,
            'viewpointDefinition')
        if res:
            return cast('ViewpointDefinition', res.referred)
        else:
            return None

    @viewpointDefinition.setter
    def viewpointDefinition(self, viewpointDefinition: '"ViewpointDefinition"'
        ):
        reference = self.get_classifier().get_reference_by_name(
            'viewpointDefinition')
        if self.viewpointDefinition:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            viewpointDefinition, viewpointDefinition.name))

    @property
    def viewpointStakeholder(self) ->'List["IPartUsage"]':
        res = get_reference_value_by_name(self, 'viewpointStakeholder')
        return [(cast('IPartUsage', r.referred) if r else None) for r in res]

    def add_to_viewpoint_stakeholder(self, new_element: '"IPartUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('viewpointStakeholder'),
            ReferenceValue(new_element, new_element.name))
