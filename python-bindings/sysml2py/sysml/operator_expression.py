from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_operator_expression
from .invocation_expression import InvocationExpression


class OperatorExpression(InvocationExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_operator_expression()

    @property
    def operator(self) ->str:
        return cast(str, get_property_value_by_name(self, 'operator'))

    @operator.setter
    def operator(self, value: str):
        property_ = self.get_classifier().require_property_by_name('operator')
        self.set_property_value(property=property_, value=value)
