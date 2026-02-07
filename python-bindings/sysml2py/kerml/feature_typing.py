from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_feature_typing
from .specialization import Specialization
if TYPE_CHECKING:
    from .i_feature import IFeature
    from .i_type import IType


class FeatureTyping(Specialization):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_feature_typing()

    @property
    def typedFeature(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self, 'typedFeature')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @typedFeature.setter
    def typedFeature(self, typedFeature: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name('typedFeature')
        if self.typedFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(typedFeature,
            typedFeature.name))

    @property
    def type(self) ->'Optional["IType"]':
        res = get_only_reference_value_by_reference_name(self, 'type')
        if res:
            return cast('IType', res.referred)
        else:
            return None

    @type.setter
    def type(self, type: '"IType"'):
        reference = self.get_classifier().get_reference_by_name('type')
        if self.type:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(type, type.name))

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
