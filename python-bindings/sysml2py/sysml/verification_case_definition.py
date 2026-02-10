from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_verification_case_definition
from .case_definition import CaseDefinition
if TYPE_CHECKING:
    from .requirement_usage import RequirementUsage


class VerificationCaseDefinition(CaseDefinition):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_verification_case_definition()

    @property
    def verifiedRequirement(self) ->'List["RequirementUsage"]':
        res = get_reference_value_by_name(self, 'verifiedRequirement')
        return [(cast('RequirementUsage', r.referred) if r else None) for r in
            res]

    def add_to_verified_requirement(self, new_element: '"RequirementUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('verifiedRequirement'),
            ReferenceValue(new_element, new_element.name))
