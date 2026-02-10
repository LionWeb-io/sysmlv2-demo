from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_objective_membership
from .feature_membership import FeatureMembership
if TYPE_CHECKING:
    from .requirement_usage import RequirementUsage


class ObjectiveMembership(FeatureMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_objective_membership()

    @property
    def ownedObjectiveRequirement(self) ->'Optional["RequirementUsage"]':
        res = get_only_reference_value_by_reference_name(self,
            'ownedObjectiveRequirement')
        if res:
            return cast('RequirementUsage', res.referred)
        else:
            return None

    @ownedObjectiveRequirement.setter
    def ownedObjectiveRequirement(self, ownedObjectiveRequirement:
        '"RequirementUsage"'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedObjectiveRequirement')
        if self.ownedObjectiveRequirement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedObjectiveRequirement, ownedObjectiveRequirement.name))
