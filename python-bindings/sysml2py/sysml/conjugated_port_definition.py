from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_conjugated_port_definition
from .port_definition import PortDefinition
if TYPE_CHECKING:
    from .port_conjugation import PortConjugation
    from .port_definition import PortDefinition


class ConjugatedPortDefinition(PortDefinition):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_conjugated_port_definition()

    @property
    def ownedPortConjugator(self) ->'Optional["PortConjugation"]':
        res = get_only_reference_value_by_reference_name(self,
            'ownedPortConjugator')
        if res:
            return cast('PortConjugation', res.referred)
        else:
            return None

    @ownedPortConjugator.setter
    def ownedPortConjugator(self, ownedPortConjugator: '"PortConjugation"'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedPortConjugator')
        if self.ownedPortConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedPortConjugator, ownedPortConjugator.name))

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
