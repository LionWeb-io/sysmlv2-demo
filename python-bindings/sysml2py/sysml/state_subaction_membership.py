from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_state_subaction_membership
from .feature_membership import FeatureMembership
from .state_subaction_kind import StateSubactionKind
if TYPE_CHECKING:
    from .i_action_usage import IActionUsage


class StateSubactionMembership(FeatureMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_state_subaction_membership()

    @property
    def kind(self) ->StateSubactionKind:
        return cast(StateSubactionKind, get_property_value_by_name(self,
            'kind'))

    @kind.setter
    def kind(self, value: StateSubactionKind):
        property_ = self.get_classifier().require_property_by_name('kind')
        self.set_property_value(property=property_, value=value)

    @property
    def action(self) ->'Optional["IActionUsage"]':
        res = get_only_reference_value_by_reference_name(self, 'action')
        if res:
            return cast('IActionUsage', res.referred)
        else:
            return None

    @action.setter
    def action(self, action: '"IActionUsage"'):
        reference = self.get_classifier().get_reference_by_name('action')
        if self.action:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(action, action.name)
            )
