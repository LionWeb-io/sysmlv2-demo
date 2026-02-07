from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_variant_membership
from .owning_membership import OwningMembership
if TYPE_CHECKING:
    from .i_usage import IUsage


class VariantMembership(OwningMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_variant_membership()

    @property
    def ownedVariantUsage(self) ->'Optional["IUsage"]':
        res = get_only_reference_value_by_reference_name(self,
            'ownedVariantUsage')
        if res:
            return cast('IUsage', res.referred)
        else:
            return None

    @ownedVariantUsage.setter
    def ownedVariantUsage(self, ownedVariantUsage: '"IUsage"'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedVariantUsage')
        if self.ownedVariantUsage:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedVariantUsage, ownedVariantUsage.name))
