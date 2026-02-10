from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_requirement_constraint_membership
from .feature_membership import FeatureMembership
from .requirement_constraint_kind import RequirementConstraintKind
if TYPE_CHECKING:
    from .i_constraint_usage import IConstraintUsage


class RequirementConstraintMembership(FeatureMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_requirement_constraint_membership()

    @property
    def kind(self) ->RequirementConstraintKind:
        return cast(RequirementConstraintKind, get_property_value_by_name(
            self, 'kind'))

    @kind.setter
    def kind(self, value: RequirementConstraintKind):
        property_ = self.get_classifier().require_property_by_name('kind')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConstraint(self) ->'Optional["IConstraintUsage"]':
        res = get_only_reference_value_by_reference_name(self,
            'ownedConstraint')
        if res:
            return cast('IConstraintUsage', res.referred)
        else:
            return None

    @ownedConstraint.setter
    def ownedConstraint(self, ownedConstraint: '"IConstraintUsage"'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConstraint')
        if self.ownedConstraint:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConstraint,
            ownedConstraint.name))

    @property
    def referencedConstraint(self) ->'Optional["IConstraintUsage"]':
        res = get_only_reference_value_by_reference_name(self,
            'referencedConstraint')
        if res:
            return cast('IConstraintUsage', res.referred)
        else:
            return None

    @referencedConstraint.setter
    def referencedConstraint(self, referencedConstraint: '"IConstraintUsage"'):
        reference = self.get_classifier().get_reference_by_name(
            'referencedConstraint')
        if self.referencedConstraint:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            referencedConstraint, referencedConstraint.name))
