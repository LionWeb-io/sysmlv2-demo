from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_index_expression
from .operator_expression import OperatorExpression


class IndexExpression(OperatorExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_index_expression()
