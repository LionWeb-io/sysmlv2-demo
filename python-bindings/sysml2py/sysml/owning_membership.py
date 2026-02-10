from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_owning_membership
from .membership import Membership
if TYPE_CHECKING:
    from .i_element import IElement


class OwningMembership(Membership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_owning_membership()

    @property
    def ownedMemberElementId(self) ->str:
        return cast(str, get_property_value_by_name(self,
            'ownedMemberElementId'))

    @ownedMemberElementId.setter
    def ownedMemberElementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name(
            'ownedMemberElementId')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedMemberShortName(self) ->str:
        return cast(str, get_property_value_by_name(self,
            'ownedMemberShortName'))

    @ownedMemberShortName.setter
    def ownedMemberShortName(self, value: str):
        property_ = self.get_classifier().require_property_by_name(
            'ownedMemberShortName')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedMemberName(self) ->str:
        return cast(str, get_property_value_by_name(self, 'ownedMemberName'))

    @ownedMemberName.setter
    def ownedMemberName(self, value: str):
        property_ = self.get_classifier().require_property_by_name(
            'ownedMemberName')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedMemberElement(self) ->'Optional["IElement"]':
        res = get_only_reference_value_by_reference_name(self,
            'ownedMemberElement')
        if res:
            return cast('IElement', res.referred)
        else:
            return None

    @ownedMemberElement.setter
    def ownedMemberElement(self, ownedMemberElement: '"IElement"'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedMemberElement')
        if self.ownedMemberElement:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedMemberElement, ownedMemberElement.name))
