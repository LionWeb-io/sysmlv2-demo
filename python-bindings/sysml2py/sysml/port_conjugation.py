from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_port_conjugation
from .conjugation import Conjugation
if TYPE_CHECKING:
    from .port_definition import PortDefinition
    from .conjugated_port_definition import ConjugatedPortDefinition


class PortConjugation(Conjugation):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_port_conjugation()

    @property
    def originalPortDefinition(self) ->'Optional["PortDefinition"]':
        res = get_only_reference_value_by_reference_name(self,
            'originalPortDefinition')
        if res:
            return cast('PortDefinition', res.referred)
        else:
            return None

    @originalPortDefinition.setter
    def originalPortDefinition(self, originalPortDefinition: '"PortDefinition"'
        ):
        reference = self.get_classifier().get_reference_by_name(
            'originalPortDefinition')
        if self.originalPortDefinition:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            originalPortDefinition, originalPortDefinition.name))

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
