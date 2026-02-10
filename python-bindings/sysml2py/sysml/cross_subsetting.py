from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_cross_subsetting
from .subsetting import Subsetting
if TYPE_CHECKING:
    from .i_feature import IFeature


class CrossSubsetting(Subsetting):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_cross_subsetting()

    @property
    def crossedFeature(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self, 'crossedFeature'
            )
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @crossedFeature.setter
    def crossedFeature(self, crossedFeature: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name(
            'crossedFeature')
        if self.crossedFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(crossedFeature,
            crossedFeature.name))

    @property
    def crossingFeature(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self,
            'crossingFeature')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @crossingFeature.setter
    def crossingFeature(self, crossingFeature: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name(
            'crossingFeature')
        if self.crossingFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(crossingFeature,
            crossingFeature.name))
