from lionweb.language import Language, Concept, Containment, Enumeration, Interface, PrimitiveType, Property, Reference, LionCoreBuiltins
from lionweb.lionweb_version import LionWebVersion
from functools import lru_cache
from sysml2py.types.language import get_language as get_types_language


@lru_cache(maxsize=1)
def get_language() ->Language:
    language = Language(lion_web_version=LionWebVersion.V2023_1, id='kerml',
        name='kerml', key='kerml', version='1')
    i_element = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-IElement', name='IElement', key='kerml-IElement')
    language.add_element(i_element)
    owning_membership = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='kerml-OwningMembership', name='OwningMembership', key=
        'kerml-OwningMembership')
    owning_membership.abstract = False
    owning_membership.partition = False
    language.add_element(owning_membership)
    membership = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Membership', name='Membership', key='kerml-Membership')
    membership.abstract = False
    membership.partition = False
    language.add_element(membership)
    i_relationship = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-IRelationship', name='IRelationship', key='kerml-IRelationship')
    language.add_element(i_relationship)
    i_namespace = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-INamespace', name='INamespace', key='kerml-INamespace')
    language.add_element(i_namespace)
    import_ = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Import', name='Import', key='kerml-Import')
    import_.abstract = True
    import_.partition = False
    language.add_element(import_)
    visibility_kind = Enumeration(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-VisibilityKind', name='VisibilityKind', key=
        'kerml-VisibilityKind')
    language.add_element(visibility_kind)
    documentation = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Documentation', name='Documentation', key='kerml-Documentation')
    documentation.abstract = False
    documentation.partition = False
    language.add_element(documentation)
    comment = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Comment', name='Comment', key='kerml-Comment')
    comment.abstract = False
    comment.partition = False
    language.add_element(comment)
    i_annotating_element = Interface(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IAnnotatingElement', name='IAnnotatingElement',
        key='kerml-IAnnotatingElement')
    language.add_element(i_annotating_element)
    annotation = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Annotation', name='Annotation', key='kerml-Annotation')
    annotation.abstract = False
    annotation.partition = False
    language.add_element(annotation)
    textual_representation = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-TextualRepresentation', name=
        'TextualRepresentation', key='kerml-TextualRepresentation')
    textual_representation.abstract = False
    textual_representation.partition = False
    language.add_element(textual_representation)
    dependency = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Dependency', name='Dependency', key='kerml-Dependency')
    dependency.abstract = False
    dependency.partition = False
    language.add_element(dependency)
    membership_import = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='kerml-MembershipImport', name='MembershipImport', key=
        'kerml-MembershipImport')
    membership_import.abstract = False
    membership_import.partition = False
    language.add_element(membership_import)
    namespace_import = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-NamespaceImport', name='NamespaceImport', key=
        'kerml-NamespaceImport')
    namespace_import.abstract = False
    namespace_import.partition = False
    language.add_element(namespace_import)
    subclassification = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='kerml-Subclassification', name='Subclassification', key=
        'kerml-Subclassification')
    subclassification.abstract = False
    subclassification.partition = False
    language.add_element(subclassification)
    specialization = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Specialization', name='Specialization', key=
        'kerml-Specialization')
    specialization.abstract = False
    specialization.partition = False
    language.add_element(specialization)
    i_type = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-IType', name='IType', key='kerml-IType')
    language.add_element(i_type)
    feature_membership = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-FeatureMembership', name='FeatureMembership', key=
        'kerml-FeatureMembership')
    feature_membership.abstract = False
    feature_membership.partition = False
    language.add_element(feature_membership)
    i_featuring = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-IFeaturing', name='IFeaturing', key='kerml-IFeaturing')
    language.add_element(i_featuring)
    i_feature = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-IFeature', name='IFeature', key='kerml-IFeature')
    language.add_element(i_feature)
    redefinition = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Redefinition', name='Redefinition', key='kerml-Redefinition')
    redefinition.abstract = False
    redefinition.partition = False
    language.add_element(redefinition)
    subsetting = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Subsetting', name='Subsetting', key='kerml-Subsetting')
    subsetting.abstract = False
    subsetting.partition = False
    language.add_element(subsetting)
    feature_typing = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-FeatureTyping', name='FeatureTyping', key='kerml-FeatureTyping')
    feature_typing.abstract = False
    feature_typing.partition = False
    language.add_element(feature_typing)
    type_featuring = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-TypeFeaturing', name='TypeFeaturing', key='kerml-TypeFeaturing')
    type_featuring.abstract = False
    type_featuring.partition = False
    language.add_element(type_featuring)
    feature_inverting = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='kerml-FeatureInverting', name='FeatureInverting', key=
        'kerml-FeatureInverting')
    feature_inverting.abstract = False
    feature_inverting.partition = False
    language.add_element(feature_inverting)
    feature_chaining = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-FeatureChaining', name='FeatureChaining', key=
        'kerml-FeatureChaining')
    feature_chaining.abstract = False
    feature_chaining.partition = False
    language.add_element(feature_chaining)
    feature_direction_kind = Enumeration(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-FeatureDirectionKind', name=
        'FeatureDirectionKind', key='kerml-FeatureDirectionKind')
    language.add_element(feature_direction_kind)
    reference_subsetting = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-ReferenceSubsetting', name='ReferenceSubsetting', key=
        'kerml-ReferenceSubsetting')
    reference_subsetting.abstract = False
    reference_subsetting.partition = False
    language.add_element(reference_subsetting)
    conjugation = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Conjugation', name='Conjugation', key='kerml-Conjugation')
    conjugation.abstract = False
    conjugation.partition = False
    language.add_element(conjugation)
    multiplicity = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Multiplicity', name='Multiplicity', key='kerml-Multiplicity')
    multiplicity.abstract = False
    multiplicity.partition = False
    language.add_element(multiplicity)
    intersecting = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Intersecting', name='Intersecting', key='kerml-Intersecting')
    intersecting.abstract = False
    intersecting.partition = False
    language.add_element(intersecting)
    unioning = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Unioning', name='Unioning', key='kerml-Unioning')
    unioning.abstract = False
    unioning.partition = False
    language.add_element(unioning)
    disjoining = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Disjoining', name='Disjoining', key='kerml-Disjoining')
    disjoining.abstract = False
    disjoining.partition = False
    language.add_element(disjoining)
    differencing = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Differencing', name='Differencing', key='kerml-Differencing')
    differencing.abstract = False
    differencing.partition = False
    language.add_element(differencing)
    i_classifier = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-IClassifier', name='IClassifier', key='kerml-IClassifier')
    language.add_element(i_classifier)
    end_feature_membership = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-EndFeatureMembership', name=
        'EndFeatureMembership', key='kerml-EndFeatureMembership')
    end_feature_membership.abstract = False
    end_feature_membership.partition = False
    language.add_element(end_feature_membership)
    element_filter_membership = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-ElementFilterMembership', name=
        'ElementFilterMembership', key='kerml-ElementFilterMembership')
    element_filter_membership.abstract = False
    element_filter_membership.partition = False
    language.add_element(element_filter_membership)
    expression = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Expression', name='Expression', key='kerml-Expression')
    expression.abstract = False
    expression.partition = False
    language.add_element(expression)
    i_step = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-IStep', name='IStep', key='kerml-IStep')
    language.add_element(i_step)
    i_behavior = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-IBehavior', name='IBehavior', key='kerml-IBehavior')
    language.add_element(i_behavior)
    i_class = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-IClass', name='IClass', key='kerml-IClass')
    language.add_element(i_class)
    function = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Function', name='Function', key='kerml-Function')
    function.abstract = False
    function.partition = False
    language.add_element(function)
    package = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Package', name='Package', key='kerml-Package')
    package.abstract = False
    package.partition = False
    language.add_element(package)
    library_package = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-LibraryPackage', name='LibraryPackage', key=
        'kerml-LibraryPackage')
    library_package.abstract = False
    library_package.partition = False
    language.add_element(library_package)
    invocation_expression = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-InvocationExpression', name='InvocationExpression', key=
        'kerml-InvocationExpression')
    invocation_expression.abstract = False
    invocation_expression.partition = False
    language.add_element(invocation_expression)
    feature_reference_expression = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-FeatureReferenceExpression', name=
        'FeatureReferenceExpression', key='kerml-FeatureReferenceExpression')
    feature_reference_expression.abstract = False
    feature_reference_expression.partition = False
    language.add_element(feature_reference_expression)
    operator_expression = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-OperatorExpression', name='OperatorExpression', key=
        'kerml-OperatorExpression')
    operator_expression.abstract = False
    operator_expression.partition = False
    language.add_element(operator_expression)
    literal_string = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-LiteralString', name='LiteralString', key='kerml-LiteralString')
    literal_string.abstract = False
    literal_string.partition = False
    language.add_element(literal_string)
    literal_expression = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-LiteralExpression', name='LiteralExpression', key=
        'kerml-LiteralExpression')
    literal_expression.abstract = False
    literal_expression.partition = False
    language.add_element(literal_expression)
    literal_boolean = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-LiteralBoolean', name='LiteralBoolean', key=
        'kerml-LiteralBoolean')
    literal_boolean.abstract = False
    literal_boolean.partition = False
    language.add_element(literal_boolean)
    literal_integer = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-LiteralInteger', name='LiteralInteger', key=
        'kerml-LiteralInteger')
    literal_integer.abstract = False
    literal_integer.partition = False
    language.add_element(literal_integer)
    null_expression = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-NullExpression', name='NullExpression', key=
        'kerml-NullExpression')
    null_expression.abstract = False
    null_expression.partition = False
    language.add_element(null_expression)
    metadata_access_expression = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-MetadataAccessExpression', name=
        'MetadataAccessExpression', key='kerml-MetadataAccessExpression')
    metadata_access_expression.abstract = False
    metadata_access_expression.partition = False
    language.add_element(metadata_access_expression)
    metadata_feature = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-MetadataFeature', name='MetadataFeature', key=
        'kerml-MetadataFeature')
    metadata_feature.abstract = False
    metadata_feature.partition = False
    language.add_element(metadata_feature)
    metaclass = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Metaclass', name='Metaclass', key='kerml-Metaclass')
    metaclass.abstract = False
    metaclass.partition = False
    language.add_element(metaclass)
    i_structure = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-IStructure', name='IStructure', key='kerml-IStructure')
    language.add_element(i_structure)
    select_expression = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='kerml-SelectExpression', name='SelectExpression', key=
        'kerml-SelectExpression')
    select_expression.abstract = False
    select_expression.partition = False
    language.add_element(select_expression)
    feature_chain_expression = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-FeatureChainExpression', name=
        'FeatureChainExpression', key='kerml-FeatureChainExpression')
    feature_chain_expression.abstract = False
    feature_chain_expression.partition = False
    language.add_element(feature_chain_expression)
    collect_expression = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-CollectExpression', name='CollectExpression', key=
        'kerml-CollectExpression')
    collect_expression.abstract = False
    collect_expression.partition = False
    language.add_element(collect_expression)
    literal_infinity = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-LiteralInfinity', name='LiteralInfinity', key=
        'kerml-LiteralInfinity')
    literal_infinity.abstract = False
    literal_infinity.partition = False
    language.add_element(literal_infinity)
    literal_rational = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-LiteralRational', name='LiteralRational', key=
        'kerml-LiteralRational')
    literal_rational.abstract = False
    literal_rational.partition = False
    language.add_element(literal_rational)
    multiplicity_range = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-MultiplicityRange', name='MultiplicityRange', key=
        'kerml-MultiplicityRange')
    multiplicity_range.abstract = False
    multiplicity_range.partition = False
    language.add_element(multiplicity_range)
    feature_value = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-FeatureValue', name='FeatureValue', key='kerml-FeatureValue')
    feature_value.abstract = False
    feature_value.partition = False
    language.add_element(feature_value)
    binding_connector = Concept(lion_web_version=LionWebVersion.V2023_1, id
        ='kerml-BindingConnector', name='BindingConnector', key=
        'kerml-BindingConnector')
    binding_connector.abstract = False
    binding_connector.partition = False
    language.add_element(binding_connector)
    i_connector = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-IConnector', name='IConnector', key='kerml-IConnector')
    language.add_element(i_connector)
    association = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Association', name='Association', key='kerml-Association')
    association.abstract = False
    association.partition = False
    language.add_element(association)
    i_succession = Interface(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-ISuccession', name='ISuccession', key='kerml-ISuccession')
    language.add_element(i_succession)
    invariant = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Invariant', name='Invariant', key='kerml-Invariant')
    invariant.abstract = False
    invariant.partition = False
    language.add_element(invariant)
    boolean_expression = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-BooleanExpression', name='BooleanExpression', key=
        'kerml-BooleanExpression')
    boolean_expression.abstract = False
    boolean_expression.partition = False
    language.add_element(boolean_expression)
    predicate = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Predicate', name='Predicate', key='kerml-Predicate')
    predicate.abstract = False
    predicate.partition = False
    language.add_element(predicate)
    return_parameter_membership = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-ReturnParameterMembership', name=
        'ReturnParameterMembership', key='kerml-ReturnParameterMembership')
    return_parameter_membership.abstract = False
    return_parameter_membership.partition = False
    language.add_element(return_parameter_membership)
    parameter_membership = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-ParameterMembership', name='ParameterMembership', key=
        'kerml-ParameterMembership')
    parameter_membership.abstract = False
    parameter_membership.partition = False
    language.add_element(parameter_membership)
    result_expression_membership = Concept(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-ResultExpressionMembership', name=
        'ResultExpressionMembership', key='kerml-ResultExpressionMembership')
    result_expression_membership.abstract = False
    result_expression_membership.partition = False
    language.add_element(result_expression_membership)
    data_type = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-DataType', name='DataType', key='kerml-DataType')
    data_type.abstract = False
    data_type.partition = False
    language.add_element(data_type)
    interaction = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Interaction', name='Interaction', key='kerml-Interaction')
    interaction.abstract = False
    interaction.partition = False
    language.add_element(interaction)
    item_flow_end = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-ItemFlowEnd', name='ItemFlowEnd', key='kerml-ItemFlowEnd')
    item_flow_end.abstract = False
    item_flow_end.partition = False
    language.add_element(item_flow_end)
    item_flow = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-ItemFlow', name='ItemFlow', key='kerml-ItemFlow')
    item_flow.abstract = False
    item_flow.partition = False
    language.add_element(item_flow)
    item_feature = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-ItemFeature', name='ItemFeature', key='kerml-ItemFeature')
    item_feature.abstract = False
    item_feature.partition = False
    language.add_element(item_feature)
    succession_item_flow = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-SuccessionItemFlow', name='SuccessionItemFlow', key=
        'kerml-SuccessionItemFlow')
    succession_item_flow.abstract = False
    succession_item_flow.partition = False
    language.add_element(succession_item_flow)
    association_structure = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-AssociationStructure', name='AssociationStructure', key=
        'kerml-AssociationStructure')
    association_structure.abstract = False
    association_structure.partition = False
    language.add_element(association_structure)
    alias_ids_container = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-AliasIdsContainer', name='AliasIdsContainer', key=
        'kerml-AliasIdsContainer')
    alias_ids_container.abstract = False
    alias_ids_container.partition = False
    language.add_element(alias_ids_container)
    featuring = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Featuring', name='Featuring', key='kerml-Featuring')
    featuring.abstract = False
    featuring.partition = False
    language.add_element(featuring)
    relationship = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Relationship', name='Relationship', key='kerml-Relationship')
    relationship.abstract = False
    relationship.partition = False
    language.add_element(relationship)
    element = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Element', name='Element', key='kerml-Element')
    element.abstract = False
    element.partition = False
    language.add_element(element)
    annotating_element = Concept(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-AnnotatingElement', name='AnnotatingElement', key=
        'kerml-AnnotatingElement')
    annotating_element.abstract = False
    annotating_element.partition = False
    language.add_element(annotating_element)
    behavior = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Behavior', name='Behavior', key='kerml-Behavior')
    behavior.abstract = False
    behavior.partition = False
    language.add_element(behavior)
    class_ = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Class', name='Class', key='kerml-Class')
    class_.abstract = False
    class_.partition = False
    language.add_element(class_)
    classifier = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Classifier', name='Classifier', key='kerml-Classifier')
    classifier.abstract = False
    classifier.partition = False
    language.add_element(classifier)
    type = Concept(lion_web_version=LionWebVersion.V2023_1, id='kerml-Type',
        name='Type', key='kerml-Type')
    type.abstract = False
    type.partition = False
    language.add_element(type)
    namespace = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Namespace', name='Namespace', key='kerml-Namespace')
    namespace.abstract = False
    namespace.partition = False
    language.add_element(namespace)
    step = Concept(lion_web_version=LionWebVersion.V2023_1, id='kerml-Step',
        name='Step', key='kerml-Step')
    step.abstract = False
    step.partition = False
    language.add_element(step)
    feature = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Feature', name='Feature', key='kerml-Feature')
    feature.abstract = False
    feature.partition = False
    language.add_element(feature)
    succession = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Succession', name='Succession', key='kerml-Succession')
    succession.abstract = False
    succession.partition = False
    language.add_element(succession)
    connector = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Connector', name='Connector', key='kerml-Connector')
    connector.abstract = False
    connector.partition = False
    language.add_element(connector)
    structure = Concept(lion_web_version=LionWebVersion.V2023_1, id=
        'kerml-Structure', name='Structure', key='kerml-Structure')
    structure.abstract = False
    structure.partition = False
    language.add_element(structure)
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-owningMembership', name='owningMembership', key=
        'kerml-IElement-owningMembership', type=owning_membership, multiple
        =False, optional=True))
    i_element.add_feature(Containment(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IElement-ownedRelationship', name=
        'ownedRelationship', key='kerml-IElement-ownedRelationship', type=
        i_relationship, multiple=True, optional=True))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-owningRelationship', name='owningRelationship',
        key='kerml-IElement-owningRelationship', type=i_relationship,
        multiple=False, optional=True))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-owningNamespace', name='owningNamespace', key=
        'kerml-IElement-owningNamespace', type=i_namespace, multiple=False,
        optional=True))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-elementId', name='elementId', key=
        'kerml-IElement-elementId', type=get_types_language().
        get_primitive_type_by_name('String')))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-owner', name='owner', key='kerml-IElement-owner',
        type=i_element, multiple=False, optional=True))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-ownedElement', name='ownedElement', key=
        'kerml-IElement-ownedElement', type=i_element, multiple=True,
        optional=True))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-documentation', name='documentation', key=
        'kerml-IElement-documentation', type=documentation, multiple=True,
        optional=True))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-ownedAnnotation', name='ownedAnnotation', key=
        'kerml-IElement-ownedAnnotation', type=annotation, multiple=True,
        optional=True))
    i_element.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-textualRepresentation', name=
        'textualRepresentation', key='kerml-IElement-textualRepresentation',
        type=textual_representation, multiple=True, optional=True))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-declaredShortName', name='declaredShortName',
        key='kerml-IElement-declaredShortName', type=get_types_language().
        get_primitive_type_by_name('String')))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-declaredName', name='declaredName', key=
        'kerml-IElement-declaredName', type=get_types_language().
        get_primitive_type_by_name('String')))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-shortName', name='shortName', key=
        'kerml-IElement-shortName', type=get_types_language().
        get_primitive_type_by_name('String')))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-name', name='name', key='kerml-IElement-name',
        type=get_types_language().get_primitive_type_by_name('String')))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-qualifiedName', name='qualifiedName', key=
        'kerml-IElement-qualifiedName', type=get_types_language().
        get_primitive_type_by_name('String')))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-isImpliedIncluded', name='isImpliedIncluded',
        key='kerml-IElement-isImpliedIncluded', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_element.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IElement-isLibraryElement', name='isLibraryElement', key=
        'kerml-IElement-isLibraryElement', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_element.add_feature(Containment(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IElement-aliasIdsContainer', name=
        'aliasIdsContainer', key='kerml-IElement-aliasIdsContainer', type=
        alias_ids_container, multiple=True, optional=True))
    owning_membership.set_extended_concept(membership)
    owning_membership.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-OwningMembership-ownedMemberElementId', name=
        'ownedMemberElementId', key=
        'kerml-OwningMembership-ownedMemberElementId', type=
        get_types_language().get_primitive_type_by_name('String')))
    owning_membership.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-OwningMembership-ownedMemberShortName', name=
        'ownedMemberShortName', key=
        'kerml-OwningMembership-ownedMemberShortName', type=
        get_types_language().get_primitive_type_by_name('String')))
    owning_membership.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-OwningMembership-ownedMemberName', name=
        'ownedMemberName', key='kerml-OwningMembership-ownedMemberName',
        type=get_types_language().get_primitive_type_by_name('String')))
    owning_membership.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='kerml-OwningMembership-ownedMemberElement', name=
        'ownedMemberElement', key=
        'kerml-OwningMembership-ownedMemberElement', type=i_element,
        multiple=False, optional=False))
    membership.add_implemented_interface(i_relationship)
    membership.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Membership-membershipOwningNamespace', name=
        'membershipOwningNamespace', key=
        'kerml-Membership-membershipOwningNamespace', type=i_namespace,
        multiple=False, optional=False))
    membership.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Membership-memberElementId', name='memberElementId', key=
        'kerml-Membership-memberElementId', type=get_types_language().
        get_primitive_type_by_name('String')))
    membership.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Membership-memberShortName', name='memberShortName', key=
        'kerml-Membership-memberShortName', type=get_types_language().
        get_primitive_type_by_name('String')))
    membership.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Membership-memberElement', name='memberElement',
        key='kerml-Membership-memberElement', type=i_element, multiple=
        False, optional=False))
    membership.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Membership-memberName', name='memberName', key=
        'kerml-Membership-memberName', type=get_types_language().
        get_primitive_type_by_name('String')))
    membership.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Membership-visibility', name='visibility', key=
        'kerml-Membership-visibility', type=visibility_kind))
    i_relationship.add_extended_interface(i_element)
    i_relationship.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IRelationship-relatedElement', name=
        'relatedElement', key='kerml-IRelationship-relatedElement', type=
        i_element, multiple=True, optional=True))
    i_relationship.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IRelationship-target', name='target', key=
        'kerml-IRelationship-target', type=i_element, multiple=True,
        optional=True))
    i_relationship.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IRelationship-source', name='source', key=
        'kerml-IRelationship-source', type=i_element, multiple=True,
        optional=True))
    i_relationship.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IRelationship-owningRelatedElement', name=
        'owningRelatedElement', key=
        'kerml-IRelationship-owningRelatedElement', type=i_element,
        multiple=False, optional=True))
    i_relationship.add_feature(Containment(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IRelationship-ownedRelatedElement', name=
        'ownedRelatedElement', key=
        'kerml-IRelationship-ownedRelatedElement', type=i_element, multiple
        =True, optional=True))
    i_relationship.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IRelationship-isImplied', name='isImplied', key=
        'kerml-IRelationship-isImplied', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_namespace.add_extended_interface(i_element)
    i_namespace.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-INamespace-membership', name='membership', key=
        'kerml-INamespace-membership', type=membership, multiple=True,
        optional=True))
    i_namespace.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-INamespace-ownedImport', name='ownedImport', key
        ='kerml-INamespace-ownedImport', type=import_, multiple=True,
        optional=True))
    i_namespace.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-INamespace-member', name='member', key=
        'kerml-INamespace-member', type=i_element, multiple=True, optional=
        True))
    i_namespace.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-INamespace-ownedMember', name='ownedMember', key
        ='kerml-INamespace-ownedMember', type=i_element, multiple=True,
        optional=True))
    i_namespace.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-INamespace-ownedMembership', name=
        'ownedMembership', key='kerml-INamespace-ownedMembership', type=
        membership, multiple=True, optional=True))
    i_namespace.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-INamespace-importedMembership', name=
        'importedMembership', key='kerml-INamespace-importedMembership',
        type=membership, multiple=True, optional=True))
    import_.add_implemented_interface(i_relationship)
    import_.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Import-visibility', name='visibility', key=
        'kerml-Import-visibility', type=visibility_kind))
    import_.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Import-isRecursive', name='isRecursive', key=
        'kerml-Import-isRecursive', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    import_.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Import-isImportAll', name='isImportAll', key=
        'kerml-Import-isImportAll', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    import_.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Import-importedElement', name='importedElement', key=
        'kerml-Import-importedElement', type=i_element, multiple=False,
        optional=False))
    import_.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Import-importOwningNamespace', name=
        'importOwningNamespace', key='kerml-Import-importOwningNamespace',
        type=i_namespace, multiple=False, optional=False))
    documentation.set_extended_concept(comment)
    documentation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Documentation-documentedElement', name=
        'documentedElement', key='kerml-Documentation-documentedElement',
        type=i_element, multiple=False, optional=False))
    comment.add_implemented_interface(i_annotating_element)
    comment.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Comment-locale', name='locale', key=
        'kerml-Comment-locale', type=get_types_language().
        get_primitive_type_by_name('String')))
    comment.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Comment-body', name='body', key='kerml-Comment-body',
        type=get_types_language().get_primitive_type_by_name('String')))
    i_annotating_element.add_extended_interface(i_element)
    i_annotating_element.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'kerml-IAnnotatingElement-annotatedElement', name=
        'annotatedElement', key='kerml-IAnnotatingElement-annotatedElement',
        type=i_element, multiple=True, optional=False))
    i_annotating_element.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'kerml-IAnnotatingElement-ownedAnnotatingRelationship', name=
        'ownedAnnotatingRelationship', key=
        'kerml-IAnnotatingElement-ownedAnnotatingRelationship', type=
        annotation, multiple=True, optional=True))
    i_annotating_element.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='kerml-IAnnotatingElement-annotation',
        name='annotation', key='kerml-IAnnotatingElement-annotation', type=
        annotation, multiple=True, optional=True))
    annotation.add_implemented_interface(i_relationship)
    annotation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Annotation-annotatingElement', name=
        'annotatingElement', key='kerml-Annotation-annotatingElement', type
        =i_annotating_element, multiple=False, optional=False))
    annotation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Annotation-annotatedElement', name=
        'annotatedElement', key='kerml-Annotation-annotatedElement', type=
        i_element, multiple=False, optional=False))
    annotation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Annotation-owningAnnotatedElement', name=
        'owningAnnotatedElement', key=
        'kerml-Annotation-owningAnnotatedElement', type=i_element, multiple
        =False, optional=True))
    annotation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Annotation-owningAnnotatingElement', name=
        'owningAnnotatingElement', key=
        'kerml-Annotation-owningAnnotatingElement', type=
        i_annotating_element, multiple=False, optional=True))
    textual_representation.add_implemented_interface(i_annotating_element)
    textual_representation.add_feature(Property(lion_web_version=
        LionWebVersion.V2023_1, id='kerml-TextualRepresentation-language',
        name='language', key='kerml-TextualRepresentation-language', type=
        get_types_language().get_primitive_type_by_name('String')))
    textual_representation.add_feature(Property(lion_web_version=
        LionWebVersion.V2023_1, id='kerml-TextualRepresentation-body', name
        ='body', key='kerml-TextualRepresentation-body', type=
        get_types_language().get_primitive_type_by_name('String')))
    textual_representation.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'kerml-TextualRepresentation-representedElement', name=
        'representedElement', key=
        'kerml-TextualRepresentation-representedElement', type=i_element,
        multiple=False, optional=False))
    dependency.add_implemented_interface(i_relationship)
    dependency.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Dependency-client', name='client', key=
        'kerml-Dependency-client', type=i_element, multiple=True, optional=
        False))
    dependency.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Dependency-supplier', name='supplier', key=
        'kerml-Dependency-supplier', type=i_element, multiple=True,
        optional=False))
    membership_import.set_extended_concept(import_)
    membership_import.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='kerml-MembershipImport-importedMembership', name=
        'importedMembership', key=
        'kerml-MembershipImport-importedMembership', type=membership,
        multiple=False, optional=False))
    namespace_import.set_extended_concept(import_)
    namespace_import.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-NamespaceImport-importedNamespace', name=
        'importedNamespace', key='kerml-NamespaceImport-importedNamespace',
        type=i_namespace, multiple=False, optional=False))
    subclassification.set_extended_concept(specialization)
    subclassification.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='kerml-Subclassification-superclassifier', name=
        'superclassifier', key='kerml-Subclassification-superclassifier',
        type=i_classifier, multiple=False, optional=False))
    subclassification.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='kerml-Subclassification-owningClassifier', name=
        'owningClassifier', key='kerml-Subclassification-owningClassifier',
        type=i_classifier, multiple=False, optional=True))
    subclassification.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='kerml-Subclassification-subclassifier', name=
        'subclassifier', key='kerml-Subclassification-subclassifier', type=
        i_classifier, multiple=False, optional=False))
    specialization.add_implemented_interface(i_relationship)
    specialization.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Specialization-owningType', name='owningType',
        key='kerml-Specialization-owningType', type=i_type, multiple=False,
        optional=True))
    specialization.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Specialization-general', name='general', key=
        'kerml-Specialization-general', type=i_type, multiple=False,
        optional=False))
    specialization.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Specialization-specific', name='specific', key=
        'kerml-Specialization-specific', type=i_type, multiple=False,
        optional=False))
    i_type.add_extended_interface(i_namespace)
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-ownedFeatureMembership', name=
        'ownedFeatureMembership', key='kerml-IType-ownedFeatureMembership',
        type=feature_membership, multiple=True, optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-ownedFeature', name='ownedFeature', key=
        'kerml-IType-ownedFeature', type=i_feature, multiple=True, optional
        =True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-ownedEndFeature', name='ownedEndFeature', key=
        'kerml-IType-ownedEndFeature', type=i_feature, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-feature', name='feature', key='kerml-IType-feature',
        type=i_feature, multiple=True, optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-input', name='input', key='kerml-IType-input', type
        =i_feature, multiple=True, optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-output', name='output', key='kerml-IType-output',
        type=i_feature, multiple=True, optional=True))
    i_type.add_feature(Property(lion_web_version=LionWebVersion.V2023_1, id
        ='kerml-IType-isAbstract', name='isAbstract', key=
        'kerml-IType-isAbstract', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-inheritedMembership', name='inheritedMembership',
        key='kerml-IType-inheritedMembership', type=membership, multiple=
        True, optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-endFeature', name='endFeature', key=
        'kerml-IType-endFeature', type=i_feature, multiple=True, optional=True)
        )
    i_type.add_feature(Property(lion_web_version=LionWebVersion.V2023_1, id
        ='kerml-IType-isSufficient', name='isSufficient', key=
        'kerml-IType-isSufficient', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-ownedConjugator', name='ownedConjugator', key=
        'kerml-IType-ownedConjugator', type=conjugation, multiple=False,
        optional=True))
    i_type.add_feature(Property(lion_web_version=LionWebVersion.V2023_1, id
        ='kerml-IType-isConjugated', name='isConjugated', key=
        'kerml-IType-isConjugated', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-inheritedFeature', name='inheritedFeature', key=
        'kerml-IType-inheritedFeature', type=i_feature, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-multiplicity', name='multiplicity', key=
        'kerml-IType-multiplicity', type=multiplicity, multiple=False,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-unioningType', name='unioningType', key=
        'kerml-IType-unioningType', type=i_type, multiple=True, optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-ownedIntersecting', name='ownedIntersecting', key=
        'kerml-IType-ownedIntersecting', type=intersecting, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-intersectingType', name='intersectingType', key=
        'kerml-IType-intersectingType', type=i_type, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-ownedUnioning', name='ownedUnioning', key=
        'kerml-IType-ownedUnioning', type=unioning, multiple=True, optional
        =True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-ownedDisjoining', name='ownedDisjoining', key=
        'kerml-IType-ownedDisjoining', type=disjoining, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-featureMembership', name='featureMembership', key=
        'kerml-IType-featureMembership', type=feature_membership, multiple=
        True, optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-differencingType', name='differencingType', key=
        'kerml-IType-differencingType', type=i_type, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-ownedDifferencing', name='ownedDifferencing', key=
        'kerml-IType-ownedDifferencing', type=differencing, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-directedFeature', name='directedFeature', key=
        'kerml-IType-directedFeature', type=i_feature, multiple=True,
        optional=True))
    i_type.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IType-ownedSpecialization', name='ownedSpecialization',
        key='kerml-IType-ownedSpecialization', type=specialization,
        multiple=True, optional=True))
    feature_membership.set_extended_concept(owning_membership)
    feature_membership.add_implemented_interface(i_featuring)
    feature_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'kerml-FeatureMembership-ownedMemberFeature', name=
        'ownedMemberFeature', key=
        'kerml-FeatureMembership-ownedMemberFeature', type=i_feature,
        multiple=False, optional=False))
    feature_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='kerml-FeatureMembership-owningType',
        name='owningType', key='kerml-FeatureMembership-owningType', type=
        i_type, multiple=False, optional=False))
    i_featuring.add_extended_interface(i_relationship)
    i_featuring.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IFeaturing-type', name='type', key=
        'kerml-IFeaturing-type', type=i_type, multiple=False, optional=False))
    i_featuring.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IFeaturing-feature', name='feature', key=
        'kerml-IFeaturing-feature', type=i_feature, multiple=False,
        optional=False))
    i_feature.add_extended_interface(i_type)
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-owningType', name='owningType', key=
        'kerml-IFeature-owningType', type=i_type, multiple=False, optional=
        True))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-isUnique', name='isUnique', key=
        'kerml-IFeature-isUnique', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-isOrdered', name='isOrdered', key=
        'kerml-IFeature-isOrdered', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-type', name='type', key='kerml-IFeature-type',
        type=i_type, multiple=True, optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-ownedRedefinition', name='ownedRedefinition',
        key='kerml-IFeature-ownedRedefinition', type=redefinition, multiple
        =True, optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-ownedSubsetting', name='ownedSubsetting', key=
        'kerml-IFeature-ownedSubsetting', type=subsetting, multiple=True,
        optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-owningFeatureMembership', name=
        'owningFeatureMembership', key=
        'kerml-IFeature-owningFeatureMembership', type=feature_membership,
        multiple=False, optional=True))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-isComposite', name='isComposite', key=
        'kerml-IFeature-isComposite', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-isEnd', name='isEnd', key='kerml-IFeature-isEnd',
        type=get_types_language().get_primitive_type_by_name('Boolean')))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-endOwningType', name='endOwningType', key=
        'kerml-IFeature-endOwningType', type=i_type, multiple=False,
        optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-ownedTyping', name='ownedTyping', key=
        'kerml-IFeature-ownedTyping', type=feature_typing, multiple=True,
        optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-featuringType', name='featuringType', key=
        'kerml-IFeature-featuringType', type=i_type, multiple=True,
        optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-ownedTypeFeaturing', name='ownedTypeFeaturing',
        key='kerml-IFeature-ownedTypeFeaturing', type=type_featuring,
        multiple=True, optional=True))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-isDerived', name='isDerived', key=
        'kerml-IFeature-isDerived', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-chainingFeature', name='chainingFeature', key=
        'kerml-IFeature-chainingFeature', type=i_feature, multiple=True,
        optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-ownedFeatureInverting', name=
        'ownedFeatureInverting', key='kerml-IFeature-ownedFeatureInverting',
        type=feature_inverting, multiple=True, optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-ownedFeatureChaining', name=
        'ownedFeatureChaining', key='kerml-IFeature-ownedFeatureChaining',
        type=feature_chaining, multiple=True, optional=True))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-isReadOnly', name='isReadOnly', key=
        'kerml-IFeature-isReadOnly', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-isPortion', name='isPortion', key=
        'kerml-IFeature-isPortion', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-direction', name='direction', key=
        'kerml-IFeature-direction', type=feature_direction_kind))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-ownedReferenceSubsetting', name=
        'ownedReferenceSubsetting', key=
        'kerml-IFeature-ownedReferenceSubsetting', type=
        reference_subsetting, multiple=False, optional=True))
    i_feature.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-featureTarget', name='featureTarget', key=
        'kerml-IFeature-featureTarget', type=i_feature, multiple=False,
        optional=False))
    i_feature.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IFeature-isNonunique', name='isNonunique', key=
        'kerml-IFeature-isNonunique', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    redefinition.set_extended_concept(subsetting)
    redefinition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Redefinition-redefiningFeature', name=
        'redefiningFeature', key='kerml-Redefinition-redefiningFeature',
        type=i_feature, multiple=False, optional=False))
    redefinition.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Redefinition-redefinedFeature', name=
        'redefinedFeature', key='kerml-Redefinition-redefinedFeature', type
        =i_feature, multiple=False, optional=False))
    subsetting.set_extended_concept(specialization)
    subsetting.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Subsetting-subsettedFeature', name=
        'subsettedFeature', key='kerml-Subsetting-subsettedFeature', type=
        i_feature, multiple=False, optional=False))
    subsetting.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Subsetting-subsettingFeature', name=
        'subsettingFeature', key='kerml-Subsetting-subsettingFeature', type
        =i_feature, multiple=False, optional=False))
    subsetting.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Subsetting-owningFeature', name='owningFeature',
        key='kerml-Subsetting-owningFeature', type=i_feature, multiple=
        False, optional=True))
    feature_typing.set_extended_concept(specialization)
    feature_typing.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-FeatureTyping-typedFeature', name='typedFeature',
        key='kerml-FeatureTyping-typedFeature', type=i_feature, multiple=
        False, optional=False))
    feature_typing.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-FeatureTyping-type', name='type', key=
        'kerml-FeatureTyping-type', type=i_type, multiple=False, optional=
        False))
    feature_typing.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-FeatureTyping-owningFeature', name=
        'owningFeature', key='kerml-FeatureTyping-owningFeature', type=
        i_feature, multiple=False, optional=True))
    type_featuring.add_implemented_interface(i_featuring)
    type_featuring.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-TypeFeaturing-featureOfType', name=
        'featureOfType', key='kerml-TypeFeaturing-featureOfType', type=
        i_feature, multiple=False, optional=False))
    type_featuring.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-TypeFeaturing-featuringType', name=
        'featuringType', key='kerml-TypeFeaturing-featuringType', type=
        i_type, multiple=False, optional=False))
    type_featuring.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-TypeFeaturing-owningFeatureOfType', name=
        'owningFeatureOfType', key=
        'kerml-TypeFeaturing-owningFeatureOfType', type=i_feature, multiple
        =False, optional=True))
    feature_inverting.add_implemented_interface(i_relationship)
    feature_inverting.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='kerml-FeatureInverting-featureInverted', name=
        'featureInverted', key='kerml-FeatureInverting-featureInverted',
        type=i_feature, multiple=False, optional=False))
    feature_inverting.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='kerml-FeatureInverting-invertingFeature', name=
        'invertingFeature', key='kerml-FeatureInverting-invertingFeature',
        type=i_feature, multiple=False, optional=False))
    feature_inverting.add_feature(Reference(lion_web_version=LionWebVersion
        .V2023_1, id='kerml-FeatureInverting-owningFeature', name=
        'owningFeature', key='kerml-FeatureInverting-owningFeature', type=
        i_feature, multiple=False, optional=True))
    feature_chaining.add_implemented_interface(i_relationship)
    feature_chaining.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-FeatureChaining-chainingFeature', name=
        'chainingFeature', key='kerml-FeatureChaining-chainingFeature',
        type=i_feature, multiple=False, optional=False))
    feature_chaining.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-FeatureChaining-featureChained', name=
        'featureChained', key='kerml-FeatureChaining-featureChained', type=
        i_feature, multiple=False, optional=False))
    reference_subsetting.set_extended_concept(subsetting)
    reference_subsetting.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'kerml-ReferenceSubsetting-referencedFeature', name=
        'referencedFeature', key=
        'kerml-ReferenceSubsetting-referencedFeature', type=i_feature,
        multiple=False, optional=False))
    reference_subsetting.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'kerml-ReferenceSubsetting-referencingFeature', name=
        'referencingFeature', key=
        'kerml-ReferenceSubsetting-referencingFeature', type=i_feature,
        multiple=False, optional=False))
    conjugation.add_implemented_interface(i_relationship)
    conjugation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Conjugation-originalType', name='originalType',
        key='kerml-Conjugation-originalType', type=i_type, multiple=False,
        optional=False))
    conjugation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Conjugation-conjugatedType', name=
        'conjugatedType', key='kerml-Conjugation-conjugatedType', type=
        i_type, multiple=False, optional=False))
    conjugation.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Conjugation-owningType', name='owningType', key=
        'kerml-Conjugation-owningType', type=i_type, multiple=False,
        optional=True))
    multiplicity.add_implemented_interface(i_feature)
    intersecting.add_implemented_interface(i_relationship)
    intersecting.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Intersecting-intersectingType', name=
        'intersectingType', key='kerml-Intersecting-intersectingType', type
        =i_type, multiple=False, optional=False))
    intersecting.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Intersecting-typeIntersected', name=
        'typeIntersected', key='kerml-Intersecting-typeIntersected', type=
        i_type, multiple=False, optional=False))
    unioning.add_implemented_interface(i_relationship)
    unioning.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Unioning-unioningType', name='unioningType', key=
        'kerml-Unioning-unioningType', type=i_type, multiple=False,
        optional=False))
    unioning.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Unioning-typeUnioned', name='typeUnioned', key=
        'kerml-Unioning-typeUnioned', type=i_type, multiple=False, optional
        =False))
    disjoining.add_implemented_interface(i_relationship)
    disjoining.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Disjoining-typeDisjoined', name='typeDisjoined',
        key='kerml-Disjoining-typeDisjoined', type=i_type, multiple=False,
        optional=False))
    disjoining.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Disjoining-disjoiningType', name=
        'disjoiningType', key='kerml-Disjoining-disjoiningType', type=
        i_type, multiple=False, optional=False))
    disjoining.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Disjoining-owningType', name='owningType', key=
        'kerml-Disjoining-owningType', type=i_type, multiple=False,
        optional=True))
    differencing.add_implemented_interface(i_relationship)
    differencing.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Differencing-differencingType', name=
        'differencingType', key='kerml-Differencing-differencingType', type
        =i_type, multiple=False, optional=False))
    differencing.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Differencing-typeDifferenced', name=
        'typeDifferenced', key='kerml-Differencing-typeDifferenced', type=
        i_type, multiple=False, optional=False))
    i_classifier.add_extended_interface(i_type)
    i_classifier.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IClassifier-ownedSubclassification', name=
        'ownedSubclassification', key=
        'kerml-IClassifier-ownedSubclassification', type=subclassification,
        multiple=True, optional=True))
    end_feature_membership.set_extended_concept(feature_membership)
    element_filter_membership.set_extended_concept(owning_membership)
    element_filter_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'kerml-ElementFilterMembership-condition', name='condition', key=
        'kerml-ElementFilterMembership-condition', type=expression,
        multiple=False, optional=False))
    expression.add_implemented_interface(i_step)
    expression.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Expression-function', name='function', key=
        'kerml-Expression-function', type=function, multiple=False,
        optional=True))
    expression.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Expression-result', name='result', key=
        'kerml-Expression-result', type=i_feature, multiple=False, optional
        =False))
    expression.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Expression-isModelLevelEvaluable', name=
        'isModelLevelEvaluable', key=
        'kerml-Expression-isModelLevelEvaluable', type=get_types_language()
        .get_primitive_type_by_name('Boolean')))
    i_step.add_extended_interface(i_feature)
    i_step.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IStep-behavior', name='behavior', key=
        'kerml-IStep-behavior', type=i_behavior, multiple=True, optional=True))
    i_step.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-IStep-parameter', name='parameter', key=
        'kerml-IStep-parameter', type=i_feature, multiple=True, optional=True))
    i_behavior.add_extended_interface(i_class)
    i_behavior.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IBehavior-step', name='step', key=
        'kerml-IBehavior-step', type=i_step, multiple=True, optional=True))
    i_behavior.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IBehavior-parameter', name='parameter', key=
        'kerml-IBehavior-parameter', type=i_feature, multiple=True,
        optional=True))
    i_class.add_extended_interface(i_classifier)
    function.add_implemented_interface(i_behavior)
    function.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Function-expression', name='expression', key=
        'kerml-Function-expression', type=expression, multiple=True,
        optional=True))
    function.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Function-result', name='result', key=
        'kerml-Function-result', type=i_feature, multiple=False, optional=
        False))
    function.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Function-isModelLevelEvaluable', name=
        'isModelLevelEvaluable', key='kerml-Function-isModelLevelEvaluable',
        type=get_types_language().get_primitive_type_by_name('Boolean')))
    package.add_implemented_interface(i_namespace)
    package.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Package-filterCondition', name='filterCondition', key=
        'kerml-Package-filterCondition', type=expression, multiple=True,
        optional=True))
    library_package.set_extended_concept(package)
    library_package.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-LibraryPackage-isStandard', name='isStandard',
        key='kerml-LibraryPackage-isStandard', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    invocation_expression.set_extended_concept(expression)
    invocation_expression.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='kerml-InvocationExpression-argument',
        name='argument', key='kerml-InvocationExpression-argument', type=
        expression, multiple=True, optional=True))
    invocation_expression.add_feature(Containment(lion_web_version=
        LionWebVersion.V2023_1, id='kerml-InvocationExpression-operand',
        name='operand', key='kerml-InvocationExpression-operand', type=
        expression, multiple=True, optional=True))
    feature_reference_expression.set_extended_concept(expression)
    feature_reference_expression.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'kerml-FeatureReferenceExpression-referent', name='referent', key=
        'kerml-FeatureReferenceExpression-referent', type=i_feature,
        multiple=False, optional=False))
    operator_expression.set_extended_concept(invocation_expression)
    operator_expression.add_feature(Property(lion_web_version=
        LionWebVersion.V2023_1, id='kerml-OperatorExpression-operator',
        name='operator', key='kerml-OperatorExpression-operator', type=
        get_types_language().get_primitive_type_by_name('String')))
    literal_string.set_extended_concept(literal_expression)
    literal_string.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-LiteralString-value', name='value', key=
        'kerml-LiteralString-value', type=get_types_language().
        get_primitive_type_by_name('String')))
    literal_expression.set_extended_concept(expression)
    literal_boolean.set_extended_concept(literal_expression)
    literal_boolean.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-LiteralBoolean-value', name='value', key=
        'kerml-LiteralBoolean-value', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    literal_integer.set_extended_concept(literal_expression)
    literal_integer.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-LiteralInteger-value', name='value', key=
        'kerml-LiteralInteger-value', type=get_types_language().
        get_primitive_type_by_name('Integer')))
    null_expression.set_extended_concept(expression)
    metadata_access_expression.set_extended_concept(expression)
    metadata_access_expression.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'kerml-MetadataAccessExpression-referencedElement', name=
        'referencedElement', key=
        'kerml-MetadataAccessExpression-referencedElement', type=i_element,
        multiple=False, optional=False))
    metadata_feature.add_implemented_interface(i_feature)
    metadata_feature.add_implemented_interface(i_annotating_element)
    metadata_feature.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-MetadataFeature-metaclass', name='metaclass',
        key='kerml-MetadataFeature-metaclass', type=metaclass, multiple=
        False, optional=True))
    metaclass.add_implemented_interface(i_structure)
    i_structure.add_extended_interface(i_class)
    select_expression.set_extended_concept(operator_expression)
    feature_chain_expression.set_extended_concept(operator_expression)
    feature_chain_expression.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'kerml-FeatureChainExpression-targetFeature', name='targetFeature',
        key='kerml-FeatureChainExpression-targetFeature', type=i_feature,
        multiple=False, optional=False))
    collect_expression.set_extended_concept(operator_expression)
    literal_infinity.set_extended_concept(literal_expression)
    literal_rational.set_extended_concept(literal_expression)
    literal_rational.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-LiteralRational-value', name='value', key=
        'kerml-LiteralRational-value', type=get_types_language().
        get_primitive_type_by_name('Real')))
    multiplicity_range.set_extended_concept(multiplicity)
    multiplicity_range.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='kerml-MultiplicityRange-lowerBound',
        name='lowerBound', key='kerml-MultiplicityRange-lowerBound', type=
        expression, multiple=False, optional=True))
    multiplicity_range.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='kerml-MultiplicityRange-upperBound',
        name='upperBound', key='kerml-MultiplicityRange-upperBound', type=
        expression, multiple=False, optional=False))
    multiplicity_range.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='kerml-MultiplicityRange-bound', name=
        'bound', key='kerml-MultiplicityRange-bound', type=expression,
        multiple=True, optional=False))
    feature_value.set_extended_concept(owning_membership)
    feature_value.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-FeatureValue-featureWithValue', name=
        'featureWithValue', key='kerml-FeatureValue-featureWithValue', type
        =i_feature, multiple=False, optional=False))
    feature_value.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-FeatureValue-value', name='value', key=
        'kerml-FeatureValue-value', type=expression, multiple=False,
        optional=False))
    feature_value.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-FeatureValue-isInitial', name='isInitial', key=
        'kerml-FeatureValue-isInitial', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    feature_value.add_feature(Property(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-FeatureValue-isDefault', name='isDefault', key=
        'kerml-FeatureValue-isDefault', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    binding_connector.add_implemented_interface(i_connector)
    i_connector.add_extended_interface(i_feature)
    i_connector.add_extended_interface(i_relationship)
    i_connector.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IConnector-relatedFeature', name=
        'relatedFeature', key='kerml-IConnector-relatedFeature', type=
        i_feature, multiple=True, optional=True))
    i_connector.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IConnector-association', name='association', key
        ='kerml-IConnector-association', type=association, multiple=True,
        optional=True))
    i_connector.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IConnector-connectorEnd', name='connectorEnd',
        key='kerml-IConnector-connectorEnd', type=i_feature, multiple=True,
        optional=True))
    i_connector.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IConnector-sourceFeature', name='sourceFeature',
        key='kerml-IConnector-sourceFeature', type=i_feature, multiple=
        False, optional=True))
    i_connector.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-IConnector-targetFeature', name='targetFeature',
        key='kerml-IConnector-targetFeature', type=i_feature, multiple=True,
        optional=True))
    association.add_implemented_interface(i_classifier)
    association.add_implemented_interface(i_relationship)
    association.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Association-relatedType', name='relatedType',
        key='kerml-Association-relatedType', type=i_type, multiple=True,
        optional=True))
    association.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Association-sourceType', name='sourceType', key=
        'kerml-Association-sourceType', type=i_type, multiple=False,
        optional=True))
    association.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Association-targetType', name='targetType', key=
        'kerml-Association-targetType', type=i_type, multiple=True,
        optional=True))
    association.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-Association-associationEnd', name=
        'associationEnd', key='kerml-Association-associationEnd', type=
        i_feature, multiple=True, optional=True))
    i_succession.add_extended_interface(i_connector)
    i_succession.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-ISuccession-transitionStep', name=
        'transitionStep', key='kerml-ISuccession-transitionStep', type=
        i_step, multiple=False, optional=True))
    i_succession.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-ISuccession-triggerStep', name='triggerStep',
        key='kerml-ISuccession-triggerStep', type=i_step, multiple=True,
        optional=True))
    i_succession.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-ISuccession-effectStep', name='effectStep', key=
        'kerml-ISuccession-effectStep', type=i_step, multiple=True,
        optional=True))
    i_succession.add_feature(Reference(lion_web_version=LionWebVersion.
        V2023_1, id='kerml-ISuccession-guardExpression', name=
        'guardExpression', key='kerml-ISuccession-guardExpression', type=
        expression, multiple=True, optional=True))
    invariant.set_extended_concept(boolean_expression)
    invariant.add_feature(Property(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-Invariant-isNegated', name='isNegated', key=
        'kerml-Invariant-isNegated', type=get_types_language().
        get_primitive_type_by_name('Boolean')))
    boolean_expression.set_extended_concept(expression)
    boolean_expression.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id='kerml-BooleanExpression-predicate',
        name='predicate', key='kerml-BooleanExpression-predicate', type=
        predicate, multiple=False, optional=True))
    predicate.set_extended_concept(function)
    return_parameter_membership.set_extended_concept(parameter_membership)
    parameter_membership.set_extended_concept(feature_membership)
    parameter_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'kerml-ParameterMembership-ownedMemberParameter', name=
        'ownedMemberParameter', key=
        'kerml-ParameterMembership-ownedMemberParameter', type=i_feature,
        multiple=False, optional=False))
    result_expression_membership.set_extended_concept(feature_membership)
    result_expression_membership.add_feature(Reference(lion_web_version=
        LionWebVersion.V2023_1, id=
        'kerml-ResultExpressionMembership-ownedResultExpression', name=
        'ownedResultExpression', key=
        'kerml-ResultExpressionMembership-ownedResultExpression', type=
        expression, multiple=False, optional=False))
    data_type.add_implemented_interface(i_classifier)
    interaction.set_extended_concept(association)
    interaction.add_implemented_interface(i_behavior)
    item_flow_end.add_implemented_interface(i_feature)
    item_flow.add_implemented_interface(i_connector)
    item_flow.add_implemented_interface(i_step)
    item_flow.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-ItemFlow-itemType', name='itemType', key=
        'kerml-ItemFlow-itemType', type=i_classifier, multiple=True,
        optional=True))
    item_flow.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-ItemFlow-targetInputFeature', name='targetInputFeature',
        key='kerml-ItemFlow-targetInputFeature', type=i_feature, multiple=
        False, optional=True))
    item_flow.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-ItemFlow-sourceOutputFeature', name='sourceOutputFeature',
        key='kerml-ItemFlow-sourceOutputFeature', type=i_feature, multiple=
        False, optional=True))
    item_flow.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-ItemFlow-itemFlowEnd', name='itemFlowEnd', key=
        'kerml-ItemFlow-itemFlowEnd', type=item_flow_end, multiple=True,
        optional=True))
    item_flow.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-ItemFlow-itemFeature', name='itemFeature', key=
        'kerml-ItemFlow-itemFeature', type=item_feature, multiple=False,
        optional=True))
    item_flow.add_feature(Reference(lion_web_version=LionWebVersion.V2023_1,
        id='kerml-ItemFlow-interaction', name='interaction', key=
        'kerml-ItemFlow-interaction', type=interaction, multiple=True,
        optional=True))
    item_feature.add_implemented_interface(i_feature)
    succession_item_flow.set_extended_concept(item_flow)
    succession_item_flow.add_implemented_interface(i_succession)
    association_structure.set_extended_concept(association)
    association_structure.add_implemented_interface(i_structure)
    alias_ids_container.add_feature(Property(lion_web_version=
        LionWebVersion.V2023_1, id='kerml-AliasIdsContainer-aliasIds', name
        ='aliasIds', key='kerml-AliasIdsContainer-aliasIds', type=
        get_types_language().get_primitive_type_by_name('String')))
    featuring.add_implemented_interface(i_featuring)
    relationship.add_implemented_interface(i_relationship)
    element.add_implemented_interface(i_element)
    annotating_element.add_implemented_interface(i_annotating_element)
    behavior.add_implemented_interface(i_behavior)
    class_.add_implemented_interface(i_class)
    classifier.add_implemented_interface(i_classifier)
    type.add_implemented_interface(i_type)
    namespace.add_implemented_interface(i_namespace)
    step.add_implemented_interface(i_step)
    feature.add_implemented_interface(i_feature)
    succession.add_implemented_interface(i_succession)
    connector.add_implemented_interface(i_connector)
    structure.add_implemented_interface(i_structure)
    return language


def get_owning_membership() ->Concept:
    return get_language().get_concept_by_name('OwningMembership')


def get_membership() ->Concept:
    return get_language().get_concept_by_name('Membership')


def get_import() ->Concept:
    return get_language().get_concept_by_name('Import')


def get_documentation() ->Concept:
    return get_language().get_concept_by_name('Documentation')


def get_comment() ->Concept:
    return get_language().get_concept_by_name('Comment')


def get_annotation() ->Concept:
    return get_language().get_concept_by_name('Annotation')


def get_textual_representation() ->Concept:
    return get_language().get_concept_by_name('TextualRepresentation')


def get_dependency() ->Concept:
    return get_language().get_concept_by_name('Dependency')


def get_membership_import() ->Concept:
    return get_language().get_concept_by_name('MembershipImport')


def get_namespace_import() ->Concept:
    return get_language().get_concept_by_name('NamespaceImport')


def get_subclassification() ->Concept:
    return get_language().get_concept_by_name('Subclassification')


def get_specialization() ->Concept:
    return get_language().get_concept_by_name('Specialization')


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


def get_element_filter_membership() ->Concept:
    return get_language().get_concept_by_name('ElementFilterMembership')


def get_expression() ->Concept:
    return get_language().get_concept_by_name('Expression')


def get_function() ->Concept:
    return get_language().get_concept_by_name('Function')


def get_package() ->Concept:
    return get_language().get_concept_by_name('Package')


def get_library_package() ->Concept:
    return get_language().get_concept_by_name('LibraryPackage')


def get_invocation_expression() ->Concept:
    return get_language().get_concept_by_name('InvocationExpression')


def get_feature_reference_expression() ->Concept:
    return get_language().get_concept_by_name('FeatureReferenceExpression')


def get_operator_expression() ->Concept:
    return get_language().get_concept_by_name('OperatorExpression')


def get_literal_string() ->Concept:
    return get_language().get_concept_by_name('LiteralString')


def get_literal_expression() ->Concept:
    return get_language().get_concept_by_name('LiteralExpression')


def get_literal_boolean() ->Concept:
    return get_language().get_concept_by_name('LiteralBoolean')


def get_literal_integer() ->Concept:
    return get_language().get_concept_by_name('LiteralInteger')


def get_null_expression() ->Concept:
    return get_language().get_concept_by_name('NullExpression')


def get_metadata_access_expression() ->Concept:
    return get_language().get_concept_by_name('MetadataAccessExpression')


def get_metadata_feature() ->Concept:
    return get_language().get_concept_by_name('MetadataFeature')


def get_metaclass() ->Concept:
    return get_language().get_concept_by_name('Metaclass')


def get_select_expression() ->Concept:
    return get_language().get_concept_by_name('SelectExpression')


def get_feature_chain_expression() ->Concept:
    return get_language().get_concept_by_name('FeatureChainExpression')


def get_collect_expression() ->Concept:
    return get_language().get_concept_by_name('CollectExpression')


def get_literal_infinity() ->Concept:
    return get_language().get_concept_by_name('LiteralInfinity')


def get_literal_rational() ->Concept:
    return get_language().get_concept_by_name('LiteralRational')


def get_multiplicity_range() ->Concept:
    return get_language().get_concept_by_name('MultiplicityRange')


def get_feature_value() ->Concept:
    return get_language().get_concept_by_name('FeatureValue')


def get_binding_connector() ->Concept:
    return get_language().get_concept_by_name('BindingConnector')


def get_association() ->Concept:
    return get_language().get_concept_by_name('Association')


def get_invariant() ->Concept:
    return get_language().get_concept_by_name('Invariant')


def get_boolean_expression() ->Concept:
    return get_language().get_concept_by_name('BooleanExpression')


def get_predicate() ->Concept:
    return get_language().get_concept_by_name('Predicate')


def get_return_parameter_membership() ->Concept:
    return get_language().get_concept_by_name('ReturnParameterMembership')


def get_parameter_membership() ->Concept:
    return get_language().get_concept_by_name('ParameterMembership')


def get_result_expression_membership() ->Concept:
    return get_language().get_concept_by_name('ResultExpressionMembership')


def get_data_type() ->Concept:
    return get_language().get_concept_by_name('DataType')


def get_interaction() ->Concept:
    return get_language().get_concept_by_name('Interaction')


def get_item_flow_end() ->Concept:
    return get_language().get_concept_by_name('ItemFlowEnd')


def get_item_flow() ->Concept:
    return get_language().get_concept_by_name('ItemFlow')


def get_item_feature() ->Concept:
    return get_language().get_concept_by_name('ItemFeature')


def get_succession_item_flow() ->Concept:
    return get_language().get_concept_by_name('SuccessionItemFlow')


def get_association_structure() ->Concept:
    return get_language().get_concept_by_name('AssociationStructure')


def get_alias_ids_container() ->Concept:
    return get_language().get_concept_by_name('AliasIdsContainer')


def get_featuring() ->Concept:
    return get_language().get_concept_by_name('Featuring')


def get_relationship() ->Concept:
    return get_language().get_concept_by_name('Relationship')


def get_element() ->Concept:
    return get_language().get_concept_by_name('Element')


def get_annotating_element() ->Concept:
    return get_language().get_concept_by_name('AnnotatingElement')


def get_behavior() ->Concept:
    return get_language().get_concept_by_name('Behavior')


def get_class() ->Concept:
    return get_language().get_concept_by_name('Class')


def get_classifier() ->Concept:
    return get_language().get_concept_by_name('Classifier')


def get_type() ->Concept:
    return get_language().get_concept_by_name('Type')


def get_namespace() ->Concept:
    return get_language().get_concept_by_name('Namespace')


def get_step() ->Concept:
    return get_language().get_concept_by_name('Step')


def get_feature() ->Concept:
    return get_language().get_concept_by_name('Feature')


def get_succession() ->Concept:
    return get_language().get_concept_by_name('Succession')


def get_connector() ->Concept:
    return get_language().get_concept_by_name('Connector')


def get_structure() ->Concept:
    return get_language().get_concept_by_name('Structure')
