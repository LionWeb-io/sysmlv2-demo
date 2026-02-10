from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_allocation_usage
from .connection_usage import ConnectionUsage
if TYPE_CHECKING:
    from .allocation_definition import AllocationDefinition


class AllocationUsage(ConnectionUsage):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_allocation_usage()

    @property
    def allocationDefinition(self) ->'List["AllocationDefinition"]':
        res = get_reference_value_by_name(self, 'allocationDefinition')
        return [(cast('AllocationDefinition', r.referred) if r else None) for
            r in res]

    def add_to_allocation_definition(self, new_element:
        '"AllocationDefinition"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('allocationDefinition'),
            ReferenceValue(new_element, new_element.name))
