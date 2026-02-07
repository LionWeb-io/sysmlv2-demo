from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_stakeholder_membership
from .parameter_membership import ParameterMembership
if TYPE_CHECKING:
    from .i_part_usage import IPartUsage


class StakeholderMembership(ParameterMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_stakeholder_membership()

    @property
    def ownedStakeholderParameter(self) ->'Optional["IPartUsage"]':
        res = get_only_reference_value_by_reference_name(self,
            'ownedStakeholderParameter')
        if res:
            return cast('IPartUsage', res.referred)
        else:
            return None

    @ownedStakeholderParameter.setter
    def ownedStakeholderParameter(self, ownedStakeholderParameter:
        '"IPartUsage"'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedStakeholderParameter')
        if self.ownedStakeholderParameter:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedStakeholderParameter, ownedStakeholderParameter.name))
