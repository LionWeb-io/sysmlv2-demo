from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_view_rendering_membership
from .feature_membership import FeatureMembership
if TYPE_CHECKING:
    from .rendering_usage import RenderingUsage


class ViewRenderingMembership(FeatureMembership):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_view_rendering_membership()

    @property
    def ownedRendering(self) ->'Optional["RenderingUsage"]':
        res = get_only_reference_value_by_reference_name(self, 'ownedRendering'
            )
        if res:
            return cast('RenderingUsage', res.referred)
        else:
            return None

    @ownedRendering.setter
    def ownedRendering(self, ownedRendering: '"RenderingUsage"'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedRendering')
        if self.ownedRendering:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedRendering,
            ownedRendering.name))

    @property
    def referencedRendering(self) ->'Optional["RenderingUsage"]':
        res = get_only_reference_value_by_reference_name(self,
            'referencedRendering')
        if res:
            return cast('RenderingUsage', res.referred)
        else:
            return None

    @referencedRendering.setter
    def referencedRendering(self, referencedRendering: '"RenderingUsage"'):
        reference = self.get_classifier().get_reference_by_name(
            'referencedRendering')
        if self.referencedRendering:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            referencedRendering, referencedRendering.name))
