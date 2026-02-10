from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_null_expression
from .expression import Expression


class NullExpression(Expression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_null_expression()
