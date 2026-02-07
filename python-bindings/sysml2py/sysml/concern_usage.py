from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_concern_usage
from .requirement_usage import RequirementUsage
if TYPE_CHECKING:
    from .concern_definition import ConcernDefinition


class ConcernUsage(RequirementUsage):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_concern_usage()

    @property
    def concernDefinition(self) ->'Optional["ConcernDefinition"]':
        res = get_only_reference_value_by_reference_name(self,
            'concernDefinition')
        if res:
            return cast('ConcernDefinition', res.referred)
        else:
            return None

    @concernDefinition.setter
    def concernDefinition(self, concernDefinition: '"ConcernDefinition"'):
        reference = self.get_classifier().get_reference_by_name(
            'concernDefinition')
        if self.concernDefinition:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            concernDefinition, concernDefinition.name))
