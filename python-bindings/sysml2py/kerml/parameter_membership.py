from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_parameter_membership
from .feature_membership import FeatureMembership
if TYPE_CHECKING:
    from .i_feature import IFeature


class ParameterMembership(FeatureMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_parameter_membership()

    @property
    def ownedMemberParameter(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self,
            'ownedMemberParameter')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @ownedMemberParameter.setter
    def ownedMemberParameter(self, ownedMemberParameter: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedMemberParameter')
        if self.ownedMemberParameter:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedMemberParameter, ownedMemberParameter.name))
