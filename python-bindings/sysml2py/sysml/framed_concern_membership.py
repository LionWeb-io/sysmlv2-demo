from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_framed_concern_membership
from .requirement_constraint_membership import RequirementConstraintMembership
if TYPE_CHECKING:
    from .concern_usage import ConcernUsage


class FramedConcernMembership(RequirementConstraintMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_framed_concern_membership()

    @property
    def ownedConcern(self) ->'Optional["ConcernUsage"]':
        res = get_only_reference_value_by_reference_name(self, 'ownedConcern')
        if res:
            return cast('ConcernUsage', res.referred)
        else:
            return None

    @ownedConcern.setter
    def ownedConcern(self, ownedConcern: '"ConcernUsage"'):
        reference = self.get_classifier().get_reference_by_name('ownedConcern')
        if self.ownedConcern:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConcern,
            ownedConcern.name))

    @property
    def referencedConcern(self) ->'Optional["ConcernUsage"]':
        res = get_only_reference_value_by_reference_name(self,
            'referencedConcern')
        if res:
            return cast('ConcernUsage', res.referred)
        else:
            return None

    @referencedConcern.setter
    def referencedConcern(self, referencedConcern: '"ConcernUsage"'):
        reference = self.get_classifier().get_reference_by_name(
            'referencedConcern')
        if self.referencedConcern:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            referencedConcern, referencedConcern.name))
