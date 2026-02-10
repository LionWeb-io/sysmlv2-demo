from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_enumeration_usage
from .attribute_usage import AttributeUsage
if TYPE_CHECKING:
    from .enumeration_definition import EnumerationDefinition


class EnumerationUsage(AttributeUsage):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_enumeration_usage()

    @property
    def enumerationDefinition(self) ->'Optional["EnumerationDefinition"]':
        res = get_only_reference_value_by_reference_name(self,
            'enumerationDefinition')
        if res:
            return cast('EnumerationDefinition', res.referred)
        else:
            return None

    @enumerationDefinition.setter
    def enumerationDefinition(self, enumerationDefinition:
        '"EnumerationDefinition"'):
        reference = self.get_classifier().get_reference_by_name(
            'enumerationDefinition')
        if self.enumerationDefinition:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            enumerationDefinition, enumerationDefinition.name))
