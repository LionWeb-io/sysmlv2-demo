from .language import get_subclassification, get_specialization, get_owning_membership, get_membership, get_documentation, get_comment, get_annotation, get_textual_representation, get_feature_membership, get_redefinition, get_subsetting, get_feature_typing, get_type_featuring, get_feature_inverting, get_feature_chaining, get_reference_subsetting, get_cross_subsetting, get_conjugation, get_multiplicity, get_intersecting, get_unioning, get_disjoining, get_differencing, get_end_feature_membership, get_result_expression_membership, get_return_parameter_membership, get_parameter_membership, get_multiplicity_range, get_feature_value, get_metadata_feature, get_item_flow_end, get_item_feature, get_element_filter_membership, get_package, get_library_package, get_feature_reference_expression, get_metadata_access_expression, get_null_expression, get_index_expression, get_operator_expression, get_invocation_expression, get_collect_expression, get_literal_infinity, get_literal_expression, get_literal_integer, get_select_expression, get_literal_rational, get_literal_boolean, get_literal_string, get_feature_chain_expression, get_dependency, get_namespace_import, get_membership_import, get_interface_usage, get_connection_usage, get_connector_as_usage, get_variant_membership, get_definition, get_reference_usage, get_attribute_usage, get_enumeration_usage, get_enumeration_definition, get_attribute_definition, get_occurrence_definition, get_life_class, get_part_definition, get_item_definition, get_port_usage, get_port_definition, get_conjugated_port_definition, get_port_conjugation, get_flow_connection_usage, get_allocation_usage, get_allocation_definition, get_connection_definition, get_state_usage, get_transition_usage, get_accept_action_usage, get_calculation_usage, get_requirement_usage, get_requirement_definition, get_constraint_definition, get_concern_usage, get_concern_definition, get_case_usage, get_case_definition, get_calculation_definition, get_action_definition, get_analysis_case_usage, get_analysis_case_definition, get_verification_case_usage, get_verification_case_definition, get_use_case_usage, get_use_case_definition, get_view_usage, get_view_definition, get_viewpoint_usage, get_viewpoint_definition, get_rendering_usage, get_rendering_definition, get_metadata_usage, get_interface_definition, get_conjugated_port_typing, get_transition_feature_membership, get_exhibit_state_usage, get_state_subaction_membership, get_state_definition, get_succession_flow_connection_usage, get_flow_connection_definition, get_requirement_verification_membership, get_requirement_constraint_membership, get_include_use_case_usage, get_objective_membership, get_satisfy_requirement_usage, get_subject_membership, get_stakeholder_membership, get_framed_concern_membership, get_actor_membership, get_view_rendering_membership, get_namespace_expose, get_membership_expose, get_binding_connector_as_usage, get_succession_as_usage, get_fork_node, get_control_node, get_join_node, get_send_action_usage, get_decision_node, get_merge_node, get_loop_action_usage, get_trigger_invocation_expression, get_assignment_action_usage, get_for_loop_action_usage, get_if_action_usage, get_while_loop_action_usage, get_terminate_action_usage, get_metadata_definition, get_alias_ids_container, get_text_container, get_featuring, get_relationship, get_element, get_annotating_element, get_step, get_feature, get_type, get_namespace, get_behavior, get_class, get_classifier, get_succession, get_connector, get_structure, get_part_usage, get_item_usage, get_occurrence_usage, get_usage, get_data_type, get_action_usage, get_item_flow, get_association_structure, get_association, get_predicate, get_function, get_perform_action_usage, get_event_occurrence_usage, get_succession_item_flow, get_interaction, get_assert_constraint_usage, get_constraint_usage, get_boolean_expression, get_expression, get_invariant, get_expose, get_import, get_binding_connector, get_metaclass
from .subclassification import Subclassification
from .specialization import Specialization
from .owning_membership import OwningMembership
from .membership import Membership
from .documentation import Documentation
from .comment import Comment
from .annotation import Annotation
from .textual_representation import TextualRepresentation
from .feature_membership import FeatureMembership
from .redefinition import Redefinition
from .subsetting import Subsetting
from .feature_typing import FeatureTyping
from .type_featuring import TypeFeaturing
from .feature_inverting import FeatureInverting
from .feature_chaining import FeatureChaining
from .reference_subsetting import ReferenceSubsetting
from .cross_subsetting import CrossSubsetting
from .conjugation import Conjugation
from .multiplicity import Multiplicity
from .intersecting import Intersecting
from .unioning import Unioning
from .disjoining import Disjoining
from .differencing import Differencing
from .end_feature_membership import EndFeatureMembership
from .result_expression_membership import ResultExpressionMembership
from .return_parameter_membership import ReturnParameterMembership
from .parameter_membership import ParameterMembership
from .multiplicity_range import MultiplicityRange
from .feature_value import FeatureValue
from .metadata_feature import MetadataFeature
from .item_flow_end import ItemFlowEnd
from .item_feature import ItemFeature
from .element_filter_membership import ElementFilterMembership
from .package import Package
from .library_package import LibraryPackage
from .feature_reference_expression import FeatureReferenceExpression
from .metadata_access_expression import MetadataAccessExpression
from .null_expression import NullExpression
from .index_expression import IndexExpression
from .operator_expression import OperatorExpression
from .invocation_expression import InvocationExpression
from .collect_expression import CollectExpression
from .literal_infinity import LiteralInfinity
from .literal_expression import LiteralExpression
from .literal_integer import LiteralInteger
from .select_expression import SelectExpression
from .literal_rational import LiteralRational
from .literal_boolean import LiteralBoolean
from .literal_string import LiteralString
from .feature_chain_expression import FeatureChainExpression
from .dependency import Dependency
from .namespace_import import NamespaceImport
from .membership_import import MembershipImport
from .interface_usage import InterfaceUsage
from .connection_usage import ConnectionUsage
from .connector_as_usage import ConnectorAsUsage
from .variant_membership import VariantMembership
from .definition import Definition
from .reference_usage import ReferenceUsage
from .attribute_usage import AttributeUsage
from .enumeration_usage import EnumerationUsage
from .enumeration_definition import EnumerationDefinition
from .attribute_definition import AttributeDefinition
from .occurrence_definition import OccurrenceDefinition
from .life_class import LifeClass
from .part_definition import PartDefinition
from .item_definition import ItemDefinition
from .port_usage import PortUsage
from .port_definition import PortDefinition
from .conjugated_port_definition import ConjugatedPortDefinition
from .port_conjugation import PortConjugation
from .flow_connection_usage import FlowConnectionUsage
from .allocation_usage import AllocationUsage
from .allocation_definition import AllocationDefinition
from .connection_definition import ConnectionDefinition
from .state_usage import StateUsage
from .transition_usage import TransitionUsage
from .accept_action_usage import AcceptActionUsage
from .calculation_usage import CalculationUsage
from .requirement_usage import RequirementUsage
from .requirement_definition import RequirementDefinition
from .constraint_definition import ConstraintDefinition
from .concern_usage import ConcernUsage
from .concern_definition import ConcernDefinition
from .case_usage import CaseUsage
from .case_definition import CaseDefinition
from .calculation_definition import CalculationDefinition
from .action_definition import ActionDefinition
from .analysis_case_usage import AnalysisCaseUsage
from .analysis_case_definition import AnalysisCaseDefinition
from .verification_case_usage import VerificationCaseUsage
from .verification_case_definition import VerificationCaseDefinition
from .use_case_usage import UseCaseUsage
from .use_case_definition import UseCaseDefinition
from .view_usage import ViewUsage
from .view_definition import ViewDefinition
from .viewpoint_usage import ViewpointUsage
from .viewpoint_definition import ViewpointDefinition
from .rendering_usage import RenderingUsage
from .rendering_definition import RenderingDefinition
from .metadata_usage import MetadataUsage
from .interface_definition import InterfaceDefinition
from .conjugated_port_typing import ConjugatedPortTyping
from .transition_feature_membership import TransitionFeatureMembership
from .exhibit_state_usage import ExhibitStateUsage
from .state_subaction_membership import StateSubactionMembership
from .state_definition import StateDefinition
from .succession_flow_connection_usage import SuccessionFlowConnectionUsage
from .flow_connection_definition import FlowConnectionDefinition
from .requirement_verification_membership import RequirementVerificationMembership
from .requirement_constraint_membership import RequirementConstraintMembership
from .include_use_case_usage import IncludeUseCaseUsage
from .objective_membership import ObjectiveMembership
from .satisfy_requirement_usage import SatisfyRequirementUsage
from .subject_membership import SubjectMembership
from .stakeholder_membership import StakeholderMembership
from .framed_concern_membership import FramedConcernMembership
from .actor_membership import ActorMembership
from .view_rendering_membership import ViewRenderingMembership
from .namespace_expose import NamespaceExpose
from .membership_expose import MembershipExpose
from .binding_connector_as_usage import BindingConnectorAsUsage
from .succession_as_usage import SuccessionAsUsage
from .fork_node import ForkNode
from .control_node import ControlNode
from .join_node import JoinNode
from .send_action_usage import SendActionUsage
from .decision_node import DecisionNode
from .merge_node import MergeNode
from .loop_action_usage import LoopActionUsage
from .trigger_invocation_expression import TriggerInvocationExpression
from .assignment_action_usage import AssignmentActionUsage
from .for_loop_action_usage import ForLoopActionUsage
from .if_action_usage import IfActionUsage
from .while_loop_action_usage import WhileLoopActionUsage
from .terminate_action_usage import TerminateActionUsage
from .metadata_definition import MetadataDefinition
from .alias_ids_container import AliasIdsContainer
from .text_container import TextContainer
from .featuring import Featuring
from .relationship import Relationship
from .element import Element
from .annotating_element import AnnotatingElement
from .step import Step
from .feature import Feature
from .type import Type
from .namespace import Namespace
from .behavior import Behavior
from .class_ import Class
from .classifier import Classifier
from .succession import Succession
from .connector import Connector
from .structure import Structure
from .part_usage import PartUsage
from .item_usage import ItemUsage
from .occurrence_usage import OccurrenceUsage
from .usage import Usage
from .data_type import DataType
from .action_usage import ActionUsage
from .item_flow import ItemFlow
from .association_structure import AssociationStructure
from .association import Association
from .predicate import Predicate
from .function import Function
from .perform_action_usage import PerformActionUsage
from .event_occurrence_usage import EventOccurrenceUsage
from .succession_item_flow import SuccessionItemFlow
from .interaction import Interaction
from .assert_constraint_usage import AssertConstraintUsage
from .constraint_usage import ConstraintUsage
from .boolean_expression import BooleanExpression
from .expression import Expression
from .invariant import Invariant
from .expose import Expose
from .import_ import Import
from .binding_connector import BindingConnector
from .metaclass import Metaclass
from lionweb.serialization import AbstractSerialization
from lionweb.serialization.data.serialized_classifier_instance import SerializedClassifierInstance


def register_deserializers(serialization: AbstractSerialization):

    def deserializer_subclassification(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Subclassification(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_subclassification().id, deserializer=deserializer_subclassification
        )

    def deserializer_specialization(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Specialization(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_specialization
        ().id, deserializer=deserializer_specialization)

    def deserializer_owningmembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return OwningMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_owning_membership().id, deserializer=deserializer_owningmembership)

    def deserializer_membership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Membership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_membership(
        ).id, deserializer=deserializer_membership)

    def deserializer_documentation(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Documentation(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_documentation
        ().id, deserializer=deserializer_documentation)

    def deserializer_comment(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Comment(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_comment().
        id, deserializer=deserializer_comment)

    def deserializer_annotation(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Annotation(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_annotation(
        ).id, deserializer=deserializer_annotation)

    def deserializer_textualrepresentation(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return TextualRepresentation(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_textual_representation().id, deserializer=
        deserializer_textualrepresentation)

    def deserializer_featuremembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return FeatureMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_feature_membership().id, deserializer=
        deserializer_featuremembership)

    def deserializer_redefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Redefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_redefinition
        ().id, deserializer=deserializer_redefinition)

    def deserializer_subsetting(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Subsetting(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_subsetting(
        ).id, deserializer=deserializer_subsetting)

    def deserializer_featuretyping(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return FeatureTyping(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_feature_typing
        ().id, deserializer=deserializer_featuretyping)

    def deserializer_typefeaturing(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return TypeFeaturing(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_type_featuring
        ().id, deserializer=deserializer_typefeaturing)

    def deserializer_featureinverting(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return FeatureInverting(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_feature_inverting().id, deserializer=deserializer_featureinverting)

    def deserializer_featurechaining(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return FeatureChaining(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_feature_chaining().id, deserializer=deserializer_featurechaining)

    def deserializer_referencesubsetting(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ReferenceSubsetting(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_reference_subsetting().id, deserializer=
        deserializer_referencesubsetting)

    def deserializer_crosssubsetting(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return CrossSubsetting(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_cross_subsetting().id, deserializer=deserializer_crosssubsetting)

    def deserializer_conjugation(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Conjugation(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_conjugation
        ().id, deserializer=deserializer_conjugation)

    def deserializer_multiplicity(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Multiplicity(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_multiplicity
        ().id, deserializer=deserializer_multiplicity)

    def deserializer_intersecting(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Intersecting(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_intersecting
        ().id, deserializer=deserializer_intersecting)

    def deserializer_unioning(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Unioning(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_unioning().
        id, deserializer=deserializer_unioning)

    def deserializer_disjoining(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Disjoining(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_disjoining(
        ).id, deserializer=deserializer_disjoining)

    def deserializer_differencing(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Differencing(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_differencing
        ().id, deserializer=deserializer_differencing)

    def deserializer_endfeaturemembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return EndFeatureMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_end_feature_membership().id, deserializer=
        deserializer_endfeaturemembership)

    def deserializer_resultexpressionmembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return ResultExpressionMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_result_expression_membership().id, deserializer=
        deserializer_resultexpressionmembership)

    def deserializer_returnparametermembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return ReturnParameterMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_return_parameter_membership().id, deserializer=
        deserializer_returnparametermembership)

    def deserializer_parametermembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ParameterMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_parameter_membership().id, deserializer=
        deserializer_parametermembership)

    def deserializer_multiplicityrange(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MultiplicityRange(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_multiplicity_range().id, deserializer=
        deserializer_multiplicityrange)

    def deserializer_featurevalue(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return FeatureValue(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_feature_value
        ().id, deserializer=deserializer_featurevalue)

    def deserializer_metadatafeature(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MetadataFeature(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_metadata_feature().id, deserializer=deserializer_metadatafeature)

    def deserializer_itemflowend(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemFlowEnd(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_item_flow_end
        ().id, deserializer=deserializer_itemflowend)

    def deserializer_itemfeature(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemFeature(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_item_feature
        ().id, deserializer=deserializer_itemfeature)

    def deserializer_elementfiltermembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return ElementFilterMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_element_filter_membership().id, deserializer=
        deserializer_elementfiltermembership)

    def deserializer_package(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Package(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_package().
        id, deserializer=deserializer_package)

    def deserializer_librarypackage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LibraryPackage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_library_package
        ().id, deserializer=deserializer_librarypackage)

    def deserializer_featurereferenceexpression(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return FeatureReferenceExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_feature_reference_expression().id, deserializer=
        deserializer_featurereferenceexpression)

    def deserializer_metadataaccessexpression(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return MetadataAccessExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_metadata_access_expression().id, deserializer=
        deserializer_metadataaccessexpression)

    def deserializer_nullexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return NullExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_null_expression
        ().id, deserializer=deserializer_nullexpression)

    def deserializer_indexexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return IndexExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_index_expression().id, deserializer=deserializer_indexexpression)

    def deserializer_operatorexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return OperatorExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_operator_expression().id, deserializer=
        deserializer_operatorexpression)

    def deserializer_invocationexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return InvocationExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_invocation_expression().id, deserializer=
        deserializer_invocationexpression)

    def deserializer_collectexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return CollectExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_collect_expression().id, deserializer=
        deserializer_collectexpression)

    def deserializer_literalinfinity(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralInfinity(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_literal_infinity().id, deserializer=deserializer_literalinfinity)

    def deserializer_literalexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_literal_expression().id, deserializer=
        deserializer_literalexpression)

    def deserializer_literalinteger(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralInteger(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literal_integer
        ().id, deserializer=deserializer_literalinteger)

    def deserializer_selectexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return SelectExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_select_expression().id, deserializer=deserializer_selectexpression)

    def deserializer_literalrational(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralRational(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_literal_rational().id, deserializer=deserializer_literalrational)

    def deserializer_literalboolean(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralBoolean(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literal_boolean
        ().id, deserializer=deserializer_literalboolean)

    def deserializer_literalstring(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralString(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literal_string
        ().id, deserializer=deserializer_literalstring)

    def deserializer_featurechainexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return FeatureChainExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_feature_chain_expression().id, deserializer=
        deserializer_featurechainexpression)

    def deserializer_dependency(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Dependency(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_dependency(
        ).id, deserializer=deserializer_dependency)

    def deserializer_namespaceimport(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return NamespaceImport(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_namespace_import().id, deserializer=deserializer_namespaceimport)

    def deserializer_membershipimport(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MembershipImport(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_membership_import().id, deserializer=deserializer_membershipimport)

    def deserializer_interfaceusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return InterfaceUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_interface_usage
        ().id, deserializer=deserializer_interfaceusage)

    def deserializer_connectionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConnectionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_connection_usage().id, deserializer=deserializer_connectionusage)

    def deserializer_connectorasusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConnectorAsUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_connector_as_usage().id, deserializer=deserializer_connectorasusage
        )

    def deserializer_variantmembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return VariantMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_variant_membership().id, deserializer=
        deserializer_variantmembership)

    def deserializer_definition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Definition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_definition(
        ).id, deserializer=deserializer_definition)

    def deserializer_referenceusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ReferenceUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_reference_usage
        ().id, deserializer=deserializer_referenceusage)

    def deserializer_attributeusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AttributeUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_attribute_usage
        ().id, deserializer=deserializer_attributeusage)

    def deserializer_enumerationusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return EnumerationUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_enumeration_usage().id, deserializer=deserializer_enumerationusage)

    def deserializer_enumerationdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return EnumerationDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_enumeration_definition().id, deserializer=
        deserializer_enumerationdefinition)

    def deserializer_attributedefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AttributeDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_attribute_definition().id, deserializer=
        deserializer_attributedefinition)

    def deserializer_occurrencedefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return OccurrenceDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_occurrence_definition().id, deserializer=
        deserializer_occurrencedefinition)

    def deserializer_lifeclass(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LifeClass(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_life_class(
        ).id, deserializer=deserializer_lifeclass)

    def deserializer_partdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return PartDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_part_definition
        ().id, deserializer=deserializer_partdefinition)

    def deserializer_itemdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_item_definition
        ().id, deserializer=deserializer_itemdefinition)

    def deserializer_portusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return PortUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_port_usage(
        ).id, deserializer=deserializer_portusage)

    def deserializer_portdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return PortDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_port_definition
        ().id, deserializer=deserializer_portdefinition)

    def deserializer_conjugatedportdefinition(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return ConjugatedPortDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_conjugated_port_definition().id, deserializer=
        deserializer_conjugatedportdefinition)

    def deserializer_portconjugation(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return PortConjugation(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_port_conjugation().id, deserializer=deserializer_portconjugation)

    def deserializer_flowconnectionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return FlowConnectionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_flow_connection_usage().id, deserializer=
        deserializer_flowconnectionusage)

    def deserializer_allocationusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AllocationUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_allocation_usage().id, deserializer=deserializer_allocationusage)

    def deserializer_allocationdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AllocationDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_allocation_definition().id, deserializer=
        deserializer_allocationdefinition)

    def deserializer_connectiondefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConnectionDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_connection_definition().id, deserializer=
        deserializer_connectiondefinition)

    def deserializer_stateusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return StateUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_state_usage
        ().id, deserializer=deserializer_stateusage)

    def deserializer_transitionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return TransitionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_transition_usage().id, deserializer=deserializer_transitionusage)

    def deserializer_acceptactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AcceptActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_accept_action_usage().id, deserializer=
        deserializer_acceptactionusage)

    def deserializer_calculationusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return CalculationUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_calculation_usage().id, deserializer=deserializer_calculationusage)

    def deserializer_requirementusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return RequirementUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_requirement_usage().id, deserializer=deserializer_requirementusage)

    def deserializer_requirementdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return RequirementDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_requirement_definition().id, deserializer=
        deserializer_requirementdefinition)

    def deserializer_constraintdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConstraintDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_constraint_definition().id, deserializer=
        deserializer_constraintdefinition)

    def deserializer_concernusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConcernUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_concern_usage
        ().id, deserializer=deserializer_concernusage)

    def deserializer_concerndefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConcernDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_concern_definition().id, deserializer=
        deserializer_concerndefinition)

    def deserializer_caseusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return CaseUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_case_usage(
        ).id, deserializer=deserializer_caseusage)

    def deserializer_casedefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return CaseDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_case_definition
        ().id, deserializer=deserializer_casedefinition)

    def deserializer_calculationdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return CalculationDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_calculation_definition().id, deserializer=
        deserializer_calculationdefinition)

    def deserializer_actiondefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ActionDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_action_definition().id, deserializer=deserializer_actiondefinition)

    def deserializer_analysiscaseusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AnalysisCaseUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_analysis_case_usage().id, deserializer=
        deserializer_analysiscaseusage)

    def deserializer_analysiscasedefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AnalysisCaseDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_analysis_case_definition().id, deserializer=
        deserializer_analysiscasedefinition)

    def deserializer_verificationcaseusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return VerificationCaseUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_verification_case_usage().id, deserializer=
        deserializer_verificationcaseusage)

    def deserializer_verificationcasedefinition(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return VerificationCaseDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_verification_case_definition().id, deserializer=
        deserializer_verificationcasedefinition)

    def deserializer_usecaseusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return UseCaseUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_use_case_usage
        ().id, deserializer=deserializer_usecaseusage)

    def deserializer_usecasedefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return UseCaseDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_use_case_definition().id, deserializer=
        deserializer_usecasedefinition)

    def deserializer_viewusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ViewUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_view_usage(
        ).id, deserializer=deserializer_viewusage)

    def deserializer_viewdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ViewDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_view_definition
        ().id, deserializer=deserializer_viewdefinition)

    def deserializer_viewpointusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ViewpointUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_viewpoint_usage
        ().id, deserializer=deserializer_viewpointusage)

    def deserializer_viewpointdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ViewpointDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_viewpoint_definition().id, deserializer=
        deserializer_viewpointdefinition)

    def deserializer_renderingusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return RenderingUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_rendering_usage
        ().id, deserializer=deserializer_renderingusage)

    def deserializer_renderingdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return RenderingDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_rendering_definition().id, deserializer=
        deserializer_renderingdefinition)

    def deserializer_metadatausage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MetadataUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_metadata_usage
        ().id, deserializer=deserializer_metadatausage)

    def deserializer_interfacedefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return InterfaceDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_interface_definition().id, deserializer=
        deserializer_interfacedefinition)

    def deserializer_conjugatedporttyping(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConjugatedPortTyping(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_conjugated_port_typing().id, deserializer=
        deserializer_conjugatedporttyping)

    def deserializer_transitionfeaturemembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return TransitionFeatureMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_transition_feature_membership().id, deserializer=
        deserializer_transitionfeaturemembership)

    def deserializer_exhibitstateusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ExhibitStateUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_exhibit_state_usage().id, deserializer=
        deserializer_exhibitstateusage)

    def deserializer_statesubactionmembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return StateSubactionMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_state_subaction_membership().id, deserializer=
        deserializer_statesubactionmembership)

    def deserializer_statedefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return StateDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_state_definition().id, deserializer=deserializer_statedefinition)

    def deserializer_successionflowconnectionusage(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return SuccessionFlowConnectionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_succession_flow_connection_usage().id, deserializer=
        deserializer_successionflowconnectionusage)

    def deserializer_flowconnectiondefinition(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return FlowConnectionDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_flow_connection_definition().id, deserializer=
        deserializer_flowconnectiondefinition)

    def deserializer_requirementverificationmembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return RequirementVerificationMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_requirement_verification_membership().id, deserializer=
        deserializer_requirementverificationmembership)

    def deserializer_requirementconstraintmembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return RequirementConstraintMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_requirement_constraint_membership().id, deserializer=
        deserializer_requirementconstraintmembership)

    def deserializer_includeusecaseusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return IncludeUseCaseUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_include_use_case_usage().id, deserializer=
        deserializer_includeusecaseusage)

    def deserializer_objectivemembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ObjectiveMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_objective_membership().id, deserializer=
        deserializer_objectivemembership)

    def deserializer_satisfyrequirementusage(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return SatisfyRequirementUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_satisfy_requirement_usage().id, deserializer=
        deserializer_satisfyrequirementusage)

    def deserializer_subjectmembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return SubjectMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_subject_membership().id, deserializer=
        deserializer_subjectmembership)

    def deserializer_stakeholdermembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return StakeholderMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_stakeholder_membership().id, deserializer=
        deserializer_stakeholdermembership)

    def deserializer_framedconcernmembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return FramedConcernMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_framed_concern_membership().id, deserializer=
        deserializer_framedconcernmembership)

    def deserializer_actormembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ActorMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_actor_membership().id, deserializer=deserializer_actormembership)

    def deserializer_viewrenderingmembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return ViewRenderingMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_view_rendering_membership().id, deserializer=
        deserializer_viewrenderingmembership)

    def deserializer_namespaceexpose(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return NamespaceExpose(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_namespace_expose().id, deserializer=deserializer_namespaceexpose)

    def deserializer_membershipexpose(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MembershipExpose(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_membership_expose().id, deserializer=deserializer_membershipexpose)

    def deserializer_bindingconnectorasusage(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return BindingConnectorAsUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_binding_connector_as_usage().id, deserializer=
        deserializer_bindingconnectorasusage)

    def deserializer_successionasusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return SuccessionAsUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_succession_as_usage().id, deserializer=
        deserializer_successionasusage)

    def deserializer_forknode(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ForkNode(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_fork_node()
        .id, deserializer=deserializer_forknode)

    def deserializer_controlnode(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ControlNode(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_control_node
        ().id, deserializer=deserializer_controlnode)

    def deserializer_joinnode(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return JoinNode(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_join_node()
        .id, deserializer=deserializer_joinnode)

    def deserializer_sendactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return SendActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_send_action_usage().id, deserializer=deserializer_sendactionusage)

    def deserializer_decisionnode(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return DecisionNode(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_decision_node
        ().id, deserializer=deserializer_decisionnode)

    def deserializer_mergenode(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MergeNode(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_merge_node(
        ).id, deserializer=deserializer_mergenode)

    def deserializer_loopactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LoopActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_loop_action_usage().id, deserializer=deserializer_loopactionusage)

    def deserializer_triggerinvocationexpression(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return TriggerInvocationExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_trigger_invocation_expression().id, deserializer=
        deserializer_triggerinvocationexpression)

    def deserializer_assignmentactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AssignmentActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_assignment_action_usage().id, deserializer=
        deserializer_assignmentactionusage)

    def deserializer_forloopactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ForLoopActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_for_loop_action_usage().id, deserializer=
        deserializer_forloopactionusage)

    def deserializer_ifactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return IfActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_if_action_usage
        ().id, deserializer=deserializer_ifactionusage)

    def deserializer_whileloopactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return WhileLoopActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_while_loop_action_usage().id, deserializer=
        deserializer_whileloopactionusage)

    def deserializer_terminateactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return TerminateActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_terminate_action_usage().id, deserializer=
        deserializer_terminateactionusage)

    def deserializer_metadatadefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MetadataDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_metadata_definition().id, deserializer=
        deserializer_metadatadefinition)

    def deserializer_aliasidscontainer(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AliasIdsContainer(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_alias_ids_container().id, deserializer=
        deserializer_aliasidscontainer)

    def deserializer_textcontainer(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return TextContainer(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_text_container
        ().id, deserializer=deserializer_textcontainer)

    def deserializer_featuring(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Featuring(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_featuring()
        .id, deserializer=deserializer_featuring)

    def deserializer_relationship(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Relationship(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_relationship
        ().id, deserializer=deserializer_relationship)

    def deserializer_element(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Element(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_element().
        id, deserializer=deserializer_element)

    def deserializer_annotatingelement(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AnnotatingElement(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_annotating_element().id, deserializer=
        deserializer_annotatingelement)

    def deserializer_step(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Step(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_step().id,
        deserializer=deserializer_step)

    def deserializer_feature(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Feature(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_feature().
        id, deserializer=deserializer_feature)

    def deserializer_type(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Type(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_type().id,
        deserializer=deserializer_type)

    def deserializer_namespace(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Namespace(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_namespace()
        .id, deserializer=deserializer_namespace)

    def deserializer_behavior(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Behavior(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_behavior().
        id, deserializer=deserializer_behavior)

    def deserializer_class(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Class(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_class().id,
        deserializer=deserializer_class)

    def deserializer_classifier(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Classifier(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_classifier(
        ).id, deserializer=deserializer_classifier)

    def deserializer_succession(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Succession(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_succession(
        ).id, deserializer=deserializer_succession)

    def deserializer_connector(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Connector(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_connector()
        .id, deserializer=deserializer_connector)

    def deserializer_structure(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Structure(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_structure()
        .id, deserializer=deserializer_structure)

    def deserializer_partusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return PartUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_part_usage(
        ).id, deserializer=deserializer_partusage)

    def deserializer_itemusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_item_usage(
        ).id, deserializer=deserializer_itemusage)

    def deserializer_occurrenceusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return OccurrenceUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_occurrence_usage().id, deserializer=deserializer_occurrenceusage)

    def deserializer_usage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Usage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_usage().id,
        deserializer=deserializer_usage)

    def deserializer_datatype(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return DataType(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_data_type()
        .id, deserializer=deserializer_datatype)

    def deserializer_actionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_action_usage
        ().id, deserializer=deserializer_actionusage)

    def deserializer_itemflow(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemFlow(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_item_flow()
        .id, deserializer=deserializer_itemflow)

    def deserializer_associationstructure(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AssociationStructure(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_association_structure().id, deserializer=
        deserializer_associationstructure)

    def deserializer_association(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Association(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_association
        ().id, deserializer=deserializer_association)

    def deserializer_predicate(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Predicate(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_predicate()
        .id, deserializer=deserializer_predicate)

    def deserializer_function(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Function(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_function().
        id, deserializer=deserializer_function)

    def deserializer_performactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return PerformActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_perform_action_usage().id, deserializer=
        deserializer_performactionusage)

    def deserializer_eventoccurrenceusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return EventOccurrenceUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_event_occurrence_usage().id, deserializer=
        deserializer_eventoccurrenceusage)

    def deserializer_successionitemflow(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return SuccessionItemFlow(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_succession_item_flow().id, deserializer=
        deserializer_successionitemflow)

    def deserializer_interaction(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Interaction(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_interaction
        ().id, deserializer=deserializer_interaction)

    def deserializer_assertconstraintusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AssertConstraintUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_assert_constraint_usage().id, deserializer=
        deserializer_assertconstraintusage)

    def deserializer_constraintusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConstraintUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_constraint_usage().id, deserializer=deserializer_constraintusage)

    def deserializer_booleanexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return BooleanExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_boolean_expression().id, deserializer=
        deserializer_booleanexpression)

    def deserializer_expression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Expression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_expression(
        ).id, deserializer=deserializer_expression)

    def deserializer_invariant(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Invariant(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_invariant()
        .id, deserializer=deserializer_invariant)

    def deserializer_expose(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Expose(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_expose().id,
        deserializer=deserializer_expose)

    def deserializer_import(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Import(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_import().id,
        deserializer=deserializer_import)

    def deserializer_bindingconnector(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return BindingConnector(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_binding_connector().id, deserializer=deserializer_bindingconnector)

    def deserializer_metaclass(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Metaclass(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_metaclass()
        .id, deserializer=deserializer_metaclass)
