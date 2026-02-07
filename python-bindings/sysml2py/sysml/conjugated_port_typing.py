from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_conjugated_port_typing
from .feature_typing import FeatureTyping
if TYPE_CHECKING:
    from .port_definition import PortDefinition
    from .conjugated_port_definition import ConjugatedPortDefinition


class ConjugatedPortTyping(FeatureTyping):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_conjugated_port_typing()

    @property
    def portDefinition(self) ->'Optional["PortDefinition"]':
        res = get_only_reference_value_by_reference_name(self, 'portDefinition'
            )
        if res:
            return cast('PortDefinition', res.referred)
        else:
            return None

    @portDefinition.setter
    def portDefinition(self, portDefinition: '"PortDefinition"'):
        reference = self.get_classifier().get_reference_by_name(
            'portDefinition')
        if self.portDefinition:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(portDefinition,
            portDefinition.name))

    @property
    def conjugatedPortDefinition(self
        ) ->'Optional["ConjugatedPortDefinition"]':
        res = get_only_reference_value_by_reference_name(self,
            'conjugatedPortDefinition')
        if res:
            return cast('ConjugatedPortDefinition', res.referred)
        else:
            return None

    @conjugatedPortDefinition.setter
    def conjugatedPortDefinition(self, conjugatedPortDefinition:
        '"ConjugatedPortDefinition"'):
        reference = self.get_classifier().get_reference_by_name(
            'conjugatedPortDefinition')
        if self.conjugatedPortDefinition:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            conjugatedPortDefinition, conjugatedPortDefinition.name))
