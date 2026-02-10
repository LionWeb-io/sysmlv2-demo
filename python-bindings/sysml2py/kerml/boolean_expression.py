from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_boolean_expression
from .expression import Expression
if TYPE_CHECKING:
    from .predicate import Predicate


class BooleanExpression(Expression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_boolean_expression()

    @property
    def predicate(self) ->'Optional["Predicate"]':
        res = get_only_reference_value_by_reference_name(self, 'predicate')
        if res:
            return cast('Predicate', res.referred)
        else:
            return None

    @predicate.setter
    def predicate(self, predicate: '"Predicate"'):
        reference = self.get_classifier().get_reference_by_name('predicate')
        if self.predicate:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(predicate,
            predicate.name))
