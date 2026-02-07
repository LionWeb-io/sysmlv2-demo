from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_trigger_invocation_expression
from .invocation_expression import InvocationExpression
from .trigger_kind import TriggerKind


class TriggerInvocationExpression(InvocationExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_trigger_invocation_expression()

    @property
    def kind(self) ->TriggerKind:
        return cast(TriggerKind, get_property_value_by_name(self, 'kind'))

    @kind.setter
    def kind(self, value: TriggerKind):
        property_ = self.get_classifier().require_property_by_name('kind')
        self.set_property_value(property=property_, value=value)
