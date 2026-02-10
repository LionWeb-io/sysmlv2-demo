from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_feature_value
from .owning_membership import OwningMembership
if TYPE_CHECKING:
    from .i_feature import IFeature
    from .expression import Expression


class FeatureValue(OwningMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_feature_value()

    @property
    def featureWithValue(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self,
            'featureWithValue')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @featureWithValue.setter
    def featureWithValue(self, featureWithValue: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name(
            'featureWithValue')
        if self.featureWithValue:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureWithValue,
            featureWithValue.name))

    @property
    def value(self) ->'Optional["Expression"]':
        res = get_only_reference_value_by_reference_name(self, 'value')
        if res:
            return cast('Expression', res.referred)
        else:
            return None

    @value.setter
    def value(self, value: '"Expression"'):
        reference = self.get_classifier().get_reference_by_name('value')
        if self.value:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(value, value.name))

    @property
    def isInitial(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isInitial'))

    @isInitial.setter
    def isInitial(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isInitial')
        self.set_property_value(property=property_, value=value)

    @property
    def isDefault(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDefault'))

    @isDefault.setter
    def isDefault(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDefault')
        self.set_property_value(property=property_, value=value)
