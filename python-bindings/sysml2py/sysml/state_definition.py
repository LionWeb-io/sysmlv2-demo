from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_state_definition
from .action_definition import ActionDefinition
if TYPE_CHECKING:
    from .state_usage import StateUsage
    from .i_action_usage import IActionUsage


class StateDefinition(ActionDefinition):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_state_definition()

    @property
    def state(self) ->'List["StateUsage"]':
        res = get_reference_value_by_name(self, 'state')
        return [(cast('StateUsage', r.referred) if r else None) for r in res]

    def add_to_state(self, new_element: '"StateUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('state'), ReferenceValue(new_element,
            new_element.name))

    @property
    def entryAction(self) ->'Optional["IActionUsage"]':
        res = get_only_reference_value_by_reference_name(self, 'entryAction')
        if res:
            return cast('IActionUsage', res.referred)
        else:
            return None

    @entryAction.setter
    def entryAction(self, entryAction: '"IActionUsage"'):
        reference = self.get_classifier().get_reference_by_name('entryAction')
        if self.entryAction:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(entryAction,
            entryAction.name))

    @property
    def doAction(self) ->'Optional["IActionUsage"]':
        res = get_only_reference_value_by_reference_name(self, 'doAction')
        if res:
            return cast('IActionUsage', res.referred)
        else:
            return None

    @doAction.setter
    def doAction(self, doAction: '"IActionUsage"'):
        reference = self.get_classifier().get_reference_by_name('doAction')
        if self.doAction:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(doAction,
            doAction.name))

    @property
    def exitAction(self) ->'Optional["IActionUsage"]':
        res = get_only_reference_value_by_reference_name(self, 'exitAction')
        if res:
            return cast('IActionUsage', res.referred)
        else:
            return None

    @exitAction.setter
    def exitAction(self, exitAction: '"IActionUsage"'):
        reference = self.get_classifier().get_reference_by_name('exitAction')
        if self.exitAction:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(exitAction,
            exitAction.name))

    @property
    def isParallel(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isParallel'))

    @isParallel.setter
    def isParallel(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isParallel'
            )
        self.set_property_value(property=property_, value=value)
