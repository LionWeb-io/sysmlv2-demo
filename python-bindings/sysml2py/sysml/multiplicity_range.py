from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_multiplicity_range
from .multiplicity import Multiplicity
if TYPE_CHECKING:
    from .i_expression import IExpression


class MultiplicityRange(Multiplicity):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_multiplicity_range()

    @property
    def lowerBound(self) ->'Optional["IExpression"]':
        res = get_only_reference_value_by_reference_name(self, 'lowerBound')
        if res:
            return cast('IExpression', res.referred)
        else:
            return None

    @lowerBound.setter
    def lowerBound(self, lowerBound: '"IExpression"'):
        reference = self.get_classifier().get_reference_by_name('lowerBound')
        if self.lowerBound:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(lowerBound,
            lowerBound.name))

    @property
    def upperBound(self) ->'Optional["IExpression"]':
        res = get_only_reference_value_by_reference_name(self, 'upperBound')
        if res:
            return cast('IExpression', res.referred)
        else:
            return None

    @upperBound.setter
    def upperBound(self, upperBound: '"IExpression"'):
        reference = self.get_classifier().get_reference_by_name('upperBound')
        if self.upperBound:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(upperBound,
            upperBound.name))

    @property
    def bound(self) ->'List["IExpression"]':
        res = get_reference_value_by_name(self, 'bound')
        return [(cast('IExpression', r.referred) if r else None) for r in res]

    def add_to_bound(self, new_element: '"IExpression"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('bound'), ReferenceValue(new_element,
            new_element.name))
