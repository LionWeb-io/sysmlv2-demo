from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_redefinition
from .subsetting import Subsetting
if TYPE_CHECKING:
    from .i_feature import IFeature


class Redefinition(Subsetting):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_redefinition()

    @property
    def redefiningFeature(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self,
            'redefiningFeature')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @redefiningFeature.setter
    def redefiningFeature(self, redefiningFeature: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name(
            'redefiningFeature')
        if self.redefiningFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            redefiningFeature, redefiningFeature.name))

    @property
    def redefinedFeature(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self,
            'redefinedFeature')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @redefinedFeature.setter
    def redefinedFeature(self, redefinedFeature: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name(
            'redefinedFeature')
        if self.redefinedFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(redefinedFeature,
            redefinedFeature.name))
