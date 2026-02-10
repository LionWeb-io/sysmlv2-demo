from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_interface_definition
from .connection_definition import ConnectionDefinition
if TYPE_CHECKING:
    from .port_usage import PortUsage


class InterfaceDefinition(ConnectionDefinition):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_interface_definition()

    @property
    def interfaceEnd(self) ->'List["PortUsage"]':
        res = get_reference_value_by_name(self, 'interfaceEnd')
        return [(cast('PortUsage', r.referred) if r else None) for r in res]

    def add_to_interface_end(self, new_element: '"PortUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('interfaceEnd'), ReferenceValue(
            new_element, new_element.name))
