from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_for_loop_action_usage
from .loop_action_usage import LoopActionUsage
if TYPE_CHECKING:
    from .i_expression import IExpression
    from .reference_usage import ReferenceUsage


class ForLoopActionUsage(LoopActionUsage):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_for_loop_action_usage()

    @property
    def seqArgument(self) ->'Optional["IExpression"]':
        res = get_only_reference_value_by_reference_name(self, 'seqArgument')
        if res:
            return cast('IExpression', res.referred)
        else:
            return None

    @seqArgument.setter
    def seqArgument(self, seqArgument: '"IExpression"'):
        reference = self.get_classifier().get_reference_by_name('seqArgument')
        if self.seqArgument:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(seqArgument,
            seqArgument.name))

    @property
    def loopVariable(self) ->'Optional["ReferenceUsage"]':
        res = get_only_reference_value_by_reference_name(self, 'loopVariable')
        if res:
            return cast('ReferenceUsage', res.referred)
        else:
            return None

    @loopVariable.setter
    def loopVariable(self, loopVariable: '"ReferenceUsage"'):
        reference = self.get_classifier().get_reference_by_name('loopVariable')
        if self.loopVariable:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(loopVariable,
            loopVariable.name))
