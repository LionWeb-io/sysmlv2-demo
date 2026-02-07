from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_requirement_verification_membership
from .requirement_constraint_membership import RequirementConstraintMembership
if TYPE_CHECKING:
    from .requirement_usage import RequirementUsage


class RequirementVerificationMembership(RequirementConstraintMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_requirement_verification_membership()

    @property
    def ownedRequirement(self) ->'Optional["RequirementUsage"]':
        res = get_only_reference_value_by_reference_name(self,
            'ownedRequirement')
        if res:
            return cast('RequirementUsage', res.referred)
        else:
            return None

    @ownedRequirement.setter
    def ownedRequirement(self, ownedRequirement: '"RequirementUsage"'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedRequirement')
        if self.ownedRequirement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedRequirement,
            ownedRequirement.name))

    @property
    def verifiedRequirement(self) ->'Optional["RequirementUsage"]':
        res = get_only_reference_value_by_reference_name(self,
            'verifiedRequirement')
        if res:
            return cast('RequirementUsage', res.referred)
        else:
            return None

    @verifiedRequirement.setter
    def verifiedRequirement(self, verifiedRequirement: '"RequirementUsage"'):
        reference = self.get_classifier().get_reference_by_name(
            'verifiedRequirement')
        if self.verifiedRequirement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            verifiedRequirement, verifiedRequirement.name))
