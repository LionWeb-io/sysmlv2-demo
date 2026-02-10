from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_use_case_usage
from .case_usage import CaseUsage
if TYPE_CHECKING:
    from .use_case_definition import UseCaseDefinition
    from .use_case_usage import UseCaseUsage


class UseCaseUsage(CaseUsage):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_use_case_usage()

    @property
    def useCaseDefinition(self) ->'Optional["UseCaseDefinition"]':
        res = get_only_reference_value_by_reference_name(self,
            'useCaseDefinition')
        if res:
            return cast('UseCaseDefinition', res.referred)
        else:
            return None

    @useCaseDefinition.setter
    def useCaseDefinition(self, useCaseDefinition: '"UseCaseDefinition"'):
        reference = self.get_classifier().get_reference_by_name(
            'useCaseDefinition')
        if self.useCaseDefinition:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            useCaseDefinition, useCaseDefinition.name))

    @property
    def includedUseCase(self) ->'List["UseCaseUsage"]':
        res = get_reference_value_by_name(self, 'includedUseCase')
        return [(cast('UseCaseUsage', r.referred) if r else None) for r in res]

    def add_to_included_use_case(self, new_element: '"UseCaseUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('includedUseCase'), ReferenceValue(
            new_element, new_element.name))
