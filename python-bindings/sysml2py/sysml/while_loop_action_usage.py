from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_while_loop_action_usage
from .loop_action_usage import LoopActionUsage
if TYPE_CHECKING:
    from .i_expression import IExpression


class WhileLoopActionUsage(LoopActionUsage):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_while_loop_action_usage()

    @property
    def whileArgument(self) ->'Optional["IExpression"]':
        res = get_only_reference_value_by_reference_name(self, 'whileArgument')
        if res:
            return cast('IExpression', res.referred)
        else:
            return None

    @whileArgument.setter
    def whileArgument(self, whileArgument: '"IExpression"'):
        reference = self.get_classifier().get_reference_by_name('whileArgument'
            )
        if self.whileArgument:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(whileArgument,
            whileArgument.name))

    @property
    def untilArgument(self) ->'Optional["IExpression"]':
        res = get_only_reference_value_by_reference_name(self, 'untilArgument')
        if res:
            return cast('IExpression', res.referred)
        else:
            return None

    @untilArgument.setter
    def untilArgument(self, untilArgument: '"IExpression"'):
        reference = self.get_classifier().get_reference_by_name('untilArgument'
            )
        if self.untilArgument:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(untilArgument,
            untilArgument.name))
