from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_literal_integer
from .literal_expression import LiteralExpression


class LiteralInteger(LiteralExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_literal_integer()

    @property
    def value(self) ->int:
        return cast(int, get_property_value_by_name(self, 'value'))

    @value.setter
    def value(self, value: int):
        property_ = self.get_classifier().require_property_by_name('value')
        self.set_property_value(property=property_, value=value)
