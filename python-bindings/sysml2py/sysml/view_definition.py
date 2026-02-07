from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_view_definition
from .part_definition import PartDefinition
if TYPE_CHECKING:
    from .view_usage import ViewUsage
    from .viewpoint_usage import ViewpointUsage
    from .rendering_usage import RenderingUsage
    from .i_expression import IExpression


class ViewDefinition(PartDefinition):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_view_definition()

    @property
    def view(self) ->'List["ViewUsage"]':
        res = get_reference_value_by_name(self, 'view')
        return [(cast('ViewUsage', r.referred) if r else None) for r in res]

    def add_to_view(self, new_element: '"ViewUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('view'), ReferenceValue(new_element,
            new_element.name))

    @property
    def satisfiedViewpoint(self) ->'List["ViewpointUsage"]':
        res = get_reference_value_by_name(self, 'satisfiedViewpoint')
        return [(cast('ViewpointUsage', r.referred) if r else None) for r in
            res]

    def add_to_satisfied_viewpoint(self, new_element: '"ViewpointUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('satisfiedViewpoint'), ReferenceValue
            (new_element, new_element.name))

    @property
    def viewRendering(self) ->'Optional["RenderingUsage"]':
        res = get_only_reference_value_by_reference_name(self, 'viewRendering')
        if res:
            return cast('RenderingUsage', res.referred)
        else:
            return None

    @viewRendering.setter
    def viewRendering(self, viewRendering: '"RenderingUsage"'):
        reference = self.get_classifier().get_reference_by_name('viewRendering'
            )
        if self.viewRendering:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(viewRendering,
            viewRendering.name))

    @property
    def viewCondition(self) ->'List["IExpression"]':
        res = get_reference_value_by_name(self, 'viewCondition')
        return [(cast('IExpression', r.referred) if r else None) for r in res]

    def add_to_view_condition(self, new_element: '"IExpression"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('viewCondition'), ReferenceValue(
            new_element, new_element.name))
