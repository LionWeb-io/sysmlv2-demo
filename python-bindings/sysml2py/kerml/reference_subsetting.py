from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_reference_subsetting
from .subsetting import Subsetting
if TYPE_CHECKING:
    from .i_feature import IFeature


class ReferenceSubsetting(Subsetting):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_reference_subsetting()

    @property
    def referencedFeature(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self,
            'referencedFeature')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @referencedFeature.setter
    def referencedFeature(self, referencedFeature: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name(
            'referencedFeature')
        if self.referencedFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            referencedFeature, referencedFeature.name))

    @property
    def referencingFeature(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self,
            'referencingFeature')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @referencingFeature.setter
    def referencingFeature(self, referencingFeature: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name(
            'referencingFeature')
        if self.referencingFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            referencingFeature, referencingFeature.name))
