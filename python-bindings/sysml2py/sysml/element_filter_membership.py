from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_element_filter_membership
from .owning_membership import OwningMembership
if TYPE_CHECKING:
    from .i_expression import IExpression


class ElementFilterMembership(OwningMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_element_filter_membership()

    @property
    def condition(self) ->'Optional["IExpression"]':
        res = get_only_reference_value_by_reference_name(self, 'condition')
        if res:
            return cast('IExpression', res.referred)
        else:
            return None

    @condition.setter
    def condition(self, condition: '"IExpression"'):
        reference = self.get_classifier().get_reference_by_name('condition')
        if self.condition:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(condition,
            condition.name))
