from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_analysis_case_definition
from .case_definition import CaseDefinition
if TYPE_CHECKING:
    from .i_expression import IExpression


class AnalysisCaseDefinition(CaseDefinition):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_analysis_case_definition()

    @property
    def resultExpression(self) ->'Optional["IExpression"]':
        res = get_only_reference_value_by_reference_name(self,
            'resultExpression')
        if res:
            return cast('IExpression', res.referred)
        else:
            return None

    @resultExpression.setter
    def resultExpression(self, resultExpression: '"IExpression"'):
        reference = self.get_classifier().get_reference_by_name(
            'resultExpression')
        if self.resultExpression:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(resultExpression,
            resultExpression.name))
