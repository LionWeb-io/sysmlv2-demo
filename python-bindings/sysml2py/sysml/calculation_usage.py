from typing import TYPE_CHECKING, Optional, cast, List
from lionweb.model.classifier_instance_utils import get_only_reference_value_by_reference_name, get_property_value_by_name, get_reference_value_by_name
from lionweb.model.reference_value import ReferenceValue
from .language import get_calculation_usage
from lionweb.model.impl.dynamic_node import DynamicNode
from .portion_kind import PortionKind
from .feature_direction_kind import FeatureDirectionKind
if TYPE_CHECKING:
    from .i_function import IFunction
    from .i_behavior import IBehavior
    from .i_feature import IFeature
    from .i_class import IClass
    from .occurrence_definition import OccurrenceDefinition
    from .i_usage import IUsage
    from .variant_membership import VariantMembership
    from .definition import Definition
    from .i_classifier import IClassifier
    from .reference_usage import ReferenceUsage
    from .attribute_usage import AttributeUsage
    from .enumeration_usage import EnumerationUsage
    from .i_occurrence_usage import IOccurrenceUsage
    from .i_item_usage import IItemUsage
    from .i_part_usage import IPartUsage
    from .port_usage import PortUsage
    from .connector_as_usage import ConnectorAsUsage
    from .flow_connection_usage import FlowConnectionUsage
    from .interface_usage import InterfaceUsage
    from .allocation_usage import AllocationUsage
    from .i_action_usage import IActionUsage
    from .state_usage import StateUsage
    from .transition_usage import TransitionUsage
    from .calculation_usage import CalculationUsage
    from .i_constraint_usage import IConstraintUsage
    from .requirement_usage import RequirementUsage
    from .concern_usage import ConcernUsage
    from .case_usage import CaseUsage
    from .analysis_case_usage import AnalysisCaseUsage
    from .verification_case_usage import VerificationCaseUsage
    from .use_case_usage import UseCaseUsage
    from .view_usage import ViewUsage
    from .viewpoint_usage import ViewpointUsage
    from .rendering_usage import RenderingUsage
    from .metadata_usage import MetadataUsage
    from .i_type import IType
    from .redefinition import Redefinition
    from .subsetting import Subsetting
    from .feature_membership import FeatureMembership
    from .feature_typing import FeatureTyping
    from .type_featuring import TypeFeaturing
    from .feature_inverting import FeatureInverting
    from .feature_chaining import FeatureChaining
    from .reference_subsetting import ReferenceSubsetting
    from .cross_subsetting import CrossSubsetting
    from .membership import Membership
    from .conjugation import Conjugation
    from .multiplicity import Multiplicity
    from .intersecting import Intersecting
    from .unioning import Unioning
    from .disjoining import Disjoining
    from .differencing import Differencing
    from .specialization import Specialization
    from .i_import import IImport
    from .i_element import IElement
    from .owning_membership import OwningMembership
    from .i_namespace import INamespace
    from .i_relationship import IRelationship
    from .documentation import Documentation
    from .annotation import Annotation
    from .textual_representation import TextualRepresentation


class CalculationUsage(DynamicNode):

    def __init__(self, id: str):
        super().__init__(id)
        self.concept = get_calculation_usage()

    @property
    def calculationDefinition(self) ->'Optional["IFunction"]':
        res = get_only_reference_value_by_reference_name(self,
            'calculationDefinition')
        if res:
            return cast('IFunction', res.referred)
        else:
            return None

    @calculationDefinition.setter
    def calculationDefinition(self, calculationDefinition: '"IFunction"'):
        reference = self.get_classifier().get_reference_by_name(
            'calculationDefinition')
        if self.calculationDefinition:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            calculationDefinition, calculationDefinition.name))

    @property
    def actionDefinition(self) ->'List["IBehavior"]':
        res = get_reference_value_by_name(self, 'actionDefinition')
        return [(cast('IBehavior', r.referred) if r else None) for r in res]

    def add_to_action_definition(self, new_element: '"IBehavior"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('actionDefinition'), ReferenceValue(
            new_element, new_element.name))

    @property
    def function(self) ->'Optional["IFunction"]':
        res = get_only_reference_value_by_reference_name(self, 'function')
        if res:
            return cast('IFunction', res.referred)
        else:
            return None

    @function.setter
    def function(self, function: '"IFunction"'):
        reference = self.get_classifier().get_reference_by_name('function')
        if self.function:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(function,
            function.name))

    @property
    def result(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self, 'result')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @result.setter
    def result(self, result: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name('result')
        if self.result:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(result, result.name)
            )

    @property
    def isModelLevelEvaluable(self) ->bool:
        return cast(bool, get_property_value_by_name(self,
            'isModelLevelEvaluable'))

    @isModelLevelEvaluable.setter
    def isModelLevelEvaluable(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isModelLevelEvaluable')
        self.set_property_value(property=property_, value=value)

    @property
    def occurrenceDefinition(self) ->'List["IClass"]':
        res = get_reference_value_by_name(self, 'occurrenceDefinition')
        return [(cast('IClass', r.referred) if r else None) for r in res]

    def add_to_occurrence_definition(self, new_element: '"IClass"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('occurrenceDefinition'),
            ReferenceValue(new_element, new_element.name))

    @property
    def individualDefinition(self) ->'Optional["OccurrenceDefinition"]':
        res = get_only_reference_value_by_reference_name(self,
            'individualDefinition')
        if res:
            return cast('OccurrenceDefinition', res.referred)
        else:
            return None

    @individualDefinition.setter
    def individualDefinition(self, individualDefinition:
        '"OccurrenceDefinition"'):
        reference = self.get_classifier().get_reference_by_name(
            'individualDefinition')
        if self.individualDefinition:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            individualDefinition, individualDefinition.name))

    @property
    def isIndividual(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isIndividual'))

    @isIndividual.setter
    def isIndividual(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isIndividual')
        self.set_property_value(property=property_, value=value)

    @property
    def portionKind(self) ->PortionKind:
        return cast(PortionKind, get_property_value_by_name(self,
            'portionKind'))

    @portionKind.setter
    def portionKind(self, value: PortionKind):
        property_ = self.get_classifier().require_property_by_name(
            'portionKind')
        self.set_property_value(property=property_, value=value)

    @property
    def behavior(self) ->'List["IBehavior"]':
        res = get_reference_value_by_name(self, 'behavior')
        return [(cast('IBehavior', r.referred) if r else None) for r in res]

    def add_to_behavior(self, new_element: '"IBehavior"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('behavior'), ReferenceValue(
            new_element, new_element.name))

    @property
    def parameter(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'parameter')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_parameter(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('parameter'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isReference(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isReference'))

    @isReference.setter
    def isReference(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isReference')
        self.set_property_value(property=property_, value=value)

    @property
    def isVariation(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isVariation'))

    @isVariation.setter
    def isVariation(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isVariation')
        self.set_property_value(property=property_, value=value)

    @property
    def variant(self) ->'List["IUsage"]':
        res = get_reference_value_by_name(self, 'variant')
        return [(cast('IUsage', r.referred) if r else None) for r in res]

    def add_to_variant(self, new_element: '"IUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('variant'), ReferenceValue(
            new_element, new_element.name))

    @property
    def variantMembership(self) ->'List["VariantMembership"]':
        res = get_reference_value_by_name(self, 'variantMembership')
        return [(cast('VariantMembership', r.referred) if r else None) for
            r in res]

    def add_to_variant_membership(self, new_element: '"VariantMembership"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('variantMembership'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningDefinition(self) ->'Optional["Definition"]':
        res = get_only_reference_value_by_reference_name(self,
            'owningDefinition')
        if res:
            return cast('Definition', res.referred)
        else:
            return None

    @owningDefinition.setter
    def owningDefinition(self, owningDefinition: '"Definition"'):
        reference = self.get_classifier().get_reference_by_name(
            'owningDefinition')
        if self.owningDefinition:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningDefinition,
            owningDefinition.name))

    @property
    def owningUsage(self) ->'Optional["IUsage"]':
        res = get_only_reference_value_by_reference_name(self, 'owningUsage')
        if res:
            return cast('IUsage', res.referred)
        else:
            return None

    @owningUsage.setter
    def owningUsage(self, owningUsage: '"IUsage"'):
        reference = self.get_classifier().get_reference_by_name('owningUsage')
        if self.owningUsage:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningUsage,
            owningUsage.name))

    @property
    def nestedUsage(self) ->'List["IUsage"]':
        res = get_reference_value_by_name(self, 'nestedUsage')
        return [(cast('IUsage', r.referred) if r else None) for r in res]

    def add_to_nested_usage(self, new_element: '"IUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedUsage'), ReferenceValue(
            new_element, new_element.name))

    @property
    def definition(self) ->'List["IClassifier"]':
        res = get_reference_value_by_name(self, 'definition')
        return [(cast('IClassifier', r.referred) if r else None) for r in res]

    def add_to_definition(self, new_element: '"IClassifier"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('definition'), ReferenceValue(
            new_element, new_element.name))

    @property
    def usage(self) ->'List["IUsage"]':
        res = get_reference_value_by_name(self, 'usage')
        return [(cast('IUsage', r.referred) if r else None) for r in res]

    def add_to_usage(self, new_element: '"IUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('usage'), ReferenceValue(new_element,
            new_element.name))

    @property
    def directedUsage(self) ->'List["IUsage"]':
        res = get_reference_value_by_name(self, 'directedUsage')
        return [(cast('IUsage', r.referred) if r else None) for r in res]

    def add_to_directed_usage(self, new_element: '"IUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedUsage'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedReference(self) ->'List["ReferenceUsage"]':
        res = get_reference_value_by_name(self, 'nestedReference')
        return [(cast('ReferenceUsage', r.referred) if r else None) for r in
            res]

    def add_to_nested_reference(self, new_element: '"ReferenceUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedReference'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedAttribute(self) ->'List["AttributeUsage"]':
        res = get_reference_value_by_name(self, 'nestedAttribute')
        return [(cast('AttributeUsage', r.referred) if r else None) for r in
            res]

    def add_to_nested_attribute(self, new_element: '"AttributeUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedAttribute'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedEnumeration(self) ->'List["EnumerationUsage"]':
        res = get_reference_value_by_name(self, 'nestedEnumeration')
        return [(cast('EnumerationUsage', r.referred) if r else None) for r in
            res]

    def add_to_nested_enumeration(self, new_element: '"EnumerationUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedEnumeration'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedOccurrence(self) ->'List["IOccurrenceUsage"]':
        res = get_reference_value_by_name(self, 'nestedOccurrence')
        return [(cast('IOccurrenceUsage', r.referred) if r else None) for r in
            res]

    def add_to_nested_occurrence(self, new_element: '"IOccurrenceUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedOccurrence'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedItem(self) ->'List["IItemUsage"]':
        res = get_reference_value_by_name(self, 'nestedItem')
        return [(cast('IItemUsage', r.referred) if r else None) for r in res]

    def add_to_nested_item(self, new_element: '"IItemUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedItem'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedPart(self) ->'List["IPartUsage"]':
        res = get_reference_value_by_name(self, 'nestedPart')
        return [(cast('IPartUsage', r.referred) if r else None) for r in res]

    def add_to_nested_part(self, new_element: '"IPartUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedPart'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedPort(self) ->'List["PortUsage"]':
        res = get_reference_value_by_name(self, 'nestedPort')
        return [(cast('PortUsage', r.referred) if r else None) for r in res]

    def add_to_nested_port(self, new_element: '"PortUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedPort'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedConnection(self) ->'List["ConnectorAsUsage"]':
        res = get_reference_value_by_name(self, 'nestedConnection')
        return [(cast('ConnectorAsUsage', r.referred) if r else None) for r in
            res]

    def add_to_nested_connection(self, new_element: '"ConnectorAsUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedConnection'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedFlow(self) ->'List["FlowConnectionUsage"]':
        res = get_reference_value_by_name(self, 'nestedFlow')
        return [(cast('FlowConnectionUsage', r.referred) if r else None) for
            r in res]

    def add_to_nested_flow(self, new_element: '"FlowConnectionUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedFlow'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedInterface(self) ->'List["InterfaceUsage"]':
        res = get_reference_value_by_name(self, 'nestedInterface')
        return [(cast('InterfaceUsage', r.referred) if r else None) for r in
            res]

    def add_to_nested_interface(self, new_element: '"InterfaceUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedInterface'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedAllocation(self) ->'List["AllocationUsage"]':
        res = get_reference_value_by_name(self, 'nestedAllocation')
        return [(cast('AllocationUsage', r.referred) if r else None) for r in
            res]

    def add_to_nested_allocation(self, new_element: '"AllocationUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedAllocation'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedAction(self) ->'List["IActionUsage"]':
        res = get_reference_value_by_name(self, 'nestedAction')
        return [(cast('IActionUsage', r.referred) if r else None) for r in res]

    def add_to_nested_action(self, new_element: '"IActionUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedAction'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedState(self) ->'List["StateUsage"]':
        res = get_reference_value_by_name(self, 'nestedState')
        return [(cast('StateUsage', r.referred) if r else None) for r in res]

    def add_to_nested_state(self, new_element: '"StateUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedState'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedTransition(self) ->'List["TransitionUsage"]':
        res = get_reference_value_by_name(self, 'nestedTransition')
        return [(cast('TransitionUsage', r.referred) if r else None) for r in
            res]

    def add_to_nested_transition(self, new_element: '"TransitionUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedTransition'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedCalculation(self) ->'List["CalculationUsage"]':
        res = get_reference_value_by_name(self, 'nestedCalculation')
        return [(cast('CalculationUsage', r.referred) if r else None) for r in
            res]

    def add_to_nested_calculation(self, new_element: '"CalculationUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedCalculation'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedConstraint(self) ->'List["IConstraintUsage"]':
        res = get_reference_value_by_name(self, 'nestedConstraint')
        return [(cast('IConstraintUsage', r.referred) if r else None) for r in
            res]

    def add_to_nested_constraint(self, new_element: '"IConstraintUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedConstraint'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedRequirement(self) ->'List["RequirementUsage"]':
        res = get_reference_value_by_name(self, 'nestedRequirement')
        return [(cast('RequirementUsage', r.referred) if r else None) for r in
            res]

    def add_to_nested_requirement(self, new_element: '"RequirementUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedRequirement'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedConcern(self) ->'List["ConcernUsage"]':
        res = get_reference_value_by_name(self, 'nestedConcern')
        return [(cast('ConcernUsage', r.referred) if r else None) for r in res]

    def add_to_nested_concern(self, new_element: '"ConcernUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedConcern'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedCase(self) ->'List["CaseUsage"]':
        res = get_reference_value_by_name(self, 'nestedCase')
        return [(cast('CaseUsage', r.referred) if r else None) for r in res]

    def add_to_nested_case(self, new_element: '"CaseUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedCase'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedAnalysisCase(self) ->'List["AnalysisCaseUsage"]':
        res = get_reference_value_by_name(self, 'nestedAnalysisCase')
        return [(cast('AnalysisCaseUsage', r.referred) if r else None) for
            r in res]

    def add_to_nested_analysis_case(self, new_element: '"AnalysisCaseUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedAnalysisCase'), ReferenceValue
            (new_element, new_element.name))

    @property
    def nestedVerificationCase(self) ->'List["VerificationCaseUsage"]':
        res = get_reference_value_by_name(self, 'nestedVerificationCase')
        return [(cast('VerificationCaseUsage', r.referred) if r else None) for
            r in res]

    def add_to_nested_verification_case(self, new_element:
        '"VerificationCaseUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedVerificationCase'),
            ReferenceValue(new_element, new_element.name))

    @property
    def nestedUseCase(self) ->'List["UseCaseUsage"]':
        res = get_reference_value_by_name(self, 'nestedUseCase')
        return [(cast('UseCaseUsage', r.referred) if r else None) for r in res]

    def add_to_nested_use_case(self, new_element: '"UseCaseUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedUseCase'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedView(self) ->'List["ViewUsage"]':
        res = get_reference_value_by_name(self, 'nestedView')
        return [(cast('ViewUsage', r.referred) if r else None) for r in res]

    def add_to_nested_view(self, new_element: '"ViewUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedView'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedViewpoint(self) ->'List["ViewpointUsage"]':
        res = get_reference_value_by_name(self, 'nestedViewpoint')
        return [(cast('ViewpointUsage', r.referred) if r else None) for r in
            res]

    def add_to_nested_viewpoint(self, new_element: '"ViewpointUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedViewpoint'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedRendering(self) ->'List["RenderingUsage"]':
        res = get_reference_value_by_name(self, 'nestedRendering')
        return [(cast('RenderingUsage', r.referred) if r else None) for r in
            res]

    def add_to_nested_rendering(self, new_element: '"RenderingUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedRendering'), ReferenceValue(
            new_element, new_element.name))

    @property
    def nestedMetadata(self) ->'List["MetadataUsage"]':
        res = get_reference_value_by_name(self, 'nestedMetadata')
        return [(cast('MetadataUsage', r.referred) if r else None) for r in res
            ]

    def add_to_nested_metadata(self, new_element: '"MetadataUsage"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('nestedMetadata'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningType(self) ->'Optional["IType"]':
        res = get_only_reference_value_by_reference_name(self, 'owningType')
        if res:
            return cast('IType', res.referred)
        else:
            return None

    @owningType.setter
    def owningType(self, owningType: '"IType"'):
        reference = self.get_classifier().get_reference_by_name('owningType')
        if self.owningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningType,
            owningType.name))

    @property
    def isUnique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isUnique'))

    @isUnique.setter
    def isUnique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isUnique')
        self.set_property_value(property=property_, value=value)

    @property
    def isOrdered(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isOrdered'))

    @isOrdered.setter
    def isOrdered(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isOrdered')
        self.set_property_value(property=property_, value=value)

    @property
    def type(self) ->'List["IType"]':
        res = get_reference_value_by_name(self, 'type')
        return [(cast('IType', r.referred) if r else None) for r in res]

    def add_to_type(self, new_element: '"IType"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('type'), ReferenceValue(new_element,
            new_element.name))

    @property
    def ownedRedefinition(self) ->'List["Redefinition"]':
        res = get_reference_value_by_name(self, 'ownedRedefinition')
        return [(cast('Redefinition', r.referred) if r else None) for r in res]

    def add_to_owned_redefinition(self, new_element: '"Redefinition"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedRedefinition'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedSubsetting(self) ->'List["Subsetting"]':
        res = get_reference_value_by_name(self, 'ownedSubsetting')
        return [(cast('Subsetting', r.referred) if r else None) for r in res]

    def add_to_owned_subsetting(self, new_element: '"Subsetting"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSubsetting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningFeatureMembership(self) ->'Optional["FeatureMembership"]':
        res = get_only_reference_value_by_reference_name(self,
            'owningFeatureMembership')
        if res:
            return cast('FeatureMembership', res.referred)
        else:
            return None

    @owningFeatureMembership.setter
    def owningFeatureMembership(self, owningFeatureMembership:
        '"FeatureMembership"'):
        reference = self.get_classifier().get_reference_by_name(
            'owningFeatureMembership')
        if self.owningFeatureMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningFeatureMembership, owningFeatureMembership.name))

    @property
    def isComposite(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isComposite'))

    @isComposite.setter
    def isComposite(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isComposite')
        self.set_property_value(property=property_, value=value)

    @property
    def isEnd(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isEnd'))

    @isEnd.setter
    def isEnd(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isEnd')
        self.set_property_value(property=property_, value=value)

    @property
    def endOwningType(self) ->'Optional["IType"]':
        res = get_only_reference_value_by_reference_name(self, 'endOwningType')
        if res:
            return cast('IType', res.referred)
        else:
            return None

    @endOwningType.setter
    def endOwningType(self, endOwningType: '"IType"'):
        reference = self.get_classifier().get_reference_by_name('endOwningType'
            )
        if self.endOwningType:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(endOwningType,
            endOwningType.name))

    @property
    def ownedTyping(self) ->'List["FeatureTyping"]':
        res = get_reference_value_by_name(self, 'ownedTyping')
        return [(cast('FeatureTyping', r.referred) if r else None) for r in res
            ]

    def add_to_owned_typing(self, new_element: '"FeatureTyping"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTyping'), ReferenceValue(
            new_element, new_element.name))

    @property
    def featuringType(self) ->'List["IType"]':
        res = get_reference_value_by_name(self, 'featuringType')
        return [(cast('IType', r.referred) if r else None) for r in res]

    def add_to_featuring_type(self, new_element: '"IType"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featuringType'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedTypeFeaturing(self) ->'List["TypeFeaturing"]':
        res = get_reference_value_by_name(self, 'ownedTypeFeaturing')
        return [(cast('TypeFeaturing', r.referred) if r else None) for r in res
            ]

    def add_to_owned_type_featuring(self, new_element: '"TypeFeaturing"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedTypeFeaturing'), ReferenceValue
            (new_element, new_element.name))

    @property
    def isDerived(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isDerived'))

    @isDerived.setter
    def isDerived(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isDerived')
        self.set_property_value(property=property_, value=value)

    @property
    def chainingFeature(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'chainingFeature')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_chaining_feature(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('chainingFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedFeatureInverting(self) ->'List["FeatureInverting"]':
        res = get_reference_value_by_name(self, 'ownedFeatureInverting')
        return [(cast('FeatureInverting', r.referred) if r else None) for r in
            res]

    def add_to_owned_feature_inverting(self, new_element: '"FeatureInverting"'
        ):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureInverting'),
            ReferenceValue(new_element, new_element.name))

    @property
    def ownedFeatureChaining(self) ->'List["FeatureChaining"]':
        res = get_reference_value_by_name(self, 'ownedFeatureChaining')
        return [(cast('FeatureChaining', r.referred) if r else None) for r in
            res]

    def add_to_owned_feature_chaining(self, new_element: '"FeatureChaining"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureChaining'),
            ReferenceValue(new_element, new_element.name))

    @property
    def isReadOnly(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isReadOnly'))

    @isReadOnly.setter
    def isReadOnly(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isReadOnly'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def isPortion(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isPortion'))

    @isPortion.setter
    def isPortion(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isPortion')
        self.set_property_value(property=property_, value=value)

    @property
    def direction(self) ->FeatureDirectionKind:
        return cast(FeatureDirectionKind, get_property_value_by_name(self,
            'direction'))

    @direction.setter
    def direction(self, value: FeatureDirectionKind):
        property_ = self.get_classifier().require_property_by_name('direction')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedReferenceSubsetting(self) ->'Optional["ReferenceSubsetting"]':
        res = get_only_reference_value_by_reference_name(self,
            'ownedReferenceSubsetting')
        if res:
            return cast('ReferenceSubsetting', res.referred)
        else:
            return None

    @ownedReferenceSubsetting.setter
    def ownedReferenceSubsetting(self, ownedReferenceSubsetting:
        '"ReferenceSubsetting"'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedReferenceSubsetting')
        if self.ownedReferenceSubsetting:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedReferenceSubsetting, ownedReferenceSubsetting.name))

    @property
    def crossFeature(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self, 'crossFeature')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @crossFeature.setter
    def crossFeature(self, crossFeature: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name('crossFeature')
        if self.crossFeature:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(crossFeature,
            crossFeature.name))

    @property
    def ownedCrossSubsetting(self) ->'Optional["CrossSubsetting"]':
        res = get_only_reference_value_by_reference_name(self,
            'ownedCrossSubsetting')
        if res:
            return cast('CrossSubsetting', res.referred)
        else:
            return None

    @ownedCrossSubsetting.setter
    def ownedCrossSubsetting(self, ownedCrossSubsetting: '"CrossSubsetting"'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedCrossSubsetting')
        if self.ownedCrossSubsetting:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            ownedCrossSubsetting, ownedCrossSubsetting.name))

    @property
    def featureTarget(self) ->'Optional["IFeature"]':
        res = get_only_reference_value_by_reference_name(self, 'featureTarget')
        if res:
            return cast('IFeature', res.referred)
        else:
            return None

    @featureTarget.setter
    def featureTarget(self, featureTarget: '"IFeature"'):
        reference = self.get_classifier().get_reference_by_name('featureTarget'
            )
        if self.featureTarget:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(featureTarget,
            featureTarget.name))

    @property
    def isNonunique(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isNonunique'))

    @isNonunique.setter
    def isNonunique(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isNonunique')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedFeatureMembership(self) ->'List["FeatureMembership"]':
        res = get_reference_value_by_name(self, 'ownedFeatureMembership')
        return [(cast('FeatureMembership', r.referred) if r else None) for
            r in res]

    def add_to_owned_feature_membership(self, new_element:
        '"FeatureMembership"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeatureMembership'),
            ReferenceValue(new_element, new_element.name))

    @property
    def ownedFeature(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'ownedFeature')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_owned_feature(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedEndFeature(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'ownedEndFeature')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_owned_end_feature(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedEndFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def feature(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'feature')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_feature(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('feature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def input(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'input')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_input(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('input'), ReferenceValue(new_element,
            new_element.name))

    @property
    def output(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'output')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_output(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('output'), ReferenceValue(new_element,
            new_element.name))

    @property
    def isAbstract(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isAbstract'))

    @isAbstract.setter
    def isAbstract(self, value: bool):
        property_ = self.get_classifier().require_property_by_name('isAbstract'
            )
        self.set_property_value(property=property_, value=value)

    @property
    def inheritedMembership(self) ->'List["Membership"]':
        res = get_reference_value_by_name(self, 'inheritedMembership')
        return [(cast('Membership', r.referred) if r else None) for r in res]

    def add_to_inherited_membership(self, new_element: '"Membership"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedMembership'),
            ReferenceValue(new_element, new_element.name))

    @property
    def endFeature(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'endFeature')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_end_feature(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('endFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def isSufficient(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isSufficient'))

    @isSufficient.setter
    def isSufficient(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isSufficient')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedConjugator(self) ->'Optional["Conjugation"]':
        res = get_only_reference_value_by_reference_name(self,
            'ownedConjugator')
        if res:
            return cast('Conjugation', res.referred)
        else:
            return None

    @ownedConjugator.setter
    def ownedConjugator(self, ownedConjugator: '"Conjugation"'):
        reference = self.get_classifier().get_reference_by_name(
            'ownedConjugator')
        if self.ownedConjugator:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(ownedConjugator,
            ownedConjugator.name))

    @property
    def isConjugated(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isConjugated'))

    @isConjugated.setter
    def isConjugated(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isConjugated')
        self.set_property_value(property=property_, value=value)

    @property
    def inheritedFeature(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'inheritedFeature')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_inherited_feature(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('inheritedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def multiplicity(self) ->'Optional["Multiplicity"]':
        res = get_only_reference_value_by_reference_name(self, 'multiplicity')
        if res:
            return cast('Multiplicity', res.referred)
        else:
            return None

    @multiplicity.setter
    def multiplicity(self, multiplicity: '"Multiplicity"'):
        reference = self.get_classifier().get_reference_by_name('multiplicity')
        if self.multiplicity:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(multiplicity,
            multiplicity.name))

    @property
    def unioningType(self) ->'List["IType"]':
        res = get_reference_value_by_name(self, 'unioningType')
        return [(cast('IType', r.referred) if r else None) for r in res]

    def add_to_unioning_type(self, new_element: '"IType"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('unioningType'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedIntersecting(self) ->'List["Intersecting"]':
        res = get_reference_value_by_name(self, 'ownedIntersecting')
        return [(cast('Intersecting', r.referred) if r else None) for r in res]

    def add_to_owned_intersecting(self, new_element: '"Intersecting"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedIntersecting'), ReferenceValue(
            new_element, new_element.name))

    @property
    def intersectingType(self) ->'List["IType"]':
        res = get_reference_value_by_name(self, 'intersectingType')
        return [(cast('IType', r.referred) if r else None) for r in res]

    def add_to_intersecting_type(self, new_element: '"IType"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('intersectingType'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedUnioning(self) ->'List["Unioning"]':
        res = get_reference_value_by_name(self, 'ownedUnioning')
        return [(cast('Unioning', r.referred) if r else None) for r in res]

    def add_to_owned_unioning(self, new_element: '"Unioning"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedUnioning'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedDisjoining(self) ->'List["Disjoining"]':
        res = get_reference_value_by_name(self, 'ownedDisjoining')
        return [(cast('Disjoining', r.referred) if r else None) for r in res]

    def add_to_owned_disjoining(self, new_element: '"Disjoining"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDisjoining'), ReferenceValue(
            new_element, new_element.name))

    @property
    def featureMembership(self) ->'List["FeatureMembership"]':
        res = get_reference_value_by_name(self, 'featureMembership')
        return [(cast('FeatureMembership', r.referred) if r else None) for
            r in res]

    def add_to_feature_membership(self, new_element: '"FeatureMembership"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('featureMembership'), ReferenceValue(
            new_element, new_element.name))

    @property
    def differencingType(self) ->'List["IType"]':
        res = get_reference_value_by_name(self, 'differencingType')
        return [(cast('IType', r.referred) if r else None) for r in res]

    def add_to_differencing_type(self, new_element: '"IType"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('differencingType'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedDifferencing(self) ->'List["Differencing"]':
        res = get_reference_value_by_name(self, 'ownedDifferencing')
        return [(cast('Differencing', r.referred) if r else None) for r in res]

    def add_to_owned_differencing(self, new_element: '"Differencing"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedDifferencing'), ReferenceValue(
            new_element, new_element.name))

    @property
    def directedFeature(self) ->'List["IFeature"]':
        res = get_reference_value_by_name(self, 'directedFeature')
        return [(cast('IFeature', r.referred) if r else None) for r in res]

    def add_to_directed_feature(self, new_element: '"IFeature"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('directedFeature'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedSpecialization(self) ->'List["Specialization"]':
        res = get_reference_value_by_name(self, 'ownedSpecialization')
        return [(cast('Specialization', r.referred) if r else None) for r in
            res]

    def add_to_owned_specialization(self, new_element: '"Specialization"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedSpecialization'),
            ReferenceValue(new_element, new_element.name))

    @property
    def membership(self) ->'List["Membership"]':
        res = get_reference_value_by_name(self, 'membership')
        return [(cast('Membership', r.referred) if r else None) for r in res]

    def add_to_membership(self, new_element: '"Membership"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('membership'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedImport(self) ->'List["IImport"]':
        res = get_reference_value_by_name(self, 'ownedImport')
        return [(cast('IImport', r.referred) if r else None) for r in res]

    def add_to_owned_import(self, new_element: '"IImport"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedImport'), ReferenceValue(
            new_element, new_element.name))

    @property
    def member(self) ->'List["IElement"]':
        res = get_reference_value_by_name(self, 'member')
        return [(cast('IElement', r.referred) if r else None) for r in res]

    def add_to_member(self, new_element: '"IElement"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('member'), ReferenceValue(new_element,
            new_element.name))

    @property
    def ownedMember(self) ->'List["IElement"]':
        res = get_reference_value_by_name(self, 'ownedMember')
        return [(cast('IElement', r.referred) if r else None) for r in res]

    def add_to_owned_member(self, new_element: '"IElement"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMember'), ReferenceValue(
            new_element, new_element.name))

    @property
    def importedMembership(self) ->'List["Membership"]':
        res = get_reference_value_by_name(self, 'importedMembership')
        return [(cast('Membership', r.referred) if r else None) for r in res]

    def add_to_imported_membership(self, new_element: '"Membership"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('importedMembership'), ReferenceValue
            (new_element, new_element.name))

    @property
    def ownedMembership(self) ->'List["Membership"]':
        res = get_reference_value_by_name(self, 'ownedMembership')
        return [(cast('Membership', r.referred) if r else None) for r in res]

    def add_to_owned_membership(self, new_element: '"Membership"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedMembership'), ReferenceValue(
            new_element, new_element.name))

    @property
    def owningMembership(self) ->'Optional["OwningMembership"]':
        res = get_only_reference_value_by_reference_name(self,
            'owningMembership')
        if res:
            return cast('OwningMembership', res.referred)
        else:
            return None

    @owningMembership.setter
    def owningMembership(self, owningMembership: '"OwningMembership"'):
        reference = self.get_classifier().get_reference_by_name(
            'owningMembership')
        if self.owningMembership:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningMembership,
            owningMembership.name))

    @property
    def owningNamespace(self) ->'Optional["INamespace"]':
        res = get_only_reference_value_by_reference_name(self,
            'owningNamespace')
        if res:
            return cast('INamespace', res.referred)
        else:
            return None

    @owningNamespace.setter
    def owningNamespace(self, owningNamespace: '"INamespace"'):
        reference = self.get_classifier().get_reference_by_name(
            'owningNamespace')
        if self.owningNamespace:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owningNamespace,
            owningNamespace.name))

    @property
    def owningRelationship(self) ->'Optional["IRelationship"]':
        res = get_only_reference_value_by_reference_name(self,
            'owningRelationship')
        if res:
            return cast('IRelationship', res.referred)
        else:
            return None

    @owningRelationship.setter
    def owningRelationship(self, owningRelationship: '"IRelationship"'):
        reference = self.get_classifier().get_reference_by_name(
            'owningRelationship')
        if self.owningRelationship:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(
            owningRelationship, owningRelationship.name))

    @property
    def elementId(self) ->str:
        return cast(str, get_property_value_by_name(self, 'elementId'))

    @elementId.setter
    def elementId(self, value: str):
        property_ = self.get_classifier().require_property_by_name('elementId')
        self.set_property_value(property=property_, value=value)

    @property
    def ownedRelationship(self) ->'List["IRelationship"]':
        res = self.get_children('ownedRelationship')
        return res

    def add_to_owned_relationship(self, new_element: '"IRelationship"'):
        self.add_child(self.get_classifier().require_containment_by_name(
            'ownedRelationship'), new_element)

    @property
    def owner(self) ->'Optional["IElement"]':
        res = get_only_reference_value_by_reference_name(self, 'owner')
        if res:
            return cast('IElement', res.referred)
        else:
            return None

    @owner.setter
    def owner(self, owner: '"IElement"'):
        reference = self.get_classifier().get_reference_by_name('owner')
        if self.owner:
            self.remove_reference_value_by_index(reference, 0)
        self.add_reference_value(reference, ReferenceValue(owner, owner.name))

    @property
    def ownedElement(self) ->'List["IElement"]':
        res = get_reference_value_by_name(self, 'ownedElement')
        return [(cast('IElement', r.referred) if r else None) for r in res]

    def add_to_owned_element(self, new_element: '"IElement"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedElement'), ReferenceValue(
            new_element, new_element.name))

    @property
    def documentation(self) ->'List["Documentation"]':
        res = get_reference_value_by_name(self, 'documentation')
        return [(cast('Documentation', r.referred) if r else None) for r in res
            ]

    def add_to_documentation(self, new_element: '"Documentation"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('documentation'), ReferenceValue(
            new_element, new_element.name))

    @property
    def ownedAnnotation(self) ->'List["Annotation"]':
        res = get_reference_value_by_name(self, 'ownedAnnotation')
        return [(cast('Annotation', r.referred) if r else None) for r in res]

    def add_to_owned_annotation(self, new_element: '"Annotation"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('ownedAnnotation'), ReferenceValue(
            new_element, new_element.name))

    @property
    def textualRepresentation(self) ->'List["TextualRepresentation"]':
        res = get_reference_value_by_name(self, 'textualRepresentation')
        return [(cast('TextualRepresentation', r.referred) if r else None) for
            r in res]

    def add_to_textual_representation(self, new_element:
        '"TextualRepresentation"'):
        self.add_reference_value(self.get_classifier().
            require_reference_by_name('textualRepresentation'),
            ReferenceValue(new_element, new_element.name))

    @property
    def declaredShortName(self) ->str:
        return cast(str, get_property_value_by_name(self, 'declaredShortName'))

    @declaredShortName.setter
    def declaredShortName(self, value: str):
        property_ = self.get_classifier().require_property_by_name(
            'declaredShortName')
        self.set_property_value(property=property_, value=value)

    @property
    def declaredName(self) ->str:
        return cast(str, get_property_value_by_name(self, 'declaredName'))

    @declaredName.setter
    def declaredName(self, value: str):
        property_ = self.get_classifier().require_property_by_name(
            'declaredName')
        self.set_property_value(property=property_, value=value)

    @property
    def shortName(self) ->str:
        return cast(str, get_property_value_by_name(self, 'shortName'))

    @shortName.setter
    def shortName(self, value: str):
        property_ = self.get_classifier().require_property_by_name('shortName')
        self.set_property_value(property=property_, value=value)

    @property
    def name(self) ->str:
        return cast(str, get_property_value_by_name(self, 'name'))

    @name.setter
    def name(self, value: str):
        property_ = self.get_classifier().require_property_by_name('name')
        self.set_property_value(property=property_, value=value)

    @property
    def qualifiedName(self) ->str:
        return cast(str, get_property_value_by_name(self, 'qualifiedName'))

    @qualifiedName.setter
    def qualifiedName(self, value: str):
        property_ = self.get_classifier().require_property_by_name(
            'qualifiedName')
        self.set_property_value(property=property_, value=value)

    @property
    def isImpliedIncluded(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isImpliedIncluded')
            )

    @isImpliedIncluded.setter
    def isImpliedIncluded(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isImpliedIncluded')
        self.set_property_value(property=property_, value=value)

    @property
    def isLibraryElement(self) ->bool:
        return cast(bool, get_property_value_by_name(self, 'isLibraryElement'))

    @isLibraryElement.setter
    def isLibraryElement(self, value: bool):
        property_ = self.get_classifier().require_property_by_name(
            'isLibraryElement')
        self.set_property_value(property=property_, value=value)

    @property
    def aliasIdsContainer(self) ->'List["AliasIdsContainer"]':
        res = self.get_children('aliasIdsContainer')
        return res

    def add_to_alias_ids_container(self, new_element: '"AliasIdsContainer"'):
        self.add_child(self.get_classifier().require_containment_by_name(
            'aliasIdsContainer'), new_element)
