from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_subject_membership
from .parameter_membership import ParameterMembership
if TYPE_CHECKING:
    from .i_usage import IUsage


class SubjectMembership(ParameterMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_subject_membership()

    @property
    def ownedSubjectParameter(self) ->'Optional["IUsage"]':
        res = get_only_reference_value_by_reference_name(self,
            'ownedSubjectParameter')
        if res:
            return cast('IUsage', res.referred)
        else:
            return None

    @ownedSubjectParameter.setter
    def ownedSubjectParameter(self, ownedSubjectParameter: '"IUsage"'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedSubjectParameter')
        if self.ownedSubjectParameter:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedSubjectParameter, ownedSubjectParameter.name))
