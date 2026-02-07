from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_feature_chain_expression
from .operator_expression import OperatorExpression
if TYPE_CHECKING:
    from .i_feature import IFeature


class FeatureChainExpression(OperatorExpression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_feature_chain_expression()

    @property
    def targetFeature(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self, 'targetFeature')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @targetFeature.setter
    def targetFeature(self, targetFeature: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name('targetFeature'
            )
        if self.targetFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(targetFeature,
            targetFeature.name))
