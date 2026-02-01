from gen.language import get_subclassification, get_specialization, get_owningmembership, get_membership, get_documentation, get_comment, get_annotation, get_textualrepresentation, get_featuremembership, get_redefinition, get_subsetting, get_featuretyping, get_typefeaturing, get_featureinverting, get_featurechaining, get_referencesubsetting, get_crosssubsetting, get_conjugation, get_multiplicity, get_intersecting, get_unioning, get_disjoining, get_differencing, get_endfeaturemembership, get_resultexpressionmembership, get_returnparametermembership, get_parametermembership, get_multiplicityrange, get_featurevalue, get_metadatafeature, get_itemflowend, get_itemfeature, get_elementfiltermembership, get_package, get_librarypackage, get_featurereferenceexpression, get_metadataaccessexpression, get_nullexpression, get_indexexpression, get_operatorexpression, get_invocationexpression, get_collectexpression, get_literalinfinity, get_literalexpression, get_literalinteger, get_selectexpression, get_literalrational, get_literalboolean, get_literalstring, get_featurechainexpression, get_dependency, get_namespaceimport, get_membershipimport, get_interfaceusage, get_connectionusage, get_connectorasusage, get_variantmembership, get_definition, get_referenceusage, get_attributeusage, get_enumerationusage, get_enumerationdefinition, get_attributedefinition, get_occurrencedefinition, get_lifeclass, get_partdefinition, get_itemdefinition, get_portusage, get_portdefinition, get_conjugatedportdefinition, get_portconjugation, get_flowconnectionusage, get_allocationusage, get_allocationdefinition, get_connectiondefinition, get_stateusage, get_transitionusage, get_acceptactionusage, get_calculationusage, get_requirementusage, get_requirementdefinition, get_constraintdefinition, get_concernusage, get_concerndefinition, get_caseusage, get_casedefinition, get_calculationdefinition, get_actiondefinition, get_analysiscaseusage, get_analysiscasedefinition, get_verificationcaseusage, get_verificationcasedefinition, get_usecaseusage, get_usecasedefinition, get_viewusage, get_viewdefinition, get_viewpointusage, get_viewpointdefinition, get_renderingusage, get_renderingdefinition, get_metadatausage, get_interfacedefinition, get_conjugatedporttyping, get_transitionfeaturemembership, get_exhibitstateusage, get_statesubactionmembership, get_statedefinition, get_successionflowconnectionusage, get_flowconnectiondefinition, get_requirementverificationmembership, get_requirementconstraintmembership, get_includeusecaseusage, get_objectivemembership, get_satisfyrequirementusage, get_subjectmembership, get_stakeholdermembership, get_framedconcernmembership, get_actormembership, get_viewrenderingmembership, get_namespaceexpose, get_membershipexpose, get_bindingconnectorasusage, get_successionasusage, get_forknode, get_controlnode, get_joinnode, get_sendactionusage, get_decisionnode, get_mergenode, get_loopactionusage, get_triggerinvocationexpression, get_assignmentactionusage, get_forloopactionusage, get_ifactionusage, get_whileloopactionusage, get_terminateactionusage, get_metadatadefinition, get_aliasidscontainer, get_textcontainer, get_featuring, get_relationship, get_element, get_annotatingelement, get_step, get_feature, get_type, get_namespace, get_behavior, get_class, get_classifier, get_succession, get_connector, get_structure, get_partusage, get_itemusage, get_occurrenceusage, get_usage, get_datatype, get_actionusage, get_itemflow, get_associationstructure, get_association, get_predicate, get_function, get_performactionusage, get_eventoccurrenceusage, get_successionitemflow, get_interaction, get_assertconstraintusage, get_constraintusage, get_booleanexpression, get_expression, get_invariant, get_expose, get_import, get_bindingconnector, get_metaclass
from gen.node_classes import Subclassification, Specialization, OwningMembership, Membership, Documentation, Comment, Annotation, TextualRepresentation, FeatureMembership, Redefinition, Subsetting, FeatureTyping, TypeFeaturing, FeatureInverting, FeatureChaining, ReferenceSubsetting, CrossSubsetting, Conjugation, Multiplicity, Intersecting, Unioning, Disjoining, Differencing, EndFeatureMembership, ResultExpressionMembership, ReturnParameterMembership, ParameterMembership, MultiplicityRange, FeatureValue, MetadataFeature, ItemFlowEnd, ItemFeature, ElementFilterMembership, Package, LibraryPackage, FeatureReferenceExpression, MetadataAccessExpression, NullExpression, IndexExpression, OperatorExpression, InvocationExpression, CollectExpression, LiteralInfinity, LiteralExpression, LiteralInteger, SelectExpression, LiteralRational, LiteralBoolean, LiteralString, FeatureChainExpression, Dependency, NamespaceImport, MembershipImport, InterfaceUsage, ConnectionUsage, ConnectorAsUsage, VariantMembership, Definition, ReferenceUsage, AttributeUsage, EnumerationUsage, EnumerationDefinition, AttributeDefinition, OccurrenceDefinition, LifeClass, PartDefinition, ItemDefinition, PortUsage, PortDefinition, ConjugatedPortDefinition, PortConjugation, FlowConnectionUsage, AllocationUsage, AllocationDefinition, ConnectionDefinition, StateUsage, TransitionUsage, AcceptActionUsage, CalculationUsage, RequirementUsage, RequirementDefinition, ConstraintDefinition, ConcernUsage, ConcernDefinition, CaseUsage, CaseDefinition, CalculationDefinition, ActionDefinition, AnalysisCaseUsage, AnalysisCaseDefinition, VerificationCaseUsage, VerificationCaseDefinition, UseCaseUsage, UseCaseDefinition, ViewUsage, ViewDefinition, ViewpointUsage, ViewpointDefinition, RenderingUsage, RenderingDefinition, MetadataUsage, InterfaceDefinition, ConjugatedPortTyping, TransitionFeatureMembership, ExhibitStateUsage, StateSubactionMembership, StateDefinition, SuccessionFlowConnectionUsage, FlowConnectionDefinition, RequirementVerificationMembership, RequirementConstraintMembership, IncludeUseCaseUsage, ObjectiveMembership, SatisfyRequirementUsage, SubjectMembership, StakeholderMembership, FramedConcernMembership, ActorMembership, ViewRenderingMembership, NamespaceExpose, MembershipExpose, BindingConnectorAsUsage, SuccessionAsUsage, ForkNode, ControlNode, JoinNode, SendActionUsage, DecisionNode, MergeNode, LoopActionUsage, TriggerInvocationExpression, AssignmentActionUsage, ForLoopActionUsage, IfActionUsage, WhileLoopActionUsage, TerminateActionUsage, MetadataDefinition, AliasIdsContainer, TextContainer, Featuring, Relationship, Element, AnnotatingElement, Step, Feature, Type, Namespace, Behavior, Class, Classifier, Succession, Connector, Structure, PartUsage, ItemUsage, OccurrenceUsage, Usage, DataType, ActionUsage, ItemFlow, AssociationStructure, Association, Predicate, Function, PerformActionUsage, EventOccurrenceUsage, SuccessionItemFlow, Interaction, AssertConstraintUsage, ConstraintUsage, BooleanExpression, Expression, Invariant, Expose, Import, BindingConnector, Metaclass
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
        get_owningmembership().id, deserializer=deserializer_owningmembership)

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
        get_textualrepresentation().id, deserializer=
        deserializer_textualrepresentation)

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

    def deserializer_crosssubsetting(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return CrossSubsetting(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_crosssubsetting
        ().id, deserializer=deserializer_crosssubsetting)

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

    def deserializer_resultexpressionmembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return ResultExpressionMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_resultexpressionmembership().id, deserializer=
        deserializer_resultexpressionmembership)

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

    def deserializer_metadatafeature(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MetadataFeature(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_metadatafeature
        ().id, deserializer=deserializer_metadatafeature)

    def deserializer_itemflowend(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemFlowEnd(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_itemflowend
        ().id, deserializer=deserializer_itemflowend)

    def deserializer_itemfeature(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemFeature(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_itemfeature
        ().id, deserializer=deserializer_itemfeature)

    def deserializer_elementfiltermembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return ElementFilterMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_elementfiltermembership().id, deserializer=
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
    serialization.instantiator.register_custom_deserializer(get_librarypackage
        ().id, deserializer=deserializer_librarypackage)

    def deserializer_featurereferenceexpression(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return FeatureReferenceExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_featurereferenceexpression().id, deserializer=
        deserializer_featurereferenceexpression)

    def deserializer_metadataaccessexpression(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return MetadataAccessExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_metadataaccessexpression().id, deserializer=
        deserializer_metadataaccessexpression)

    def deserializer_nullexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return NullExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_nullexpression
        ().id, deserializer=deserializer_nullexpression)

    def deserializer_indexexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return IndexExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_indexexpression
        ().id, deserializer=deserializer_indexexpression)

    def deserializer_operatorexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return OperatorExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_operatorexpression().id, deserializer=
        deserializer_operatorexpression)

    def deserializer_invocationexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return InvocationExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_invocationexpression().id, deserializer=
        deserializer_invocationexpression)

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

    def deserializer_literalexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_literalexpression().id, deserializer=deserializer_literalexpression
        )

    def deserializer_literalinteger(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralInteger(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literalinteger
        ().id, deserializer=deserializer_literalinteger)

    def deserializer_selectexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return SelectExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_selectexpression().id, deserializer=deserializer_selectexpression)

    def deserializer_literalrational(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralRational(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literalrational
        ().id, deserializer=deserializer_literalrational)

    def deserializer_literalboolean(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralBoolean(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literalboolean
        ().id, deserializer=deserializer_literalboolean)

    def deserializer_literalstring(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LiteralString(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_literalstring
        ().id, deserializer=deserializer_literalstring)

    def deserializer_featurechainexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return FeatureChainExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_featurechainexpression().id, deserializer=
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
    serialization.instantiator.register_custom_deserializer(get_namespaceimport
        ().id, deserializer=deserializer_namespaceimport)

    def deserializer_membershipimport(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MembershipImport(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_membershipimport().id, deserializer=deserializer_membershipimport)

    def deserializer_interfaceusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return InterfaceUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_interfaceusage
        ().id, deserializer=deserializer_interfaceusage)

    def deserializer_connectionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConnectionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_connectionusage
        ().id, deserializer=deserializer_connectionusage)

    def deserializer_connectorasusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConnectorAsUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_connectorasusage().id, deserializer=deserializer_connectorasusage)

    def deserializer_variantmembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return VariantMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_variantmembership().id, deserializer=deserializer_variantmembership
        )

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
    serialization.instantiator.register_custom_deserializer(get_referenceusage
        ().id, deserializer=deserializer_referenceusage)

    def deserializer_attributeusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AttributeUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_attributeusage
        ().id, deserializer=deserializer_attributeusage)

    def deserializer_enumerationusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return EnumerationUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_enumerationusage().id, deserializer=deserializer_enumerationusage)

    def deserializer_enumerationdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return EnumerationDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_enumerationdefinition().id, deserializer=
        deserializer_enumerationdefinition)

    def deserializer_attributedefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AttributeDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_attributedefinition().id, deserializer=
        deserializer_attributedefinition)

    def deserializer_occurrencedefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return OccurrenceDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_occurrencedefinition().id, deserializer=
        deserializer_occurrencedefinition)

    def deserializer_lifeclass(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LifeClass(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_lifeclass()
        .id, deserializer=deserializer_lifeclass)

    def deserializer_partdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return PartDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_partdefinition
        ().id, deserializer=deserializer_partdefinition)

    def deserializer_itemdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_itemdefinition
        ().id, deserializer=deserializer_itemdefinition)

    def deserializer_portusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return PortUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_portusage()
        .id, deserializer=deserializer_portusage)

    def deserializer_portdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return PortDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_portdefinition
        ().id, deserializer=deserializer_portdefinition)

    def deserializer_conjugatedportdefinition(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return ConjugatedPortDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_conjugatedportdefinition().id, deserializer=
        deserializer_conjugatedportdefinition)

    def deserializer_portconjugation(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return PortConjugation(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_portconjugation
        ().id, deserializer=deserializer_portconjugation)

    def deserializer_flowconnectionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return FlowConnectionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_flowconnectionusage().id, deserializer=
        deserializer_flowconnectionusage)

    def deserializer_allocationusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AllocationUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_allocationusage
        ().id, deserializer=deserializer_allocationusage)

    def deserializer_allocationdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AllocationDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_allocationdefinition().id, deserializer=
        deserializer_allocationdefinition)

    def deserializer_connectiondefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConnectionDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_connectiondefinition().id, deserializer=
        deserializer_connectiondefinition)

    def deserializer_stateusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return StateUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_stateusage(
        ).id, deserializer=deserializer_stateusage)

    def deserializer_transitionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return TransitionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_transitionusage
        ().id, deserializer=deserializer_transitionusage)

    def deserializer_acceptactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AcceptActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_acceptactionusage().id, deserializer=deserializer_acceptactionusage
        )

    def deserializer_calculationusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return CalculationUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_calculationusage().id, deserializer=deserializer_calculationusage)

    def deserializer_requirementusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return RequirementUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_requirementusage().id, deserializer=deserializer_requirementusage)

    def deserializer_requirementdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return RequirementDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_requirementdefinition().id, deserializer=
        deserializer_requirementdefinition)

    def deserializer_constraintdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConstraintDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_constraintdefinition().id, deserializer=
        deserializer_constraintdefinition)

    def deserializer_concernusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConcernUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_concernusage
        ().id, deserializer=deserializer_concernusage)

    def deserializer_concerndefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConcernDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_concerndefinition().id, deserializer=deserializer_concerndefinition
        )

    def deserializer_caseusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return CaseUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_caseusage()
        .id, deserializer=deserializer_caseusage)

    def deserializer_casedefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return CaseDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_casedefinition
        ().id, deserializer=deserializer_casedefinition)

    def deserializer_calculationdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return CalculationDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_calculationdefinition().id, deserializer=
        deserializer_calculationdefinition)

    def deserializer_actiondefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ActionDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_actiondefinition().id, deserializer=deserializer_actiondefinition)

    def deserializer_analysiscaseusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AnalysisCaseUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_analysiscaseusage().id, deserializer=deserializer_analysiscaseusage
        )

    def deserializer_analysiscasedefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AnalysisCaseDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_analysiscasedefinition().id, deserializer=
        deserializer_analysiscasedefinition)

    def deserializer_verificationcaseusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return VerificationCaseUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_verificationcaseusage().id, deserializer=
        deserializer_verificationcaseusage)

    def deserializer_verificationcasedefinition(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return VerificationCaseDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_verificationcasedefinition().id, deserializer=
        deserializer_verificationcasedefinition)

    def deserializer_usecaseusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return UseCaseUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_usecaseusage
        ().id, deserializer=deserializer_usecaseusage)

    def deserializer_usecasedefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return UseCaseDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_usecasedefinition().id, deserializer=deserializer_usecasedefinition
        )

    def deserializer_viewusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ViewUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_viewusage()
        .id, deserializer=deserializer_viewusage)

    def deserializer_viewdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ViewDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_viewdefinition
        ().id, deserializer=deserializer_viewdefinition)

    def deserializer_viewpointusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ViewpointUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_viewpointusage
        ().id, deserializer=deserializer_viewpointusage)

    def deserializer_viewpointdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ViewpointDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_viewpointdefinition().id, deserializer=
        deserializer_viewpointdefinition)

    def deserializer_renderingusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return RenderingUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_renderingusage
        ().id, deserializer=deserializer_renderingusage)

    def deserializer_renderingdefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return RenderingDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_renderingdefinition().id, deserializer=
        deserializer_renderingdefinition)

    def deserializer_metadatausage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MetadataUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_metadatausage
        ().id, deserializer=deserializer_metadatausage)

    def deserializer_interfacedefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return InterfaceDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_interfacedefinition().id, deserializer=
        deserializer_interfacedefinition)

    def deserializer_conjugatedporttyping(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConjugatedPortTyping(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_conjugatedporttyping().id, deserializer=
        deserializer_conjugatedporttyping)

    def deserializer_transitionfeaturemembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return TransitionFeatureMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_transitionfeaturemembership().id, deserializer=
        deserializer_transitionfeaturemembership)

    def deserializer_exhibitstateusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ExhibitStateUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_exhibitstateusage().id, deserializer=deserializer_exhibitstateusage
        )

    def deserializer_statesubactionmembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return StateSubactionMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_statesubactionmembership().id, deserializer=
        deserializer_statesubactionmembership)

    def deserializer_statedefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return StateDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_statedefinition
        ().id, deserializer=deserializer_statedefinition)

    def deserializer_successionflowconnectionusage(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return SuccessionFlowConnectionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_successionflowconnectionusage().id, deserializer=
        deserializer_successionflowconnectionusage)

    def deserializer_flowconnectiondefinition(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return FlowConnectionDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_flowconnectiondefinition().id, deserializer=
        deserializer_flowconnectiondefinition)

    def deserializer_requirementverificationmembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return RequirementVerificationMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_requirementverificationmembership().id, deserializer=
        deserializer_requirementverificationmembership)

    def deserializer_requirementconstraintmembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return RequirementConstraintMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_requirementconstraintmembership().id, deserializer=
        deserializer_requirementconstraintmembership)

    def deserializer_includeusecaseusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return IncludeUseCaseUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_includeusecaseusage().id, deserializer=
        deserializer_includeusecaseusage)

    def deserializer_objectivemembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ObjectiveMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_objectivemembership().id, deserializer=
        deserializer_objectivemembership)

    def deserializer_satisfyrequirementusage(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return SatisfyRequirementUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_satisfyrequirementusage().id, deserializer=
        deserializer_satisfyrequirementusage)

    def deserializer_subjectmembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return SubjectMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_subjectmembership().id, deserializer=deserializer_subjectmembership
        )

    def deserializer_stakeholdermembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return StakeholderMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_stakeholdermembership().id, deserializer=
        deserializer_stakeholdermembership)

    def deserializer_framedconcernmembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return FramedConcernMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_framedconcernmembership().id, deserializer=
        deserializer_framedconcernmembership)

    def deserializer_actormembership(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ActorMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_actormembership
        ().id, deserializer=deserializer_actormembership)

    def deserializer_viewrenderingmembership(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return ViewRenderingMembership(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_viewrenderingmembership().id, deserializer=
        deserializer_viewrenderingmembership)

    def deserializer_namespaceexpose(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return NamespaceExpose(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_namespaceexpose
        ().id, deserializer=deserializer_namespaceexpose)

    def deserializer_membershipexpose(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MembershipExpose(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_membershipexpose().id, deserializer=deserializer_membershipexpose)

    def deserializer_bindingconnectorasusage(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return BindingConnectorAsUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_bindingconnectorasusage().id, deserializer=
        deserializer_bindingconnectorasusage)

    def deserializer_successionasusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return SuccessionAsUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_successionasusage().id, deserializer=deserializer_successionasusage
        )

    def deserializer_forknode(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ForkNode(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_forknode().
        id, deserializer=deserializer_forknode)

    def deserializer_controlnode(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ControlNode(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_controlnode
        ().id, deserializer=deserializer_controlnode)

    def deserializer_joinnode(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return JoinNode(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_joinnode().
        id, deserializer=deserializer_joinnode)

    def deserializer_sendactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return SendActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_sendactionusage
        ().id, deserializer=deserializer_sendactionusage)

    def deserializer_decisionnode(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return DecisionNode(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_decisionnode
        ().id, deserializer=deserializer_decisionnode)

    def deserializer_mergenode(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MergeNode(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_mergenode()
        .id, deserializer=deserializer_mergenode)

    def deserializer_loopactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return LoopActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_loopactionusage
        ().id, deserializer=deserializer_loopactionusage)

    def deserializer_triggerinvocationexpression(classifier,
        serialized_instance: SerializedClassifierInstance,
        deserialized_instances_by_id, properties_values):
        return TriggerInvocationExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_triggerinvocationexpression().id, deserializer=
        deserializer_triggerinvocationexpression)

    def deserializer_assignmentactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AssignmentActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_assignmentactionusage().id, deserializer=
        deserializer_assignmentactionusage)

    def deserializer_forloopactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ForLoopActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_forloopactionusage().id, deserializer=
        deserializer_forloopactionusage)

    def deserializer_ifactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return IfActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_ifactionusage
        ().id, deserializer=deserializer_ifactionusage)

    def deserializer_whileloopactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return WhileLoopActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_whileloopactionusage().id, deserializer=
        deserializer_whileloopactionusage)

    def deserializer_terminateactionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return TerminateActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_terminateactionusage().id, deserializer=
        deserializer_terminateactionusage)

    def deserializer_metadatadefinition(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return MetadataDefinition(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_metadatadefinition().id, deserializer=
        deserializer_metadatadefinition)

    def deserializer_aliasidscontainer(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AliasIdsContainer(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_aliasidscontainer().id, deserializer=deserializer_aliasidscontainer
        )

    def deserializer_textcontainer(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return TextContainer(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_textcontainer
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
        get_annotatingelement().id, deserializer=deserializer_annotatingelement
        )

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
    serialization.instantiator.register_custom_deserializer(get_partusage()
        .id, deserializer=deserializer_partusage)

    def deserializer_itemusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_itemusage()
        .id, deserializer=deserializer_itemusage)

    def deserializer_occurrenceusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return OccurrenceUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_occurrenceusage
        ().id, deserializer=deserializer_occurrenceusage)

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
    serialization.instantiator.register_custom_deserializer(get_datatype().
        id, deserializer=deserializer_datatype)

    def deserializer_actionusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ActionUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_actionusage
        ().id, deserializer=deserializer_actionusage)

    def deserializer_itemflow(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ItemFlow(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_itemflow().
        id, deserializer=deserializer_itemflow)

    def deserializer_associationstructure(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return AssociationStructure(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_associationstructure().id, deserializer=
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
        get_performactionusage().id, deserializer=
        deserializer_performactionusage)

    def deserializer_eventoccurrenceusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return EventOccurrenceUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_eventoccurrenceusage().id, deserializer=
        deserializer_eventoccurrenceusage)

    def deserializer_successionitemflow(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return SuccessionItemFlow(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_successionitemflow().id, deserializer=
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
        get_assertconstraintusage().id, deserializer=
        deserializer_assertconstraintusage)

    def deserializer_constraintusage(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return ConstraintUsage(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_constraintusage
        ().id, deserializer=deserializer_constraintusage)

    def deserializer_booleanexpression(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return BooleanExpression(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(
        get_booleanexpression().id, deserializer=deserializer_booleanexpression
        )

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
        get_bindingconnector().id, deserializer=deserializer_bindingconnector)

    def deserializer_metaclass(classifier, serialized_instance:
        SerializedClassifierInstance, deserialized_instances_by_id,
        properties_values):
        return Metaclass(serialized_instance.id)
    serialization.instantiator.register_custom_deserializer(get_metaclass()
        .id, deserializer=deserializer_metaclass)
