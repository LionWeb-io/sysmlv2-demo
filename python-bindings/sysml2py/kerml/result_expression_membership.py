from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_result_expression_membership
from .feature_membership import FeatureMembership
if TYPE_CHECKING:
    from .expression import Expression


class ResultExpressionMembership(FeatureMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_result_expression_membership()

    @property
    def ownedResultExpression(self) ->'Optional["Expression"]':
        res = get_only_reference_value_by_reference_name(self,
            'ownedResultExpression')
        if res:
            return cast('Expression', res.referred)
        else:
            return None

    @ownedResultExpression.setter
    def ownedResultExpression(self, ownedResultExpression: '"Expression"'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedResultExpression')
        if self.ownedResultExpression:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedResultExpression, ownedResultExpression.name))
