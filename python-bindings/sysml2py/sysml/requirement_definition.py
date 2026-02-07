from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_requirement_definition
from .constraint_definition import ConstraintDefinition
if TYPE_CHECKING:
    from .i_usage import IUsage
    from .i_part_usage import IPartUsage
    from .i_constraint_usage import IConstraintUsage
    from .concern_usage import ConcernUsage


class RequirementDefinition(ConstraintDefinition):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_requirement_definition()

    @property
    def reqId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'reqId'))

    @reqId.setter
    def reqId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('reqId')
        self.set_property_value(property=property_, value=value)

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

    @property
    def stakeholderParameter(self) ->'List["IPartUsage"]':
        res = get_reference_value_by_name(self, 'stakeholderParameter')
        return [(cast('IPartUsage', r.referred) if r else None) for r in res]

    def add_to_stakeholder_parameter(self, new_element: '"IPartUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('stakeholderParameter'),
            ReferenceValue(new_element, new_element.name))

    @property
    def assumedConstraint(self) ->'List["IConstraintUsage"]':
        res = get_reference_value_by_name(self, 'assumedConstraint')
        return [(cast('IConstraintUsage', r.referred) if r else None) for r in
            res]

    def add_to_assumed_constraint(self, new_element: '"IConstraintUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('assumedConstraint'), ReferenceValue(
            new_element, new_element.name))

    @property
    def requiredConstraint(self) ->'List["IConstraintUsage"]':
        res = get_reference_value_by_name(self, 'requiredConstraint')
        return [(cast('IConstraintUsage', r.referred) if r else None) for r in
            res]

    def add_to_required_constraint(self, new_element: '"IConstraintUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('requiredConstraint'), ReferenceValue
            (new_element, new_element.name))

    @property
    def framedConcern(self) ->'List["ConcernUsage"]':
        res = get_reference_value_by_name(self, 'framedConcern')
        return [(cast('ConcernUsage', r.referred) if r else None) for r in res]

    def add_to_framed_concern(self, new_element: '"ConcernUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('framedConcern'), ReferenceValue(
            new_element, new_element.name))

    @property
    def textContainer(self) ->'List["TextContainer"]':
        res = self.get_children('textContainer')
        return res

    def add_to_text_container(self, new_element: '"TextContainer"'):
        self.add_child(self.get_classifier().require_containment_by_name(
            'textContainer'), new_element)
