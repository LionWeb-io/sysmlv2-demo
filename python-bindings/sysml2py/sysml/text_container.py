from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_text_container
from lionweb.model.impl.dynamic_node import DynamicNode


class TextContainer(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_text_container()

    @property
    def text(self) ->str:
        return cast(str, get_property_value_by_name(self, 'text'))

    @text.setter
    def text(self, value: str):
        property_ = self.get_classifier().require_property_by_name('text')
        self.set_property_value(property=property_, value=value)
