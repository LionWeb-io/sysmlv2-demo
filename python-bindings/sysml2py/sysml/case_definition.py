from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_case_definition
from .calculation_definition import CalculationDefinition
if TYPE_CHECKING:
    from .requirement_usage import RequirementUsage
    from .i_usage import IUsage
    from .i_part_usage import IPartUsage


class CaseDefinition(CalculationDefinition):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_case_definition()

    @property
    def objectiveRequirement(self) ->'Optional["RequirementUsage"]':
        res = get_only_reference_value_by_reference_name(self,
            'objectiveRequirement')
        if res:
            return cast('RequirementUsage', res.referred)
        else:
            return None

    @objectiveRequirement.setter
    def objectiveRequirement(self, objectiveRequirement: '"RequirementUsage"'):
        reference = self.get_classifier().get_reference_by_name(
            'objectiveRequirement')
        if self.objectiveRequirement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            objectiveRequirement, objectiveRequirement.name))

    @property
    def subjectParameter(self) ->'Optional["IUsage"]':
        res = get_only_reference_value_by_reference_name(self,
            'subjectParameter')
        if res:
            return cast('IUsage', res.referred)
        else:
            return None

    @subjectParameter.setter
    def subjectParameter(self, subjectParameter: '"IUsage"'):
        reference = self.get_classifier().get_reference_by_name(
            'subjectParameter')
        if self.subjectParameter:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(subjectParameter,
            subjectParameter.name))

    @property
    def actorParameter(self) ->'List["IPartUsage"]':
        res = get_reference_value_by_name(self, 'actorParameter')
        return [(cast('IPartUsage', r.referred) if r else None) for r in res]

    def add_to_actor_parameter(self, new_element: '"IPartUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('actorParameter'), ReferenceValue(
            new_element, new_element.name))
