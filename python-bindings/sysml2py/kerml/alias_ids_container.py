from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_alias_ids_container
from lionweb.model.impl.dynamic_node import DynamicNode


class AliasIdsContainer(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_alias_ids_container()

    @property
    def aliasIds(self) ->str:
        return cast(str, get_property_value_by_name(self, 'aliasIds'))

    @aliasIds.setter
    def aliasIds(self, value: str):
        property_ = self.get_classifier().require_property_by_name('aliasIds')
        self.set_property_value(property=property_, value=value)
