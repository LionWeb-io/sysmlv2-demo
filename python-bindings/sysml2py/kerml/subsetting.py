from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_subsetting
from .specialization import Specialization
if TYPE_CHECKING:
    from .i_feature import IFeature


class Subsetting(Specialization):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_subsetting()

    @property
    def subsettedFeature(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self,
            'subsettedFeature')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @subsettedFeature.setter
    def subsettedFeature(self, subsettedFeature: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name(
            'subsettedFeature')
        if self.subsettedFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(subsettedFeature,
            subsettedFeature.name))

    @property
    def subsettingFeature(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self,
            'subsettingFeature')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @subsettingFeature.setter
    def subsettingFeature(self, subsettingFeature: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name(
            'subsettingFeature')
        if self.subsettingFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            subsettingFeature, subsettingFeature.name))

    @property
    def owningFeature(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self, 'owningFeature')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @owningFeature.setter
    def owningFeature(self, owningFeature: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name('owningFeature'
            )
        if self.owningFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningFeature,
            owningFeature.name))
