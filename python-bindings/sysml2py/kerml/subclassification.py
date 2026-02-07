from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_subclassification
from .specialization import Specialization
if TYPE_CHECKING:
    from .i_classifier import IClassifier


class Subclassification(Specialization):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_subclassification()

    @property
    def superclassifier(self) ->'Optional["IClassifier"]':
        res = get_only_reference_value_by_reference_name(self,
            'superclassifier')
        if res:
            return cast('IClassifier', res.referred)
        else:
            return None

    @superclassifier.setter
    def superclassifier(self, superclassifier: '"IClassifier"'):
        reference = self.get_classifier().get_reference_by_name(
            'superclassifier')
        if self.superclassifier:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(superclassifier,
            superclassifier.name))

    @property
    def owningClassifier(self) ->'Optional["IClassifier"]':
        res = get_only_reference_value_by_reference_name(self,
            'owningClassifier')
        if res:
            return cast('IClassifier', res.referred)
        else:
            return None

    @owningClassifier.setter
    def owningClassifier(self, owningClassifier: '"IClassifier"'):
        reference = self.get_classifier().get_reference_by_name(
            'owningClassifier')
        if self.owningClassifier:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningClassifier,
            owningClassifier.name))

    @property
    def subclassifier(self) ->'Optional["IClassifier"]':
        res = get_only_reference_value_by_reference_name(self, 'subclassifier')
        if res:
            return cast('IClassifier', res.referred)
        else:
            return None

    @subclassifier.setter
    def subclassifier(self, subclassifier: '"IClassifier"'):
        reference = self.get_classifier().get_reference_by_name('subclassifier'
            )
        if self.subclassifier:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(subclassifier,
            subclassifier.name))
