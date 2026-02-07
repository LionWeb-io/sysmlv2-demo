from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_invocation_expression
from .expression import Expression
if TYPE_CHECKING:
    from .expression import Expression


class InvocationExpression(Expression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_invocation_expression()

    @property
    def argument(self) ->'List["Expression"]':
        res = get_reference_value_by_name(self, 'argument')
        return [(cast('Expression', r.referred) if r else None) for r in res]

    def add_to_argument(self, new_element: '"Expression"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('argument'), ReferenceValue(
            new_element, new_element.name))

    @property
    def operand(self) ->'List["Expression"]':
        res = self.get_children('operand')
        return res

    def add_to_operand(self, new_element: '"Expression"'):
        self.add_child(self.get_classifier().require_containment_by_name(
            'operand'), new_element)
