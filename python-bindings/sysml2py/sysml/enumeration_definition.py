from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_enumeration_definition
from .attribute_definition import AttributeDefinition
if TYPE_CHECKING:
    from .enumeration_usage import EnumerationUsage


class EnumerationDefinition(AttributeDefinition):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_enumeration_definition()

    @property
    def enumeratedValue(self) ->'List["EnumerationUsage"]':
        res = get_reference_value_by_name(self, 'enumeratedValue')
        return [(cast('EnumerationUsage', r.referred) if r else None) for r in
            res]

    def add_to_enumerated_value(self, new_element: '"EnumerationUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('enumeratedValue'), ReferenceValue(
            new_element, new_element.name))
