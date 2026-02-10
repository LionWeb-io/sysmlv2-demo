from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_membership_import
from .import_ import Import
if TYPE_CHECKING:
    from .membership import Membership


class MembershipImport(Import):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_membership_import()

    @property
    def importedMembership(self) ->'Optional["Membership"]':
        res = get_only_reference_value_by_reference_name(self,
            'importedMembership')
        if res:
            return cast('Membership', res.referred)
        else:
            return None

    @importedMembership.setter
    def importedMembership(self, importedMembership: '"Membership"'):
        reference = self.get_classifier().get_reference_by_name(
            'importedMembership')
        if self.importedMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            importedMembership, importedMembership.name))
