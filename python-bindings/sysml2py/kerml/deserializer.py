from gen.language import get_owningmembership, get_membership, get_import, get_documentation, get_comment, get_annotation, get_textualrepresentation, get_dependency, get_membershipimport, get_namespaceimport, get_subclassification, get_specialization, get_featuremembership, get_redefinition, get_subsetting, get_featuretyping, get_typefeaturing, get_featureinverting, get_featurechaining, get_referencesubsetting, get_conjugation, get_multiplicity, get_intersecting, get_unioning, get_disjoining, get_differencing, get_endfeaturemembership, get_elementfiltermembership, get_expression, get_function, get_package, get_librarypackage, get_invocationexpression, get_featurereferenceexpression, get_operatorexpression, get_literalstring, get_literalexpression, get_literalboolean, get_literalinteger, get_nullexpression, get_metadataaccessexpression, get_metadatafeature, get_metaclass, get_selectexpression, get_featurechainexpression, get_collectexpression, get_literalinfinity, get_literalrational, get_multiplicityrange, get_featurevalue, get_bindingconnector, get_association, get_invariant, get_booleanexpression, get_predicate, get_returnparametermembership, get_parametermembership, get_resultexpressionmembership, get_datatype, get_interaction, get_itemflowend, get_itemflow, get_itemfeature, get_successionitemflow, get_associationstructure, get_aliasidscontainer, get_featuring, get_relationship, get_element, get_annotatingelement, get_behavior, get_class, get_classifier, get_type, get_namespace, get_step, get_feature, get_succession, get_connector, get_structure
from gen.node_classes import OwningMembership, Membership, Import, Documentation, Comment, Annotation, TextualRepresentation, Dependency, MembershipImport, NamespaceImport, Subclassification, Specialization, FeatureMembership, Redefinition, Subsetting, FeatureTyping, TypeFeaturing, FeatureInverting, FeatureChaining, ReferenceSubsetting, Conjugation, Multiplicity, Intersecting, Unioning, Disjoining, Differencing, EndFeatureMembership, ElementFilterMembership, Expression, Function, Package, LibraryPackage, InvocationExpression, FeatureReferenceExpression, OperatorExpression, LiteralString, LiteralExpression, LiteralBoolean, LiteralInteger, NullExpression, MetadataAccessExpression, MetadataFeature, Metaclass, SelectExpression, FeatureChainExpression, CollectExpression, LiteralInfinity, LiteralRational, MultiplicityRange, FeatureValue, BindingConnector, Association, Invariant, BooleanExpression, Predicate, ReturnParameterMembership, ParameterMembership, ResultExpressionMembership, DataType, Interaction, ItemFlowEnd, ItemFlow, ItemFeature, SuccessionItemFlow, AssociationStructure, AliasIdsContainer, Featuring, Relationship, Element, AnnotatingElement, Behavior, Class, Classifier, Type, Namespace, Step, Feature, Succession, Connector, Structure
from lionweb.serialization import AbstractSerialization
from lionweb.serialization.data.serialized_classifier_instance import SerializedClassifierInstance


def register_deserializers(serialization: AbstractSerialization):

    def deserializer_owningmembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return OwningMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_owningmembership().id, deserializer=deserializer_owningmembership)

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
        get_textualrepresentation().id, deserializer=
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
        get_membershipimport().id, deserializer=deserializer_membershipimport)

    def deserializer_namespaceimport(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return NamespaceImport(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_namespaceimport
        ().id, deserializer=deserializer_namespaceimport)

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
        get_featuremembership().id, deserializer=deserializer_featuremembership
        )

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
    serialization.instantiator.register_custom_deserializer(get_featuretyping
        ().id, deserializer=deserializer_featuretyping)

    def deserializer_typefeaturing(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return TypeFeaturing(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_typefeaturing
        ().id, deserializer=deserializer_typefeaturing)

    def deserializer_featureinverting(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return FeatureInverting(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_featureinverting().id, deserializer=deserializer_featureinverting)

    def deserializer_featurechaining(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return FeatureChaining(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_featurechaining
        ().id, deserializer=deserializer_featurechaining)

    def deserializer_referencesubsetting(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ReferenceSubsetting(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_referencesubsetting().id, deserializer=
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
        get_endfeaturemembership().id, deserializer=
        deserializer_endfeaturemembership)

    def deserializer_elementfiltermembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return ElementFilterMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_elementfiltermembership().id, deserializer=
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
    serialization.instantiator.register_custom_deserializer(get_librarypackage
        ().id, deserializer=deserializer_librarypackage)

    def deserializer_invocationexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return InvocationExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_invocationexpression().id, deserializer=
        deserializer_invocationexpression)

    def deserializer_featurereferenceexpression(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return FeatureReferenceExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_featurereferenceexpression().id, deserializer=
        deserializer_featurereferenceexpression)

    def deserializer_operatorexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return OperatorExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_operatorexpression().id, deserializer=
        deserializer_operatorexpression)

    def deserializer_literalstring(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralString(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literalstring
        ().id, deserializer=deserializer_literalstring)

    def deserializer_literalexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_literalexpression().id, deserializer=deserializer_literalexpression
        )

    def deserializer_literalboolean(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralBoolean(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literalboolean
        ().id, deserializer=deserializer_literalboolean)

    def deserializer_literalinteger(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralInteger(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literalinteger
        ().id, deserializer=deserializer_literalinteger)

    def deserializer_nullexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return NullExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_nullexpression
        ().id, deserializer=deserializer_nullexpression)

    def deserializer_metadataaccessexpression(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return MetadataAccessExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_metadataaccessexpression().id, deserializer=
        deserializer_metadataaccessexpression)

    def deserializer_metadatafeature(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MetadataFeature(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_metadatafeature
        ().id, deserializer=deserializer_metadatafeature)

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
        get_selectexpression().id, deserializer=deserializer_selectexpression)

    def deserializer_featurechainexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return FeatureChainExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_featurechainexpression().id, deserializer=
        deserializer_featurechainexpression)

    def deserializer_collectexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return CollectExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_collectexpression().id, deserializer=deserializer_collectexpression
        )

    def deserializer_literalinfinity(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralInfinity(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literalinfinity
        ().id, deserializer=deserializer_literalinfinity)

    def deserializer_literalrational(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralRational(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literalrational
        ().id, deserializer=deserializer_literalrational)

    def deserializer_multiplicityrange(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MultiplicityRange(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_multiplicityrange().id, deserializer=deserializer_multiplicityrange
        )

    def deserializer_featurevalue(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return FeatureValue(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_featurevalue
        ().id, deserializer=deserializer_featurevalue)

    def deserializer_bindingconnector(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return BindingConnector(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_bindingconnector().id, deserializer=deserializer_bindingconnector)

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
        get_booleanexpression().id, deserializer=deserializer_booleanexpression
        )

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
        get_returnparametermembership().id, deserializer=
        deserializer_returnparametermembership)

    def deserializer_parametermembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ParameterMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_parametermembership().id, deserializer=
        deserializer_parametermembership)

    def deserializer_resultexpressionmembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return ResultExpressionMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_resultexpressionmembership().id, deserializer=
        deserializer_resultexpressionmembership)

    def deserializer_datatype(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return DataType(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_datatype().
        id, deserializer=deserializer_datatype)

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
    serialization.instantiator.register_custom_deserializer(get_itemflowend
        ().id, deserializer=deserializer_itemflowend)

    def deserializer_itemflow(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemFlow(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_itemflow().
        id, deserializer=deserializer_itemflow)

    def deserializer_itemfeature(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemFeature(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_itemfeature
        ().id, deserializer=deserializer_itemfeature)

    def deserializer_successionitemflow(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return SuccessionItemFlow(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_successionitemflow().id, deserializer=
        deserializer_successionitemflow)

    def deserializer_associationstructure(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AssociationStructure(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_associationstructure().id, deserializer=
        deserializer_associationstructure)

    def deserializer_aliasidscontainer(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AliasIdsContainer(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_aliasidscontainer().id, deserializer=deserializer_aliasidscontainer
        )

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
        get_annotatingelement().id, deserializer=deserializer_annotatingelement
        )

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
