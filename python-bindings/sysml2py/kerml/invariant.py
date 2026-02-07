from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_invariant
from .boolean_expression import BooleanExpression


class Invariant(BooleanExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_invariant()

    @property
    def isNegated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNegated'))

    @isNegated.setter
    def isNegated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isNegated')
        self.set_property_value(property=property_, value=value)
