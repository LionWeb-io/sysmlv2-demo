from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_transition_feature_membership
from .feature_membership import FeatureMembership
from .transition_feature_kind import TransitionFeatureKind
if TYPE_CHECKING:
    from .i_step import IStep


class TransitionFeatureMembership(FeatureMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_transition_feature_membership()

    @property
    def kind(self) ->TransitionFeatureKind:
        return cast(TransitionFeatureKind, get_property_value_by_name(self,
            'kind'))

    @kind.setter
    def kind(self, value: TransitionFeatureKind):
        property_ = self.get_classifier().require_property_by_name('kind')
        self.set_property_value(property=property_, value=value)

    @property
    def transitionFeature(self) ->'Optional["IStep"]':
        res = get_only_reference_value_by_reference_name(self,
            'transitionFeature')
        if res:
            return cast('IStep', res.referred)
        else:
            return None

    @transitionFeature.setter
    def transitionFeature(self, transitionFeature: '"IStep"'):
        reference = self.get_classifier().get_reference_by_name(
            'transitionFeature')
        if self.transitionFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            transitionFeature, transitionFeature.name))
