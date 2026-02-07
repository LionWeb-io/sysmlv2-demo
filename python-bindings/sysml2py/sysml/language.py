from lionweb.language import Language, Concept, Containment, Enumeration, Interface, PrimitiveType, Property, Reference, LionCoreBuiltins
from lionweb.lionweb_version import LionWebVersion
from functools import lru_cache
from sysml2py.types.language import get_language as get_types_language


@lru_cache(maxsize=1)
def get_language() ->Language:
    language = Language(lion_web_version=LionWebVersion.V2023_1, id='sysml',
        name='sysml', key='sysml', version='1')
    subclassification = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-Subclassification', name='Subclassification', key=
        'sysml-Subclassification')
    subclassification.abstract = False
    subclassification.partition = False
    language.add_element(subclassification)
    specialization = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Specialization', name='Specialization', key=
        'sysml-Specialization')
    specialization.abstract = False
    specialization.partition = False
    language.add_element(specialization)
    i_relationship = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IRelationship', name='IRelationship', key='sysml-IRelationship')
    language.add_element(i_relationship)
    i_element = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IElement', name='IElement', key='sysml-IElement')
    language.add_element(i_element)
    owning_membership = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-OwningMembership', name='OwningMembership', key=
        'sysml-OwningMembership')
    owning_membership.abstract = False
    owning_membership.partition = False
    language.add_element(owning_membership)
    membership = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Membership', name='Membership', key='sysml-Membership')
    membership.abstract = False
    membership.partition = False
    language.add_element(membership)
    i_namespace = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-INamespace', name='INamespace', key='sysml-INamespace')
    language.add_element(i_namespace)
    i_import = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IImport', name='IImport', key='sysml-IImport')
    language.add_element(i_import)
    visibility_kind = Enumeration(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-VisibilityKind', name='VisibilityKind', key=
        'sysml-VisibilityKind')
    language.add_element(visibility_kind)
    documentation = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Documentation', name='Documentation', key='sysml-Documentation')
    documentation.abstract = False
    documentation.partition = False
    language.add_element(documentation)
    comment = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Comment', name='Comment', key='sysml-Comment')
    comment.abstract = False
    comment.partition = False
    language.add_element(comment)
    i_annotating_element = Interface(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IAnnotatingElement', name='IAnnotatingElement',
        key='sysml-IAnnotatingElement')
    language.add_element(i_annotating_element)
    annotation = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Annotation', name='Annotation', key='sysml-Annotation')
    annotation.abstract = False
    annotation.partition = False
    language.add_element(annotation)
    textual_representation = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-TextualRepresentation', name=
        'TextualRepresentation', key='sysml-TextualRepresentation')
    textual_representation.abstract = False
    textual_representation.partition = False
    language.add_element(textual_representation)
    i_type = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IType', name='IType', key='sysml-IType')
    language.add_element(i_type)
    feature_membership = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-FeatureMembership', name='FeatureMembership', key=
        'sysml-FeatureMembership')
    feature_membership.abstract = False
    feature_membership.partition = False
    language.add_element(feature_membership)
    i_featuring = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IFeaturing', name='IFeaturing', key='sysml-IFeaturing')
    language.add_element(i_featuring)
    i_feature = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IFeature', name='IFeature', key='sysml-IFeature')
    language.add_element(i_feature)
    redefinition = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Redefinition', name='Redefinition', key='sysml-Redefinition')
    redefinition.abstract = False
    redefinition.partition = False
    language.add_element(redefinition)
    subsetting = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Subsetting', name='Subsetting', key='sysml-Subsetting')
    subsetting.abstract = False
    subsetting.partition = False
    language.add_element(subsetting)
    feature_typing = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-FeatureTyping', name='FeatureTyping', key='sysml-FeatureTyping')
    feature_typing.abstract = False
    feature_typing.partition = False
    language.add_element(feature_typing)
    type_featuring = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-TypeFeaturing', name='TypeFeaturing', key='sysml-TypeFeaturing')
    type_featuring.abstract = False
    type_featuring.partition = False
    language.add_element(type_featuring)
    feature_inverting = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-FeatureInverting', name='FeatureInverting', key=
        'sysml-FeatureInverting')
    feature_inverting.abstract = False
    feature_inverting.partition = False
    language.add_element(feature_inverting)
    feature_chaining = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-FeatureChaining', name='FeatureChaining', key=
        'sysml-FeatureChaining')
    feature_chaining.abstract = False
    feature_chaining.partition = False
    language.add_element(feature_chaining)
    feature_direction_kind = Enumeration(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-FeatureDirectionKind', name=
        'FeatureDirectionKind', key='sysml-FeatureDirectionKind')
    language.add_element(feature_direction_kind)
    reference_subsetting = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-ReferenceSubsetting', name='ReferenceSubsetting', key=
        'sysml-ReferenceSubsetting')
    reference_subsetting.abstract = False
    reference_subsetting.partition = False
    language.add_element(reference_subsetting)
    cross_subsetting = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-CrossSubsetting', name='CrossSubsetting', key=
        'sysml-CrossSubsetting')
    cross_subsetting.abstract = False
    cross_subsetting.partition = False
    language.add_element(cross_subsetting)
    conjugation = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Conjugation', name='Conjugation', key='sysml-Conjugation')
    conjugation.abstract = False
    conjugation.partition = False
    language.add_element(conjugation)
    multiplicity = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Multiplicity', name='Multiplicity', key='sysml-Multiplicity')
    multiplicity.abstract = False
    multiplicity.partition = False
    language.add_element(multiplicity)
    intersecting = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Intersecting', name='Intersecting', key='sysml-Intersecting')
    intersecting.abstract = False
    intersecting.partition = False
    language.add_element(intersecting)
    unioning = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Unioning', name='Unioning', key='sysml-Unioning')
    unioning.abstract = False
    unioning.partition = False
    language.add_element(unioning)
    disjoining = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Disjoining', name='Disjoining', key='sysml-Disjoining')
    disjoining.abstract = False
    disjoining.partition = False
    language.add_element(disjoining)
    differencing = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Differencing', name='Differencing', key='sysml-Differencing')
    differencing.abstract = False
    differencing.partition = False
    language.add_element(differencing)
    i_classifier = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IClassifier', name='IClassifier', key='sysml-IClassifier')
    language.add_element(i_classifier)
    end_feature_membership = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-EndFeatureMembership', name=
        'EndFeatureMembership', key='sysml-EndFeatureMembership')
    end_feature_membership.abstract = False
    end_feature_membership.partition = False
    language.add_element(end_feature_membership)
    i_expression = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IExpression', name='IExpression', key='sysml-IExpression')
    language.add_element(i_expression)
    i_step = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IStep', name='IStep', key='sysml-IStep')
    language.add_element(i_step)
    i_behavior = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IBehavior', name='IBehavior', key='sysml-IBehavior')
    language.add_element(i_behavior)
    i_class = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IClass', name='IClass', key='sysml-IClass')
    language.add_element(i_class)
    i_function = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IFunction', name='IFunction', key='sysml-IFunction')
    language.add_element(i_function)
    result_expression_membership = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ResultExpressionMembership', name=
        'ResultExpressionMembership', key='sysml-ResultExpressionMembership')
    result_expression_membership.abstract = False
    result_expression_membership.partition = False
    language.add_element(result_expression_membership)
    i_invariant = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IInvariant', name='IInvariant', key='sysml-IInvariant')
    language.add_element(i_invariant)
    i_boolean_expression = Interface(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IBooleanExpression', name='IBooleanExpression',
        key='sysml-IBooleanExpression')
    language.add_element(i_boolean_expression)
    i_predicate = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IPredicate', name='IPredicate', key='sysml-IPredicate')
    language.add_element(i_predicate)
    return_parameter_membership = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ReturnParameterMembership', name=
        'ReturnParameterMembership', key='sysml-ReturnParameterMembership')
    return_parameter_membership.abstract = False
    return_parameter_membership.partition = False
    language.add_element(return_parameter_membership)
    parameter_membership = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-ParameterMembership', name='ParameterMembership', key=
        'sysml-ParameterMembership')
    parameter_membership.abstract = False
    parameter_membership.partition = False
    language.add_element(parameter_membership)
    multiplicity_range = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-MultiplicityRange', name='MultiplicityRange', key=
        'sysml-MultiplicityRange')
    multiplicity_range.abstract = False
    multiplicity_range.partition = False
    language.add_element(multiplicity_range)
    i_structure = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IStructure', name='IStructure', key='sysml-IStructure')
    language.add_element(i_structure)
    feature_value = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-FeatureValue', name='FeatureValue', key='sysml-FeatureValue')
    feature_value.abstract = False
    feature_value.partition = False
    language.add_element(feature_value)
    i_metaclass = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IMetaclass', name='IMetaclass', key='sysml-IMetaclass')
    language.add_element(i_metaclass)
    metadata_feature = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-MetadataFeature', name='MetadataFeature', key=
        'sysml-MetadataFeature')
    metadata_feature.abstract = False
    metadata_feature.partition = False
    language.add_element(metadata_feature)
    i_item_flow = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IItemFlow', name='IItemFlow', key='sysml-IItemFlow')
    language.add_element(i_item_flow)
    i_connector = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IConnector', name='IConnector', key='sysml-IConnector')
    language.add_element(i_connector)
    i_association = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IAssociation', name='IAssociation', key='sysml-IAssociation')
    language.add_element(i_association)
    item_flow_end = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ItemFlowEnd', name='ItemFlowEnd', key='sysml-ItemFlowEnd')
    item_flow_end.abstract = False
    item_flow_end.partition = False
    language.add_element(item_flow_end)
    item_feature = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ItemFeature', name='ItemFeature', key='sysml-ItemFeature')
    item_feature.abstract = False
    item_feature.partition = False
    language.add_element(item_feature)
    i_interaction = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IInteraction', name='IInteraction', key='sysml-IInteraction')
    language.add_element(i_interaction)
    i_succession_item_flow = Interface(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ISuccessionItemFlow', name='ISuccessionItemFlow',
        key='sysml-ISuccessionItemFlow')
    language.add_element(i_succession_item_flow)
    i_succession = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ISuccession', name='ISuccession', key='sysml-ISuccession')
    language.add_element(i_succession)
    element_filter_membership = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ElementFilterMembership', name=
        'ElementFilterMembership', key='sysml-ElementFilterMembership')
    element_filter_membership.abstract = False
    element_filter_membership.partition = False
    language.add_element(element_filter_membership)
    package = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Package', name='Package', key='sysml-Package')
    package.abstract = False
    package.partition = False
    language.add_element(package)
    library_package = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-LibraryPackage', name='LibraryPackage', key=
        'sysml-LibraryPackage')
    library_package.abstract = False
    library_package.partition = False
    language.add_element(library_package)
    i_data_type = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IDataType', name='IDataType', key='sysml-IDataType')
    language.add_element(i_data_type)
    feature_reference_expression = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-FeatureReferenceExpression', name=
        'FeatureReferenceExpression', key='sysml-FeatureReferenceExpression')
    feature_reference_expression.abstract = False
    feature_reference_expression.partition = False
    language.add_element(feature_reference_expression)
    metadata_access_expression = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-MetadataAccessExpression', name=
        'MetadataAccessExpression', key='sysml-MetadataAccessExpression')
    metadata_access_expression.abstract = False
    metadata_access_expression.partition = False
    language.add_element(metadata_access_expression)
    null_expression = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-NullExpression', name='NullExpression', key=
        'sysml-NullExpression')
    null_expression.abstract = False
    null_expression.partition = False
    language.add_element(null_expression)
    index_expression = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IndexExpression', name='IndexExpression', key=
        'sysml-IndexExpression')
    index_expression.abstract = False
    index_expression.partition = False
    language.add_element(index_expression)
    operator_expression = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-OperatorExpression', name='OperatorExpression', key=
        'sysml-OperatorExpression')
    operator_expression.abstract = False
    operator_expression.partition = False
    language.add_element(operator_expression)
    invocation_expression = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-InvocationExpression', name='InvocationExpression', key=
        'sysml-InvocationExpression')
    invocation_expression.abstract = False
    invocation_expression.partition = False
    language.add_element(invocation_expression)
    collect_expression = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-CollectExpression', name='CollectExpression', key=
        'sysml-CollectExpression')
    collect_expression.abstract = False
    collect_expression.partition = False
    language.add_element(collect_expression)
    literal_infinity = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-LiteralInfinity', name='LiteralInfinity', key=
        'sysml-LiteralInfinity')
    literal_infinity.abstract = False
    literal_infinity.partition = False
    language.add_element(literal_infinity)
    literal_expression = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-LiteralExpression', name='LiteralExpression', key=
        'sysml-LiteralExpression')
    literal_expression.abstract = False
    literal_expression.partition = False
    language.add_element(literal_expression)
    literal_integer = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-LiteralInteger', name='LiteralInteger', key=
        'sysml-LiteralInteger')
    literal_integer.abstract = False
    literal_integer.partition = False
    language.add_element(literal_integer)
    select_expression = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-SelectExpression', name='SelectExpression', key=
        'sysml-SelectExpression')
    select_expression.abstract = False
    select_expression.partition = False
    language.add_element(select_expression)
    literal_rational = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-LiteralRational', name='LiteralRational', key=
        'sysml-LiteralRational')
    literal_rational.abstract = False
    literal_rational.partition = False
    language.add_element(literal_rational)
    literal_boolean = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-LiteralBoolean', name='LiteralBoolean', key=
        'sysml-LiteralBoolean')
    literal_boolean.abstract = False
    literal_boolean.partition = False
    language.add_element(literal_boolean)
    literal_string = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-LiteralString', name='LiteralString', key='sysml-LiteralString')
    literal_string.abstract = False
    literal_string.partition = False
    language.add_element(literal_string)
    feature_chain_expression = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-FeatureChainExpression', name=
        'FeatureChainExpression', key='sysml-FeatureChainExpression')
    feature_chain_expression.abstract = False
    feature_chain_expression.partition = False
    language.add_element(feature_chain_expression)
    i_binding_connector = Interface(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IBindingConnector', name='IBindingConnector', key=
        'sysml-IBindingConnector')
    language.add_element(i_binding_connector)
    i_association_structure = Interface(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IAssociationStructure', name=
        'IAssociationStructure', key='sysml-IAssociationStructure')
    language.add_element(i_association_structure)
    dependency = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Dependency', name='Dependency', key='sysml-Dependency')
    dependency.abstract = False
    dependency.partition = False
    language.add_element(dependency)
    namespace_import = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-NamespaceImport', name='NamespaceImport', key=
        'sysml-NamespaceImport')
    namespace_import.abstract = False
    namespace_import.partition = False
    language.add_element(namespace_import)
    membership_import = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-MembershipImport', name='MembershipImport', key=
        'sysml-MembershipImport')
    membership_import.abstract = False
    membership_import.partition = False
    language.add_element(membership_import)
    interface_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-InterfaceUsage', name='InterfaceUsage', key=
        'sysml-InterfaceUsage')
    interface_usage.abstract = False
    interface_usage.partition = False
    language.add_element(interface_usage)
    connection_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ConnectionUsage', name='ConnectionUsage', key=
        'sysml-ConnectionUsage')
    connection_usage.abstract = False
    connection_usage.partition = False
    language.add_element(connection_usage)
    connector_as_usage = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-ConnectorAsUsage', name='ConnectorAsUsage', key=
        'sysml-ConnectorAsUsage')
    connector_as_usage.abstract = True
    connector_as_usage.partition = False
    language.add_element(connector_as_usage)
    i_usage = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IUsage', name='IUsage', key='sysml-IUsage')
    language.add_element(i_usage)
    variant_membership = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-VariantMembership', name='VariantMembership', key=
        'sysml-VariantMembership')
    variant_membership.abstract = False
    variant_membership.partition = False
    language.add_element(variant_membership)
    definition = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Definition', name='Definition', key='sysml-Definition')
    definition.abstract = False
    definition.partition = False
    language.add_element(definition)
    reference_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ReferenceUsage', name='ReferenceUsage', key=
        'sysml-ReferenceUsage')
    reference_usage.abstract = False
    reference_usage.partition = False
    language.add_element(reference_usage)
    attribute_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-AttributeUsage', name='AttributeUsage', key=
        'sysml-AttributeUsage')
    attribute_usage.abstract = False
    attribute_usage.partition = False
    language.add_element(attribute_usage)
    enumeration_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-EnumerationUsage', name='EnumerationUsage', key=
        'sysml-EnumerationUsage')
    enumeration_usage.abstract = False
    enumeration_usage.partition = False
    language.add_element(enumeration_usage)
    enumeration_definition = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-EnumerationDefinition', name=
        'EnumerationDefinition', key='sysml-EnumerationDefinition')
    enumeration_definition.abstract = False
    enumeration_definition.partition = False
    language.add_element(enumeration_definition)
    attribute_definition = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-AttributeDefinition', name='AttributeDefinition', key=
        'sysml-AttributeDefinition')
    attribute_definition.abstract = False
    attribute_definition.partition = False
    language.add_element(attribute_definition)
    i_occurrence_usage = Interface(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IOccurrenceUsage', name='IOccurrenceUsage', key=
        'sysml-IOccurrenceUsage')
    language.add_element(i_occurrence_usage)
    occurrence_definition = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-OccurrenceDefinition', name='OccurrenceDefinition', key=
        'sysml-OccurrenceDefinition')
    occurrence_definition.abstract = False
    occurrence_definition.partition = False
    language.add_element(occurrence_definition)
    life_class = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-LifeClass', name='LifeClass', key='sysml-LifeClass')
    life_class.abstract = False
    life_class.partition = False
    language.add_element(life_class)
    portion_kind = Enumeration(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-PortionKind', name='PortionKind', key='sysml-PortionKind')
    language.add_element(portion_kind)
    i_item_usage = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IItemUsage', name='IItemUsage', key='sysml-IItemUsage')
    language.add_element(i_item_usage)
    i_part_usage = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IPartUsage', name='IPartUsage', key='sysml-IPartUsage')
    language.add_element(i_part_usage)
    part_definition = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-PartDefinition', name='PartDefinition', key=
        'sysml-PartDefinition')
    part_definition.abstract = False
    part_definition.partition = False
    language.add_element(part_definition)
    item_definition = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ItemDefinition', name='ItemDefinition', key=
        'sysml-ItemDefinition')
    item_definition.abstract = False
    item_definition.partition = False
    language.add_element(item_definition)
    port_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-PortUsage', name='PortUsage', key='sysml-PortUsage')
    port_usage.abstract = False
    port_usage.partition = False
    language.add_element(port_usage)
    port_definition = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-PortDefinition', name='PortDefinition', key=
        'sysml-PortDefinition')
    port_definition.abstract = False
    port_definition.partition = False
    language.add_element(port_definition)
    conjugated_port_definition = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ConjugatedPortDefinition', name=
        'ConjugatedPortDefinition', key='sysml-ConjugatedPortDefinition')
    conjugated_port_definition.abstract = False
    conjugated_port_definition.partition = False
    language.add_element(conjugated_port_definition)
    port_conjugation = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-PortConjugation', name='PortConjugation', key=
        'sysml-PortConjugation')
    port_conjugation.abstract = False
    port_conjugation.partition = False
    language.add_element(port_conjugation)
    flow_connection_usage = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-FlowConnectionUsage', name='FlowConnectionUsage', key=
        'sysml-FlowConnectionUsage')
    flow_connection_usage.abstract = False
    flow_connection_usage.partition = False
    language.add_element(flow_connection_usage)
    i_action_usage = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IActionUsage', name='IActionUsage', key='sysml-IActionUsage')
    language.add_element(i_action_usage)
    allocation_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-AllocationUsage', name='AllocationUsage', key=
        'sysml-AllocationUsage')
    allocation_usage.abstract = False
    allocation_usage.partition = False
    language.add_element(allocation_usage)
    allocation_definition = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-AllocationDefinition', name='AllocationDefinition', key=
        'sysml-AllocationDefinition')
    allocation_definition.abstract = False
    allocation_definition.partition = False
    language.add_element(allocation_definition)
    connection_definition = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-ConnectionDefinition', name='ConnectionDefinition', key=
        'sysml-ConnectionDefinition')
    connection_definition.abstract = False
    connection_definition.partition = False
    language.add_element(connection_definition)
    state_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-StateUsage', name='StateUsage', key='sysml-StateUsage')
    state_usage.abstract = False
    state_usage.partition = False
    language.add_element(state_usage)
    transition_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-TransitionUsage', name='TransitionUsage', key=
        'sysml-TransitionUsage')
    transition_usage.abstract = False
    transition_usage.partition = False
    language.add_element(transition_usage)
    accept_action_usage = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-AcceptActionUsage', name='AcceptActionUsage', key=
        'sysml-AcceptActionUsage')
    accept_action_usage.abstract = False
    accept_action_usage.partition = False
    language.add_element(accept_action_usage)
    calculation_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-CalculationUsage', name='CalculationUsage', key=
        'sysml-CalculationUsage')
    calculation_usage.abstract = False
    calculation_usage.partition = False
    language.add_element(calculation_usage)
    i_constraint_usage = Interface(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IConstraintUsage', name='IConstraintUsage', key=
        'sysml-IConstraintUsage')
    language.add_element(i_constraint_usage)
    requirement_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-RequirementUsage', name='RequirementUsage', key=
        'sysml-RequirementUsage')
    requirement_usage.abstract = False
    requirement_usage.partition = False
    language.add_element(requirement_usage)
    requirement_definition = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-RequirementDefinition', name=
        'RequirementDefinition', key='sysml-RequirementDefinition')
    requirement_definition.abstract = False
    requirement_definition.partition = False
    language.add_element(requirement_definition)
    constraint_definition = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-ConstraintDefinition', name='ConstraintDefinition', key=
        'sysml-ConstraintDefinition')
    constraint_definition.abstract = False
    constraint_definition.partition = False
    language.add_element(constraint_definition)
    concern_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ConcernUsage', name='ConcernUsage', key='sysml-ConcernUsage')
    concern_usage.abstract = False
    concern_usage.partition = False
    language.add_element(concern_usage)
    concern_definition = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-ConcernDefinition', name='ConcernDefinition', key=
        'sysml-ConcernDefinition')
    concern_definition.abstract = False
    concern_definition.partition = False
    language.add_element(concern_definition)
    case_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-CaseUsage', name='CaseUsage', key='sysml-CaseUsage')
    case_usage.abstract = False
    case_usage.partition = False
    language.add_element(case_usage)
    case_definition = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-CaseDefinition', name='CaseDefinition', key=
        'sysml-CaseDefinition')
    case_definition.abstract = False
    case_definition.partition = False
    language.add_element(case_definition)
    calculation_definition = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-CalculationDefinition', name=
        'CalculationDefinition', key='sysml-CalculationDefinition')
    calculation_definition.abstract = False
    calculation_definition.partition = False
    language.add_element(calculation_definition)
    action_definition = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-ActionDefinition', name='ActionDefinition', key=
        'sysml-ActionDefinition')
    action_definition.abstract = False
    action_definition.partition = False
    language.add_element(action_definition)
    analysis_case_usage = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-AnalysisCaseUsage', name='AnalysisCaseUsage', key=
        'sysml-AnalysisCaseUsage')
    analysis_case_usage.abstract = False
    analysis_case_usage.partition = False
    language.add_element(analysis_case_usage)
    analysis_case_definition = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-AnalysisCaseDefinition', name=
        'AnalysisCaseDefinition', key='sysml-AnalysisCaseDefinition')
    analysis_case_definition.abstract = False
    analysis_case_definition.partition = False
    language.add_element(analysis_case_definition)
    verification_case_usage = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-VerificationCaseUsage', name=
        'VerificationCaseUsage', key='sysml-VerificationCaseUsage')
    verification_case_usage.abstract = False
    verification_case_usage.partition = False
    language.add_element(verification_case_usage)
    verification_case_definition = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-VerificationCaseDefinition', name=
        'VerificationCaseDefinition', key='sysml-VerificationCaseDefinition')
    verification_case_definition.abstract = False
    verification_case_definition.partition = False
    language.add_element(verification_case_definition)
    use_case_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-UseCaseUsage', name='UseCaseUsage', key='sysml-UseCaseUsage')
    use_case_usage.abstract = False
    use_case_usage.partition = False
    language.add_element(use_case_usage)
    use_case_definition = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-UseCaseDefinition', name='UseCaseDefinition', key=
        'sysml-UseCaseDefinition')
    use_case_definition.abstract = False
    use_case_definition.partition = False
    language.add_element(use_case_definition)
    view_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ViewUsage', name='ViewUsage', key='sysml-ViewUsage')
    view_usage.abstract = False
    view_usage.partition = False
    language.add_element(view_usage)
    view_definition = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ViewDefinition', name='ViewDefinition', key=
        'sysml-ViewDefinition')
    view_definition.abstract = False
    view_definition.partition = False
    language.add_element(view_definition)
    viewpoint_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ViewpointUsage', name='ViewpointUsage', key=
        'sysml-ViewpointUsage')
    viewpoint_usage.abstract = False
    viewpoint_usage.partition = False
    language.add_element(viewpoint_usage)
    viewpoint_definition = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-ViewpointDefinition', name='ViewpointDefinition', key=
        'sysml-ViewpointDefinition')
    viewpoint_definition.abstract = False
    viewpoint_definition.partition = False
    language.add_element(viewpoint_definition)
    rendering_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-RenderingUsage', name='RenderingUsage', key=
        'sysml-RenderingUsage')
    rendering_usage.abstract = False
    rendering_usage.partition = False
    language.add_element(rendering_usage)
    rendering_definition = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-RenderingDefinition', name='RenderingDefinition', key=
        'sysml-RenderingDefinition')
    rendering_definition.abstract = False
    rendering_definition.partition = False
    language.add_element(rendering_definition)
    metadata_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-MetadataUsage', name='MetadataUsage', key='sysml-MetadataUsage')
    metadata_usage.abstract = False
    metadata_usage.partition = False
    language.add_element(metadata_usage)
    interface_definition = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-InterfaceDefinition', name='InterfaceDefinition', key=
        'sysml-InterfaceDefinition')
    interface_definition.abstract = False
    interface_definition.partition = False
    language.add_element(interface_definition)
    conjugated_port_typing = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ConjugatedPortTyping', name=
        'ConjugatedPortTyping', key='sysml-ConjugatedPortTyping')
    conjugated_port_typing.abstract = False
    conjugated_port_typing.partition = False
    language.add_element(conjugated_port_typing)
    transition_feature_membership = Concept(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-TransitionFeatureMembership', name=
        'TransitionFeatureMembership', key='sysml-TransitionFeatureMembership')
    transition_feature_membership.abstract = False
    transition_feature_membership.partition = False
    language.add_element(transition_feature_membership)
    transition_feature_kind = Enumeration(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-TransitionFeatureKind', name=
        'TransitionFeatureKind', key='sysml-TransitionFeatureKind')
    language.add_element(transition_feature_kind)
    exhibit_state_usage = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-ExhibitStateUsage', name='ExhibitStateUsage', key=
        'sysml-ExhibitStateUsage')
    exhibit_state_usage.abstract = False
    exhibit_state_usage.partition = False
    language.add_element(exhibit_state_usage)
    i_perform_action_usage = Interface(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IPerformActionUsage', name='IPerformActionUsage',
        key='sysml-IPerformActionUsage')
    language.add_element(i_perform_action_usage)
    i_event_occurrence_usage = Interface(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IEventOccurrenceUsage', name=
        'IEventOccurrenceUsage', key='sysml-IEventOccurrenceUsage')
    language.add_element(i_event_occurrence_usage)
    state_subaction_kind = Enumeration(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-StateSubactionKind', name='StateSubactionKind',
        key='sysml-StateSubactionKind')
    language.add_element(state_subaction_kind)
    state_subaction_membership = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-StateSubactionMembership', name=
        'StateSubactionMembership', key='sysml-StateSubactionMembership')
    state_subaction_membership.abstract = False
    state_subaction_membership.partition = False
    language.add_element(state_subaction_membership)
    state_definition = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-StateDefinition', name='StateDefinition', key=
        'sysml-StateDefinition')
    state_definition.abstract = False
    state_definition.partition = False
    language.add_element(state_definition)
    succession_flow_connection_usage = Concept(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-SuccessionFlowConnectionUsage',
        name='SuccessionFlowConnectionUsage', key=
        'sysml-SuccessionFlowConnectionUsage')
    succession_flow_connection_usage.abstract = False
    succession_flow_connection_usage.partition = False
    language.add_element(succession_flow_connection_usage)
    flow_connection_definition = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-FlowConnectionDefinition', name=
        'FlowConnectionDefinition', key='sysml-FlowConnectionDefinition')
    flow_connection_definition.abstract = False
    flow_connection_definition.partition = False
    language.add_element(flow_connection_definition)
    requirement_verification_membership = Concept(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-RequirementVerificationMembership', name=
        'RequirementVerificationMembership', key=
        'sysml-RequirementVerificationMembership')
    requirement_verification_membership.abstract = False
    requirement_verification_membership.partition = False
    language.add_element(requirement_verification_membership)
    requirement_constraint_membership = Concept(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-RequirementConstraintMembership',
        name='RequirementConstraintMembership', key=
        'sysml-RequirementConstraintMembership')
    requirement_constraint_membership.abstract = False
    requirement_constraint_membership.partition = False
    language.add_element(requirement_constraint_membership)
    requirement_constraint_kind = Enumeration(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-RequirementConstraintKind', name=
        'RequirementConstraintKind', key='sysml-RequirementConstraintKind')
    language.add_element(requirement_constraint_kind)
    include_use_case_usage = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IncludeUseCaseUsage', name='IncludeUseCaseUsage',
        key='sysml-IncludeUseCaseUsage')
    include_use_case_usage.abstract = False
    include_use_case_usage.partition = False
    language.add_element(include_use_case_usage)
    objective_membership = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-ObjectiveMembership', name='ObjectiveMembership', key=
        'sysml-ObjectiveMembership')
    objective_membership.abstract = False
    objective_membership.partition = False
    language.add_element(objective_membership)
    satisfy_requirement_usage = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-SatisfyRequirementUsage', name=
        'SatisfyRequirementUsage', key='sysml-SatisfyRequirementUsage')
    satisfy_requirement_usage.abstract = False
    satisfy_requirement_usage.partition = False
    language.add_element(satisfy_requirement_usage)
    i_assert_constraint_usage = Interface(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IAssertConstraintUsage', name=
        'IAssertConstraintUsage', key='sysml-IAssertConstraintUsage')
    language.add_element(i_assert_constraint_usage)
    subject_membership = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-SubjectMembership', name='SubjectMembership', key=
        'sysml-SubjectMembership')
    subject_membership.abstract = False
    subject_membership.partition = False
    language.add_element(subject_membership)
    stakeholder_membership = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-StakeholderMembership', name=
        'StakeholderMembership', key='sysml-StakeholderMembership')
    stakeholder_membership.abstract = False
    stakeholder_membership.partition = False
    language.add_element(stakeholder_membership)
    framed_concern_membership = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-FramedConcernMembership', name=
        'FramedConcernMembership', key='sysml-FramedConcernMembership')
    framed_concern_membership.abstract = False
    framed_concern_membership.partition = False
    language.add_element(framed_concern_membership)
    actor_membership = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ActorMembership', name='ActorMembership', key=
        'sysml-ActorMembership')
    actor_membership.abstract = False
    actor_membership.partition = False
    language.add_element(actor_membership)
    view_rendering_membership = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ViewRenderingMembership', name=
        'ViewRenderingMembership', key='sysml-ViewRenderingMembership')
    view_rendering_membership.abstract = False
    view_rendering_membership.partition = False
    language.add_element(view_rendering_membership)
    namespace_expose = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-NamespaceExpose', name='NamespaceExpose', key=
        'sysml-NamespaceExpose')
    namespace_expose.abstract = False
    namespace_expose.partition = False
    language.add_element(namespace_expose)
    i_expose = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IExpose', name='IExpose', key='sysml-IExpose')
    language.add_element(i_expose)
    membership_expose = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-MembershipExpose', name='MembershipExpose', key=
        'sysml-MembershipExpose')
    membership_expose.abstract = False
    membership_expose.partition = False
    language.add_element(membership_expose)
    binding_connector_as_usage = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-BindingConnectorAsUsage', name=
        'BindingConnectorAsUsage', key='sysml-BindingConnectorAsUsage')
    binding_connector_as_usage.abstract = False
    binding_connector_as_usage.partition = False
    language.add_element(binding_connector_as_usage)
    succession_as_usage = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-SuccessionAsUsage', name='SuccessionAsUsage', key=
        'sysml-SuccessionAsUsage')
    succession_as_usage.abstract = False
    succession_as_usage.partition = False
    language.add_element(succession_as_usage)
    fork_node = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ForkNode', name='ForkNode', key='sysml-ForkNode')
    fork_node.abstract = False
    fork_node.partition = False
    language.add_element(fork_node)
    control_node = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ControlNode', name='ControlNode', key='sysml-ControlNode')
    control_node.abstract = True
    control_node.partition = False
    language.add_element(control_node)
    join_node = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-JoinNode', name='JoinNode', key='sysml-JoinNode')
    join_node.abstract = False
    join_node.partition = False
    language.add_element(join_node)
    send_action_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-SendActionUsage', name='SendActionUsage', key=
        'sysml-SendActionUsage')
    send_action_usage.abstract = False
    send_action_usage.partition = False
    language.add_element(send_action_usage)
    decision_node = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-DecisionNode', name='DecisionNode', key='sysml-DecisionNode')
    decision_node.abstract = False
    decision_node.partition = False
    language.add_element(decision_node)
    merge_node = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-MergeNode', name='MergeNode', key='sysml-MergeNode')
    merge_node.abstract = False
    merge_node.partition = False
    language.add_element(merge_node)
    loop_action_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-LoopActionUsage', name='LoopActionUsage', key=
        'sysml-LoopActionUsage')
    loop_action_usage.abstract = True
    loop_action_usage.partition = False
    language.add_element(loop_action_usage)
    trigger_invocation_expression = Concept(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-TriggerInvocationExpression', name=
        'TriggerInvocationExpression', key='sysml-TriggerInvocationExpression')
    trigger_invocation_expression.abstract = False
    trigger_invocation_expression.partition = False
    language.add_element(trigger_invocation_expression)
    trigger_kind = Enumeration(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-TriggerKind', name='TriggerKind', key='sysml-TriggerKind')
    language.add_element(trigger_kind)
    assignment_action_usage = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-AssignmentActionUsage', name=
        'AssignmentActionUsage', key='sysml-AssignmentActionUsage')
    assignment_action_usage.abstract = False
    assignment_action_usage.partition = False
    language.add_element(assignment_action_usage)
    for_loop_action_usage = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-ForLoopActionUsage', name='ForLoopActionUsage', key=
        'sysml-ForLoopActionUsage')
    for_loop_action_usage.abstract = False
    for_loop_action_usage.partition = False
    language.add_element(for_loop_action_usage)
    if_action_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-IfActionUsage', name='IfActionUsage', key='sysml-IfActionUsage')
    if_action_usage.abstract = False
    if_action_usage.partition = False
    language.add_element(if_action_usage)
    while_loop_action_usage = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-WhileLoopActionUsage', name=
        'WhileLoopActionUsage', key='sysml-WhileLoopActionUsage')
    while_loop_action_usage.abstract = False
    while_loop_action_usage.partition = False
    language.add_element(while_loop_action_usage)
    terminate_action_usage = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-TerminateActionUsage', name=
        'TerminateActionUsage', key='sysml-TerminateActionUsage')
    terminate_action_usage.abstract = False
    terminate_action_usage.partition = False
    language.add_element(terminate_action_usage)
    metadata_definition = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-MetadataDefinition', name='MetadataDefinition', key=
        'sysml-MetadataDefinition')
    metadata_definition.abstract = False
    metadata_definition.partition = False
    language.add_element(metadata_definition)
    alias_ids_container = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-AliasIdsContainer', name='AliasIdsContainer', key=
        'sysml-AliasIdsContainer')
    alias_ids_container.abstract = False
    alias_ids_container.partition = False
    language.add_element(alias_ids_container)
    text_container = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-TextContainer', name='TextContainer', key='sysml-TextContainer')
    text_container.abstract = False
    text_container.partition = False
    language.add_element(text_container)
    featuring = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Featuring', name='Featuring', key='sysml-Featuring')
    featuring.abstract = False
    featuring.partition = False
    language.add_element(featuring)
    relationship = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Relationship', name='Relationship', key='sysml-Relationship')
    relationship.abstract = False
    relationship.partition = False
    language.add_element(relationship)
    element = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Element', name='Element', key='sysml-Element')
    element.abstract = False
    element.partition = False
    language.add_element(element)
    annotating_element = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-AnnotatingElement', name='AnnotatingElement', key=
        'sysml-AnnotatingElement')
    annotating_element.abstract = False
    annotating_element.partition = False
    language.add_element(annotating_element)
    step = Concept(lion_web_version=LionWebVersion.V2023_1, id='sysml-Step',
        name='Step', key='sysml-Step')
    step.abstract = False
    step.partition = False
    language.add_element(step)
    feature = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Feature', name='Feature', key='sysml-Feature')
    feature.abstract = False
    feature.partition = False
    language.add_element(feature)
    type = Concept(lion_web_version=LionWebVersion.V2023_1, id='sysml-Type',
        name='Type', key='sysml-Type')
    type.abstract = False
    type.partition = False
    language.add_element(type)
    namespace = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Namespace', name='Namespace', key='sysml-Namespace')
    namespace.abstract = False
    namespace.partition = False
    language.add_element(namespace)
    behavior = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Behavior', name='Behavior', key='sysml-Behavior')
    behavior.abstract = False
    behavior.partition = False
    language.add_element(behavior)
    class_ = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Class', name='Class', key='sysml-Class')
    class_.abstract = False
    class_.partition = False
    language.add_element(class_)
    classifier = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Classifier', name='Classifier', key='sysml-Classifier')
    classifier.abstract = False
    classifier.partition = False
    language.add_element(classifier)
    succession = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Succession', name='Succession', key='sysml-Succession')
    succession.abstract = False
    succession.partition = False
    language.add_element(succession)
    connector = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Connector', name='Connector', key='sysml-Connector')
    connector.abstract = False
    connector.partition = False
    language.add_element(connector)
    structure = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Structure', name='Structure', key='sysml-Structure')
    structure.abstract = False
    structure.partition = False
    language.add_element(structure)
    part_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-PartUsage', name='PartUsage', key='sysml-PartUsage')
    part_usage.abstract = False
    part_usage.partition = False
    language.add_element(part_usage)
    item_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ItemUsage', name='ItemUsage', key='sysml-ItemUsage')
    item_usage.abstract = False
    item_usage.partition = False
    language.add_element(item_usage)
    occurrence_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-OccurrenceUsage', name='OccurrenceUsage', key=
        'sysml-OccurrenceUsage')
    occurrence_usage.abstract = False
    occurrence_usage.partition = False
    language.add_element(occurrence_usage)
    usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Usage', name='Usage', key='sysml-Usage')
    usage.abstract = False
    usage.partition = False
    language.add_element(usage)
    data_type = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-DataType', name='DataType', key='sysml-DataType')
    data_type.abstract = False
    data_type.partition = False
    language.add_element(data_type)
    action_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ActionUsage', name='ActionUsage', key='sysml-ActionUsage')
    action_usage.abstract = False
    action_usage.partition = False
    language.add_element(action_usage)
    item_flow = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ItemFlow', name='ItemFlow', key='sysml-ItemFlow')
    item_flow.abstract = False
    item_flow.partition = False
    language.add_element(item_flow)
    association_structure = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-AssociationStructure', name='AssociationStructure', key=
        'sysml-AssociationStructure')
    association_structure.abstract = False
    association_structure.partition = False
    language.add_element(association_structure)
    association = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Association', name='Association', key='sysml-Association')
    association.abstract = False
    association.partition = False
    language.add_element(association)
    predicate = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Predicate', name='Predicate', key='sysml-Predicate')
    predicate.abstract = False
    predicate.partition = False
    language.add_element(predicate)
    function = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Function', name='Function', key='sysml-Function')
    function.abstract = False
    function.partition = False
    language.add_element(function)
    perform_action_usage = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-PerformActionUsage', name='PerformActionUsage', key=
        'sysml-PerformActionUsage')
    perform_action_usage.abstract = False
    perform_action_usage.partition = False
    language.add_element(perform_action_usage)
    event_occurrence_usage = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-EventOccurrenceUsage', name=
        'EventOccurrenceUsage', key='sysml-EventOccurrenceUsage')
    event_occurrence_usage.abstract = False
    event_occurrence_usage.partition = False
    language.add_element(event_occurrence_usage)
    succession_item_flow = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-SuccessionItemFlow', name='SuccessionItemFlow', key=
        'sysml-SuccessionItemFlow')
    succession_item_flow.abstract = False
    succession_item_flow.partition = False
    language.add_element(succession_item_flow)
    interaction = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Interaction', name='Interaction', key='sysml-Interaction')
    interaction.abstract = False
    interaction.partition = False
    language.add_element(interaction)
    assert_constraint_usage = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-AssertConstraintUsage', name=
        'AssertConstraintUsage', key='sysml-AssertConstraintUsage')
    assert_constraint_usage.abstract = False
    assert_constraint_usage.partition = False
    language.add_element(assert_constraint_usage)
    constraint_usage = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-ConstraintUsage', name='ConstraintUsage', key=
        'sysml-ConstraintUsage')
    constraint_usage.abstract = False
    constraint_usage.partition = False
    language.add_element(constraint_usage)
    boolean_expression = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-BooleanExpression', name='BooleanExpression', key=
        'sysml-BooleanExpression')
    boolean_expression.abstract = False
    boolean_expression.partition = False
    language.add_element(boolean_expression)
    expression = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Expression', name='Expression', key='sysml-Expression')
    expression.abstract = False
    expression.partition = False
    language.add_element(expression)
    invariant = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Invariant', name='Invariant', key='sysml-Invariant')
    invariant.abstract = False
    invariant.partition = False
    language.add_element(invariant)
    expose = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Expose', name='Expose', key='sysml-Expose')
    expose.abstract = False
    expose.partition = False
    language.add_element(expose)
    import_ = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Import', name='Import', key='sysml-Import')
    import_.abstract = False
    import_.partition = False
    language.add_element(import_)
    binding_connector = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-BindingConnector', name='BindingConnector', key=
        'sysml-BindingConnector')
    binding_connector.abstract = False
    binding_connector.partition = False
    language.add_element(binding_connector)
    metaclass = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-Metaclass', name='Metaclass', key='sysml-Metaclass')
    metaclass.abstract = False
    metaclass.partition = False
    language.add_element(metaclass)
    subclassification.set_extended_concept(specialization)
    subclassification.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-Subclassification-superclassifier', name=
        'superclassifier', key='sysml-Subclassification-superclassifier',
        type=i_classifier, multiple=False, optional=False))
    subclassification.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-Subclassification-owningClassifier', name=
        'owningClassifier', key='sysml-Subclassification-owningClassifier',
        type=i_classifier, multiple=False, optional=True))
    subclassification.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-Subclassification-subclassifier', name=
        'subclassifier', key='sysml-Subclassification-subclassifier', type=
        i_classifier, multiple=False, optional=False))
    specialization.add_implemented_interface(i_relationship)
    specialization.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Specialization-owningType', name='owningType',
        key='sysml-Specialization-owningType', type=i_type, multiple=False,
        optional=True))
    specialization.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Specialization-general', name='general', key=
        'sysml-Specialization-general', type=i_type, multiple=False,
        optional=False))
    specialization.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Specialization-specific', name='specific', key=
        'sysml-Specialization-specific', type=i_type, multiple=False,
        optional=False))
    i_relationship.add_extended_interface(i_element)
    i_relationship.add_feature(Containment(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IRelationship-ownedRelatedElement', name=
        'ownedRelatedElement', key=
        'sysml-IRelationship-ownedRelatedElement', type=i_element, multiple
        =True, optional=True))
    i_relationship.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IRelationship-owningRelatedElement', name=
        'owningRelatedElement', key=
        'sysml-IRelationship-owningRelatedElement', type=i_element,
        multiple=False, optional=True))
    i_relationship.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IRelationship-relatedElement', name=
        'relatedElement', key='sysml-IRelationship-relatedElement', type=
        i_element, multiple=True, optional=True))
    i_relationship.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IRelationship-target', name='target', key=
        'sysml-IRelationship-target', type=i_element, multiple=True,
        optional=True))
    i_relationship.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IRelationship-source', name='source', key=
        'sysml-IRelationship-source', type=i_element, multiple=True,
        optional=True))
    i_relationship.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IRelationship-isImplied', name='isImplied', key=
        'sysml-IRelationship-isImplied', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-owningMembership', name='owningMembership', key=
        'sysml-IElement-owningMembership', type=owning_membership, multiple
        =False, optional=True))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-owningNamespace', name='owningNamespace', key=
        'sysml-IElement-owningNamespace', type=i_namespace, multiple=False,
        optional=True))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-owningRelationship', name='owningRelationship',
        key='sysml-IElement-owningRelationship', type=i_relationship,
        multiple=False, optional=True))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-elementId', name='elementId', key=
        'sysml-IElement-elementId', type=get_types_language().
        get_primitive_type_by_name('String')))
    i_element.add_feature(Containment(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IElement-ownedRelationship', name=
        'ownedRelationship', key='sysml-IElement-ownedRelationship', type=
        i_relationship, multiple=True, optional=True))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-owner', name='owner', key='sysml-IElement-owner',
        type=i_element, multiple=False, optional=True))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-ownedElement', name='ownedElement', key=
        'sysml-IElement-ownedElement', type=i_element, multiple=True,
        optional=True))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-documentation', name='documentation', key=
        'sysml-IElement-documentation', type=documentation, multiple=True,
        optional=True))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-ownedAnnotation', name='ownedAnnotation', key=
        'sysml-IElement-ownedAnnotation', type=annotation, multiple=True,
        optional=True))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-textualRepresentation', name=
        'textualRepresentation', key='sysml-IElement-textualRepresentation',
        type=textual_representation, multiple=True, optional=True))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-declaredShortName', name='declaredShortName',
        key='sysml-IElement-declaredShortName', type=get_types_language().
        get_primitive_type_by_name('String')))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-declaredName', name='declaredName', key=
        'sysml-IElement-declaredName', type=get_types_language().
        get_primitive_type_by_name('String')))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-shortName', name='shortName', key=
        'sysml-IElement-shortName', type=get_types_language().
        get_primitive_type_by_name('String')))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-name', name='name', key='sysml-IElement-name',
        type=get_types_language().get_primitive_type_by_name('String')))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-qualifiedName', name='qualifiedName', key=
        'sysml-IElement-qualifiedName', type=get_types_language().
        get_primitive_type_by_name('String')))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-isImpliedIncluded', name='isImpliedIncluded',
        key='sysml-IElement-isImpliedIncluded', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IElement-isLibraryElement', name='isLibraryElement', key=
        'sysml-IElement-isLibraryElement', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_element.add_feature(Containment(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IElement-aliasIdsContainer', name=
        'aliasIdsContainer', key='sysml-IElement-aliasIdsContainer', type=
        alias_ids_container, multiple=True, optional=True))
    owning_membership.set_extended_concept(membership)
    owning_membership.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-OwningMembership-ownedMemberElementId', name=
        'ownedMemberElementId', key=
        'sysml-OwningMembership-ownedMemberElementId', type=
        get_types_language().get_primitive_type_by_name('String')))
    owning_membership.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-OwningMembership-ownedMemberShortName', name=
        'ownedMemberShortName', key=
        'sysml-OwningMembership-ownedMemberShortName', type=
        get_types_language().get_primitive_type_by_name('String')))
    owning_membership.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-OwningMembership-ownedMemberName', name=
        'ownedMemberName', key='sysml-OwningMembership-ownedMemberName',
        type=get_types_language().get_primitive_type_by_name('String')))
    owning_membership.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-OwningMembership-ownedMemberElement', name=
        'ownedMemberElement', key=
        'sysml-OwningMembership-ownedMemberElement', type=i_element,
        multiple=False, optional=False))
    membership.add_implemented_interface(i_relationship)
    membership.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-Membership-memberElementId', name='memberElementId', key=
        'sysml-Membership-memberElementId', type=get_types_language().
        get_primitive_type_by_name('String')))
    membership.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Membership-membershipOwningNamespace', name=
        'membershipOwningNamespace', key=
        'sysml-Membership-membershipOwningNamespace', type=i_namespace,
        multiple=False, optional=False))
    membership.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-Membership-memberShortName', name='memberShortName', key=
        'sysml-Membership-memberShortName', type=get_types_language().
        get_primitive_type_by_name('String')))
    membership.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Membership-memberElement', name='memberElement',
        key='sysml-Membership-memberElement', type=i_element, multiple=
        False, optional=False))
    membership.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-Membership-memberName', name='memberName', key=
        'sysml-Membership-memberName', type=get_types_language().
        get_primitive_type_by_name('String')))
    membership.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-Membership-visibility', name='visibility', key=
        'sysml-Membership-visibility', type=visibility_kind))
    i_namespace.add_extended_interface(i_element)
    i_namespace.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-INamespace-membership', name='membership', key=
        'sysml-INamespace-membership', type=membership, multiple=True,
        optional=True))
    i_namespace.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-INamespace-ownedImport', name='ownedImport', key
        ='sysml-INamespace-ownedImport', type=i_import, multiple=True,
        optional=True))
    i_namespace.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-INamespace-member', name='member', key=
        'sysml-INamespace-member', type=i_element, multiple=True, optional=
        True))
    i_namespace.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-INamespace-ownedMember', name='ownedMember', key
        ='sysml-INamespace-ownedMember', type=i_element, multiple=True,
        optional=True))
    i_namespace.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-INamespace-importedMembership', name=
        'importedMembership', key='sysml-INamespace-importedMembership',
        type=membership, multiple=True, optional=True))
    i_namespace.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-INamespace-ownedMembership', name=
        'ownedMembership', key='sysml-INamespace-ownedMembership', type=
        membership, multiple=True, optional=True))
    i_import.add_extended_interface(i_relationship)
    i_import.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IImport-visibility', name='visibility', key=
        'sysml-IImport-visibility', type=visibility_kind))
    i_import.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IImport-isRecursive', name='isRecursive', key=
        'sysml-IImport-isRecursive', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_import.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IImport-isImportAll', name='isImportAll', key=
        'sysml-IImport-isImportAll', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_import.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IImport-importedElement', name='importedElement', key=
        'sysml-IImport-importedElement', type=i_element, multiple=False,
        optional=False))
    i_import.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IImport-importOwningNamespace', name=
        'importOwningNamespace', key='sysml-IImport-importOwningNamespace',
        type=i_namespace, multiple=False, optional=False))
    documentation.set_extended_concept(comment)
    documentation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Documentation-documentedElement', name=
        'documentedElement', key='sysml-Documentation-documentedElement',
        type=i_element, multiple=False, optional=False))
    comment.add_implemented_interface(i_annotating_element)
    comment.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-Comment-locale', name='locale', key=
        'sysml-Comment-locale', type=get_types_language().
        get_primitive_type_by_name('String')))
    comment.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-Comment-body', name='body', key='sysml-Comment-body',
        type=get_types_language().get_primitive_type_by_name('String')))
    i_annotating_element.add_extended_interface(i_element)
    i_annotating_element.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-IAnnotatingElement-annotatedElement', name=
        'annotatedElement', key='sysml-IAnnotatingElement-annotatedElement',
        type=i_element, multiple=True, optional=False))
    i_annotating_element.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-IAnnotatingElement-ownedAnnotatingRelationship', name=
        'ownedAnnotatingRelationship', key=
        'sysml-IAnnotatingElement-ownedAnnotatingRelationship', type=
        annotation, multiple=True, optional=True))
    i_annotating_element.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-IAnnotatingElement-annotation',
        name='annotation', key='sysml-IAnnotatingElement-annotation', type=
        annotation, multiple=True, optional=True))
    i_annotating_element.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-IAnnotatingElement-owningAnnotatingRelationship', name=
        'owningAnnotatingRelationship', key=
        'sysml-IAnnotatingElement-owningAnnotatingRelationship', type=
        annotation, multiple=False, optional=True))
    annotation.add_implemented_interface(i_relationship)
    annotation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Annotation-annotatingElement', name=
        'annotatingElement', key='sysml-Annotation-annotatingElement', type
        =i_annotating_element, multiple=False, optional=False))
    annotation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Annotation-annotatedElement', name=
        'annotatedElement', key='sysml-Annotation-annotatedElement', type=
        i_element, multiple=False, optional=False))
    annotation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Annotation-owningAnnotatedElement', name=
        'owningAnnotatedElement', key=
        'sysml-Annotation-owningAnnotatedElement', type=i_element, multiple
        =False, optional=True))
    annotation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Annotation-ownedAnnotatingElement', name=
        'ownedAnnotatingElement', key=
        'sysml-Annotation-ownedAnnotatingElement', type=
        i_annotating_element, multiple=False, optional=True))
    annotation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Annotation-owningAnnotatingElement', name=
        'owningAnnotatingElement', key=
        'sysml-Annotation-owningAnnotatingElement', type=
        i_annotating_element, multiple=False, optional=True))
    textual_representation.add_implemented_interface(i_annotating_element)
    textual_representation.add_feature(Property(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-TextualRepresentation-language',
        name='language', key='sysml-TextualRepresentation-language', type=
        get_types_language().get_primitive_type_by_name('String')))
    textual_representation.add_feature(Property(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-TextualRepresentation-body', name
        ='body', key='sysml-TextualRepresentation-body', type=
        get_types_language().get_primitive_type_by_name('String')))
    textual_representation.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-TextualRepresentation-representedElement', name=
        'representedElement', key=
        'sysml-TextualRepresentation-representedElement', type=i_element,
        multiple=False, optional=False))
    i_type.add_extended_interface(i_namespace)
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-ownedFeatureMembership', name=
        'ownedFeatureMembership', key='sysml-IType-ownedFeatureMembership',
        type=feature_membership, multiple=True, optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-ownedFeature', name='ownedFeature', key=
        'sysml-IType-ownedFeature', type=i_feature, multiple=True, optional
        =True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-ownedEndFeature', name='ownedEndFeature', key=
        'sysml-IType-ownedEndFeature', type=i_feature, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-feature', name='feature', key='sysml-IType-feature',
        type=i_feature, multiple=True, optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-input', name='input', key='sysml-IType-input', type
        =i_feature, multiple=True, optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-output', name='output', key='sysml-IType-output',
        type=i_feature, multiple=True, optional=True))
    i_type.add_feature(Property(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-IType-isAbstract', name='isAbstract', key=
        'sysml-IType-isAbstract', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-inheritedMembership', name='inheritedMembership',
        key='sysml-IType-inheritedMembership', type=membership, multiple=
        True, optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-endFeature', name='endFeature', key=
        'sysml-IType-endFeature', type=i_feature, multiple=True, optional=True)
        )
    i_type.add_feature(Property(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-IType-isSufficient', name='isSufficient', key=
        'sysml-IType-isSufficient', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-ownedConjugator', name='ownedConjugator', key=
        'sysml-IType-ownedConjugator', type=conjugation, multiple=False,
        optional=True))
    i_type.add_feature(Property(lion_web_version=LionWebVersion.V2023_1, id
        ='sysml-IType-isConjugated', name='isConjugated', key=
        'sysml-IType-isConjugated', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-inheritedFeature', name='inheritedFeature', key=
        'sysml-IType-inheritedFeature', type=i_feature, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-multiplicity', name='multiplicity', key=
        'sysml-IType-multiplicity', type=multiplicity, multiple=False,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-unioningType', name='unioningType', key=
        'sysml-IType-unioningType', type=i_type, multiple=True, optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-ownedIntersecting', name='ownedIntersecting', key=
        'sysml-IType-ownedIntersecting', type=intersecting, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-intersectingType', name='intersectingType', key=
        'sysml-IType-intersectingType', type=i_type, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-ownedUnioning', name='ownedUnioning', key=
        'sysml-IType-ownedUnioning', type=unioning, multiple=True, optional
        =True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-ownedDisjoining', name='ownedDisjoining', key=
        'sysml-IType-ownedDisjoining', type=disjoining, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-featureMembership', name='featureMembership', key=
        'sysml-IType-featureMembership', type=feature_membership, multiple=
        True, optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-differencingType', name='differencingType', key=
        'sysml-IType-differencingType', type=i_type, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-ownedDifferencing', name='ownedDifferencing', key=
        'sysml-IType-ownedDifferencing', type=differencing, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-directedFeature', name='directedFeature', key=
        'sysml-IType-directedFeature', type=i_feature, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IType-ownedSpecialization', name='ownedSpecialization',
        key='sysml-IType-ownedSpecialization', type=specialization,
        multiple=True, optional=True))
    feature_membership.set_extended_concept(owning_membership)
    feature_membership.add_implemented_interface(i_featuring)
    feature_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-FeatureMembership-ownedMemberFeature', name=
        'ownedMemberFeature', key=
        'sysml-FeatureMembership-ownedMemberFeature', type=i_feature,
        multiple=False, optional=False))
    feature_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-FeatureMembership-owningType',
        name='owningType', key='sysml-FeatureMembership-owningType', type=
        i_type, multiple=False, optional=False))
    i_featuring.add_extended_interface(i_relationship)
    i_featuring.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IFeaturing-type', name='type', key=
        'sysml-IFeaturing-type', type=i_type, multiple=False, optional=False))
    i_featuring.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IFeaturing-feature', name='feature', key=
        'sysml-IFeaturing-feature', type=i_feature, multiple=False,
        optional=False))
    i_feature.add_extended_interface(i_type)
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-owningType', name='owningType', key=
        'sysml-IFeature-owningType', type=i_type, multiple=False, optional=
        True))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-isUnique', name='isUnique', key=
        'sysml-IFeature-isUnique', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-isOrdered', name='isOrdered', key=
        'sysml-IFeature-isOrdered', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-type', name='type', key='sysml-IFeature-type',
        type=i_type, multiple=True, optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-ownedRedefinition', name='ownedRedefinition',
        key='sysml-IFeature-ownedRedefinition', type=redefinition, multiple
        =True, optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-ownedSubsetting', name='ownedSubsetting', key=
        'sysml-IFeature-ownedSubsetting', type=subsetting, multiple=True,
        optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-owningFeatureMembership', name=
        'owningFeatureMembership', key=
        'sysml-IFeature-owningFeatureMembership', type=feature_membership,
        multiple=False, optional=True))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-isComposite', name='isComposite', key=
        'sysml-IFeature-isComposite', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-isEnd', name='isEnd', key='sysml-IFeature-isEnd',
        type=get_types_language().get_primitive_type_by_name('Boolean')))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-endOwningType', name='endOwningType', key=
        'sysml-IFeature-endOwningType', type=i_type, multiple=False,
        optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-ownedTyping', name='ownedTyping', key=
        'sysml-IFeature-ownedTyping', type=feature_typing, multiple=True,
        optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-featuringType', name='featuringType', key=
        'sysml-IFeature-featuringType', type=i_type, multiple=True,
        optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-ownedTypeFeaturing', name='ownedTypeFeaturing',
        key='sysml-IFeature-ownedTypeFeaturing', type=type_featuring,
        multiple=True, optional=True))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-isDerived', name='isDerived', key=
        'sysml-IFeature-isDerived', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-chainingFeature', name='chainingFeature', key=
        'sysml-IFeature-chainingFeature', type=i_feature, multiple=True,
        optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-ownedFeatureInverting', name=
        'ownedFeatureInverting', key='sysml-IFeature-ownedFeatureInverting',
        type=feature_inverting, multiple=True, optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-ownedFeatureChaining', name=
        'ownedFeatureChaining', key='sysml-IFeature-ownedFeatureChaining',
        type=feature_chaining, multiple=True, optional=True))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-isReadOnly', name='isReadOnly', key=
        'sysml-IFeature-isReadOnly', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-isPortion', name='isPortion', key=
        'sysml-IFeature-isPortion', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-direction', name='direction', key=
        'sysml-IFeature-direction', type=feature_direction_kind))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-ownedReferenceSubsetting', name=
        'ownedReferenceSubsetting', key=
        'sysml-IFeature-ownedReferenceSubsetting', type=
        reference_subsetting, multiple=False, optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-crossFeature', name='crossFeature', key=
        'sysml-IFeature-crossFeature', type=i_feature, multiple=False,
        optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-ownedCrossSubsetting', name=
        'ownedCrossSubsetting', key='sysml-IFeature-ownedCrossSubsetting',
        type=cross_subsetting, multiple=False, optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-featureTarget', name='featureTarget', key=
        'sysml-IFeature-featureTarget', type=i_feature, multiple=False,
        optional=False))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFeature-isNonunique', name='isNonunique', key=
        'sysml-IFeature-isNonunique', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    redefinition.set_extended_concept(subsetting)
    redefinition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Redefinition-redefiningFeature', name=
        'redefiningFeature', key='sysml-Redefinition-redefiningFeature',
        type=i_feature, multiple=False, optional=False))
    redefinition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Redefinition-redefinedFeature', name=
        'redefinedFeature', key='sysml-Redefinition-redefinedFeature', type
        =i_feature, multiple=False, optional=False))
    subsetting.set_extended_concept(specialization)
    subsetting.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Subsetting-subsettedFeature', name=
        'subsettedFeature', key='sysml-Subsetting-subsettedFeature', type=
        i_feature, multiple=False, optional=False))
    subsetting.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Subsetting-subsettingFeature', name=
        'subsettingFeature', key='sysml-Subsetting-subsettingFeature', type
        =i_feature, multiple=False, optional=False))
    subsetting.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Subsetting-owningFeature', name='owningFeature',
        key='sysml-Subsetting-owningFeature', type=i_feature, multiple=
        False, optional=True))
    feature_typing.set_extended_concept(specialization)
    feature_typing.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-FeatureTyping-typedFeature', name='typedFeature',
        key='sysml-FeatureTyping-typedFeature', type=i_feature, multiple=
        False, optional=False))
    feature_typing.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-FeatureTyping-type', name='type', key=
        'sysml-FeatureTyping-type', type=i_type, multiple=False, optional=
        False))
    feature_typing.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-FeatureTyping-owningFeature', name=
        'owningFeature', key='sysml-FeatureTyping-owningFeature', type=
        i_feature, multiple=False, optional=True))
    type_featuring.add_implemented_interface(i_featuring)
    type_featuring.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-TypeFeaturing-featureOfType', name=
        'featureOfType', key='sysml-TypeFeaturing-featureOfType', type=
        i_feature, multiple=False, optional=False))
    type_featuring.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-TypeFeaturing-featuringType', name=
        'featuringType', key='sysml-TypeFeaturing-featuringType', type=
        i_type, multiple=False, optional=False))
    type_featuring.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-TypeFeaturing-owningFeatureOfType', name=
        'owningFeatureOfType', key=
        'sysml-TypeFeaturing-owningFeatureOfType', type=i_feature, multiple
        =False, optional=True))
    feature_inverting.add_implemented_interface(i_relationship)
    feature_inverting.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-FeatureInverting-featureInverted', name=
        'featureInverted', key='sysml-FeatureInverting-featureInverted',
        type=i_feature, multiple=False, optional=False))
    feature_inverting.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-FeatureInverting-invertingFeature', name=
        'invertingFeature', key='sysml-FeatureInverting-invertingFeature',
        type=i_feature, multiple=False, optional=False))
    feature_inverting.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-FeatureInverting-owningFeature', name=
        'owningFeature', key='sysml-FeatureInverting-owningFeature', type=
        i_feature, multiple=False, optional=True))
    feature_chaining.add_implemented_interface(i_relationship)
    feature_chaining.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-FeatureChaining-chainingFeature', name=
        'chainingFeature', key='sysml-FeatureChaining-chainingFeature',
        type=i_feature, multiple=False, optional=False))
    feature_chaining.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-FeatureChaining-featureChained', name=
        'featureChained', key='sysml-FeatureChaining-featureChained', type=
        i_feature, multiple=False, optional=False))
    reference_subsetting.set_extended_concept(subsetting)
    reference_subsetting.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-ReferenceSubsetting-referencedFeature', name=
        'referencedFeature', key=
        'sysml-ReferenceSubsetting-referencedFeature', type=i_feature,
        multiple=False, optional=False))
    reference_subsetting.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-ReferenceSubsetting-referencingFeature', name=
        'referencingFeature', key=
        'sysml-ReferenceSubsetting-referencingFeature', type=i_feature,
        multiple=False, optional=False))
    cross_subsetting.set_extended_concept(subsetting)
    cross_subsetting.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-CrossSubsetting-crossedFeature', name=
        'crossedFeature', key='sysml-CrossSubsetting-crossedFeature', type=
        i_feature, multiple=False, optional=False))
    cross_subsetting.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-CrossSubsetting-crossingFeature', name=
        'crossingFeature', key='sysml-CrossSubsetting-crossingFeature',
        type=i_feature, multiple=False, optional=False))
    conjugation.add_implemented_interface(i_relationship)
    conjugation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Conjugation-originalType', name='originalType',
        key='sysml-Conjugation-originalType', type=i_type, multiple=False,
        optional=False))
    conjugation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Conjugation-conjugatedType', name=
        'conjugatedType', key='sysml-Conjugation-conjugatedType', type=
        i_type, multiple=False, optional=False))
    conjugation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Conjugation-owningType', name='owningType', key=
        'sysml-Conjugation-owningType', type=i_type, multiple=False,
        optional=True))
    multiplicity.add_implemented_interface(i_feature)
    intersecting.add_implemented_interface(i_relationship)
    intersecting.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Intersecting-intersectingType', name=
        'intersectingType', key='sysml-Intersecting-intersectingType', type
        =i_type, multiple=False, optional=False))
    intersecting.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Intersecting-typeIntersected', name=
        'typeIntersected', key='sysml-Intersecting-typeIntersected', type=
        i_type, multiple=False, optional=False))
    unioning.add_implemented_interface(i_relationship)
    unioning.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-Unioning-unioningType', name='unioningType', key=
        'sysml-Unioning-unioningType', type=i_type, multiple=False,
        optional=False))
    unioning.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-Unioning-typeUnioned', name='typeUnioned', key=
        'sysml-Unioning-typeUnioned', type=i_type, multiple=False, optional
        =False))
    disjoining.add_implemented_interface(i_relationship)
    disjoining.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Disjoining-typeDisjoined', name='typeDisjoined',
        key='sysml-Disjoining-typeDisjoined', type=i_type, multiple=False,
        optional=False))
    disjoining.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Disjoining-disjoiningType', name=
        'disjoiningType', key='sysml-Disjoining-disjoiningType', type=
        i_type, multiple=False, optional=False))
    disjoining.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Disjoining-owningType', name='owningType', key=
        'sysml-Disjoining-owningType', type=i_type, multiple=False,
        optional=True))
    differencing.add_implemented_interface(i_relationship)
    differencing.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Differencing-differencingType', name=
        'differencingType', key='sysml-Differencing-differencingType', type
        =i_type, multiple=False, optional=False))
    differencing.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Differencing-typeDifferenced', name=
        'typeDifferenced', key='sysml-Differencing-typeDifferenced', type=
        i_type, multiple=False, optional=False))
    i_classifier.add_extended_interface(i_type)
    i_classifier.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IClassifier-ownedSubclassification', name=
        'ownedSubclassification', key=
        'sysml-IClassifier-ownedSubclassification', type=subclassification,
        multiple=True, optional=True))
    end_feature_membership.set_extended_concept(feature_membership)
    i_expression.add_extended_interface(i_step)
    i_expression.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IExpression-function', name='function', key=
        'sysml-IExpression-function', type=i_function, multiple=False,
        optional=True))
    i_expression.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IExpression-result', name='result', key=
        'sysml-IExpression-result', type=i_feature, multiple=False,
        optional=False))
    i_expression.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IExpression-isModelLevelEvaluable', name=
        'isModelLevelEvaluable', key=
        'sysml-IExpression-isModelLevelEvaluable', type=get_types_language(
        ).get_primitive_type_by_name('Boolean')))
    i_step.add_extended_interface(i_feature)
    i_step.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IStep-behavior', name='behavior', key=
        'sysml-IStep-behavior', type=i_behavior, multiple=True, optional=True))
    i_step.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IStep-parameter', name='parameter', key=
        'sysml-IStep-parameter', type=i_feature, multiple=True, optional=True))
    i_behavior.add_extended_interface(i_class)
    i_behavior.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IBehavior-step', name='step', key=
        'sysml-IBehavior-step', type=i_step, multiple=True, optional=True))
    i_behavior.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IBehavior-parameter', name='parameter', key=
        'sysml-IBehavior-parameter', type=i_feature, multiple=True,
        optional=True))
    i_class.add_extended_interface(i_classifier)
    i_function.add_extended_interface(i_behavior)
    i_function.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IFunction-expression', name='expression', key=
        'sysml-IFunction-expression', type=i_expression, multiple=True,
        optional=True))
    i_function.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IFunction-result', name='result', key=
        'sysml-IFunction-result', type=i_feature, multiple=False, optional=
        False))
    i_function.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IFunction-isModelLevelEvaluable', name=
        'isModelLevelEvaluable', key=
        'sysml-IFunction-isModelLevelEvaluable', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    result_expression_membership.set_extended_concept(feature_membership)
    result_expression_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-ResultExpressionMembership-ownedResultExpression', name=
        'ownedResultExpression', key=
        'sysml-ResultExpressionMembership-ownedResultExpression', type=
        i_expression, multiple=False, optional=False))
    i_invariant.add_extended_interface(i_boolean_expression)
    i_invariant.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IInvariant-isNegated', name='isNegated', key=
        'sysml-IInvariant-isNegated', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_boolean_expression.add_extended_interface(i_expression)
    i_boolean_expression.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-IBooleanExpression-predicate',
        name='predicate', key='sysml-IBooleanExpression-predicate', type=
        i_predicate, multiple=False, optional=True))
    i_predicate.add_extended_interface(i_function)
    return_parameter_membership.set_extended_concept(parameter_membership)
    parameter_membership.set_extended_concept(feature_membership)
    parameter_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-ParameterMembership-ownedMemberParameter', name=
        'ownedMemberParameter', key=
        'sysml-ParameterMembership-ownedMemberParameter', type=i_feature,
        multiple=False, optional=False))
    multiplicity_range.set_extended_concept(multiplicity)
    multiplicity_range.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-MultiplicityRange-lowerBound',
        name='lowerBound', key='sysml-MultiplicityRange-lowerBound', type=
        i_expression, multiple=False, optional=True))
    multiplicity_range.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-MultiplicityRange-upperBound',
        name='upperBound', key='sysml-MultiplicityRange-upperBound', type=
        i_expression, multiple=False, optional=False))
    multiplicity_range.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-MultiplicityRange-bound', name=
        'bound', key='sysml-MultiplicityRange-bound', type=i_expression,
        multiple=True, optional=False))
    i_structure.add_extended_interface(i_class)
    feature_value.set_extended_concept(owning_membership)
    feature_value.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-FeatureValue-featureWithValue', name=
        'featureWithValue', key='sysml-FeatureValue-featureWithValue', type
        =i_feature, multiple=False, optional=False))
    feature_value.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-FeatureValue-value', name='value', key=
        'sysml-FeatureValue-value', type=i_expression, multiple=False,
        optional=False))
    feature_value.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-FeatureValue-isInitial', name='isInitial', key=
        'sysml-FeatureValue-isInitial', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    feature_value.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-FeatureValue-isDefault', name='isDefault', key=
        'sysml-FeatureValue-isDefault', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_metaclass.add_extended_interface(i_structure)
    metadata_feature.add_implemented_interface(i_feature)
    metadata_feature.add_implemented_interface(i_annotating_element)
    metadata_feature.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-MetadataFeature-metaclass', name='metaclass',
        key='sysml-MetadataFeature-metaclass', type=i_metaclass, multiple=
        False, optional=True))
    i_item_flow.add_extended_interface(i_connector)
    i_item_flow.add_extended_interface(i_step)
    i_item_flow.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IItemFlow-itemType', name='itemType', key=
        'sysml-IItemFlow-itemType', type=i_classifier, multiple=True,
        optional=True))
    i_item_flow.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IItemFlow-targetInputFeature', name=
        'targetInputFeature', key='sysml-IItemFlow-targetInputFeature',
        type=i_feature, multiple=False, optional=True))
    i_item_flow.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IItemFlow-sourceOutputFeature', name=
        'sourceOutputFeature', key='sysml-IItemFlow-sourceOutputFeature',
        type=i_feature, multiple=False, optional=True))
    i_item_flow.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IItemFlow-itemFlowEnd', name='itemFlowEnd', key=
        'sysml-IItemFlow-itemFlowEnd', type=item_flow_end, multiple=True,
        optional=True))
    i_item_flow.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IItemFlow-itemFeature', name='itemFeature', key=
        'sysml-IItemFlow-itemFeature', type=item_feature, multiple=False,
        optional=True))
    i_item_flow.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IItemFlow-interaction', name='interaction', key=
        'sysml-IItemFlow-interaction', type=i_interaction, multiple=True,
        optional=True))
    i_connector.add_extended_interface(i_feature)
    i_connector.add_extended_interface(i_relationship)
    i_connector.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IConnector-relatedFeature', name=
        'relatedFeature', key='sysml-IConnector-relatedFeature', type=
        i_feature, multiple=True, optional=True))
    i_connector.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IConnector-association', name='association', key
        ='sysml-IConnector-association', type=i_association, multiple=True,
        optional=True))
    i_connector.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IConnector-connectorEnd', name='connectorEnd',
        key='sysml-IConnector-connectorEnd', type=i_feature, multiple=True,
        optional=True))
    i_connector.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IConnector-sourceFeature', name='sourceFeature',
        key='sysml-IConnector-sourceFeature', type=i_feature, multiple=
        False, optional=True))
    i_connector.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IConnector-targetFeature', name='targetFeature',
        key='sysml-IConnector-targetFeature', type=i_feature, multiple=True,
        optional=True))
    i_association.add_extended_interface(i_classifier)
    i_association.add_extended_interface(i_relationship)
    i_association.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IAssociation-relatedType', name='relatedType',
        key='sysml-IAssociation-relatedType', type=i_type, multiple=True,
        optional=True))
    i_association.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IAssociation-sourceType', name='sourceType', key
        ='sysml-IAssociation-sourceType', type=i_type, multiple=False,
        optional=True))
    i_association.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IAssociation-targetType', name='targetType', key
        ='sysml-IAssociation-targetType', type=i_type, multiple=True,
        optional=True))
    i_association.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IAssociation-associationEnd', name=
        'associationEnd', key='sysml-IAssociation-associationEnd', type=
        i_feature, multiple=True, optional=True))
    item_flow_end.add_implemented_interface(i_feature)
    item_feature.add_implemented_interface(i_feature)
    i_interaction.add_extended_interface(i_association)
    i_interaction.add_extended_interface(i_behavior)
    i_succession_item_flow.add_extended_interface(i_item_flow)
    i_succession_item_flow.add_extended_interface(i_succession)
    i_succession.add_extended_interface(i_connector)
    i_succession.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ISuccession-transitionStep', name=
        'transitionStep', key='sysml-ISuccession-transitionStep', type=
        i_step, multiple=False, optional=True))
    i_succession.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ISuccession-triggerStep', name='triggerStep',
        key='sysml-ISuccession-triggerStep', type=i_step, multiple=True,
        optional=True))
    i_succession.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ISuccession-effectStep', name='effectStep', key=
        'sysml-ISuccession-effectStep', type=i_step, multiple=True,
        optional=True))
    i_succession.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ISuccession-guardExpression', name=
        'guardExpression', key='sysml-ISuccession-guardExpression', type=
        i_expression, multiple=True, optional=True))
    element_filter_membership.set_extended_concept(owning_membership)
    element_filter_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-ElementFilterMembership-condition', name='condition', key=
        'sysml-ElementFilterMembership-condition', type=i_expression,
        multiple=False, optional=False))
    package.add_implemented_interface(i_namespace)
    package.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-Package-filterCondition', name='filterCondition', key=
        'sysml-Package-filterCondition', type=i_expression, multiple=True,
        optional=True))
    library_package.set_extended_concept(package)
    library_package.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-LibraryPackage-isStandard', name='isStandard',
        key='sysml-LibraryPackage-isStandard', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_data_type.add_extended_interface(i_classifier)
    feature_reference_expression.add_implemented_interface(i_expression)
    feature_reference_expression.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-FeatureReferenceExpression-referent', name='referent', key=
        'sysml-FeatureReferenceExpression-referent', type=i_feature,
        multiple=False, optional=False))
    metadata_access_expression.add_implemented_interface(i_expression)
    metadata_access_expression.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-MetadataAccessExpression-referencedElement', name=
        'referencedElement', key=
        'sysml-MetadataAccessExpression-referencedElement', type=i_element,
        multiple=False, optional=False))
    null_expression.add_implemented_interface(i_expression)
    index_expression.set_extended_concept(operator_expression)
    operator_expression.set_extended_concept(invocation_expression)
    operator_expression.add_feature(Property(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-OperatorExpression-operator',
        name='operator', key='sysml-OperatorExpression-operator', type=
        get_types_language().get_primitive_type_by_name('String')))
    invocation_expression.add_implemented_interface(i_expression)
    invocation_expression.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-InvocationExpression-argument',
        name='argument', key='sysml-InvocationExpression-argument', type=
        i_expression, multiple=True, optional=True))
    invocation_expression.add_feature(Containment(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-InvocationExpression-operand',
        name='operand', key='sysml-InvocationExpression-operand', type=
        i_expression, multiple=True, optional=True))
    collect_expression.set_extended_concept(operator_expression)
    literal_infinity.set_extended_concept(literal_expression)
    literal_expression.add_implemented_interface(i_expression)
    literal_integer.set_extended_concept(literal_expression)
    literal_integer.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-LiteralInteger-value', name='value', key=
        'sysml-LiteralInteger-value', type=get_types_language().
        get_primitive_type_by_name('Integer')))
    select_expression.set_extended_concept(operator_expression)
    literal_rational.set_extended_concept(literal_expression)
    literal_rational.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-LiteralRational-value', name='value', key=
        'sysml-LiteralRational-value', type=get_types_language().
        get_primitive_type_by_name('Real')))
    literal_boolean.set_extended_concept(literal_expression)
    literal_boolean.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-LiteralBoolean-value', name='value', key=
        'sysml-LiteralBoolean-value', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    literal_string.set_extended_concept(literal_expression)
    literal_string.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-LiteralString-value', name='value', key=
        'sysml-LiteralString-value', type=get_types_language().
        get_primitive_type_by_name('String')))
    feature_chain_expression.set_extended_concept(operator_expression)
    feature_chain_expression.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-FeatureChainExpression-targetFeature', name='targetFeature',
        key='sysml-FeatureChainExpression-targetFeature', type=i_feature,
        multiple=False, optional=False))
    i_binding_connector.add_extended_interface(i_connector)
    i_association_structure.add_extended_interface(i_association)
    i_association_structure.add_extended_interface(i_structure)
    dependency.add_implemented_interface(i_relationship)
    dependency.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Dependency-client', name='client', key=
        'sysml-Dependency-client', type=i_element, multiple=True, optional=
        False))
    dependency.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Dependency-supplier', name='supplier', key=
        'sysml-Dependency-supplier', type=i_element, multiple=True,
        optional=False))
    namespace_import.add_implemented_interface(i_import)
    namespace_import.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-NamespaceImport-importedNamespace', name=
        'importedNamespace', key='sysml-NamespaceImport-importedNamespace',
        type=i_namespace, multiple=False, optional=False))
    membership_import.add_implemented_interface(i_import)
    membership_import.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-MembershipImport-importedMembership', name=
        'importedMembership', key=
        'sysml-MembershipImport-importedMembership', type=membership,
        multiple=False, optional=False))
    interface_usage.set_extended_concept(connection_usage)
    interface_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-InterfaceUsage-interfaceDefinition', name=
        'interfaceDefinition', key=
        'sysml-InterfaceUsage-interfaceDefinition', type=
        interface_definition, multiple=True, optional=True))
    connection_usage.set_extended_concept(connector_as_usage)
    connection_usage.add_implemented_interface(i_part_usage)
    connection_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ConnectionUsage-connectionDefinition', name=
        'connectionDefinition', key=
        'sysml-ConnectionUsage-connectionDefinition', type=
        i_association_structure, multiple=True, optional=True))
    connector_as_usage.add_implemented_interface(i_usage)
    connector_as_usage.add_implemented_interface(i_connector)
    i_usage.add_extended_interface(i_feature)
    i_usage.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-isReference', name='isReference', key=
        'sysml-IUsage-isReference', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_usage.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-isVariation', name='isVariation', key=
        'sysml-IUsage-isVariation', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-variant', name='variant', key=
        'sysml-IUsage-variant', type=i_usage, multiple=True, optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-variantMembership', name='variantMembership', key=
        'sysml-IUsage-variantMembership', type=variant_membership, multiple
        =True, optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-owningDefinition', name='owningDefinition', key=
        'sysml-IUsage-owningDefinition', type=definition, multiple=False,
        optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-owningUsage', name='owningUsage', key=
        'sysml-IUsage-owningUsage', type=i_usage, multiple=False, optional=
        True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedUsage', name='nestedUsage', key=
        'sysml-IUsage-nestedUsage', type=i_usage, multiple=True, optional=True)
        )
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-definition', name='definition', key=
        'sysml-IUsage-definition', type=i_classifier, multiple=True,
        optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-usage', name='usage', key='sysml-IUsage-usage',
        type=i_usage, multiple=True, optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-directedUsage', name='directedUsage', key=
        'sysml-IUsage-directedUsage', type=i_usage, multiple=True, optional
        =True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedReference', name='nestedReference', key=
        'sysml-IUsage-nestedReference', type=reference_usage, multiple=True,
        optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedAttribute', name='nestedAttribute', key=
        'sysml-IUsage-nestedAttribute', type=attribute_usage, multiple=True,
        optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedEnumeration', name='nestedEnumeration', key=
        'sysml-IUsage-nestedEnumeration', type=enumeration_usage, multiple=
        True, optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedOccurrence', name='nestedOccurrence', key=
        'sysml-IUsage-nestedOccurrence', type=i_occurrence_usage, multiple=
        True, optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedItem', name='nestedItem', key=
        'sysml-IUsage-nestedItem', type=i_item_usage, multiple=True,
        optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedPart', name='nestedPart', key=
        'sysml-IUsage-nestedPart', type=i_part_usage, multiple=True,
        optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedPort', name='nestedPort', key=
        'sysml-IUsage-nestedPort', type=port_usage, multiple=True, optional
        =True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedConnection', name='nestedConnection', key=
        'sysml-IUsage-nestedConnection', type=connector_as_usage, multiple=
        True, optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedFlow', name='nestedFlow', key=
        'sysml-IUsage-nestedFlow', type=flow_connection_usage, multiple=
        True, optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedInterface', name='nestedInterface', key=
        'sysml-IUsage-nestedInterface', type=interface_usage, multiple=True,
        optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedAllocation', name='nestedAllocation', key=
        'sysml-IUsage-nestedAllocation', type=allocation_usage, multiple=
        True, optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedAction', name='nestedAction', key=
        'sysml-IUsage-nestedAction', type=i_action_usage, multiple=True,
        optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedState', name='nestedState', key=
        'sysml-IUsage-nestedState', type=state_usage, multiple=True,
        optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedTransition', name='nestedTransition', key=
        'sysml-IUsage-nestedTransition', type=transition_usage, multiple=
        True, optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedCalculation', name='nestedCalculation', key=
        'sysml-IUsage-nestedCalculation', type=calculation_usage, multiple=
        True, optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedConstraint', name='nestedConstraint', key=
        'sysml-IUsage-nestedConstraint', type=i_constraint_usage, multiple=
        True, optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedRequirement', name='nestedRequirement', key=
        'sysml-IUsage-nestedRequirement', type=requirement_usage, multiple=
        True, optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedConcern', name='nestedConcern', key=
        'sysml-IUsage-nestedConcern', type=concern_usage, multiple=True,
        optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedCase', name='nestedCase', key=
        'sysml-IUsage-nestedCase', type=case_usage, multiple=True, optional
        =True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedAnalysisCase', name='nestedAnalysisCase',
        key='sysml-IUsage-nestedAnalysisCase', type=analysis_case_usage,
        multiple=True, optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedVerificationCase', name=
        'nestedVerificationCase', key='sysml-IUsage-nestedVerificationCase',
        type=verification_case_usage, multiple=True, optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedUseCase', name='nestedUseCase', key=
        'sysml-IUsage-nestedUseCase', type=use_case_usage, multiple=True,
        optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedView', name='nestedView', key=
        'sysml-IUsage-nestedView', type=view_usage, multiple=True, optional
        =True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedViewpoint', name='nestedViewpoint', key=
        'sysml-IUsage-nestedViewpoint', type=viewpoint_usage, multiple=True,
        optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedRendering', name='nestedRendering', key=
        'sysml-IUsage-nestedRendering', type=rendering_usage, multiple=True,
        optional=True))
    i_usage.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-IUsage-nestedMetadata', name='nestedMetadata', key=
        'sysml-IUsage-nestedMetadata', type=metadata_usage, multiple=True,
        optional=True))
    variant_membership.set_extended_concept(owning_membership)
    variant_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-VariantMembership-ownedVariantUsage', name=
        'ownedVariantUsage', key=
        'sysml-VariantMembership-ownedVariantUsage', type=i_usage, multiple
        =False, optional=False))
    definition.add_implemented_interface(i_classifier)
    definition.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='sysml-Definition-isVariation', name='isVariation', key=
        'sysml-Definition-isVariation', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-variant', name='variant', key=
        'sysml-Definition-variant', type=i_usage, multiple=True, optional=True)
        )
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-variantMembership', name=
        'variantMembership', key='sysml-Definition-variantMembership', type
        =variant_membership, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-usage', name='usage', key=
        'sysml-Definition-usage', type=i_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-directedUsage', name='directedUsage',
        key='sysml-Definition-directedUsage', type=i_usage, multiple=True,
        optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedReference', name=
        'ownedReference', key='sysml-Definition-ownedReference', type=
        reference_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedAttribute', name=
        'ownedAttribute', key='sysml-Definition-ownedAttribute', type=
        attribute_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedEnumeration', name=
        'ownedEnumeration', key='sysml-Definition-ownedEnumeration', type=
        enumeration_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedOccurrence', name=
        'ownedOccurrence', key='sysml-Definition-ownedOccurrence', type=
        i_occurrence_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedItem', name='ownedItem', key=
        'sysml-Definition-ownedItem', type=i_item_usage, multiple=True,
        optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedPart', name='ownedPart', key=
        'sysml-Definition-ownedPart', type=i_part_usage, multiple=True,
        optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedPort', name='ownedPort', key=
        'sysml-Definition-ownedPort', type=port_usage, multiple=True,
        optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedConnection', name=
        'ownedConnection', key='sysml-Definition-ownedConnection', type=
        connector_as_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedFlow', name='ownedFlow', key=
        'sysml-Definition-ownedFlow', type=flow_connection_usage, multiple=
        True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedInterface', name=
        'ownedInterface', key='sysml-Definition-ownedInterface', type=
        interface_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedAllocation', name=
        'ownedAllocation', key='sysml-Definition-ownedAllocation', type=
        allocation_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedAction', name='ownedAction', key
        ='sysml-Definition-ownedAction', type=i_action_usage, multiple=True,
        optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedState', name='ownedState', key=
        'sysml-Definition-ownedState', type=state_usage, multiple=True,
        optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedTransition', name=
        'ownedTransition', key='sysml-Definition-ownedTransition', type=
        transition_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedCalculation', name=
        'ownedCalculation', key='sysml-Definition-ownedCalculation', type=
        calculation_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedConstraint', name=
        'ownedConstraint', key='sysml-Definition-ownedConstraint', type=
        i_constraint_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedRequirement', name=
        'ownedRequirement', key='sysml-Definition-ownedRequirement', type=
        requirement_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedConcern', name='ownedConcern',
        key='sysml-Definition-ownedConcern', type=concern_usage, multiple=
        True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedCase', name='ownedCase', key=
        'sysml-Definition-ownedCase', type=case_usage, multiple=True,
        optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedAnalysisCase', name=
        'ownedAnalysisCase', key='sysml-Definition-ownedAnalysisCase', type
        =analysis_case_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedVerificationCase', name=
        'ownedVerificationCase', key=
        'sysml-Definition-ownedVerificationCase', type=
        verification_case_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedUseCase', name='ownedUseCase',
        key='sysml-Definition-ownedUseCase', type=use_case_usage, multiple=
        True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedView', name='ownedView', key=
        'sysml-Definition-ownedView', type=view_usage, multiple=True,
        optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedViewpoint', name=
        'ownedViewpoint', key='sysml-Definition-ownedViewpoint', type=
        viewpoint_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedRendering', name=
        'ownedRendering', key='sysml-Definition-ownedRendering', type=
        rendering_usage, multiple=True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedMetadata', name='ownedMetadata',
        key='sysml-Definition-ownedMetadata', type=metadata_usage, multiple
        =True, optional=True))
    definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-Definition-ownedUsage', name='ownedUsage', key=
        'sysml-Definition-ownedUsage', type=i_usage, multiple=True,
        optional=True))
    reference_usage.add_implemented_interface(i_usage)
    attribute_usage.add_implemented_interface(i_usage)
    attribute_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-AttributeUsage-attributeDefinition', name=
        'attributeDefinition', key=
        'sysml-AttributeUsage-attributeDefinition', type=i_data_type,
        multiple=True, optional=True))
    enumeration_usage.set_extended_concept(attribute_usage)
    enumeration_usage.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-EnumerationUsage-enumerationDefinition', name=
        'enumerationDefinition', key=
        'sysml-EnumerationUsage-enumerationDefinition', type=
        enumeration_definition, multiple=False, optional=False))
    enumeration_definition.set_extended_concept(attribute_definition)
    enumeration_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-EnumerationDefinition-enumeratedValue', name=
        'enumeratedValue', key=
        'sysml-EnumerationDefinition-enumeratedValue', type=
        enumeration_usage, multiple=True, optional=True))
    attribute_definition.set_extended_concept(definition)
    attribute_definition.add_implemented_interface(i_data_type)
    i_occurrence_usage.add_extended_interface(i_usage)
    i_occurrence_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-IOccurrenceUsage-occurrenceDefinition', name=
        'occurrenceDefinition', key=
        'sysml-IOccurrenceUsage-occurrenceDefinition', type=i_class,
        multiple=True, optional=True))
    i_occurrence_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-IOccurrenceUsage-individualDefinition', name=
        'individualDefinition', key=
        'sysml-IOccurrenceUsage-individualDefinition', type=
        occurrence_definition, multiple=False, optional=True))
    i_occurrence_usage.add_feature(Property(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-IOccurrenceUsage-isIndividual', name=
        'isIndividual', key='sysml-IOccurrenceUsage-isIndividual', type=
        get_types_language().get_primitive_type_by_name('Boolean')))
    i_occurrence_usage.add_feature(Property(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-IOccurrenceUsage-portionKind', name=
        'portionKind', key='sysml-IOccurrenceUsage-portionKind', type=
        portion_kind))
    occurrence_definition.set_extended_concept(definition)
    occurrence_definition.add_implemented_interface(i_class)
    occurrence_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-OccurrenceDefinition-lifeClass',
        name='lifeClass', key='sysml-OccurrenceDefinition-lifeClass', type=
        life_class, multiple=False, optional=True))
    occurrence_definition.add_feature(Property(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-OccurrenceDefinition-isIndividual', name='isIndividual', key
        ='sysml-OccurrenceDefinition-isIndividual', type=get_types_language
        ().get_primitive_type_by_name('Boolean')))
    life_class.add_implemented_interface(i_class)
    i_item_usage.add_extended_interface(i_occurrence_usage)
    i_item_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IItemUsage-itemDefinition', name=
        'itemDefinition', key='sysml-IItemUsage-itemDefinition', type=
        i_structure, multiple=True, optional=True))
    i_part_usage.add_extended_interface(i_item_usage)
    i_part_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IPartUsage-partDefinition', name=
        'partDefinition', key='sysml-IPartUsage-partDefinition', type=
        part_definition, multiple=True, optional=True))
    part_definition.set_extended_concept(item_definition)
    item_definition.set_extended_concept(occurrence_definition)
    item_definition.add_implemented_interface(i_structure)
    port_usage.add_implemented_interface(i_occurrence_usage)
    port_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-PortUsage-portDefinition', name='portDefinition',
        key='sysml-PortUsage-portDefinition', type=port_definition,
        multiple=True, optional=True))
    port_definition.set_extended_concept(occurrence_definition)
    port_definition.add_implemented_interface(i_structure)
    port_definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-PortDefinition-conjugatedPortDefinition', name=
        'conjugatedPortDefinition', key=
        'sysml-PortDefinition-conjugatedPortDefinition', type=
        conjugated_port_definition, multiple=False, optional=True))
    conjugated_port_definition.set_extended_concept(port_definition)
    conjugated_port_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-ConjugatedPortDefinition-ownedPortConjugator', name=
        'ownedPortConjugator', key=
        'sysml-ConjugatedPortDefinition-ownedPortConjugator', type=
        port_conjugation, multiple=False, optional=False))
    conjugated_port_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-ConjugatedPortDefinition-originalPortDefinition', name=
        'originalPortDefinition', key=
        'sysml-ConjugatedPortDefinition-originalPortDefinition', type=
        port_definition, multiple=False, optional=False))
    port_conjugation.set_extended_concept(conjugation)
    port_conjugation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-PortConjugation-originalPortDefinition', name=
        'originalPortDefinition', key=
        'sysml-PortConjugation-originalPortDefinition', type=
        port_definition, multiple=False, optional=False))
    port_conjugation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-PortConjugation-conjugatedPortDefinition', name=
        'conjugatedPortDefinition', key=
        'sysml-PortConjugation-conjugatedPortDefinition', type=
        conjugated_port_definition, multiple=False, optional=False))
    flow_connection_usage.set_extended_concept(connector_as_usage)
    flow_connection_usage.add_implemented_interface(i_action_usage)
    flow_connection_usage.add_implemented_interface(i_item_flow)
    flow_connection_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-FlowConnectionUsage-flowConnectionDefinition', name=
        'flowConnectionDefinition', key=
        'sysml-FlowConnectionUsage-flowConnectionDefinition', type=
        i_interaction, multiple=True, optional=True))
    i_action_usage.add_extended_interface(i_occurrence_usage)
    i_action_usage.add_extended_interface(i_step)
    i_action_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IActionUsage-actionDefinition', name=
        'actionDefinition', key='sysml-IActionUsage-actionDefinition', type
        =i_behavior, multiple=True, optional=True))
    allocation_usage.set_extended_concept(connection_usage)
    allocation_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-AllocationUsage-allocationDefinition', name=
        'allocationDefinition', key=
        'sysml-AllocationUsage-allocationDefinition', type=
        allocation_definition, multiple=True, optional=True))
    allocation_definition.set_extended_concept(connection_definition)
    allocation_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-AllocationDefinition-allocation',
        name='allocation', key='sysml-AllocationDefinition-allocation',
        type=allocation_usage, multiple=True, optional=True))
    connection_definition.set_extended_concept(part_definition)
    connection_definition.add_implemented_interface(i_association_structure)
    connection_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-ConnectionDefinition-connectionEnd', name='connectionEnd',
        key='sysml-ConnectionDefinition-connectionEnd', type=i_usage,
        multiple=True, optional=True))
    state_usage.add_implemented_interface(i_action_usage)
    state_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-StateUsage-stateDefinition', name=
        'stateDefinition', key='sysml-StateUsage-stateDefinition', type=
        i_behavior, multiple=True, optional=True))
    state_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-StateUsage-entryAction', name='entryAction', key
        ='sysml-StateUsage-entryAction', type=i_action_usage, multiple=
        False, optional=True))
    state_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-StateUsage-doAction', name='doAction', key=
        'sysml-StateUsage-doAction', type=i_action_usage, multiple=False,
        optional=True))
    state_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-StateUsage-exitAction', name='exitAction', key=
        'sysml-StateUsage-exitAction', type=i_action_usage, multiple=False,
        optional=True))
    state_usage.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-StateUsage-isParallel', name='isParallel', key=
        'sysml-StateUsage-isParallel', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    transition_usage.add_implemented_interface(i_action_usage)
    transition_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-TransitionUsage-source', name='source', key=
        'sysml-TransitionUsage-source', type=i_action_usage, multiple=False,
        optional=False))
    transition_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-TransitionUsage-target', name='target', key=
        'sysml-TransitionUsage-target', type=i_action_usage, multiple=False,
        optional=False))
    transition_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-TransitionUsage-triggerAction', name=
        'triggerAction', key='sysml-TransitionUsage-triggerAction', type=
        accept_action_usage, multiple=True, optional=True))
    transition_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-TransitionUsage-guardExpression', name=
        'guardExpression', key='sysml-TransitionUsage-guardExpression',
        type=i_expression, multiple=True, optional=True))
    transition_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-TransitionUsage-effectAction', name=
        'effectAction', key='sysml-TransitionUsage-effectAction', type=
        i_action_usage, multiple=True, optional=True))
    transition_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-TransitionUsage-succession', name='succession',
        key='sysml-TransitionUsage-succession', type=i_succession, multiple
        =False, optional=False))
    accept_action_usage.add_implemented_interface(i_action_usage)
    accept_action_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-AcceptActionUsage-receiverArgument', name='receiverArgument',
        key='sysml-AcceptActionUsage-receiverArgument', type=i_expression,
        multiple=False, optional=True))
    accept_action_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-AcceptActionUsage-payloadParameter', name='payloadParameter',
        key='sysml-AcceptActionUsage-payloadParameter', type=
        reference_usage, multiple=False, optional=False))
    accept_action_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-AcceptActionUsage-payloadArgument', name='payloadArgument',
        key='sysml-AcceptActionUsage-payloadArgument', type=i_expression,
        multiple=False, optional=True))
    calculation_usage.add_implemented_interface(i_action_usage)
    calculation_usage.add_implemented_interface(i_expression)
    calculation_usage.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-CalculationUsage-calculationDefinition', name=
        'calculationDefinition', key=
        'sysml-CalculationUsage-calculationDefinition', type=i_function,
        multiple=False, optional=True))
    i_constraint_usage.add_extended_interface(i_occurrence_usage)
    i_constraint_usage.add_extended_interface(i_boolean_expression)
    i_constraint_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-IConstraintUsage-constraintDefinition', name=
        'constraintDefinition', key=
        'sysml-IConstraintUsage-constraintDefinition', type=i_predicate,
        multiple=False, optional=True))
    requirement_usage.add_implemented_interface(i_constraint_usage)
    requirement_usage.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-RequirementUsage-requirementDefinition', name=
        'requirementDefinition', key=
        'sysml-RequirementUsage-requirementDefinition', type=
        requirement_definition, multiple=False, optional=True))
    requirement_usage.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-RequirementUsage-reqId', name='reqId', key=
        'sysml-RequirementUsage-reqId', type=get_types_language().
        get_primitive_type_by_name('String')))
    requirement_usage.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-RequirementUsage-requiredConstraint', name=
        'requiredConstraint', key=
        'sysml-RequirementUsage-requiredConstraint', type=
        i_constraint_usage, multiple=True, optional=True))
    requirement_usage.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-RequirementUsage-assumedConstraint', name=
        'assumedConstraint', key='sysml-RequirementUsage-assumedConstraint',
        type=i_constraint_usage, multiple=True, optional=True))
    requirement_usage.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-RequirementUsage-subjectParameter', name=
        'subjectParameter', key='sysml-RequirementUsage-subjectParameter',
        type=i_usage, multiple=False, optional=False))
    requirement_usage.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-RequirementUsage-framedConcern', name=
        'framedConcern', key='sysml-RequirementUsage-framedConcern', type=
        concern_usage, multiple=True, optional=True))
    requirement_usage.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-RequirementUsage-actorParameter', name=
        'actorParameter', key='sysml-RequirementUsage-actorParameter', type
        =i_part_usage, multiple=True, optional=True))
    requirement_usage.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-RequirementUsage-stakeholderParameter', name=
        'stakeholderParameter', key=
        'sysml-RequirementUsage-stakeholderParameter', type=i_part_usage,
        multiple=True, optional=True))
    requirement_usage.add_feature(Containment(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-RequirementUsage-textContainer',
        name='textContainer', key='sysml-RequirementUsage-textContainer',
        type=text_container, multiple=True, optional=True))
    requirement_definition.set_extended_concept(constraint_definition)
    requirement_definition.add_feature(Property(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-RequirementDefinition-reqId',
        name='reqId', key='sysml-RequirementDefinition-reqId', type=
        get_types_language().get_primitive_type_by_name('String')))
    requirement_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-RequirementDefinition-subjectParameter', name=
        'subjectParameter', key=
        'sysml-RequirementDefinition-subjectParameter', type=i_usage,
        multiple=False, optional=False))
    requirement_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-RequirementDefinition-actorParameter', name='actorParameter',
        key='sysml-RequirementDefinition-actorParameter', type=i_part_usage,
        multiple=True, optional=True))
    requirement_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-RequirementDefinition-stakeholderParameter', name=
        'stakeholderParameter', key=
        'sysml-RequirementDefinition-stakeholderParameter', type=
        i_part_usage, multiple=True, optional=True))
    requirement_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-RequirementDefinition-assumedConstraint', name=
        'assumedConstraint', key=
        'sysml-RequirementDefinition-assumedConstraint', type=
        i_constraint_usage, multiple=True, optional=True))
    requirement_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-RequirementDefinition-requiredConstraint', name=
        'requiredConstraint', key=
        'sysml-RequirementDefinition-requiredConstraint', type=
        i_constraint_usage, multiple=True, optional=True))
    requirement_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-RequirementDefinition-framedConcern', name='framedConcern',
        key='sysml-RequirementDefinition-framedConcern', type=concern_usage,
        multiple=True, optional=True))
    requirement_definition.add_feature(Containment(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-RequirementDefinition-textContainer', name='textContainer',
        key='sysml-RequirementDefinition-textContainer', type=
        text_container, multiple=True, optional=True))
    constraint_definition.set_extended_concept(occurrence_definition)
    constraint_definition.add_implemented_interface(i_predicate)
    concern_usage.set_extended_concept(requirement_usage)
    concern_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ConcernUsage-concernDefinition', name=
        'concernDefinition', key='sysml-ConcernUsage-concernDefinition',
        type=concern_definition, multiple=False, optional=True))
    concern_definition.set_extended_concept(requirement_definition)
    case_usage.set_extended_concept(calculation_usage)
    case_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-CaseUsage-objectiveRequirement', name=
        'objectiveRequirement', key='sysml-CaseUsage-objectiveRequirement',
        type=requirement_usage, multiple=False, optional=True))
    case_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-CaseUsage-caseDefinition', name='caseDefinition',
        key='sysml-CaseUsage-caseDefinition', type=case_definition,
        multiple=False, optional=True))
    case_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-CaseUsage-subjectParameter', name=
        'subjectParameter', key='sysml-CaseUsage-subjectParameter', type=
        i_usage, multiple=False, optional=False))
    case_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-CaseUsage-actorParameter', name='actorParameter',
        key='sysml-CaseUsage-actorParameter', type=i_part_usage, multiple=
        True, optional=True))
    case_definition.set_extended_concept(calculation_definition)
    case_definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-CaseDefinition-objectiveRequirement', name=
        'objectiveRequirement', key=
        'sysml-CaseDefinition-objectiveRequirement', type=requirement_usage,
        multiple=False, optional=True))
    case_definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-CaseDefinition-subjectParameter', name=
        'subjectParameter', key='sysml-CaseDefinition-subjectParameter',
        type=i_usage, multiple=False, optional=False))
    case_definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-CaseDefinition-actorParameter', name=
        'actorParameter', key='sysml-CaseDefinition-actorParameter', type=
        i_part_usage, multiple=True, optional=True))
    calculation_definition.set_extended_concept(action_definition)
    calculation_definition.add_implemented_interface(i_function)
    calculation_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-CalculationDefinition-calculation', name='calculation', key=
        'sysml-CalculationDefinition-calculation', type=calculation_usage,
        multiple=True, optional=True))
    action_definition.set_extended_concept(occurrence_definition)
    action_definition.add_implemented_interface(i_behavior)
    action_definition.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-ActionDefinition-action', name='action', key=
        'sysml-ActionDefinition-action', type=i_action_usage, multiple=True,
        optional=True))
    analysis_case_usage.set_extended_concept(case_usage)
    analysis_case_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-AnalysisCaseUsage-analysisCaseDefinition', name=
        'analysisCaseDefinition', key=
        'sysml-AnalysisCaseUsage-analysisCaseDefinition', type=
        analysis_case_definition, multiple=False, optional=True))
    analysis_case_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-AnalysisCaseUsage-resultExpression', name='resultExpression',
        key='sysml-AnalysisCaseUsage-resultExpression', type=i_expression,
        multiple=False, optional=True))
    analysis_case_definition.set_extended_concept(case_definition)
    analysis_case_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-AnalysisCaseDefinition-resultExpression', name=
        'resultExpression', key=
        'sysml-AnalysisCaseDefinition-resultExpression', type=i_expression,
        multiple=False, optional=True))
    verification_case_usage.set_extended_concept(case_usage)
    verification_case_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-VerificationCaseUsage-verificationCaseDefinition', name=
        'verificationCaseDefinition', key=
        'sysml-VerificationCaseUsage-verificationCaseDefinition', type=
        verification_case_definition, multiple=False, optional=True))
    verification_case_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-VerificationCaseUsage-verifiedRequirement', name=
        'verifiedRequirement', key=
        'sysml-VerificationCaseUsage-verifiedRequirement', type=
        requirement_usage, multiple=True, optional=True))
    verification_case_definition.set_extended_concept(case_definition)
    verification_case_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-VerificationCaseDefinition-verifiedRequirement', name=
        'verifiedRequirement', key=
        'sysml-VerificationCaseDefinition-verifiedRequirement', type=
        requirement_usage, multiple=True, optional=True))
    use_case_usage.set_extended_concept(case_usage)
    use_case_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-UseCaseUsage-useCaseDefinition', name=
        'useCaseDefinition', key='sysml-UseCaseUsage-useCaseDefinition',
        type=use_case_definition, multiple=False, optional=True))
    use_case_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-UseCaseUsage-includedUseCase', name=
        'includedUseCase', key='sysml-UseCaseUsage-includedUseCase', type=
        use_case_usage, multiple=True, optional=True))
    use_case_definition.set_extended_concept(case_definition)
    use_case_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-UseCaseDefinition-includedUseCase', name='includedUseCase',
        key='sysml-UseCaseDefinition-includedUseCase', type=use_case_usage,
        multiple=True, optional=True))
    view_usage.add_implemented_interface(i_part_usage)
    view_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ViewUsage-viewDefinition', name='viewDefinition',
        key='sysml-ViewUsage-viewDefinition', type=view_definition,
        multiple=False, optional=True))
    view_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ViewUsage-satisfiedViewpoint', name=
        'satisfiedViewpoint', key='sysml-ViewUsage-satisfiedViewpoint',
        type=viewpoint_usage, multiple=True, optional=True))
    view_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ViewUsage-exposedElement', name='exposedElement',
        key='sysml-ViewUsage-exposedElement', type=i_element, multiple=True,
        optional=True))
    view_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ViewUsage-viewRendering', name='viewRendering',
        key='sysml-ViewUsage-viewRendering', type=rendering_usage, multiple
        =False, optional=True))
    view_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ViewUsage-viewCondition', name='viewCondition',
        key='sysml-ViewUsage-viewCondition', type=i_expression, multiple=
        True, optional=True))
    view_definition.set_extended_concept(part_definition)
    view_definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ViewDefinition-view', name='view', key=
        'sysml-ViewDefinition-view', type=view_usage, multiple=True,
        optional=True))
    view_definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ViewDefinition-satisfiedViewpoint', name=
        'satisfiedViewpoint', key='sysml-ViewDefinition-satisfiedViewpoint',
        type=viewpoint_usage, multiple=True, optional=True))
    view_definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ViewDefinition-viewRendering', name=
        'viewRendering', key='sysml-ViewDefinition-viewRendering', type=
        rendering_usage, multiple=False, optional=True))
    view_definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ViewDefinition-viewCondition', name=
        'viewCondition', key='sysml-ViewDefinition-viewCondition', type=
        i_expression, multiple=True, optional=True))
    viewpoint_usage.set_extended_concept(requirement_usage)
    viewpoint_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ViewpointUsage-viewpointDefinition', name=
        'viewpointDefinition', key=
        'sysml-ViewpointUsage-viewpointDefinition', type=
        viewpoint_definition, multiple=False, optional=True))
    viewpoint_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ViewpointUsage-viewpointStakeholder', name=
        'viewpointStakeholder', key=
        'sysml-ViewpointUsage-viewpointStakeholder', type=i_part_usage,
        multiple=True, optional=True))
    viewpoint_definition.set_extended_concept(requirement_definition)
    viewpoint_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-ViewpointDefinition-viewpointStakeholder', name=
        'viewpointStakeholder', key=
        'sysml-ViewpointDefinition-viewpointStakeholder', type=i_part_usage,
        multiple=True, optional=True))
    rendering_usage.add_implemented_interface(i_part_usage)
    rendering_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-RenderingUsage-renderingDefinition', name=
        'renderingDefinition', key=
        'sysml-RenderingUsage-renderingDefinition', type=
        rendering_definition, multiple=False, optional=True))
    rendering_definition.set_extended_concept(part_definition)
    rendering_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-RenderingDefinition-rendering',
        name='rendering', key='sysml-RenderingDefinition-rendering', type=
        rendering_usage, multiple=True, optional=True))
    metadata_usage.set_extended_concept(metadata_feature)
    metadata_usage.add_implemented_interface(i_item_usage)
    metadata_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-MetadataUsage-metadataDefinition', name=
        'metadataDefinition', key='sysml-MetadataUsage-metadataDefinition',
        type=i_metaclass, multiple=False, optional=True))
    interface_definition.set_extended_concept(connection_definition)
    interface_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-InterfaceDefinition-interfaceEnd',
        name='interfaceEnd', key='sysml-InterfaceDefinition-interfaceEnd',
        type=port_usage, multiple=True, optional=True))
    conjugated_port_typing.set_extended_concept(feature_typing)
    conjugated_port_typing.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-ConjugatedPortTyping-portDefinition', name='portDefinition',
        key='sysml-ConjugatedPortTyping-portDefinition', type=
        port_definition, multiple=False, optional=False))
    conjugated_port_typing.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-ConjugatedPortTyping-conjugatedPortDefinition', name=
        'conjugatedPortDefinition', key=
        'sysml-ConjugatedPortTyping-conjugatedPortDefinition', type=
        conjugated_port_definition, multiple=False, optional=False))
    transition_feature_membership.set_extended_concept(feature_membership)
    transition_feature_membership.add_feature(Property(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-TransitionFeatureMembership-kind',
        name='kind', key='sysml-TransitionFeatureMembership-kind', type=
        transition_feature_kind))
    transition_feature_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-TransitionFeatureMembership-transitionFeature', name=
        'transitionFeature', key=
        'sysml-TransitionFeatureMembership-transitionFeature', type=i_step,
        multiple=False, optional=False))
    exhibit_state_usage.set_extended_concept(state_usage)
    exhibit_state_usage.add_implemented_interface(i_perform_action_usage)
    exhibit_state_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-ExhibitStateUsage-exhibitedState',
        name='exhibitedState', key='sysml-ExhibitStateUsage-exhibitedState',
        type=state_usage, multiple=False, optional=False))
    i_perform_action_usage.add_extended_interface(i_action_usage)
    i_perform_action_usage.add_extended_interface(i_event_occurrence_usage)
    i_perform_action_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-IPerformActionUsage-performedAction', name='performedAction',
        key='sysml-IPerformActionUsage-performedAction', type=
        i_action_usage, multiple=False, optional=False))
    i_event_occurrence_usage.add_extended_interface(i_occurrence_usage)
    i_event_occurrence_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-IEventOccurrenceUsage-eventOccurrence', name=
        'eventOccurrence', key=
        'sysml-IEventOccurrenceUsage-eventOccurrence', type=
        i_occurrence_usage, multiple=False, optional=False))
    state_subaction_membership.set_extended_concept(feature_membership)
    state_subaction_membership.add_feature(Property(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-StateSubactionMembership-kind',
        name='kind', key='sysml-StateSubactionMembership-kind', type=
        state_subaction_kind))
    state_subaction_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-StateSubactionMembership-action',
        name='action', key='sysml-StateSubactionMembership-action', type=
        i_action_usage, multiple=False, optional=False))
    state_definition.set_extended_concept(action_definition)
    state_definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-StateDefinition-state', name='state', key=
        'sysml-StateDefinition-state', type=state_usage, multiple=True,
        optional=True))
    state_definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-StateDefinition-entryAction', name='entryAction',
        key='sysml-StateDefinition-entryAction', type=i_action_usage,
        multiple=False, optional=True))
    state_definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-StateDefinition-doAction', name='doAction', key=
        'sysml-StateDefinition-doAction', type=i_action_usage, multiple=
        False, optional=True))
    state_definition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-StateDefinition-exitAction', name='exitAction',
        key='sysml-StateDefinition-exitAction', type=i_action_usage,
        multiple=False, optional=True))
    state_definition.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-StateDefinition-isParallel', name='isParallel',
        key='sysml-StateDefinition-isParallel', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    succession_flow_connection_usage.set_extended_concept(flow_connection_usage
        )
    succession_flow_connection_usage.add_implemented_interface(
        i_succession_item_flow)
    flow_connection_definition.set_extended_concept(action_definition)
    flow_connection_definition.add_implemented_interface(i_interaction)
    flow_connection_definition.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-FlowConnectionDefinition-flowConnectionEnd', name=
        'flowConnectionEnd', key=
        'sysml-FlowConnectionDefinition-flowConnectionEnd', type=i_usage,
        multiple=True, optional=True))
    requirement_verification_membership.set_extended_concept(
        requirement_constraint_membership)
    requirement_verification_membership.add_feature(Reference(
        lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-RequirementVerificationMembership-ownedRequirement', name=
        'ownedRequirement', key=
        'sysml-RequirementVerificationMembership-ownedRequirement', type=
        requirement_usage, multiple=False, optional=False))
    requirement_verification_membership.add_feature(Reference(
        lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-RequirementVerificationMembership-verifiedRequirement', name
        ='verifiedRequirement', key=
        'sysml-RequirementVerificationMembership-verifiedRequirement', type
        =requirement_usage, multiple=False, optional=False))
    requirement_constraint_membership.set_extended_concept(feature_membership)
    requirement_constraint_membership.add_feature(Property(lion_web_version
        =LionWebVersion.V2023_1, id=
        'sysml-RequirementConstraintMembership-kind', name='kind', key=
        'sysml-RequirementConstraintMembership-kind', type=
        requirement_constraint_kind))
    requirement_constraint_membership.add_feature(Reference(
        lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-RequirementConstraintMembership-ownedConstraint', name=
        'ownedConstraint', key=
        'sysml-RequirementConstraintMembership-ownedConstraint', type=
        i_constraint_usage, multiple=False, optional=False))
    requirement_constraint_membership.add_feature(Reference(
        lion_web_version=LionWebVersion.V2023_1, id=
        'sysml-RequirementConstraintMembership-referencedConstraint', name=
        'referencedConstraint', key=
        'sysml-RequirementConstraintMembership-referencedConstraint', type=
        i_constraint_usage, multiple=False, optional=False))
    include_use_case_usage.set_extended_concept(use_case_usage)
    include_use_case_usage.add_implemented_interface(i_perform_action_usage)
    include_use_case_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-IncludeUseCaseUsage-useCaseIncluded', name='useCaseIncluded',
        key='sysml-IncludeUseCaseUsage-useCaseIncluded', type=
        use_case_usage, multiple=False, optional=False))
    objective_membership.set_extended_concept(feature_membership)
    objective_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-ObjectiveMembership-ownedObjectiveRequirement', name=
        'ownedObjectiveRequirement', key=
        'sysml-ObjectiveMembership-ownedObjectiveRequirement', type=
        requirement_usage, multiple=False, optional=False))
    satisfy_requirement_usage.set_extended_concept(requirement_usage)
    satisfy_requirement_usage.add_implemented_interface(
        i_assert_constraint_usage)
    satisfy_requirement_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-SatisfyRequirementUsage-satisfiedRequirement', name=
        'satisfiedRequirement', key=
        'sysml-SatisfyRequirementUsage-satisfiedRequirement', type=
        requirement_usage, multiple=False, optional=False))
    satisfy_requirement_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-SatisfyRequirementUsage-satisfyingFeature', name=
        'satisfyingFeature', key=
        'sysml-SatisfyRequirementUsage-satisfyingFeature', type=i_feature,
        multiple=False, optional=False))
    i_assert_constraint_usage.add_extended_interface(i_constraint_usage)
    i_assert_constraint_usage.add_extended_interface(i_invariant)
    i_assert_constraint_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-IAssertConstraintUsage-assertedConstraint', name=
        'assertedConstraint', key=
        'sysml-IAssertConstraintUsage-assertedConstraint', type=
        i_constraint_usage, multiple=False, optional=False))
    subject_membership.set_extended_concept(parameter_membership)
    subject_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-SubjectMembership-ownedSubjectParameter', name=
        'ownedSubjectParameter', key=
        'sysml-SubjectMembership-ownedSubjectParameter', type=i_usage,
        multiple=False, optional=False))
    stakeholder_membership.set_extended_concept(parameter_membership)
    stakeholder_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-StakeholderMembership-ownedStakeholderParameter', name=
        'ownedStakeholderParameter', key=
        'sysml-StakeholderMembership-ownedStakeholderParameter', type=
        i_part_usage, multiple=False, optional=False))
    framed_concern_membership.set_extended_concept(
        requirement_constraint_membership)
    framed_concern_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-FramedConcernMembership-ownedConcern', name='ownedConcern',
        key='sysml-FramedConcernMembership-ownedConcern', type=
        concern_usage, multiple=False, optional=False))
    framed_concern_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-FramedConcernMembership-referencedConcern', name=
        'referencedConcern', key=
        'sysml-FramedConcernMembership-referencedConcern', type=
        concern_usage, multiple=False, optional=False))
    actor_membership.set_extended_concept(parameter_membership)
    actor_membership.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-ActorMembership-ownedActorParameter', name=
        'ownedActorParameter', key=
        'sysml-ActorMembership-ownedActorParameter', type=i_part_usage,
        multiple=False, optional=False))
    view_rendering_membership.set_extended_concept(feature_membership)
    view_rendering_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-ViewRenderingMembership-ownedRendering', name=
        'ownedRendering', key=
        'sysml-ViewRenderingMembership-ownedRendering', type=
        rendering_usage, multiple=False, optional=False))
    view_rendering_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-ViewRenderingMembership-referencedRendering', name=
        'referencedRendering', key=
        'sysml-ViewRenderingMembership-referencedRendering', type=
        rendering_usage, multiple=False, optional=False))
    namespace_expose.set_extended_concept(namespace_import)
    namespace_expose.add_implemented_interface(i_expose)
    i_expose.add_extended_interface(i_import)
    membership_expose.set_extended_concept(membership_import)
    membership_expose.add_implemented_interface(i_expose)
    binding_connector_as_usage.set_extended_concept(connector_as_usage)
    binding_connector_as_usage.add_implemented_interface(i_binding_connector)
    succession_as_usage.set_extended_concept(connector_as_usage)
    succession_as_usage.add_implemented_interface(i_succession)
    fork_node.set_extended_concept(control_node)
    control_node.add_implemented_interface(i_action_usage)
    join_node.set_extended_concept(control_node)
    send_action_usage.add_implemented_interface(i_action_usage)
    send_action_usage.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-SendActionUsage-receiverArgument', name=
        'receiverArgument', key='sysml-SendActionUsage-receiverArgument',
        type=i_expression, multiple=False, optional=True))
    send_action_usage.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-SendActionUsage-payloadArgument', name=
        'payloadArgument', key='sysml-SendActionUsage-payloadArgument',
        type=i_expression, multiple=False, optional=False))
    send_action_usage.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-SendActionUsage-senderArgument', name=
        'senderArgument', key='sysml-SendActionUsage-senderArgument', type=
        i_expression, multiple=False, optional=True))
    decision_node.set_extended_concept(control_node)
    merge_node.set_extended_concept(control_node)
    loop_action_usage.add_implemented_interface(i_action_usage)
    loop_action_usage.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='sysml-LoopActionUsage-bodyAction', name='bodyAction',
        key='sysml-LoopActionUsage-bodyAction', type=i_action_usage,
        multiple=False, optional=False))
    trigger_invocation_expression.set_extended_concept(invocation_expression)
    trigger_invocation_expression.add_feature(Property(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-TriggerInvocationExpression-kind',
        name='kind', key='sysml-TriggerInvocationExpression-kind', type=
        trigger_kind))
    assignment_action_usage.add_implemented_interface(i_action_usage)
    assignment_action_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-AssignmentActionUsage-targetArgument', name='targetArgument',
        key='sysml-AssignmentActionUsage-targetArgument', type=i_expression,
        multiple=False, optional=True))
    assignment_action_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-AssignmentActionUsage-valueExpression', name=
        'valueExpression', key=
        'sysml-AssignmentActionUsage-valueExpression', type=i_expression,
        multiple=False, optional=True))
    assignment_action_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-AssignmentActionUsage-referent',
        name='referent', key='sysml-AssignmentActionUsage-referent', type=
        i_feature, multiple=False, optional=False))
    for_loop_action_usage.set_extended_concept(loop_action_usage)
    for_loop_action_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-ForLoopActionUsage-seqArgument',
        name='seqArgument', key='sysml-ForLoopActionUsage-seqArgument',
        type=i_expression, multiple=False, optional=False))
    for_loop_action_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-ForLoopActionUsage-loopVariable',
        name='loopVariable', key='sysml-ForLoopActionUsage-loopVariable',
        type=reference_usage, multiple=False, optional=False))
    if_action_usage.add_implemented_interface(i_action_usage)
    if_action_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IfActionUsage-elseAction', name='elseAction',
        key='sysml-IfActionUsage-elseAction', type=i_action_usage, multiple
        =False, optional=True))
    if_action_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IfActionUsage-thenAction', name='thenAction',
        key='sysml-IfActionUsage-thenAction', type=i_action_usage, multiple
        =False, optional=False))
    if_action_usage.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-IfActionUsage-ifArgument', name='ifArgument',
        key='sysml-IfActionUsage-ifArgument', type=i_expression, multiple=
        False, optional=False))
    while_loop_action_usage.set_extended_concept(loop_action_usage)
    while_loop_action_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-WhileLoopActionUsage-whileArgument', name='whileArgument',
        key='sysml-WhileLoopActionUsage-whileArgument', type=i_expression,
        multiple=False, optional=False))
    while_loop_action_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-WhileLoopActionUsage-untilArgument', name='untilArgument',
        key='sysml-WhileLoopActionUsage-untilArgument', type=i_expression,
        multiple=False, optional=True))
    terminate_action_usage.add_implemented_interface(i_action_usage)
    terminate_action_usage.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'sysml-TerminateActionUsage-terminatedOccurrenceArgument', name=
        'terminatedOccurrenceArgument', key=
        'sysml-TerminateActionUsage-terminatedOccurrenceArgument', type=
        i_expression, multiple=False, optional=True))
    metadata_definition.set_extended_concept(item_definition)
    metadata_definition.add_implemented_interface(i_metaclass)
    alias_ids_container.add_feature(Property(lion_web_version=
        LionWebVersion.V2023_1, id='sysml-AliasIdsContainer-aliasIds', name
        ='aliasIds', key='sysml-AliasIdsContainer-aliasIds', type=
        get_types_language().get_primitive_type_by_name('String')))
    text_container.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='sysml-TextContainer-text', name='text', key=
        'sysml-TextContainer-text', type=get_types_language().
        get_primitive_type_by_name('String')))
    featuring.add_implemented_interface(i_featuring)
    relationship.add_implemented_interface(i_relationship)
    element.add_implemented_interface(i_element)
    annotating_element.add_implemented_interface(i_annotating_element)
    step.add_implemented_interface(i_step)
    feature.add_implemented_interface(i_feature)
    type.add_implemented_interface(i_type)
    namespace.add_implemented_interface(i_namespace)
    behavior.add_implemented_interface(i_behavior)
    class_.add_implemented_interface(i_class)
    classifier.add_implemented_interface(i_classifier)
    succession.add_implemented_interface(i_succession)
    connector.add_implemented_interface(i_connector)
    structure.add_implemented_interface(i_structure)
    part_usage.add_implemented_interface(i_part_usage)
    item_usage.add_implemented_interface(i_item_usage)
    occurrence_usage.add_implemented_interface(i_occurrence_usage)
    usage.add_implemented_interface(i_usage)
    data_type.add_implemented_interface(i_data_type)
    action_usage.add_implemented_interface(i_action_usage)
    item_flow.add_implemented_interface(i_item_flow)
    association_structure.add_implemented_interface(i_association_structure)
    association.add_implemented_interface(i_association)
    predicate.add_implemented_interface(i_predicate)
    function.add_implemented_interface(i_function)
    perform_action_usage.add_implemented_interface(i_perform_action_usage)
    event_occurrence_usage.add_implemented_interface(i_event_occurrence_usage)
    succession_item_flow.add_implemented_interface(i_succession_item_flow)
    interaction.add_implemented_interface(i_interaction)
    assert_constraint_usage.add_implemented_interface(i_assert_constraint_usage
        )
    constraint_usage.add_implemented_interface(i_constraint_usage)
    boolean_expression.add_implemented_interface(i_boolean_expression)
    expression.add_implemented_interface(i_expression)
    invariant.add_implemented_interface(i_invariant)
    expose.add_implemented_interface(i_expose)
    import_.add_implemented_interface(i_import)
    binding_connector.add_implemented_interface(i_binding_connector)
    metaclass.add_implemented_interface(i_metaclass)
    return language


def get_subclassification() ->Concept:
    return get_language().get_concept_by_name('Subclassification')


def get_specialization() ->Concept:
    return get_language().get_concept_by_name('Specialization')


def get_owning_membership() ->Concept:
    return get_language().get_concept_by_name('OwningMembership')


def get_membership() ->Concept:
    return get_language().get_concept_by_name('Membership')


def get_documentation() ->Concept:
    return get_language().get_concept_by_name('Documentation')


def get_comment() ->Concept:
    return get_language().get_concept_by_name('Comment')


def get_annotation() ->Concept:
    return get_language().get_concept_by_name('Annotation')


def get_textual_representation() ->Concept:
    return get_language().get_concept_by_name('TextualRepresentation')


def get_feature_membership() ->Concept:
    return get_language().get_concept_by_name('FeatureMembership')


def get_redefinition() ->Concept:
    return get_language().get_concept_by_name('Redefinition')


def get_subsetting() ->Concept:
    return get_language().get_concept_by_name('Subsetting')


def get_feature_typing() ->Concept:
    return get_language().get_concept_by_name('FeatureTyping')


def get_type_featuring() ->Concept:
    return get_language().get_concept_by_name('TypeFeaturing')


def get_feature_inverting() ->Concept:
    return get_language().get_concept_by_name('FeatureInverting')


def get_feature_chaining() ->Concept:
    return get_language().get_concept_by_name('FeatureChaining')


def get_reference_subsetting() ->Concept:
    return get_language().get_concept_by_name('ReferenceSubsetting')


def get_cross_subsetting() ->Concept:
    return get_language().get_concept_by_name('CrossSubsetting')


def get_conjugation() ->Concept:
    return get_language().get_concept_by_name('Conjugation')


def get_multiplicity() ->Concept:
    return get_language().get_concept_by_name('Multiplicity')


def get_intersecting() ->Concept:
    return get_language().get_concept_by_name('Intersecting')


def get_unioning() ->Concept:
    return get_language().get_concept_by_name('Unioning')


def get_disjoining() ->Concept:
    return get_language().get_concept_by_name('Disjoining')


def get_differencing() ->Concept:
    return get_language().get_concept_by_name('Differencing')


def get_end_feature_membership() ->Concept:
    return get_language().get_concept_by_name('EndFeatureMembership')


def get_result_expression_membership() ->Concept:
    return get_language().get_concept_by_name('ResultExpressionMembership')


def get_return_parameter_membership() ->Concept:
    return get_language().get_concept_by_name('ReturnParameterMembership')


def get_parameter_membership() ->Concept:
    return get_language().get_concept_by_name('ParameterMembership')


def get_multiplicity_range() ->Concept:
    return get_language().get_concept_by_name('MultiplicityRange')


def get_feature_value() ->Concept:
    return get_language().get_concept_by_name('FeatureValue')


def get_metadata_feature() ->Concept:
    return get_language().get_concept_by_name('MetadataFeature')


def get_item_flow_end() ->Concept:
    return get_language().get_concept_by_name('ItemFlowEnd')


def get_item_feature() ->Concept:
    return get_language().get_concept_by_name('ItemFeature')


def get_element_filter_membership() ->Concept:
    return get_language().get_concept_by_name('ElementFilterMembership')


def get_package() ->Concept:
    return get_language().get_concept_by_name('Package')


def get_library_package() ->Concept:
    return get_language().get_concept_by_name('LibraryPackage')


def get_feature_reference_expression() ->Concept:
    return get_language().get_concept_by_name('FeatureReferenceExpression')


def get_metadata_access_expression() ->Concept:
    return get_language().get_concept_by_name('MetadataAccessExpression')


def get_null_expression() ->Concept:
    return get_language().get_concept_by_name('NullExpression')


def get_index_expression() ->Concept:
    return get_language().get_concept_by_name('IndexExpression')


def get_operator_expression() ->Concept:
    return get_language().get_concept_by_name('OperatorExpression')


def get_invocation_expression() ->Concept:
    return get_language().get_concept_by_name('InvocationExpression')


def get_collect_expression() ->Concept:
    return get_language().get_concept_by_name('CollectExpression')


def get_literal_infinity() ->Concept:
    return get_language().get_concept_by_name('LiteralInfinity')


def get_literal_expression() ->Concept:
    return get_language().get_concept_by_name('LiteralExpression')


def get_literal_integer() ->Concept:
    return get_language().get_concept_by_name('LiteralInteger')


def get_select_expression() ->Concept:
    return get_language().get_concept_by_name('SelectExpression')


def get_literal_rational() ->Concept:
    return get_language().get_concept_by_name('LiteralRational')


def get_literal_boolean() ->Concept:
    return get_language().get_concept_by_name('LiteralBoolean')


def get_literal_string() ->Concept:
    return get_language().get_concept_by_name('LiteralString')


def get_feature_chain_expression() ->Concept:
    return get_language().get_concept_by_name('FeatureChainExpression')


def get_dependency() ->Concept:
    return get_language().get_concept_by_name('Dependency')


def get_namespace_import() ->Concept:
    return get_language().get_concept_by_name('NamespaceImport')


def get_membership_import() ->Concept:
    return get_language().get_concept_by_name('MembershipImport')


def get_interface_usage() ->Concept:
    return get_language().get_concept_by_name('InterfaceUsage')


def get_connection_usage() ->Concept:
    return get_language().get_concept_by_name('ConnectionUsage')


def get_connector_as_usage() ->Concept:
    return get_language().get_concept_by_name('ConnectorAsUsage')


def get_variant_membership() ->Concept:
    return get_language().get_concept_by_name('VariantMembership')


def get_definition() ->Concept:
    return get_language().get_concept_by_name('Definition')


def get_reference_usage() ->Concept:
    return get_language().get_concept_by_name('ReferenceUsage')


def get_attribute_usage() ->Concept:
    return get_language().get_concept_by_name('AttributeUsage')


def get_enumeration_usage() ->Concept:
    return get_language().get_concept_by_name('EnumerationUsage')


def get_enumeration_definition() ->Concept:
    return get_language().get_concept_by_name('EnumerationDefinition')


def get_attribute_definition() ->Concept:
    return get_language().get_concept_by_name('AttributeDefinition')


def get_occurrence_definition() ->Concept:
    return get_language().get_concept_by_name('OccurrenceDefinition')


def get_life_class() ->Concept:
    return get_language().get_concept_by_name('LifeClass')


def get_part_definition() ->Concept:
    return get_language().get_concept_by_name('PartDefinition')


def get_item_definition() ->Concept:
    return get_language().get_concept_by_name('ItemDefinition')


def get_port_usage() ->Concept:
    return get_language().get_concept_by_name('PortUsage')


def get_port_definition() ->Concept:
    return get_language().get_concept_by_name('PortDefinition')


def get_conjugated_port_definition() ->Concept:
    return get_language().get_concept_by_name('ConjugatedPortDefinition')


def get_port_conjugation() ->Concept:
    return get_language().get_concept_by_name('PortConjugation')


def get_flow_connection_usage() ->Concept:
    return get_language().get_concept_by_name('FlowConnectionUsage')


def get_allocation_usage() ->Concept:
    return get_language().get_concept_by_name('AllocationUsage')


def get_allocation_definition() ->Concept:
    return get_language().get_concept_by_name('AllocationDefinition')


def get_connection_definition() ->Concept:
    return get_language().get_concept_by_name('ConnectionDefinition')


def get_state_usage() ->Concept:
    return get_language().get_concept_by_name('StateUsage')


def get_transition_usage() ->Concept:
    return get_language().get_concept_by_name('TransitionUsage')


def get_accept_action_usage() ->Concept:
    return get_language().get_concept_by_name('AcceptActionUsage')


def get_calculation_usage() ->Concept:
    return get_language().get_concept_by_name('CalculationUsage')


def get_requirement_usage() ->Concept:
    return get_language().get_concept_by_name('RequirementUsage')


def get_requirement_definition() ->Concept:
    return get_language().get_concept_by_name('RequirementDefinition')


def get_constraint_definition() ->Concept:
    return get_language().get_concept_by_name('ConstraintDefinition')


def get_concern_usage() ->Concept:
    return get_language().get_concept_by_name('ConcernUsage')


def get_concern_definition() ->Concept:
    return get_language().get_concept_by_name('ConcernDefinition')


def get_case_usage() ->Concept:
    return get_language().get_concept_by_name('CaseUsage')


def get_case_definition() ->Concept:
    return get_language().get_concept_by_name('CaseDefinition')


def get_calculation_definition() ->Concept:
    return get_language().get_concept_by_name('CalculationDefinition')


def get_action_definition() ->Concept:
    return get_language().get_concept_by_name('ActionDefinition')


def get_analysis_case_usage() ->Concept:
    return get_language().get_concept_by_name('AnalysisCaseUsage')


def get_analysis_case_definition() ->Concept:
    return get_language().get_concept_by_name('AnalysisCaseDefinition')


def get_verification_case_usage() ->Concept:
    return get_language().get_concept_by_name('VerificationCaseUsage')


def get_verification_case_definition() ->Concept:
    return get_language().get_concept_by_name('VerificationCaseDefinition')


def get_use_case_usage() ->Concept:
    return get_language().get_concept_by_name('UseCaseUsage')


def get_use_case_definition() ->Concept:
    return get_language().get_concept_by_name('UseCaseDefinition')


def get_view_usage() ->Concept:
    return get_language().get_concept_by_name('ViewUsage')


def get_view_definition() ->Concept:
    return get_language().get_concept_by_name('ViewDefinition')


def get_viewpoint_usage() ->Concept:
    return get_language().get_concept_by_name('ViewpointUsage')


def get_viewpoint_definition() ->Concept:
    return get_language().get_concept_by_name('ViewpointDefinition')


def get_rendering_usage() ->Concept:
    return get_language().get_concept_by_name('RenderingUsage')


def get_rendering_definition() ->Concept:
    return get_language().get_concept_by_name('RenderingDefinition')


def get_metadata_usage() ->Concept:
    return get_language().get_concept_by_name('MetadataUsage')


def get_interface_definition() ->Concept:
    return get_language().get_concept_by_name('InterfaceDefinition')


def get_conjugated_port_typing() ->Concept:
    return get_language().get_concept_by_name('ConjugatedPortTyping')


def get_transition_feature_membership() ->Concept:
    return get_language().get_concept_by_name('TransitionFeatureMembership')


def get_exhibit_state_usage() ->Concept:
    return get_language().get_concept_by_name('ExhibitStateUsage')


def get_state_subaction_membership() ->Concept:
    return get_language().get_concept_by_name('StateSubactionMembership')


def get_state_definition() ->Concept:
    return get_language().get_concept_by_name('StateDefinition')


def get_succession_flow_connection_usage() ->Concept:
    return get_language().get_concept_by_name('SuccessionFlowConnectionUsage')


def get_flow_connection_definition() ->Concept:
    return get_language().get_concept_by_name('FlowConnectionDefinition')


def get_requirement_verification_membership() ->Concept:
    return get_language().get_concept_by_name(
        'RequirementVerificationMembership')


def get_requirement_constraint_membership() ->Concept:
    return get_language().get_concept_by_name('RequirementConstraintMembership'
        )


def get_include_use_case_usage() ->Concept:
    return get_language().get_concept_by_name('IncludeUseCaseUsage')


def get_objective_membership() ->Concept:
    return get_language().get_concept_by_name('ObjectiveMembership')


def get_satisfy_requirement_usage() ->Concept:
    return get_language().get_concept_by_name('SatisfyRequirementUsage')


def get_subject_membership() ->Concept:
    return get_language().get_concept_by_name('SubjectMembership')


def get_stakeholder_membership() ->Concept:
    return get_language().get_concept_by_name('StakeholderMembership')


def get_framed_concern_membership() ->Concept:
    return get_language().get_concept_by_name('FramedConcernMembership')


def get_actor_membership() ->Concept:
    return get_language().get_concept_by_name('ActorMembership')


def get_view_rendering_membership() ->Concept:
    return get_language().get_concept_by_name('ViewRenderingMembership')


def get_namespace_expose() ->Concept:
    return get_language().get_concept_by_name('NamespaceExpose')


def get_membership_expose() ->Concept:
    return get_language().get_concept_by_name('MembershipExpose')


def get_binding_connector_as_usage() ->Concept:
    return get_language().get_concept_by_name('BindingConnectorAsUsage')


def get_succession_as_usage() ->Concept:
    return get_language().get_concept_by_name('SuccessionAsUsage')


def get_fork_node() ->Concept:
    return get_language().get_concept_by_name('ForkNode')


def get_control_node() ->Concept:
    return get_language().get_concept_by_name('ControlNode')


def get_join_node() ->Concept:
    return get_language().get_concept_by_name('JoinNode')


def get_send_action_usage() ->Concept:
    return get_language().get_concept_by_name('SendActionUsage')


def get_decision_node() ->Concept:
    return get_language().get_concept_by_name('DecisionNode')


def get_merge_node() ->Concept:
    return get_language().get_concept_by_name('MergeNode')


def get_loop_action_usage() ->Concept:
    return get_language().get_concept_by_name('LoopActionUsage')


def get_trigger_invocation_expression() ->Concept:
    return get_language().get_concept_by_name('TriggerInvocationExpression')


def get_assignment_action_usage() ->Concept:
    return get_language().get_concept_by_name('AssignmentActionUsage')


def get_for_loop_action_usage() ->Concept:
    return get_language().get_concept_by_name('ForLoopActionUsage')


def get_if_action_usage() ->Concept:
    return get_language().get_concept_by_name('IfActionUsage')


def get_while_loop_action_usage() ->Concept:
    return get_language().get_concept_by_name('WhileLoopActionUsage')


def get_terminate_action_usage() ->Concept:
    return get_language().get_concept_by_name('TerminateActionUsage')


def get_metadata_definition() ->Concept:
    return get_language().get_concept_by_name('MetadataDefinition')


def get_alias_ids_container() ->Concept:
    return get_language().get_concept_by_name('AliasIdsContainer')


def get_text_container() ->Concept:
    return get_language().get_concept_by_name('TextContainer')


def get_featuring() ->Concept:
    return get_language().get_concept_by_name('Featuring')


def get_relationship() ->Concept:
    return get_language().get_concept_by_name('Relationship')


def get_element() ->Concept:
    return get_language().get_concept_by_name('Element')


def get_annotating_element() ->Concept:
    return get_language().get_concept_by_name('AnnotatingElement')


def get_step() ->Concept:
    return get_language().get_concept_by_name('Step')


def get_feature() ->Concept:
    return get_language().get_concept_by_name('Feature')


def get_type() ->Concept:
    return get_language().get_concept_by_name('Type')


def get_namespace() ->Concept:
    return get_language().get_concept_by_name('Namespace')


def get_behavior() ->Concept:
    return get_language().get_concept_by_name('Behavior')


def get_class() ->Concept:
    return get_language().get_concept_by_name('Class')


def get_classifier() ->Concept:
    return get_language().get_concept_by_name('Classifier')


def get_succession() ->Concept:
    return get_language().get_concept_by_name('Succession')


def get_connector() ->Concept:
    return get_language().get_concept_by_name('Connector')


def get_structure() ->Concept:
    return get_language().get_concept_by_name('Structure')


def get_part_usage() ->Concept:
    return get_language().get_concept_by_name('PartUsage')


def get_item_usage() ->Concept:
    return get_language().get_concept_by_name('ItemUsage')


def get_occurrence_usage() ->Concept:
    return get_language().get_concept_by_name('OccurrenceUsage')


def get_usage() ->Concept:
    return get_language().get_concept_by_name('Usage')


def get_data_type() ->Concept:
    return get_language().get_concept_by_name('DataType')


def get_action_usage() ->Concept:
    return get_language().get_concept_by_name('ActionUsage')


def get_item_flow() ->Concept:
    return get_language().get_concept_by_name('ItemFlow')


def get_association_structure() ->Concept:
    return get_language().get_concept_by_name('AssociationStructure')


def get_association() ->Concept:
    return get_language().get_concept_by_name('Association')


def get_predicate() ->Concept:
    return get_language().get_concept_by_name('Predicate')


def get_function() ->Concept:
    return get_language().get_concept_by_name('Function')


def get_perform_action_usage() ->Concept:
    return get_language().get_concept_by_name('PerformActionUsage')


def get_event_occurrence_usage() ->Concept:
    return get_language().get_concept_by_name('EventOccurrenceUsage')


def get_succession_item_flow() ->Concept:
    return get_language().get_concept_by_name('SuccessionItemFlow')


def get_interaction() ->Concept:
    return get_language().get_concept_by_name('Interaction')


def get_assert_constraint_usage() ->Concept:
    return get_language().get_concept_by_name('AssertConstraintUsage')


def get_constraint_usage() ->Concept:
    return get_language().get_concept_by_name('ConstraintUsage')


def get_boolean_expression() ->Concept:
    return get_language().get_concept_by_name('BooleanExpression')


def get_expression() ->Concept:
    return get_language().get_concept_by_name('Expression')


def get_invariant() ->Concept:
    return get_language().get_concept_by_name('Invariant')


def get_expose() ->Concept:
    return get_language().get_concept_by_name('Expose')


def get_import() ->Concept:
    return get_language().get_concept_by_name('Import')


def get_binding_connector() ->Concept:
    return get_language().get_concept_by_name('BindingConnector')


def get_metaclass() ->Concept:
    return get_language().get_concept_by_name('Metaclass')
