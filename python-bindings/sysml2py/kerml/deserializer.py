from .language import get_owning_membership, get_membership, get_import, get_documentation, get_comment, get_annotation, get_textual_representation, get_dependency, get_membership_import, get_namespace_import, get_subclassification, get_specialization, get_feature_membership, get_redefinition, get_subsetting, get_feature_typing, get_type_featuring, get_feature_inverting, get_feature_chaining, get_reference_subsetting, get_conjugation, get_multiplicity, get_intersecting, get_unioning, get_disjoining, get_differencing, get_end_feature_membership, get_element_filter_membership, get_expression, get_function, get_package, get_library_package, get_invocation_expression, get_feature_reference_expression, get_operator_expression, get_literal_string, get_literal_expression, get_literal_boolean, get_literal_integer, get_null_expression, get_metadata_access_expression, get_metadata_feature, get_metaclass, get_select_expression, get_feature_chain_expression, get_collect_expression, get_literal_infinity, get_literal_rational, get_multiplicity_range, get_feature_value, get_binding_connector, get_association, get_invariant, get_boolean_expression, get_predicate, get_return_parameter_membership, get_parameter_membership, get_result_expression_membership, get_data_type, get_interaction, get_item_flow_end, get_item_flow, get_item_feature, get_succession_item_flow, get_association_structure, get_alias_ids_container, get_featuring, get_relationship, get_element, get_annotating_element, get_behavior, get_class, get_classifier, get_type, get_namespace, get_step, get_feature, get_succession, get_connector, get_structure
from .owning_membership import OwningMembership
from .membership import Membership
from .import_ import Import
from .documentation import Documentation
from .comment import Comment
from .annotation import Annotation
from .textual_representation import TextualRepresentation
from .dependency import Dependency
from .membership_import import MembershipImport
from .namespace_import import NamespaceImport
from .subclassification import Subclassification
from .specialization import Specialization
from .feature_membership import FeatureMembership
from .redefinition import Redefinition
from .subsetting import Subsetting
from .feature_typing import FeatureTyping
from .type_featuring import TypeFeaturing
from .feature_inverting import FeatureInverting
from .feature_chaining import FeatureChaining
from .reference_subsetting import ReferenceSubsetting
from .conjugation import Conjugation
from .multiplicity import Multiplicity
from .intersecting import Intersecting
from .unioning import Unioning
from .disjoining import Disjoining
from .differencing import Differencing
from .end_feature_membership import EndFeatureMembership
from .element_filter_membership import ElementFilterMembership
from .expression import Expression
from .function import Function
from .package import Package
from .library_package import LibraryPackage
from .invocation_expression import InvocationExpression
from .feature_reference_expression import FeatureReferenceExpression
from .operator_expression import OperatorExpression
from .literal_string import LiteralString
from .literal_expression import LiteralExpression
from .literal_boolean import LiteralBoolean
from .literal_integer import LiteralInteger
from .null_expression import NullExpression
from .metadata_access_expression import MetadataAccessExpression
from .metadata_feature import MetadataFeature
from .metaclass import Metaclass
from .select_expression import SelectExpression
from .feature_chain_expression import FeatureChainExpression
from .collect_expression import CollectExpression
from .literal_infinity import LiteralInfinity
from .literal_rational import LiteralRational
from .multiplicity_range import MultiplicityRange
from .feature_value import FeatureValue
from .binding_connector import BindingConnector
from .association import Association
from .invariant import Invariant
from .boolean_expression import BooleanExpression
from .predicate import Predicate
from .return_parameter_membership import ReturnParameterMembership
from .parameter_membership import ParameterMembership
from .result_expression_membership import ResultExpressionMembership
from .data_type import DataType
from .interaction import Interaction
from .item_flow_end import ItemFlowEnd
from .item_flow import ItemFlow
from .item_feature import ItemFeature
from .succession_item_flow import SuccessionItemFlow
from .association_structure import AssociationStructure
from .alias_ids_container import AliasIdsContainer
from .featuring import Featuring
from .relationship import Relationship
from .element import Element
from .annotating_element import AnnotatingElement
from .behavior import Behavior
from .class_ import Class
from .classifier import Classifier
from .type import Type
from .namespace import Namespace
from .step import Step
from .feature import Feature
from .succession import Succession
from .connector import Connector
from .structure import Structure
from lionweb.serialization import AbstractSerialization
from lionweb.serialization.data.serialized_classifier_instance import SerializedClassifierInstance


def register_deserializers(serialization: AbstractSerialization):

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

    def deserializer_import(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Import(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_import().id,
        deserializer=deserializer_import)

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

    def deserializer_dependency(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Dependency(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_dependency(
        ).id, deserializer=deserializer_dependency)

    def deserializer_membershipimport(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MembershipImport(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_membership_import().id, deserializer=deserializer_membershipimport)

    def deserializer_namespaceimport(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return NamespaceImport(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_namespace_import().id, deserializer=deserializer_namespaceimport)

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

    def deserializer_elementfiltermembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return ElementFilterMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_element_filter_membership().id, deserializer=
        deserializer_elementfiltermembership)

    def deserializer_expression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Expression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_expression(
        ).id, deserializer=deserializer_expression)

    def deserializer_function(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Function(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_function().
        id, deserializer=deserializer_function)

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

    def deserializer_invocationexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return InvocationExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_invocation_expression().id, deserializer=
        deserializer_invocationexpression)

    def deserializer_featurereferenceexpression(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return FeatureReferenceExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_feature_reference_expression().id, deserializer=
        deserializer_featurereferenceexpression)

    def deserializer_operatorexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return OperatorExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_operator_expression().id, deserializer=
        deserializer_operatorexpression)

    def deserializer_literalstring(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralString(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literal_string
        ().id, deserializer=deserializer_literalstring)

    def deserializer_literalexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_literal_expression().id, deserializer=
        deserializer_literalexpression)

    def deserializer_literalboolean(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralBoolean(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literal_boolean
        ().id, deserializer=deserializer_literalboolean)

    def deserializer_literalinteger(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralInteger(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literal_integer
        ().id, deserializer=deserializer_literalinteger)

    def deserializer_nullexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return NullExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_null_expression
        ().id, deserializer=deserializer_nullexpression)

    def deserializer_metadataaccessexpression(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return MetadataAccessExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_metadata_access_expression().id, deserializer=
        deserializer_metadataaccessexpression)

    def deserializer_metadatafeature(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MetadataFeature(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_metadata_feature().id, deserializer=deserializer_metadatafeature)

    def deserializer_metaclass(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Metaclass(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_metaclass()
        .id, deserializer=deserializer_metaclass)

    def deserializer_selectexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return SelectExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_select_expression().id, deserializer=deserializer_selectexpression)

    def deserializer_featurechainexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return FeatureChainExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_feature_chain_expression().id, deserializer=
        deserializer_featurechainexpression)

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

    def deserializer_literalrational(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralRational(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_literal_rational().id, deserializer=deserializer_literalrational)

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

    def deserializer_bindingconnector(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return BindingConnector(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_binding_connector().id, deserializer=deserializer_bindingconnector)

    def deserializer_association(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Association(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_association
        ().id, deserializer=deserializer_association)

    def deserializer_invariant(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Invariant(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_invariant()
        .id, deserializer=deserializer_invariant)

    def deserializer_booleanexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return BooleanExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_boolean_expression().id, deserializer=
        deserializer_booleanexpression)

    def deserializer_predicate(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Predicate(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_predicate()
        .id, deserializer=deserializer_predicate)

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

    def deserializer_resultexpressionmembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return ResultExpressionMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_result_expression_membership().id, deserializer=
        deserializer_resultexpressionmembership)

    def deserializer_datatype(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return DataType(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_data_type()
        .id, deserializer=deserializer_datatype)

    def deserializer_interaction(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Interaction(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_interaction
        ().id, deserializer=deserializer_interaction)

    def deserializer_itemflowend(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemFlowEnd(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_item_flow_end
        ().id, deserializer=deserializer_itemflowend)

    def deserializer_itemflow(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemFlow(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_item_flow()
        .id, deserializer=deserializer_itemflow)

    def deserializer_itemfeature(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemFeature(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_item_feature
        ().id, deserializer=deserializer_itemfeature)

    def deserializer_successionitemflow(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return SuccessionItemFlow(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_succession_item_flow().id, deserializer=
        deserializer_successionitemflow)

    def deserializer_associationstructure(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AssociationStructure(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_association_structure().id, deserializer=
        deserializer_associationstructure)

    def deserializer_aliasidscontainer(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AliasIdsContainer(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_alias_ids_container().id, deserializer=
        deserializer_aliasidscontainer)

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
