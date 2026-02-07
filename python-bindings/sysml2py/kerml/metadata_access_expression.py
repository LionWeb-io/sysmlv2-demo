from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_metadata_access_expression
from .expression import Expression
if TYPE_CHECKING:
    from .i_element import IElement


class MetadataAccessExpression(Expression):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_metadata_access_expression()

    @property
    def referencedElement(self) ->'Optional["IElement"]':
        res = get_only_reference_value_by_reference_name(self,
            'referencedElement')
        if res:
            return cast('IElement', res.referred)
        else:
            return None

    @referencedElement.setter
    def referencedElement(self, referencedElement: '"IElement"'):
        reference = self.get_classifier().get_reference_by_name(
            'referencedElement')
        if self.referencedElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            referencedElement, referencedElement.name))
