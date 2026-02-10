package io.lionweb.sysml2;

import io.lionweb.LionWebVersion;
import io.lionweb.language.Concept;
import io.lionweb.language.Containment;
import io.lionweb.language.Enumeration;
import io.lionweb.language.EnumerationLiteral;
import io.lionweb.language.Interface;
import io.lionweb.language.Language;
import io.lionweb.language.Property;
import io.lionweb.language.Reference;

public class SysmlLanguage extends Language {
  private static SysmlLanguage INSTANCE;

  private SysmlLanguage() {
    super(LionWebVersion.v2023_1);
    this.setName("sysml");
    this.setVersion("1");
    this.setID("sysml");
    this.setKey("sysml");
    this.addDependency(TypesLanguage.getInstance());
    createElements();
    initSubclassification();
    initSpecialization();
    initOwningMembership();
    initMembership();
    initDocumentation();
    initComment();
    initAnnotation();
    initTextualRepresentation();
    initFeatureMembership();
    initRedefinition();
    initSubsetting();
    initFeatureTyping();
    initTypeFeaturing();
    initFeatureInverting();
    initFeatureChaining();
    initReferenceSubsetting();
    initCrossSubsetting();
    initConjugation();
    initMultiplicity();
    initIntersecting();
    initUnioning();
    initDisjoining();
    initDifferencing();
    initEndFeatureMembership();
    initResultExpressionMembership();
    initReturnParameterMembership();
    initParameterMembership();
    initMultiplicityRange();
    initFeatureValue();
    initMetadataFeature();
    initItemFlowEnd();
    initItemFeature();
    initElementFilterMembership();
    initPackage();
    initLibraryPackage();
    initFeatureReferenceExpression();
    initMetadataAccessExpression();
    initNullExpression();
    initIndexExpression();
    initOperatorExpression();
    initInvocationExpression();
    initCollectExpression();
    initLiteralInfinity();
    initLiteralExpression();
    initLiteralInteger();
    initSelectExpression();
    initLiteralRational();
    initLiteralBoolean();
    initLiteralString();
    initFeatureChainExpression();
    initDependency();
    initNamespaceImport();
    initMembershipImport();
    initInterfaceUsage();
    initConnectionUsage();
    initConnectorAsUsage();
    initVariantMembership();
    initDefinition();
    initReferenceUsage();
    initAttributeUsage();
    initEnumerationUsage();
    initEnumerationDefinition();
    initAttributeDefinition();
    initOccurrenceDefinition();
    initLifeClass();
    initPartDefinition();
    initItemDefinition();
    initPortUsage();
    initPortDefinition();
    initConjugatedPortDefinition();
    initPortConjugation();
    initFlowConnectionUsage();
    initAllocationUsage();
    initAllocationDefinition();
    initConnectionDefinition();
    initStateUsage();
    initTransitionUsage();
    initAcceptActionUsage();
    initCalculationUsage();
    initRequirementUsage();
    initRequirementDefinition();
    initConstraintDefinition();
    initConcernUsage();
    initConcernDefinition();
    initCaseUsage();
    initCaseDefinition();
    initCalculationDefinition();
    initActionDefinition();
    initAnalysisCaseUsage();
    initAnalysisCaseDefinition();
    initVerificationCaseUsage();
    initVerificationCaseDefinition();
    initUseCaseUsage();
    initUseCaseDefinition();
    initViewUsage();
    initViewDefinition();
    initViewpointUsage();
    initViewpointDefinition();
    initRenderingUsage();
    initRenderingDefinition();
    initMetadataUsage();
    initInterfaceDefinition();
    initConjugatedPortTyping();
    initTransitionFeatureMembership();
    initExhibitStateUsage();
    initStateSubactionMembership();
    initStateDefinition();
    initSuccessionFlowConnectionUsage();
    initFlowConnectionDefinition();
    initRequirementVerificationMembership();
    initRequirementConstraintMembership();
    initIncludeUseCaseUsage();
    initObjectiveMembership();
    initSatisfyRequirementUsage();
    initSubjectMembership();
    initStakeholderMembership();
    initFramedConcernMembership();
    initActorMembership();
    initViewRenderingMembership();
    initNamespaceExpose();
    initMembershipExpose();
    initBindingConnectorAsUsage();
    initSuccessionAsUsage();
    initForkNode();
    initControlNode();
    initJoinNode();
    initSendActionUsage();
    initDecisionNode();
    initMergeNode();
    initLoopActionUsage();
    initTriggerInvocationExpression();
    initAssignmentActionUsage();
    initForLoopActionUsage();
    initIfActionUsage();
    initWhileLoopActionUsage();
    initTerminateActionUsage();
    initMetadataDefinition();
    initAliasIdsContainer();
    initTextContainer();
    initFeaturing();
    initRelationship();
    initElement();
    initAnnotatingElement();
    initStep();
    initFeature();
    initType();
    initNamespace();
    initBehavior();
    initClass();
    initClassifier();
    initSuccession();
    initConnector();
    initStructure();
    initPartUsage();
    initItemUsage();
    initOccurrenceUsage();
    initUsage();
    initDataType();
    initActionUsage();
    initItemFlow();
    initAssociationStructure();
    initAssociation();
    initPredicate();
    initFunction();
    initPerformActionUsage();
    initEventOccurrenceUsage();
    initSuccessionItemFlow();
    initInteraction();
    initAssertConstraintUsage();
    initConstraintUsage();
    initBooleanExpression();
    initExpression();
    initInvariant();
    initExpose();
    initImport();
    initBindingConnector();
    initMetaclass();
    initIRelationship();
    initIElement();
    initINamespace();
    initIImport();
    initIAnnotatingElement();
    initIType();
    initIFeaturing();
    initIFeature();
    initIClassifier();
    initIExpression();
    initIStep();
    initIBehavior();
    initIClass();
    initIFunction();
    initIInvariant();
    initIBooleanExpression();
    initIPredicate();
    initIStructure();
    initIMetaclass();
    initIItemFlow();
    initIConnector();
    initIAssociation();
    initIInteraction();
    initISuccessionItemFlow();
    initISuccession();
    initIDataType();
    initIBindingConnector();
    initIAssociationStructure();
    initIUsage();
    initIOccurrenceUsage();
    initIItemUsage();
    initIPartUsage();
    initIActionUsage();
    initIConstraintUsage();
    initIPerformActionUsage();
    initIEventOccurrenceUsage();
    initIAssertConstraintUsage();
    initIExpose();
  }

  public static SysmlLanguage getInstance() {
    if (INSTANCE == null) {
      INSTANCE = new SysmlLanguage();
    }
    return INSTANCE;
  }

  public Concept getSubclassification() {
    return this.requireConceptByName("Subclassification");
  }

  private void initSubclassification() {
    Concept concept = this.requireConceptByName("Subclassification");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Specialization"));
    Reference superclassifier = new Reference("superclassifier", concept, "sysml-Subclassification-superclassifier");
    superclassifier.setKey("sysml-Subclassification-superclassifier");
    superclassifier.setType(this.requireClassifierByName("IClassifier"));
    superclassifier.setOptional(false);
    superclassifier.setMultiple(false);
    Reference owningClassifier = new Reference("owningClassifier", concept, "sysml-Subclassification-owningClassifier");
    owningClassifier.setKey("sysml-Subclassification-owningClassifier");
    owningClassifier.setType(this.requireClassifierByName("IClassifier"));
    owningClassifier.setOptional(true);
    owningClassifier.setMultiple(false);
    Reference subclassifier = new Reference("subclassifier", concept, "sysml-Subclassification-subclassifier");
    subclassifier.setKey("sysml-Subclassification-subclassifier");
    subclassifier.setType(this.requireClassifierByName("IClassifier"));
    subclassifier.setOptional(false);
    subclassifier.setMultiple(false);
  }

  public Concept getSpecialization() {
    return this.requireConceptByName("Specialization");
  }

  private void initSpecialization() {
    Concept concept = this.requireConceptByName("Specialization");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Reference owningType = new Reference("owningType", concept, "sysml-Specialization-owningType");
    owningType.setKey("sysml-Specialization-owningType");
    owningType.setType(this.requireClassifierByName("IType"));
    owningType.setOptional(true);
    owningType.setMultiple(false);
    Reference general = new Reference("general", concept, "sysml-Specialization-general");
    general.setKey("sysml-Specialization-general");
    general.setType(this.requireClassifierByName("IType"));
    general.setOptional(false);
    general.setMultiple(false);
    Reference specific = new Reference("specific", concept, "sysml-Specialization-specific");
    specific.setKey("sysml-Specialization-specific");
    specific.setType(this.requireClassifierByName("IType"));
    specific.setOptional(false);
    specific.setMultiple(false);
  }

  public Concept getOwningMembership() {
    return this.requireConceptByName("OwningMembership");
  }

  private void initOwningMembership() {
    Concept concept = this.requireConceptByName("OwningMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Membership"));
    Property ownedMemberElementId = new Property("ownedMemberElementId", concept, "sysml-OwningMembership-ownedMemberElementId");
    ownedMemberElementId.setKey("sysml-OwningMembership-ownedMemberElementId");
    ownedMemberElementId.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    ownedMemberElementId.setOptional(false);
    Property ownedMemberShortName = new Property("ownedMemberShortName", concept, "sysml-OwningMembership-ownedMemberShortName");
    ownedMemberShortName.setKey("sysml-OwningMembership-ownedMemberShortName");
    ownedMemberShortName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    ownedMemberShortName.setOptional(true);
    Property ownedMemberName = new Property("ownedMemberName", concept, "sysml-OwningMembership-ownedMemberName");
    ownedMemberName.setKey("sysml-OwningMembership-ownedMemberName");
    ownedMemberName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    ownedMemberName.setOptional(true);
    Reference ownedMemberElement = new Reference("ownedMemberElement", concept, "sysml-OwningMembership-ownedMemberElement");
    ownedMemberElement.setKey("sysml-OwningMembership-ownedMemberElement");
    ownedMemberElement.setType(this.requireClassifierByName("IElement"));
    ownedMemberElement.setOptional(false);
    ownedMemberElement.setMultiple(false);
  }

  public Concept getMembership() {
    return this.requireConceptByName("Membership");
  }

  private void initMembership() {
    Concept concept = this.requireConceptByName("Membership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Property memberElementId = new Property("memberElementId", concept, "sysml-Membership-memberElementId");
    memberElementId.setKey("sysml-Membership-memberElementId");
    memberElementId.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    memberElementId.setOptional(false);
    Reference membershipOwningNamespace = new Reference("membershipOwningNamespace", concept, "sysml-Membership-membershipOwningNamespace");
    membershipOwningNamespace.setKey("sysml-Membership-membershipOwningNamespace");
    membershipOwningNamespace.setType(this.requireClassifierByName("INamespace"));
    membershipOwningNamespace.setOptional(false);
    membershipOwningNamespace.setMultiple(false);
    Property memberShortName = new Property("memberShortName", concept, "sysml-Membership-memberShortName");
    memberShortName.setKey("sysml-Membership-memberShortName");
    memberShortName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    memberShortName.setOptional(true);
    Reference memberElement = new Reference("memberElement", concept, "sysml-Membership-memberElement");
    memberElement.setKey("sysml-Membership-memberElement");
    memberElement.setType(this.requireClassifierByName("IElement"));
    memberElement.setOptional(false);
    memberElement.setMultiple(false);
    Property memberName = new Property("memberName", concept, "sysml-Membership-memberName");
    memberName.setKey("sysml-Membership-memberName");
    memberName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    memberName.setOptional(true);
    Property visibility = new Property("visibility", concept, "sysml-Membership-visibility");
    visibility.setKey("sysml-Membership-visibility");
    visibility.setType(this.requireDataTypeByName("VisibilityKind"));
    visibility.setOptional(false);
  }

  public Concept getDocumentation() {
    return this.requireConceptByName("Documentation");
  }

  private void initDocumentation() {
    Concept concept = this.requireConceptByName("Documentation");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Comment"));
    Reference documentedElement = new Reference("documentedElement", concept, "sysml-Documentation-documentedElement");
    documentedElement.setKey("sysml-Documentation-documentedElement");
    documentedElement.setType(this.requireClassifierByName("IElement"));
    documentedElement.setOptional(false);
    documentedElement.setMultiple(false);
  }

  public Concept getComment() {
    return this.requireConceptByName("Comment");
  }

  private void initComment() {
    Concept concept = this.requireConceptByName("Comment");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IAnnotatingElement"));
    Property locale = new Property("locale", concept, "sysml-Comment-locale");
    locale.setKey("sysml-Comment-locale");
    locale.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    locale.setOptional(true);
    Property body = new Property("body", concept, "sysml-Comment-body");
    body.setKey("sysml-Comment-body");
    body.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    body.setOptional(false);
  }

  public Concept getAnnotation() {
    return this.requireConceptByName("Annotation");
  }

  private void initAnnotation() {
    Concept concept = this.requireConceptByName("Annotation");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Reference annotatingElement = new Reference("annotatingElement", concept, "sysml-Annotation-annotatingElement");
    annotatingElement.setKey("sysml-Annotation-annotatingElement");
    annotatingElement.setType(this.requireClassifierByName("IAnnotatingElement"));
    annotatingElement.setOptional(false);
    annotatingElement.setMultiple(false);
    Reference annotatedElement = new Reference("annotatedElement", concept, "sysml-Annotation-annotatedElement");
    annotatedElement.setKey("sysml-Annotation-annotatedElement");
    annotatedElement.setType(this.requireClassifierByName("IElement"));
    annotatedElement.setOptional(false);
    annotatedElement.setMultiple(false);
    Reference owningAnnotatedElement = new Reference("owningAnnotatedElement", concept, "sysml-Annotation-owningAnnotatedElement");
    owningAnnotatedElement.setKey("sysml-Annotation-owningAnnotatedElement");
    owningAnnotatedElement.setType(this.requireClassifierByName("IElement"));
    owningAnnotatedElement.setOptional(true);
    owningAnnotatedElement.setMultiple(false);
    Reference ownedAnnotatingElement = new Reference("ownedAnnotatingElement", concept, "sysml-Annotation-ownedAnnotatingElement");
    ownedAnnotatingElement.setKey("sysml-Annotation-ownedAnnotatingElement");
    ownedAnnotatingElement.setType(this.requireClassifierByName("IAnnotatingElement"));
    ownedAnnotatingElement.setOptional(true);
    ownedAnnotatingElement.setMultiple(false);
    Reference owningAnnotatingElement = new Reference("owningAnnotatingElement", concept, "sysml-Annotation-owningAnnotatingElement");
    owningAnnotatingElement.setKey("sysml-Annotation-owningAnnotatingElement");
    owningAnnotatingElement.setType(this.requireClassifierByName("IAnnotatingElement"));
    owningAnnotatingElement.setOptional(true);
    owningAnnotatingElement.setMultiple(false);
  }

  public Concept getTextualRepresentation() {
    return this.requireConceptByName("TextualRepresentation");
  }

  private void initTextualRepresentation() {
    Concept concept = this.requireConceptByName("TextualRepresentation");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IAnnotatingElement"));
    Property language = new Property("language", concept, "sysml-TextualRepresentation-language");
    language.setKey("sysml-TextualRepresentation-language");
    language.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    language.setOptional(false);
    Property body = new Property("body", concept, "sysml-TextualRepresentation-body");
    body.setKey("sysml-TextualRepresentation-body");
    body.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    body.setOptional(false);
    Reference representedElement = new Reference("representedElement", concept, "sysml-TextualRepresentation-representedElement");
    representedElement.setKey("sysml-TextualRepresentation-representedElement");
    representedElement.setType(this.requireClassifierByName("IElement"));
    representedElement.setOptional(false);
    representedElement.setMultiple(false);
  }

  public Concept getFeatureMembership() {
    return this.requireConceptByName("FeatureMembership");
  }

  private void initFeatureMembership() {
    Concept concept = this.requireConceptByName("FeatureMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("OwningMembership"));
    concept.addImplementedInterface(this.requireInterfaceByName("IFeaturing"));
    Reference ownedMemberFeature = new Reference("ownedMemberFeature", concept, "sysml-FeatureMembership-ownedMemberFeature");
    ownedMemberFeature.setKey("sysml-FeatureMembership-ownedMemberFeature");
    ownedMemberFeature.setType(this.requireClassifierByName("IFeature"));
    ownedMemberFeature.setOptional(false);
    ownedMemberFeature.setMultiple(false);
    Reference owningType = new Reference("owningType", concept, "sysml-FeatureMembership-owningType");
    owningType.setKey("sysml-FeatureMembership-owningType");
    owningType.setType(this.requireClassifierByName("IType"));
    owningType.setOptional(false);
    owningType.setMultiple(false);
  }

  public Concept getRedefinition() {
    return this.requireConceptByName("Redefinition");
  }

  private void initRedefinition() {
    Concept concept = this.requireConceptByName("Redefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Subsetting"));
    Reference redefiningFeature = new Reference("redefiningFeature", concept, "sysml-Redefinition-redefiningFeature");
    redefiningFeature.setKey("sysml-Redefinition-redefiningFeature");
    redefiningFeature.setType(this.requireClassifierByName("IFeature"));
    redefiningFeature.setOptional(false);
    redefiningFeature.setMultiple(false);
    Reference redefinedFeature = new Reference("redefinedFeature", concept, "sysml-Redefinition-redefinedFeature");
    redefinedFeature.setKey("sysml-Redefinition-redefinedFeature");
    redefinedFeature.setType(this.requireClassifierByName("IFeature"));
    redefinedFeature.setOptional(false);
    redefinedFeature.setMultiple(false);
  }

  public Concept getSubsetting() {
    return this.requireConceptByName("Subsetting");
  }

  private void initSubsetting() {
    Concept concept = this.requireConceptByName("Subsetting");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Specialization"));
    Reference subsettedFeature = new Reference("subsettedFeature", concept, "sysml-Subsetting-subsettedFeature");
    subsettedFeature.setKey("sysml-Subsetting-subsettedFeature");
    subsettedFeature.setType(this.requireClassifierByName("IFeature"));
    subsettedFeature.setOptional(false);
    subsettedFeature.setMultiple(false);
    Reference subsettingFeature = new Reference("subsettingFeature", concept, "sysml-Subsetting-subsettingFeature");
    subsettingFeature.setKey("sysml-Subsetting-subsettingFeature");
    subsettingFeature.setType(this.requireClassifierByName("IFeature"));
    subsettingFeature.setOptional(false);
    subsettingFeature.setMultiple(false);
    Reference owningFeature = new Reference("owningFeature", concept, "sysml-Subsetting-owningFeature");
    owningFeature.setKey("sysml-Subsetting-owningFeature");
    owningFeature.setType(this.requireClassifierByName("IFeature"));
    owningFeature.setOptional(true);
    owningFeature.setMultiple(false);
  }

  public Concept getFeatureTyping() {
    return this.requireConceptByName("FeatureTyping");
  }

  private void initFeatureTyping() {
    Concept concept = this.requireConceptByName("FeatureTyping");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Specialization"));
    Reference typedFeature = new Reference("typedFeature", concept, "sysml-FeatureTyping-typedFeature");
    typedFeature.setKey("sysml-FeatureTyping-typedFeature");
    typedFeature.setType(this.requireClassifierByName("IFeature"));
    typedFeature.setOptional(false);
    typedFeature.setMultiple(false);
    Reference type = new Reference("type", concept, "sysml-FeatureTyping-type");
    type.setKey("sysml-FeatureTyping-type");
    type.setType(this.requireClassifierByName("IType"));
    type.setOptional(false);
    type.setMultiple(false);
    Reference owningFeature = new Reference("owningFeature", concept, "sysml-FeatureTyping-owningFeature");
    owningFeature.setKey("sysml-FeatureTyping-owningFeature");
    owningFeature.setType(this.requireClassifierByName("IFeature"));
    owningFeature.setOptional(true);
    owningFeature.setMultiple(false);
  }

  public Concept getTypeFeaturing() {
    return this.requireConceptByName("TypeFeaturing");
  }

  private void initTypeFeaturing() {
    Concept concept = this.requireConceptByName("TypeFeaturing");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IFeaturing"));
    Reference featureOfType = new Reference("featureOfType", concept, "sysml-TypeFeaturing-featureOfType");
    featureOfType.setKey("sysml-TypeFeaturing-featureOfType");
    featureOfType.setType(this.requireClassifierByName("IFeature"));
    featureOfType.setOptional(false);
    featureOfType.setMultiple(false);
    Reference featuringType = new Reference("featuringType", concept, "sysml-TypeFeaturing-featuringType");
    featuringType.setKey("sysml-TypeFeaturing-featuringType");
    featuringType.setType(this.requireClassifierByName("IType"));
    featuringType.setOptional(false);
    featuringType.setMultiple(false);
    Reference owningFeatureOfType = new Reference("owningFeatureOfType", concept, "sysml-TypeFeaturing-owningFeatureOfType");
    owningFeatureOfType.setKey("sysml-TypeFeaturing-owningFeatureOfType");
    owningFeatureOfType.setType(this.requireClassifierByName("IFeature"));
    owningFeatureOfType.setOptional(true);
    owningFeatureOfType.setMultiple(false);
  }

  public Concept getFeatureInverting() {
    return this.requireConceptByName("FeatureInverting");
  }

  private void initFeatureInverting() {
    Concept concept = this.requireConceptByName("FeatureInverting");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Reference featureInverted = new Reference("featureInverted", concept, "sysml-FeatureInverting-featureInverted");
    featureInverted.setKey("sysml-FeatureInverting-featureInverted");
    featureInverted.setType(this.requireClassifierByName("IFeature"));
    featureInverted.setOptional(false);
    featureInverted.setMultiple(false);
    Reference invertingFeature = new Reference("invertingFeature", concept, "sysml-FeatureInverting-invertingFeature");
    invertingFeature.setKey("sysml-FeatureInverting-invertingFeature");
    invertingFeature.setType(this.requireClassifierByName("IFeature"));
    invertingFeature.setOptional(false);
    invertingFeature.setMultiple(false);
    Reference owningFeature = new Reference("owningFeature", concept, "sysml-FeatureInverting-owningFeature");
    owningFeature.setKey("sysml-FeatureInverting-owningFeature");
    owningFeature.setType(this.requireClassifierByName("IFeature"));
    owningFeature.setOptional(true);
    owningFeature.setMultiple(false);
  }

  public Concept getFeatureChaining() {
    return this.requireConceptByName("FeatureChaining");
  }

  private void initFeatureChaining() {
    Concept concept = this.requireConceptByName("FeatureChaining");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Reference chainingFeature = new Reference("chainingFeature", concept, "sysml-FeatureChaining-chainingFeature");
    chainingFeature.setKey("sysml-FeatureChaining-chainingFeature");
    chainingFeature.setType(this.requireClassifierByName("IFeature"));
    chainingFeature.setOptional(false);
    chainingFeature.setMultiple(false);
    Reference featureChained = new Reference("featureChained", concept, "sysml-FeatureChaining-featureChained");
    featureChained.setKey("sysml-FeatureChaining-featureChained");
    featureChained.setType(this.requireClassifierByName("IFeature"));
    featureChained.setOptional(false);
    featureChained.setMultiple(false);
  }

  public Concept getReferenceSubsetting() {
    return this.requireConceptByName("ReferenceSubsetting");
  }

  private void initReferenceSubsetting() {
    Concept concept = this.requireConceptByName("ReferenceSubsetting");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Subsetting"));
    Reference referencedFeature = new Reference("referencedFeature", concept, "sysml-ReferenceSubsetting-referencedFeature");
    referencedFeature.setKey("sysml-ReferenceSubsetting-referencedFeature");
    referencedFeature.setType(this.requireClassifierByName("IFeature"));
    referencedFeature.setOptional(false);
    referencedFeature.setMultiple(false);
    Reference referencingFeature = new Reference("referencingFeature", concept, "sysml-ReferenceSubsetting-referencingFeature");
    referencingFeature.setKey("sysml-ReferenceSubsetting-referencingFeature");
    referencingFeature.setType(this.requireClassifierByName("IFeature"));
    referencingFeature.setOptional(false);
    referencingFeature.setMultiple(false);
  }

  public Concept getCrossSubsetting() {
    return this.requireConceptByName("CrossSubsetting");
  }

  private void initCrossSubsetting() {
    Concept concept = this.requireConceptByName("CrossSubsetting");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Subsetting"));
    Reference crossedFeature = new Reference("crossedFeature", concept, "sysml-CrossSubsetting-crossedFeature");
    crossedFeature.setKey("sysml-CrossSubsetting-crossedFeature");
    crossedFeature.setType(this.requireClassifierByName("IFeature"));
    crossedFeature.setOptional(false);
    crossedFeature.setMultiple(false);
    Reference crossingFeature = new Reference("crossingFeature", concept, "sysml-CrossSubsetting-crossingFeature");
    crossingFeature.setKey("sysml-CrossSubsetting-crossingFeature");
    crossingFeature.setType(this.requireClassifierByName("IFeature"));
    crossingFeature.setOptional(false);
    crossingFeature.setMultiple(false);
  }

  public Concept getConjugation() {
    return this.requireConceptByName("Conjugation");
  }

  private void initConjugation() {
    Concept concept = this.requireConceptByName("Conjugation");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Reference originalType = new Reference("originalType", concept, "sysml-Conjugation-originalType");
    originalType.setKey("sysml-Conjugation-originalType");
    originalType.setType(this.requireClassifierByName("IType"));
    originalType.setOptional(false);
    originalType.setMultiple(false);
    Reference conjugatedType = new Reference("conjugatedType", concept, "sysml-Conjugation-conjugatedType");
    conjugatedType.setKey("sysml-Conjugation-conjugatedType");
    conjugatedType.setType(this.requireClassifierByName("IType"));
    conjugatedType.setOptional(false);
    conjugatedType.setMultiple(false);
    Reference owningType = new Reference("owningType", concept, "sysml-Conjugation-owningType");
    owningType.setKey("sysml-Conjugation-owningType");
    owningType.setType(this.requireClassifierByName("IType"));
    owningType.setOptional(true);
    owningType.setMultiple(false);
  }

  public Concept getMultiplicity() {
    return this.requireConceptByName("Multiplicity");
  }

  private void initMultiplicity() {
    Concept concept = this.requireConceptByName("Multiplicity");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IFeature"));
  }

  public Concept getIntersecting() {
    return this.requireConceptByName("Intersecting");
  }

  private void initIntersecting() {
    Concept concept = this.requireConceptByName("Intersecting");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Reference intersectingType = new Reference("intersectingType", concept, "sysml-Intersecting-intersectingType");
    intersectingType.setKey("sysml-Intersecting-intersectingType");
    intersectingType.setType(this.requireClassifierByName("IType"));
    intersectingType.setOptional(false);
    intersectingType.setMultiple(false);
    Reference typeIntersected = new Reference("typeIntersected", concept, "sysml-Intersecting-typeIntersected");
    typeIntersected.setKey("sysml-Intersecting-typeIntersected");
    typeIntersected.setType(this.requireClassifierByName("IType"));
    typeIntersected.setOptional(false);
    typeIntersected.setMultiple(false);
  }

  public Concept getUnioning() {
    return this.requireConceptByName("Unioning");
  }

  private void initUnioning() {
    Concept concept = this.requireConceptByName("Unioning");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Reference unioningType = new Reference("unioningType", concept, "sysml-Unioning-unioningType");
    unioningType.setKey("sysml-Unioning-unioningType");
    unioningType.setType(this.requireClassifierByName("IType"));
    unioningType.setOptional(false);
    unioningType.setMultiple(false);
    Reference typeUnioned = new Reference("typeUnioned", concept, "sysml-Unioning-typeUnioned");
    typeUnioned.setKey("sysml-Unioning-typeUnioned");
    typeUnioned.setType(this.requireClassifierByName("IType"));
    typeUnioned.setOptional(false);
    typeUnioned.setMultiple(false);
  }

  public Concept getDisjoining() {
    return this.requireConceptByName("Disjoining");
  }

  private void initDisjoining() {
    Concept concept = this.requireConceptByName("Disjoining");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Reference typeDisjoined = new Reference("typeDisjoined", concept, "sysml-Disjoining-typeDisjoined");
    typeDisjoined.setKey("sysml-Disjoining-typeDisjoined");
    typeDisjoined.setType(this.requireClassifierByName("IType"));
    typeDisjoined.setOptional(false);
    typeDisjoined.setMultiple(false);
    Reference disjoiningType = new Reference("disjoiningType", concept, "sysml-Disjoining-disjoiningType");
    disjoiningType.setKey("sysml-Disjoining-disjoiningType");
    disjoiningType.setType(this.requireClassifierByName("IType"));
    disjoiningType.setOptional(false);
    disjoiningType.setMultiple(false);
    Reference owningType = new Reference("owningType", concept, "sysml-Disjoining-owningType");
    owningType.setKey("sysml-Disjoining-owningType");
    owningType.setType(this.requireClassifierByName("IType"));
    owningType.setOptional(true);
    owningType.setMultiple(false);
  }

  public Concept getDifferencing() {
    return this.requireConceptByName("Differencing");
  }

  private void initDifferencing() {
    Concept concept = this.requireConceptByName("Differencing");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Reference differencingType = new Reference("differencingType", concept, "sysml-Differencing-differencingType");
    differencingType.setKey("sysml-Differencing-differencingType");
    differencingType.setType(this.requireClassifierByName("IType"));
    differencingType.setOptional(false);
    differencingType.setMultiple(false);
    Reference typeDifferenced = new Reference("typeDifferenced", concept, "sysml-Differencing-typeDifferenced");
    typeDifferenced.setKey("sysml-Differencing-typeDifferenced");
    typeDifferenced.setType(this.requireClassifierByName("IType"));
    typeDifferenced.setOptional(false);
    typeDifferenced.setMultiple(false);
  }

  public Concept getEndFeatureMembership() {
    return this.requireConceptByName("EndFeatureMembership");
  }

  private void initEndFeatureMembership() {
    Concept concept = this.requireConceptByName("EndFeatureMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("FeatureMembership"));
  }

  public Concept getResultExpressionMembership() {
    return this.requireConceptByName("ResultExpressionMembership");
  }

  private void initResultExpressionMembership() {
    Concept concept = this.requireConceptByName("ResultExpressionMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("FeatureMembership"));
    Reference ownedResultExpression = new Reference("ownedResultExpression", concept, "sysml-ResultExpressionMembership-ownedResultExpression");
    ownedResultExpression.setKey("sysml-ResultExpressionMembership-ownedResultExpression");
    ownedResultExpression.setType(this.requireClassifierByName("IExpression"));
    ownedResultExpression.setOptional(false);
    ownedResultExpression.setMultiple(false);
  }

  public Concept getReturnParameterMembership() {
    return this.requireConceptByName("ReturnParameterMembership");
  }

  private void initReturnParameterMembership() {
    Concept concept = this.requireConceptByName("ReturnParameterMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ParameterMembership"));
  }

  public Concept getParameterMembership() {
    return this.requireConceptByName("ParameterMembership");
  }

  private void initParameterMembership() {
    Concept concept = this.requireConceptByName("ParameterMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("FeatureMembership"));
    Reference ownedMemberParameter = new Reference("ownedMemberParameter", concept, "sysml-ParameterMembership-ownedMemberParameter");
    ownedMemberParameter.setKey("sysml-ParameterMembership-ownedMemberParameter");
    ownedMemberParameter.setType(this.requireClassifierByName("IFeature"));
    ownedMemberParameter.setOptional(false);
    ownedMemberParameter.setMultiple(false);
  }

  public Concept getMultiplicityRange() {
    return this.requireConceptByName("MultiplicityRange");
  }

  private void initMultiplicityRange() {
    Concept concept = this.requireConceptByName("MultiplicityRange");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Multiplicity"));
    Reference lowerBound = new Reference("lowerBound", concept, "sysml-MultiplicityRange-lowerBound");
    lowerBound.setKey("sysml-MultiplicityRange-lowerBound");
    lowerBound.setType(this.requireClassifierByName("IExpression"));
    lowerBound.setOptional(true);
    lowerBound.setMultiple(false);
    Reference upperBound = new Reference("upperBound", concept, "sysml-MultiplicityRange-upperBound");
    upperBound.setKey("sysml-MultiplicityRange-upperBound");
    upperBound.setType(this.requireClassifierByName("IExpression"));
    upperBound.setOptional(false);
    upperBound.setMultiple(false);
    Reference bound = new Reference("bound", concept, "sysml-MultiplicityRange-bound");
    bound.setKey("sysml-MultiplicityRange-bound");
    bound.setType(this.requireClassifierByName("IExpression"));
    bound.setOptional(false);
    bound.setMultiple(true);
  }

  public Concept getFeatureValue() {
    return this.requireConceptByName("FeatureValue");
  }

  private void initFeatureValue() {
    Concept concept = this.requireConceptByName("FeatureValue");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("OwningMembership"));
    Reference featureWithValue = new Reference("featureWithValue", concept, "sysml-FeatureValue-featureWithValue");
    featureWithValue.setKey("sysml-FeatureValue-featureWithValue");
    featureWithValue.setType(this.requireClassifierByName("IFeature"));
    featureWithValue.setOptional(false);
    featureWithValue.setMultiple(false);
    Reference value = new Reference("value", concept, "sysml-FeatureValue-value");
    value.setKey("sysml-FeatureValue-value");
    value.setType(this.requireClassifierByName("IExpression"));
    value.setOptional(false);
    value.setMultiple(false);
    Property isInitial = new Property("isInitial", concept, "sysml-FeatureValue-isInitial");
    isInitial.setKey("sysml-FeatureValue-isInitial");
    isInitial.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isInitial.setOptional(false);
    Property isDefault = new Property("isDefault", concept, "sysml-FeatureValue-isDefault");
    isDefault.setKey("sysml-FeatureValue-isDefault");
    isDefault.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isDefault.setOptional(false);
  }

  public Concept getMetadataFeature() {
    return this.requireConceptByName("MetadataFeature");
  }

  private void initMetadataFeature() {
    Concept concept = this.requireConceptByName("MetadataFeature");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IFeature"));
    concept.addImplementedInterface(this.requireInterfaceByName("IAnnotatingElement"));
    Reference metaclass = new Reference("metaclass", concept, "sysml-MetadataFeature-metaclass");
    metaclass.setKey("sysml-MetadataFeature-metaclass");
    metaclass.setType(this.requireClassifierByName("IMetaclass"));
    metaclass.setOptional(true);
    metaclass.setMultiple(false);
  }

  public Concept getItemFlowEnd() {
    return this.requireConceptByName("ItemFlowEnd");
  }

  private void initItemFlowEnd() {
    Concept concept = this.requireConceptByName("ItemFlowEnd");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IFeature"));
  }

  public Concept getItemFeature() {
    return this.requireConceptByName("ItemFeature");
  }

  private void initItemFeature() {
    Concept concept = this.requireConceptByName("ItemFeature");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IFeature"));
  }

  public Concept getElementFilterMembership() {
    return this.requireConceptByName("ElementFilterMembership");
  }

  private void initElementFilterMembership() {
    Concept concept = this.requireConceptByName("ElementFilterMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("OwningMembership"));
    Reference condition = new Reference("condition", concept, "sysml-ElementFilterMembership-condition");
    condition.setKey("sysml-ElementFilterMembership-condition");
    condition.setType(this.requireClassifierByName("IExpression"));
    condition.setOptional(false);
    condition.setMultiple(false);
  }

  public Concept getPackage() {
    return this.requireConceptByName("Package");
  }

  private void initPackage() {
    Concept concept = this.requireConceptByName("Package");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("INamespace"));
    Reference filterCondition = new Reference("filterCondition", concept, "sysml-Package-filterCondition");
    filterCondition.setKey("sysml-Package-filterCondition");
    filterCondition.setType(this.requireClassifierByName("IExpression"));
    filterCondition.setOptional(true);
    filterCondition.setMultiple(true);
  }

  public Concept getLibraryPackage() {
    return this.requireConceptByName("LibraryPackage");
  }

  private void initLibraryPackage() {
    Concept concept = this.requireConceptByName("LibraryPackage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Package"));
    Property isStandard = new Property("isStandard", concept, "sysml-LibraryPackage-isStandard");
    isStandard.setKey("sysml-LibraryPackage-isStandard");
    isStandard.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isStandard.setOptional(false);
  }

  public Concept getFeatureReferenceExpression() {
    return this.requireConceptByName("FeatureReferenceExpression");
  }

  private void initFeatureReferenceExpression() {
    Concept concept = this.requireConceptByName("FeatureReferenceExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IExpression"));
    Reference referent = new Reference("referent", concept, "sysml-FeatureReferenceExpression-referent");
    referent.setKey("sysml-FeatureReferenceExpression-referent");
    referent.setType(this.requireClassifierByName("IFeature"));
    referent.setOptional(false);
    referent.setMultiple(false);
  }

  public Concept getMetadataAccessExpression() {
    return this.requireConceptByName("MetadataAccessExpression");
  }

  private void initMetadataAccessExpression() {
    Concept concept = this.requireConceptByName("MetadataAccessExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IExpression"));
    Reference referencedElement = new Reference("referencedElement", concept, "sysml-MetadataAccessExpression-referencedElement");
    referencedElement.setKey("sysml-MetadataAccessExpression-referencedElement");
    referencedElement.setType(this.requireClassifierByName("IElement"));
    referencedElement.setOptional(false);
    referencedElement.setMultiple(false);
  }

  public Concept getNullExpression() {
    return this.requireConceptByName("NullExpression");
  }

  private void initNullExpression() {
    Concept concept = this.requireConceptByName("NullExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IExpression"));
  }

  public Concept getIndexExpression() {
    return this.requireConceptByName("IndexExpression");
  }

  private void initIndexExpression() {
    Concept concept = this.requireConceptByName("IndexExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("OperatorExpression"));
  }

  public Concept getOperatorExpression() {
    return this.requireConceptByName("OperatorExpression");
  }

  private void initOperatorExpression() {
    Concept concept = this.requireConceptByName("OperatorExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("InvocationExpression"));
    Property operator = new Property("operator", concept, "sysml-OperatorExpression-operator");
    operator.setKey("sysml-OperatorExpression-operator");
    operator.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    operator.setOptional(false);
  }

  public Concept getInvocationExpression() {
    return this.requireConceptByName("InvocationExpression");
  }

  private void initInvocationExpression() {
    Concept concept = this.requireConceptByName("InvocationExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IExpression"));
    Reference argument = new Reference("argument", concept, "sysml-InvocationExpression-argument");
    argument.setKey("sysml-InvocationExpression-argument");
    argument.setType(this.requireClassifierByName("IExpression"));
    argument.setOptional(true);
    argument.setMultiple(true);
    Containment operand = new Containment("operand", concept, "sysml-InvocationExpression-operand");
    operand.setKey("sysml-InvocationExpression-operand");
    operand.setType(this.requireClassifierByName("IExpression"));
    operand.setOptional(true);
    operand.setMultiple(true);
  }

  public Concept getCollectExpression() {
    return this.requireConceptByName("CollectExpression");
  }

  private void initCollectExpression() {
    Concept concept = this.requireConceptByName("CollectExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("OperatorExpression"));
  }

  public Concept getLiteralInfinity() {
    return this.requireConceptByName("LiteralInfinity");
  }

  private void initLiteralInfinity() {
    Concept concept = this.requireConceptByName("LiteralInfinity");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("LiteralExpression"));
  }

  public Concept getLiteralExpression() {
    return this.requireConceptByName("LiteralExpression");
  }

  private void initLiteralExpression() {
    Concept concept = this.requireConceptByName("LiteralExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IExpression"));
  }

  public Concept getLiteralInteger() {
    return this.requireConceptByName("LiteralInteger");
  }

  private void initLiteralInteger() {
    Concept concept = this.requireConceptByName("LiteralInteger");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("LiteralExpression"));
    Property value = new Property("value", concept, "sysml-LiteralInteger-value");
    value.setKey("sysml-LiteralInteger-value");
    value.setType(TypesLanguage.getInstance().requireDataTypeByName("Integer"));
    value.setOptional(false);
  }

  public Concept getSelectExpression() {
    return this.requireConceptByName("SelectExpression");
  }

  private void initSelectExpression() {
    Concept concept = this.requireConceptByName("SelectExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("OperatorExpression"));
  }

  public Concept getLiteralRational() {
    return this.requireConceptByName("LiteralRational");
  }

  private void initLiteralRational() {
    Concept concept = this.requireConceptByName("LiteralRational");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("LiteralExpression"));
    Property value = new Property("value", concept, "sysml-LiteralRational-value");
    value.setKey("sysml-LiteralRational-value");
    value.setType(TypesLanguage.getInstance().requireDataTypeByName("Real"));
    value.setOptional(false);
  }

  public Concept getLiteralBoolean() {
    return this.requireConceptByName("LiteralBoolean");
  }

  private void initLiteralBoolean() {
    Concept concept = this.requireConceptByName("LiteralBoolean");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("LiteralExpression"));
    Property value = new Property("value", concept, "sysml-LiteralBoolean-value");
    value.setKey("sysml-LiteralBoolean-value");
    value.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    value.setOptional(false);
  }

  public Concept getLiteralString() {
    return this.requireConceptByName("LiteralString");
  }

  private void initLiteralString() {
    Concept concept = this.requireConceptByName("LiteralString");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("LiteralExpression"));
    Property value = new Property("value", concept, "sysml-LiteralString-value");
    value.setKey("sysml-LiteralString-value");
    value.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    value.setOptional(false);
  }

  public Concept getFeatureChainExpression() {
    return this.requireConceptByName("FeatureChainExpression");
  }

  private void initFeatureChainExpression() {
    Concept concept = this.requireConceptByName("FeatureChainExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("OperatorExpression"));
    Reference targetFeature = new Reference("targetFeature", concept, "sysml-FeatureChainExpression-targetFeature");
    targetFeature.setKey("sysml-FeatureChainExpression-targetFeature");
    targetFeature.setType(this.requireClassifierByName("IFeature"));
    targetFeature.setOptional(false);
    targetFeature.setMultiple(false);
  }

  public Concept getDependency() {
    return this.requireConceptByName("Dependency");
  }

  private void initDependency() {
    Concept concept = this.requireConceptByName("Dependency");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Reference client = new Reference("client", concept, "sysml-Dependency-client");
    client.setKey("sysml-Dependency-client");
    client.setType(this.requireClassifierByName("IElement"));
    client.setOptional(false);
    client.setMultiple(true);
    Reference supplier = new Reference("supplier", concept, "sysml-Dependency-supplier");
    supplier.setKey("sysml-Dependency-supplier");
    supplier.setType(this.requireClassifierByName("IElement"));
    supplier.setOptional(false);
    supplier.setMultiple(true);
  }

  public Concept getNamespaceImport() {
    return this.requireConceptByName("NamespaceImport");
  }

  private void initNamespaceImport() {
    Concept concept = this.requireConceptByName("NamespaceImport");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IImport"));
    Reference importedNamespace = new Reference("importedNamespace", concept, "sysml-NamespaceImport-importedNamespace");
    importedNamespace.setKey("sysml-NamespaceImport-importedNamespace");
    importedNamespace.setType(this.requireClassifierByName("INamespace"));
    importedNamespace.setOptional(false);
    importedNamespace.setMultiple(false);
  }

  public Concept getMembershipImport() {
    return this.requireConceptByName("MembershipImport");
  }

  private void initMembershipImport() {
    Concept concept = this.requireConceptByName("MembershipImport");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IImport"));
    Reference importedMembership = new Reference("importedMembership", concept, "sysml-MembershipImport-importedMembership");
    importedMembership.setKey("sysml-MembershipImport-importedMembership");
    importedMembership.setType(this.requireClassifierByName("Membership"));
    importedMembership.setOptional(false);
    importedMembership.setMultiple(false);
  }

  public Concept getInterfaceUsage() {
    return this.requireConceptByName("InterfaceUsage");
  }

  private void initInterfaceUsage() {
    Concept concept = this.requireConceptByName("InterfaceUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ConnectionUsage"));
    Reference interfaceDefinition = new Reference("interfaceDefinition", concept, "sysml-InterfaceUsage-interfaceDefinition");
    interfaceDefinition.setKey("sysml-InterfaceUsage-interfaceDefinition");
    interfaceDefinition.setType(this.requireClassifierByName("InterfaceDefinition"));
    interfaceDefinition.setOptional(true);
    interfaceDefinition.setMultiple(true);
  }

  public Concept getConnectionUsage() {
    return this.requireConceptByName("ConnectionUsage");
  }

  private void initConnectionUsage() {
    Concept concept = this.requireConceptByName("ConnectionUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ConnectorAsUsage"));
    concept.addImplementedInterface(this.requireInterfaceByName("IPartUsage"));
    Reference connectionDefinition = new Reference("connectionDefinition", concept, "sysml-ConnectionUsage-connectionDefinition");
    connectionDefinition.setKey("sysml-ConnectionUsage-connectionDefinition");
    connectionDefinition.setType(this.requireClassifierByName("IAssociationStructure"));
    connectionDefinition.setOptional(true);
    connectionDefinition.setMultiple(true);
  }

  public Concept getConnectorAsUsage() {
    return this.requireConceptByName("ConnectorAsUsage");
  }

  private void initConnectorAsUsage() {
    Concept concept = this.requireConceptByName("ConnectorAsUsage");
    concept.setAbstract(true);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IUsage"));
    concept.addImplementedInterface(this.requireInterfaceByName("IConnector"));
  }

  public Concept getVariantMembership() {
    return this.requireConceptByName("VariantMembership");
  }

  private void initVariantMembership() {
    Concept concept = this.requireConceptByName("VariantMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("OwningMembership"));
    Reference ownedVariantUsage = new Reference("ownedVariantUsage", concept, "sysml-VariantMembership-ownedVariantUsage");
    ownedVariantUsage.setKey("sysml-VariantMembership-ownedVariantUsage");
    ownedVariantUsage.setType(this.requireClassifierByName("IUsage"));
    ownedVariantUsage.setOptional(false);
    ownedVariantUsage.setMultiple(false);
  }

  public Concept getDefinition() {
    return this.requireConceptByName("Definition");
  }

  private void initDefinition() {
    Concept concept = this.requireConceptByName("Definition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IClassifier"));
    Property isVariation = new Property("isVariation", concept, "sysml-Definition-isVariation");
    isVariation.setKey("sysml-Definition-isVariation");
    isVariation.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isVariation.setOptional(false);
    Reference variant = new Reference("variant", concept, "sysml-Definition-variant");
    variant.setKey("sysml-Definition-variant");
    variant.setType(this.requireClassifierByName("IUsage"));
    variant.setOptional(true);
    variant.setMultiple(true);
    Reference variantMembership = new Reference("variantMembership", concept, "sysml-Definition-variantMembership");
    variantMembership.setKey("sysml-Definition-variantMembership");
    variantMembership.setType(this.requireClassifierByName("VariantMembership"));
    variantMembership.setOptional(true);
    variantMembership.setMultiple(true);
    Reference usage = new Reference("usage", concept, "sysml-Definition-usage");
    usage.setKey("sysml-Definition-usage");
    usage.setType(this.requireClassifierByName("IUsage"));
    usage.setOptional(true);
    usage.setMultiple(true);
    Reference directedUsage = new Reference("directedUsage", concept, "sysml-Definition-directedUsage");
    directedUsage.setKey("sysml-Definition-directedUsage");
    directedUsage.setType(this.requireClassifierByName("IUsage"));
    directedUsage.setOptional(true);
    directedUsage.setMultiple(true);
    Reference ownedReference = new Reference("ownedReference", concept, "sysml-Definition-ownedReference");
    ownedReference.setKey("sysml-Definition-ownedReference");
    ownedReference.setType(this.requireClassifierByName("ReferenceUsage"));
    ownedReference.setOptional(true);
    ownedReference.setMultiple(true);
    Reference ownedAttribute = new Reference("ownedAttribute", concept, "sysml-Definition-ownedAttribute");
    ownedAttribute.setKey("sysml-Definition-ownedAttribute");
    ownedAttribute.setType(this.requireClassifierByName("AttributeUsage"));
    ownedAttribute.setOptional(true);
    ownedAttribute.setMultiple(true);
    Reference ownedEnumeration = new Reference("ownedEnumeration", concept, "sysml-Definition-ownedEnumeration");
    ownedEnumeration.setKey("sysml-Definition-ownedEnumeration");
    ownedEnumeration.setType(this.requireClassifierByName("EnumerationUsage"));
    ownedEnumeration.setOptional(true);
    ownedEnumeration.setMultiple(true);
    Reference ownedOccurrence = new Reference("ownedOccurrence", concept, "sysml-Definition-ownedOccurrence");
    ownedOccurrence.setKey("sysml-Definition-ownedOccurrence");
    ownedOccurrence.setType(this.requireClassifierByName("IOccurrenceUsage"));
    ownedOccurrence.setOptional(true);
    ownedOccurrence.setMultiple(true);
    Reference ownedItem = new Reference("ownedItem", concept, "sysml-Definition-ownedItem");
    ownedItem.setKey("sysml-Definition-ownedItem");
    ownedItem.setType(this.requireClassifierByName("IItemUsage"));
    ownedItem.setOptional(true);
    ownedItem.setMultiple(true);
    Reference ownedPart = new Reference("ownedPart", concept, "sysml-Definition-ownedPart");
    ownedPart.setKey("sysml-Definition-ownedPart");
    ownedPart.setType(this.requireClassifierByName("IPartUsage"));
    ownedPart.setOptional(true);
    ownedPart.setMultiple(true);
    Reference ownedPort = new Reference("ownedPort", concept, "sysml-Definition-ownedPort");
    ownedPort.setKey("sysml-Definition-ownedPort");
    ownedPort.setType(this.requireClassifierByName("PortUsage"));
    ownedPort.setOptional(true);
    ownedPort.setMultiple(true);
    Reference ownedConnection = new Reference("ownedConnection", concept, "sysml-Definition-ownedConnection");
    ownedConnection.setKey("sysml-Definition-ownedConnection");
    ownedConnection.setType(this.requireClassifierByName("ConnectorAsUsage"));
    ownedConnection.setOptional(true);
    ownedConnection.setMultiple(true);
    Reference ownedFlow = new Reference("ownedFlow", concept, "sysml-Definition-ownedFlow");
    ownedFlow.setKey("sysml-Definition-ownedFlow");
    ownedFlow.setType(this.requireClassifierByName("FlowConnectionUsage"));
    ownedFlow.setOptional(true);
    ownedFlow.setMultiple(true);
    Reference ownedInterface = new Reference("ownedInterface", concept, "sysml-Definition-ownedInterface");
    ownedInterface.setKey("sysml-Definition-ownedInterface");
    ownedInterface.setType(this.requireClassifierByName("InterfaceUsage"));
    ownedInterface.setOptional(true);
    ownedInterface.setMultiple(true);
    Reference ownedAllocation = new Reference("ownedAllocation", concept, "sysml-Definition-ownedAllocation");
    ownedAllocation.setKey("sysml-Definition-ownedAllocation");
    ownedAllocation.setType(this.requireClassifierByName("AllocationUsage"));
    ownedAllocation.setOptional(true);
    ownedAllocation.setMultiple(true);
    Reference ownedAction = new Reference("ownedAction", concept, "sysml-Definition-ownedAction");
    ownedAction.setKey("sysml-Definition-ownedAction");
    ownedAction.setType(this.requireClassifierByName("IActionUsage"));
    ownedAction.setOptional(true);
    ownedAction.setMultiple(true);
    Reference ownedState = new Reference("ownedState", concept, "sysml-Definition-ownedState");
    ownedState.setKey("sysml-Definition-ownedState");
    ownedState.setType(this.requireClassifierByName("StateUsage"));
    ownedState.setOptional(true);
    ownedState.setMultiple(true);
    Reference ownedTransition = new Reference("ownedTransition", concept, "sysml-Definition-ownedTransition");
    ownedTransition.setKey("sysml-Definition-ownedTransition");
    ownedTransition.setType(this.requireClassifierByName("TransitionUsage"));
    ownedTransition.setOptional(true);
    ownedTransition.setMultiple(true);
    Reference ownedCalculation = new Reference("ownedCalculation", concept, "sysml-Definition-ownedCalculation");
    ownedCalculation.setKey("sysml-Definition-ownedCalculation");
    ownedCalculation.setType(this.requireClassifierByName("CalculationUsage"));
    ownedCalculation.setOptional(true);
    ownedCalculation.setMultiple(true);
    Reference ownedConstraint = new Reference("ownedConstraint", concept, "sysml-Definition-ownedConstraint");
    ownedConstraint.setKey("sysml-Definition-ownedConstraint");
    ownedConstraint.setType(this.requireClassifierByName("IConstraintUsage"));
    ownedConstraint.setOptional(true);
    ownedConstraint.setMultiple(true);
    Reference ownedRequirement = new Reference("ownedRequirement", concept, "sysml-Definition-ownedRequirement");
    ownedRequirement.setKey("sysml-Definition-ownedRequirement");
    ownedRequirement.setType(this.requireClassifierByName("RequirementUsage"));
    ownedRequirement.setOptional(true);
    ownedRequirement.setMultiple(true);
    Reference ownedConcern = new Reference("ownedConcern", concept, "sysml-Definition-ownedConcern");
    ownedConcern.setKey("sysml-Definition-ownedConcern");
    ownedConcern.setType(this.requireClassifierByName("ConcernUsage"));
    ownedConcern.setOptional(true);
    ownedConcern.setMultiple(true);
    Reference ownedCase = new Reference("ownedCase", concept, "sysml-Definition-ownedCase");
    ownedCase.setKey("sysml-Definition-ownedCase");
    ownedCase.setType(this.requireClassifierByName("CaseUsage"));
    ownedCase.setOptional(true);
    ownedCase.setMultiple(true);
    Reference ownedAnalysisCase = new Reference("ownedAnalysisCase", concept, "sysml-Definition-ownedAnalysisCase");
    ownedAnalysisCase.setKey("sysml-Definition-ownedAnalysisCase");
    ownedAnalysisCase.setType(this.requireClassifierByName("AnalysisCaseUsage"));
    ownedAnalysisCase.setOptional(true);
    ownedAnalysisCase.setMultiple(true);
    Reference ownedVerificationCase = new Reference("ownedVerificationCase", concept, "sysml-Definition-ownedVerificationCase");
    ownedVerificationCase.setKey("sysml-Definition-ownedVerificationCase");
    ownedVerificationCase.setType(this.requireClassifierByName("VerificationCaseUsage"));
    ownedVerificationCase.setOptional(true);
    ownedVerificationCase.setMultiple(true);
    Reference ownedUseCase = new Reference("ownedUseCase", concept, "sysml-Definition-ownedUseCase");
    ownedUseCase.setKey("sysml-Definition-ownedUseCase");
    ownedUseCase.setType(this.requireClassifierByName("UseCaseUsage"));
    ownedUseCase.setOptional(true);
    ownedUseCase.setMultiple(true);
    Reference ownedView = new Reference("ownedView", concept, "sysml-Definition-ownedView");
    ownedView.setKey("sysml-Definition-ownedView");
    ownedView.setType(this.requireClassifierByName("ViewUsage"));
    ownedView.setOptional(true);
    ownedView.setMultiple(true);
    Reference ownedViewpoint = new Reference("ownedViewpoint", concept, "sysml-Definition-ownedViewpoint");
    ownedViewpoint.setKey("sysml-Definition-ownedViewpoint");
    ownedViewpoint.setType(this.requireClassifierByName("ViewpointUsage"));
    ownedViewpoint.setOptional(true);
    ownedViewpoint.setMultiple(true);
    Reference ownedRendering = new Reference("ownedRendering", concept, "sysml-Definition-ownedRendering");
    ownedRendering.setKey("sysml-Definition-ownedRendering");
    ownedRendering.setType(this.requireClassifierByName("RenderingUsage"));
    ownedRendering.setOptional(true);
    ownedRendering.setMultiple(true);
    Reference ownedMetadata = new Reference("ownedMetadata", concept, "sysml-Definition-ownedMetadata");
    ownedMetadata.setKey("sysml-Definition-ownedMetadata");
    ownedMetadata.setType(this.requireClassifierByName("MetadataUsage"));
    ownedMetadata.setOptional(true);
    ownedMetadata.setMultiple(true);
    Reference ownedUsage = new Reference("ownedUsage", concept, "sysml-Definition-ownedUsage");
    ownedUsage.setKey("sysml-Definition-ownedUsage");
    ownedUsage.setType(this.requireClassifierByName("IUsage"));
    ownedUsage.setOptional(true);
    ownedUsage.setMultiple(true);
  }

  public Concept getReferenceUsage() {
    return this.requireConceptByName("ReferenceUsage");
  }

  private void initReferenceUsage() {
    Concept concept = this.requireConceptByName("ReferenceUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IUsage"));
  }

  public Concept getAttributeUsage() {
    return this.requireConceptByName("AttributeUsage");
  }

  private void initAttributeUsage() {
    Concept concept = this.requireConceptByName("AttributeUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IUsage"));
    Reference attributeDefinition = new Reference("attributeDefinition", concept, "sysml-AttributeUsage-attributeDefinition");
    attributeDefinition.setKey("sysml-AttributeUsage-attributeDefinition");
    attributeDefinition.setType(this.requireClassifierByName("IDataType"));
    attributeDefinition.setOptional(true);
    attributeDefinition.setMultiple(true);
  }

  public Concept getEnumerationUsage() {
    return this.requireConceptByName("EnumerationUsage");
  }

  private void initEnumerationUsage() {
    Concept concept = this.requireConceptByName("EnumerationUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("AttributeUsage"));
    Reference enumerationDefinition = new Reference("enumerationDefinition", concept, "sysml-EnumerationUsage-enumerationDefinition");
    enumerationDefinition.setKey("sysml-EnumerationUsage-enumerationDefinition");
    enumerationDefinition.setType(this.requireClassifierByName("EnumerationDefinition"));
    enumerationDefinition.setOptional(false);
    enumerationDefinition.setMultiple(false);
  }

  public Concept getEnumerationDefinition() {
    return this.requireConceptByName("EnumerationDefinition");
  }

  private void initEnumerationDefinition() {
    Concept concept = this.requireConceptByName("EnumerationDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("AttributeDefinition"));
    Reference enumeratedValue = new Reference("enumeratedValue", concept, "sysml-EnumerationDefinition-enumeratedValue");
    enumeratedValue.setKey("sysml-EnumerationDefinition-enumeratedValue");
    enumeratedValue.setType(this.requireClassifierByName("EnumerationUsage"));
    enumeratedValue.setOptional(true);
    enumeratedValue.setMultiple(true);
  }

  public Concept getAttributeDefinition() {
    return this.requireConceptByName("AttributeDefinition");
  }

  private void initAttributeDefinition() {
    Concept concept = this.requireConceptByName("AttributeDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Definition"));
    concept.addImplementedInterface(this.requireInterfaceByName("IDataType"));
  }

  public Concept getOccurrenceDefinition() {
    return this.requireConceptByName("OccurrenceDefinition");
  }

  private void initOccurrenceDefinition() {
    Concept concept = this.requireConceptByName("OccurrenceDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Definition"));
    concept.addImplementedInterface(this.requireInterfaceByName("IClass"));
    Reference lifeClass = new Reference("lifeClass", concept, "sysml-OccurrenceDefinition-lifeClass");
    lifeClass.setKey("sysml-OccurrenceDefinition-lifeClass");
    lifeClass.setType(this.requireClassifierByName("LifeClass"));
    lifeClass.setOptional(true);
    lifeClass.setMultiple(false);
    Property isIndividual = new Property("isIndividual", concept, "sysml-OccurrenceDefinition-isIndividual");
    isIndividual.setKey("sysml-OccurrenceDefinition-isIndividual");
    isIndividual.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isIndividual.setOptional(false);
  }

  public Concept getLifeClass() {
    return this.requireConceptByName("LifeClass");
  }

  private void initLifeClass() {
    Concept concept = this.requireConceptByName("LifeClass");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IClass"));
  }

  public Concept getPartDefinition() {
    return this.requireConceptByName("PartDefinition");
  }

  private void initPartDefinition() {
    Concept concept = this.requireConceptByName("PartDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ItemDefinition"));
  }

  public Concept getItemDefinition() {
    return this.requireConceptByName("ItemDefinition");
  }

  private void initItemDefinition() {
    Concept concept = this.requireConceptByName("ItemDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("OccurrenceDefinition"));
    concept.addImplementedInterface(this.requireInterfaceByName("IStructure"));
  }

  public Concept getPortUsage() {
    return this.requireConceptByName("PortUsage");
  }

  private void initPortUsage() {
    Concept concept = this.requireConceptByName("PortUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IOccurrenceUsage"));
    Reference portDefinition = new Reference("portDefinition", concept, "sysml-PortUsage-portDefinition");
    portDefinition.setKey("sysml-PortUsage-portDefinition");
    portDefinition.setType(this.requireClassifierByName("PortDefinition"));
    portDefinition.setOptional(true);
    portDefinition.setMultiple(true);
  }

  public Concept getPortDefinition() {
    return this.requireConceptByName("PortDefinition");
  }

  private void initPortDefinition() {
    Concept concept = this.requireConceptByName("PortDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("OccurrenceDefinition"));
    concept.addImplementedInterface(this.requireInterfaceByName("IStructure"));
    Reference conjugatedPortDefinition = new Reference("conjugatedPortDefinition", concept, "sysml-PortDefinition-conjugatedPortDefinition");
    conjugatedPortDefinition.setKey("sysml-PortDefinition-conjugatedPortDefinition");
    conjugatedPortDefinition.setType(this.requireClassifierByName("ConjugatedPortDefinition"));
    conjugatedPortDefinition.setOptional(true);
    conjugatedPortDefinition.setMultiple(false);
  }

  public Concept getConjugatedPortDefinition() {
    return this.requireConceptByName("ConjugatedPortDefinition");
  }

  private void initConjugatedPortDefinition() {
    Concept concept = this.requireConceptByName("ConjugatedPortDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("PortDefinition"));
    Reference ownedPortConjugator = new Reference("ownedPortConjugator", concept, "sysml-ConjugatedPortDefinition-ownedPortConjugator");
    ownedPortConjugator.setKey("sysml-ConjugatedPortDefinition-ownedPortConjugator");
    ownedPortConjugator.setType(this.requireClassifierByName("PortConjugation"));
    ownedPortConjugator.setOptional(false);
    ownedPortConjugator.setMultiple(false);
    Reference originalPortDefinition = new Reference("originalPortDefinition", concept, "sysml-ConjugatedPortDefinition-originalPortDefinition");
    originalPortDefinition.setKey("sysml-ConjugatedPortDefinition-originalPortDefinition");
    originalPortDefinition.setType(this.requireClassifierByName("PortDefinition"));
    originalPortDefinition.setOptional(false);
    originalPortDefinition.setMultiple(false);
  }

  public Concept getPortConjugation() {
    return this.requireConceptByName("PortConjugation");
  }

  private void initPortConjugation() {
    Concept concept = this.requireConceptByName("PortConjugation");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Conjugation"));
    Reference originalPortDefinition = new Reference("originalPortDefinition", concept, "sysml-PortConjugation-originalPortDefinition");
    originalPortDefinition.setKey("sysml-PortConjugation-originalPortDefinition");
    originalPortDefinition.setType(this.requireClassifierByName("PortDefinition"));
    originalPortDefinition.setOptional(false);
    originalPortDefinition.setMultiple(false);
    Reference conjugatedPortDefinition = new Reference("conjugatedPortDefinition", concept, "sysml-PortConjugation-conjugatedPortDefinition");
    conjugatedPortDefinition.setKey("sysml-PortConjugation-conjugatedPortDefinition");
    conjugatedPortDefinition.setType(this.requireClassifierByName("ConjugatedPortDefinition"));
    conjugatedPortDefinition.setOptional(false);
    conjugatedPortDefinition.setMultiple(false);
  }

  public Concept getFlowConnectionUsage() {
    return this.requireConceptByName("FlowConnectionUsage");
  }

  private void initFlowConnectionUsage() {
    Concept concept = this.requireConceptByName("FlowConnectionUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ConnectorAsUsage"));
    concept.addImplementedInterface(this.requireInterfaceByName("IActionUsage"));
    concept.addImplementedInterface(this.requireInterfaceByName("IItemFlow"));
    Reference flowConnectionDefinition = new Reference("flowConnectionDefinition", concept, "sysml-FlowConnectionUsage-flowConnectionDefinition");
    flowConnectionDefinition.setKey("sysml-FlowConnectionUsage-flowConnectionDefinition");
    flowConnectionDefinition.setType(this.requireClassifierByName("IInteraction"));
    flowConnectionDefinition.setOptional(true);
    flowConnectionDefinition.setMultiple(true);
  }

  public Concept getAllocationUsage() {
    return this.requireConceptByName("AllocationUsage");
  }

  private void initAllocationUsage() {
    Concept concept = this.requireConceptByName("AllocationUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ConnectionUsage"));
    Reference allocationDefinition = new Reference("allocationDefinition", concept, "sysml-AllocationUsage-allocationDefinition");
    allocationDefinition.setKey("sysml-AllocationUsage-allocationDefinition");
    allocationDefinition.setType(this.requireClassifierByName("AllocationDefinition"));
    allocationDefinition.setOptional(true);
    allocationDefinition.setMultiple(true);
  }

  public Concept getAllocationDefinition() {
    return this.requireConceptByName("AllocationDefinition");
  }

  private void initAllocationDefinition() {
    Concept concept = this.requireConceptByName("AllocationDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ConnectionDefinition"));
    Reference allocation = new Reference("allocation", concept, "sysml-AllocationDefinition-allocation");
    allocation.setKey("sysml-AllocationDefinition-allocation");
    allocation.setType(this.requireClassifierByName("AllocationUsage"));
    allocation.setOptional(true);
    allocation.setMultiple(true);
  }

  public Concept getConnectionDefinition() {
    return this.requireConceptByName("ConnectionDefinition");
  }

  private void initConnectionDefinition() {
    Concept concept = this.requireConceptByName("ConnectionDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("PartDefinition"));
    concept.addImplementedInterface(this.requireInterfaceByName("IAssociationStructure"));
    Reference connectionEnd = new Reference("connectionEnd", concept, "sysml-ConnectionDefinition-connectionEnd");
    connectionEnd.setKey("sysml-ConnectionDefinition-connectionEnd");
    connectionEnd.setType(this.requireClassifierByName("IUsage"));
    connectionEnd.setOptional(true);
    connectionEnd.setMultiple(true);
  }

  public Concept getStateUsage() {
    return this.requireConceptByName("StateUsage");
  }

  private void initStateUsage() {
    Concept concept = this.requireConceptByName("StateUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IActionUsage"));
    Reference stateDefinition = new Reference("stateDefinition", concept, "sysml-StateUsage-stateDefinition");
    stateDefinition.setKey("sysml-StateUsage-stateDefinition");
    stateDefinition.setType(this.requireClassifierByName("IBehavior"));
    stateDefinition.setOptional(true);
    stateDefinition.setMultiple(true);
    Reference entryAction = new Reference("entryAction", concept, "sysml-StateUsage-entryAction");
    entryAction.setKey("sysml-StateUsage-entryAction");
    entryAction.setType(this.requireClassifierByName("IActionUsage"));
    entryAction.setOptional(true);
    entryAction.setMultiple(false);
    Reference doAction = new Reference("doAction", concept, "sysml-StateUsage-doAction");
    doAction.setKey("sysml-StateUsage-doAction");
    doAction.setType(this.requireClassifierByName("IActionUsage"));
    doAction.setOptional(true);
    doAction.setMultiple(false);
    Reference exitAction = new Reference("exitAction", concept, "sysml-StateUsage-exitAction");
    exitAction.setKey("sysml-StateUsage-exitAction");
    exitAction.setType(this.requireClassifierByName("IActionUsage"));
    exitAction.setOptional(true);
    exitAction.setMultiple(false);
    Property isParallel = new Property("isParallel", concept, "sysml-StateUsage-isParallel");
    isParallel.setKey("sysml-StateUsage-isParallel");
    isParallel.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isParallel.setOptional(false);
  }

  public Concept getTransitionUsage() {
    return this.requireConceptByName("TransitionUsage");
  }

  private void initTransitionUsage() {
    Concept concept = this.requireConceptByName("TransitionUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IActionUsage"));
    Reference source = new Reference("source", concept, "sysml-TransitionUsage-source");
    source.setKey("sysml-TransitionUsage-source");
    source.setType(this.requireClassifierByName("IActionUsage"));
    source.setOptional(false);
    source.setMultiple(false);
    Reference target = new Reference("target", concept, "sysml-TransitionUsage-target");
    target.setKey("sysml-TransitionUsage-target");
    target.setType(this.requireClassifierByName("IActionUsage"));
    target.setOptional(false);
    target.setMultiple(false);
    Reference triggerAction = new Reference("triggerAction", concept, "sysml-TransitionUsage-triggerAction");
    triggerAction.setKey("sysml-TransitionUsage-triggerAction");
    triggerAction.setType(this.requireClassifierByName("AcceptActionUsage"));
    triggerAction.setOptional(true);
    triggerAction.setMultiple(true);
    Reference guardExpression = new Reference("guardExpression", concept, "sysml-TransitionUsage-guardExpression");
    guardExpression.setKey("sysml-TransitionUsage-guardExpression");
    guardExpression.setType(this.requireClassifierByName("IExpression"));
    guardExpression.setOptional(true);
    guardExpression.setMultiple(true);
    Reference effectAction = new Reference("effectAction", concept, "sysml-TransitionUsage-effectAction");
    effectAction.setKey("sysml-TransitionUsage-effectAction");
    effectAction.setType(this.requireClassifierByName("IActionUsage"));
    effectAction.setOptional(true);
    effectAction.setMultiple(true);
    Reference succession = new Reference("succession", concept, "sysml-TransitionUsage-succession");
    succession.setKey("sysml-TransitionUsage-succession");
    succession.setType(this.requireClassifierByName("ISuccession"));
    succession.setOptional(false);
    succession.setMultiple(false);
  }

  public Concept getAcceptActionUsage() {
    return this.requireConceptByName("AcceptActionUsage");
  }

  private void initAcceptActionUsage() {
    Concept concept = this.requireConceptByName("AcceptActionUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IActionUsage"));
    Reference receiverArgument = new Reference("receiverArgument", concept, "sysml-AcceptActionUsage-receiverArgument");
    receiverArgument.setKey("sysml-AcceptActionUsage-receiverArgument");
    receiverArgument.setType(this.requireClassifierByName("IExpression"));
    receiverArgument.setOptional(true);
    receiverArgument.setMultiple(false);
    Reference payloadParameter = new Reference("payloadParameter", concept, "sysml-AcceptActionUsage-payloadParameter");
    payloadParameter.setKey("sysml-AcceptActionUsage-payloadParameter");
    payloadParameter.setType(this.requireClassifierByName("ReferenceUsage"));
    payloadParameter.setOptional(false);
    payloadParameter.setMultiple(false);
    Reference payloadArgument = new Reference("payloadArgument", concept, "sysml-AcceptActionUsage-payloadArgument");
    payloadArgument.setKey("sysml-AcceptActionUsage-payloadArgument");
    payloadArgument.setType(this.requireClassifierByName("IExpression"));
    payloadArgument.setOptional(true);
    payloadArgument.setMultiple(false);
  }

  public Concept getCalculationUsage() {
    return this.requireConceptByName("CalculationUsage");
  }

  private void initCalculationUsage() {
    Concept concept = this.requireConceptByName("CalculationUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IActionUsage"));
    concept.addImplementedInterface(this.requireInterfaceByName("IExpression"));
    Reference calculationDefinition = new Reference("calculationDefinition", concept, "sysml-CalculationUsage-calculationDefinition");
    calculationDefinition.setKey("sysml-CalculationUsage-calculationDefinition");
    calculationDefinition.setType(this.requireClassifierByName("IFunction"));
    calculationDefinition.setOptional(true);
    calculationDefinition.setMultiple(false);
  }

  public Concept getRequirementUsage() {
    return this.requireConceptByName("RequirementUsage");
  }

  private void initRequirementUsage() {
    Concept concept = this.requireConceptByName("RequirementUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IConstraintUsage"));
    Reference requirementDefinition = new Reference("requirementDefinition", concept, "sysml-RequirementUsage-requirementDefinition");
    requirementDefinition.setKey("sysml-RequirementUsage-requirementDefinition");
    requirementDefinition.setType(this.requireClassifierByName("RequirementDefinition"));
    requirementDefinition.setOptional(true);
    requirementDefinition.setMultiple(false);
    Property reqId = new Property("reqId", concept, "sysml-RequirementUsage-reqId");
    reqId.setKey("sysml-RequirementUsage-reqId");
    reqId.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    reqId.setOptional(true);
    Reference requiredConstraint = new Reference("requiredConstraint", concept, "sysml-RequirementUsage-requiredConstraint");
    requiredConstraint.setKey("sysml-RequirementUsage-requiredConstraint");
    requiredConstraint.setType(this.requireClassifierByName("IConstraintUsage"));
    requiredConstraint.setOptional(true);
    requiredConstraint.setMultiple(true);
    Reference assumedConstraint = new Reference("assumedConstraint", concept, "sysml-RequirementUsage-assumedConstraint");
    assumedConstraint.setKey("sysml-RequirementUsage-assumedConstraint");
    assumedConstraint.setType(this.requireClassifierByName("IConstraintUsage"));
    assumedConstraint.setOptional(true);
    assumedConstraint.setMultiple(true);
    Reference subjectParameter = new Reference("subjectParameter", concept, "sysml-RequirementUsage-subjectParameter");
    subjectParameter.setKey("sysml-RequirementUsage-subjectParameter");
    subjectParameter.setType(this.requireClassifierByName("IUsage"));
    subjectParameter.setOptional(false);
    subjectParameter.setMultiple(false);
    Reference framedConcern = new Reference("framedConcern", concept, "sysml-RequirementUsage-framedConcern");
    framedConcern.setKey("sysml-RequirementUsage-framedConcern");
    framedConcern.setType(this.requireClassifierByName("ConcernUsage"));
    framedConcern.setOptional(true);
    framedConcern.setMultiple(true);
    Reference actorParameter = new Reference("actorParameter", concept, "sysml-RequirementUsage-actorParameter");
    actorParameter.setKey("sysml-RequirementUsage-actorParameter");
    actorParameter.setType(this.requireClassifierByName("IPartUsage"));
    actorParameter.setOptional(true);
    actorParameter.setMultiple(true);
    Reference stakeholderParameter = new Reference("stakeholderParameter", concept, "sysml-RequirementUsage-stakeholderParameter");
    stakeholderParameter.setKey("sysml-RequirementUsage-stakeholderParameter");
    stakeholderParameter.setType(this.requireClassifierByName("IPartUsage"));
    stakeholderParameter.setOptional(true);
    stakeholderParameter.setMultiple(true);
    Containment textContainer = new Containment("textContainer", concept, "sysml-RequirementUsage-textContainer");
    textContainer.setKey("sysml-RequirementUsage-textContainer");
    textContainer.setType(this.requireClassifierByName("TextContainer"));
    textContainer.setOptional(true);
    textContainer.setMultiple(true);
  }

  public Concept getRequirementDefinition() {
    return this.requireConceptByName("RequirementDefinition");
  }

  private void initRequirementDefinition() {
    Concept concept = this.requireConceptByName("RequirementDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ConstraintDefinition"));
    Property reqId = new Property("reqId", concept, "sysml-RequirementDefinition-reqId");
    reqId.setKey("sysml-RequirementDefinition-reqId");
    reqId.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    reqId.setOptional(true);
    Reference subjectParameter = new Reference("subjectParameter", concept, "sysml-RequirementDefinition-subjectParameter");
    subjectParameter.setKey("sysml-RequirementDefinition-subjectParameter");
    subjectParameter.setType(this.requireClassifierByName("IUsage"));
    subjectParameter.setOptional(false);
    subjectParameter.setMultiple(false);
    Reference actorParameter = new Reference("actorParameter", concept, "sysml-RequirementDefinition-actorParameter");
    actorParameter.setKey("sysml-RequirementDefinition-actorParameter");
    actorParameter.setType(this.requireClassifierByName("IPartUsage"));
    actorParameter.setOptional(true);
    actorParameter.setMultiple(true);
    Reference stakeholderParameter = new Reference("stakeholderParameter", concept, "sysml-RequirementDefinition-stakeholderParameter");
    stakeholderParameter.setKey("sysml-RequirementDefinition-stakeholderParameter");
    stakeholderParameter.setType(this.requireClassifierByName("IPartUsage"));
    stakeholderParameter.setOptional(true);
    stakeholderParameter.setMultiple(true);
    Reference assumedConstraint = new Reference("assumedConstraint", concept, "sysml-RequirementDefinition-assumedConstraint");
    assumedConstraint.setKey("sysml-RequirementDefinition-assumedConstraint");
    assumedConstraint.setType(this.requireClassifierByName("IConstraintUsage"));
    assumedConstraint.setOptional(true);
    assumedConstraint.setMultiple(true);
    Reference requiredConstraint = new Reference("requiredConstraint", concept, "sysml-RequirementDefinition-requiredConstraint");
    requiredConstraint.setKey("sysml-RequirementDefinition-requiredConstraint");
    requiredConstraint.setType(this.requireClassifierByName("IConstraintUsage"));
    requiredConstraint.setOptional(true);
    requiredConstraint.setMultiple(true);
    Reference framedConcern = new Reference("framedConcern", concept, "sysml-RequirementDefinition-framedConcern");
    framedConcern.setKey("sysml-RequirementDefinition-framedConcern");
    framedConcern.setType(this.requireClassifierByName("ConcernUsage"));
    framedConcern.setOptional(true);
    framedConcern.setMultiple(true);
    Containment textContainer = new Containment("textContainer", concept, "sysml-RequirementDefinition-textContainer");
    textContainer.setKey("sysml-RequirementDefinition-textContainer");
    textContainer.setType(this.requireClassifierByName("TextContainer"));
    textContainer.setOptional(true);
    textContainer.setMultiple(true);
  }

  public Concept getConstraintDefinition() {
    return this.requireConceptByName("ConstraintDefinition");
  }

  private void initConstraintDefinition() {
    Concept concept = this.requireConceptByName("ConstraintDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("OccurrenceDefinition"));
    concept.addImplementedInterface(this.requireInterfaceByName("IPredicate"));
  }

  public Concept getConcernUsage() {
    return this.requireConceptByName("ConcernUsage");
  }

  private void initConcernUsage() {
    Concept concept = this.requireConceptByName("ConcernUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("RequirementUsage"));
    Reference concernDefinition = new Reference("concernDefinition", concept, "sysml-ConcernUsage-concernDefinition");
    concernDefinition.setKey("sysml-ConcernUsage-concernDefinition");
    concernDefinition.setType(this.requireClassifierByName("ConcernDefinition"));
    concernDefinition.setOptional(true);
    concernDefinition.setMultiple(false);
  }

  public Concept getConcernDefinition() {
    return this.requireConceptByName("ConcernDefinition");
  }

  private void initConcernDefinition() {
    Concept concept = this.requireConceptByName("ConcernDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("RequirementDefinition"));
  }

  public Concept getCaseUsage() {
    return this.requireConceptByName("CaseUsage");
  }

  private void initCaseUsage() {
    Concept concept = this.requireConceptByName("CaseUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("CalculationUsage"));
    Reference objectiveRequirement = new Reference("objectiveRequirement", concept, "sysml-CaseUsage-objectiveRequirement");
    objectiveRequirement.setKey("sysml-CaseUsage-objectiveRequirement");
    objectiveRequirement.setType(this.requireClassifierByName("RequirementUsage"));
    objectiveRequirement.setOptional(true);
    objectiveRequirement.setMultiple(false);
    Reference caseDefinition = new Reference("caseDefinition", concept, "sysml-CaseUsage-caseDefinition");
    caseDefinition.setKey("sysml-CaseUsage-caseDefinition");
    caseDefinition.setType(this.requireClassifierByName("CaseDefinition"));
    caseDefinition.setOptional(true);
    caseDefinition.setMultiple(false);
    Reference subjectParameter = new Reference("subjectParameter", concept, "sysml-CaseUsage-subjectParameter");
    subjectParameter.setKey("sysml-CaseUsage-subjectParameter");
    subjectParameter.setType(this.requireClassifierByName("IUsage"));
    subjectParameter.setOptional(false);
    subjectParameter.setMultiple(false);
    Reference actorParameter = new Reference("actorParameter", concept, "sysml-CaseUsage-actorParameter");
    actorParameter.setKey("sysml-CaseUsage-actorParameter");
    actorParameter.setType(this.requireClassifierByName("IPartUsage"));
    actorParameter.setOptional(true);
    actorParameter.setMultiple(true);
  }

  public Concept getCaseDefinition() {
    return this.requireConceptByName("CaseDefinition");
  }

  private void initCaseDefinition() {
    Concept concept = this.requireConceptByName("CaseDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("CalculationDefinition"));
    Reference objectiveRequirement = new Reference("objectiveRequirement", concept, "sysml-CaseDefinition-objectiveRequirement");
    objectiveRequirement.setKey("sysml-CaseDefinition-objectiveRequirement");
    objectiveRequirement.setType(this.requireClassifierByName("RequirementUsage"));
    objectiveRequirement.setOptional(true);
    objectiveRequirement.setMultiple(false);
    Reference subjectParameter = new Reference("subjectParameter", concept, "sysml-CaseDefinition-subjectParameter");
    subjectParameter.setKey("sysml-CaseDefinition-subjectParameter");
    subjectParameter.setType(this.requireClassifierByName("IUsage"));
    subjectParameter.setOptional(false);
    subjectParameter.setMultiple(false);
    Reference actorParameter = new Reference("actorParameter", concept, "sysml-CaseDefinition-actorParameter");
    actorParameter.setKey("sysml-CaseDefinition-actorParameter");
    actorParameter.setType(this.requireClassifierByName("IPartUsage"));
    actorParameter.setOptional(true);
    actorParameter.setMultiple(true);
  }

  public Concept getCalculationDefinition() {
    return this.requireConceptByName("CalculationDefinition");
  }

  private void initCalculationDefinition() {
    Concept concept = this.requireConceptByName("CalculationDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ActionDefinition"));
    concept.addImplementedInterface(this.requireInterfaceByName("IFunction"));
    Reference calculation = new Reference("calculation", concept, "sysml-CalculationDefinition-calculation");
    calculation.setKey("sysml-CalculationDefinition-calculation");
    calculation.setType(this.requireClassifierByName("CalculationUsage"));
    calculation.setOptional(true);
    calculation.setMultiple(true);
  }

  public Concept getActionDefinition() {
    return this.requireConceptByName("ActionDefinition");
  }

  private void initActionDefinition() {
    Concept concept = this.requireConceptByName("ActionDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("OccurrenceDefinition"));
    concept.addImplementedInterface(this.requireInterfaceByName("IBehavior"));
    Reference action = new Reference("action", concept, "sysml-ActionDefinition-action");
    action.setKey("sysml-ActionDefinition-action");
    action.setType(this.requireClassifierByName("IActionUsage"));
    action.setOptional(true);
    action.setMultiple(true);
  }

  public Concept getAnalysisCaseUsage() {
    return this.requireConceptByName("AnalysisCaseUsage");
  }

  private void initAnalysisCaseUsage() {
    Concept concept = this.requireConceptByName("AnalysisCaseUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("CaseUsage"));
    Reference analysisCaseDefinition = new Reference("analysisCaseDefinition", concept, "sysml-AnalysisCaseUsage-analysisCaseDefinition");
    analysisCaseDefinition.setKey("sysml-AnalysisCaseUsage-analysisCaseDefinition");
    analysisCaseDefinition.setType(this.requireClassifierByName("AnalysisCaseDefinition"));
    analysisCaseDefinition.setOptional(true);
    analysisCaseDefinition.setMultiple(false);
    Reference resultExpression = new Reference("resultExpression", concept, "sysml-AnalysisCaseUsage-resultExpression");
    resultExpression.setKey("sysml-AnalysisCaseUsage-resultExpression");
    resultExpression.setType(this.requireClassifierByName("IExpression"));
    resultExpression.setOptional(true);
    resultExpression.setMultiple(false);
  }

  public Concept getAnalysisCaseDefinition() {
    return this.requireConceptByName("AnalysisCaseDefinition");
  }

  private void initAnalysisCaseDefinition() {
    Concept concept = this.requireConceptByName("AnalysisCaseDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("CaseDefinition"));
    Reference resultExpression = new Reference("resultExpression", concept, "sysml-AnalysisCaseDefinition-resultExpression");
    resultExpression.setKey("sysml-AnalysisCaseDefinition-resultExpression");
    resultExpression.setType(this.requireClassifierByName("IExpression"));
    resultExpression.setOptional(true);
    resultExpression.setMultiple(false);
  }

  public Concept getVerificationCaseUsage() {
    return this.requireConceptByName("VerificationCaseUsage");
  }

  private void initVerificationCaseUsage() {
    Concept concept = this.requireConceptByName("VerificationCaseUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("CaseUsage"));
    Reference verificationCaseDefinition = new Reference("verificationCaseDefinition", concept, "sysml-VerificationCaseUsage-verificationCaseDefinition");
    verificationCaseDefinition.setKey("sysml-VerificationCaseUsage-verificationCaseDefinition");
    verificationCaseDefinition.setType(this.requireClassifierByName("VerificationCaseDefinition"));
    verificationCaseDefinition.setOptional(true);
    verificationCaseDefinition.setMultiple(false);
    Reference verifiedRequirement = new Reference("verifiedRequirement", concept, "sysml-VerificationCaseUsage-verifiedRequirement");
    verifiedRequirement.setKey("sysml-VerificationCaseUsage-verifiedRequirement");
    verifiedRequirement.setType(this.requireClassifierByName("RequirementUsage"));
    verifiedRequirement.setOptional(true);
    verifiedRequirement.setMultiple(true);
  }

  public Concept getVerificationCaseDefinition() {
    return this.requireConceptByName("VerificationCaseDefinition");
  }

  private void initVerificationCaseDefinition() {
    Concept concept = this.requireConceptByName("VerificationCaseDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("CaseDefinition"));
    Reference verifiedRequirement = new Reference("verifiedRequirement", concept, "sysml-VerificationCaseDefinition-verifiedRequirement");
    verifiedRequirement.setKey("sysml-VerificationCaseDefinition-verifiedRequirement");
    verifiedRequirement.setType(this.requireClassifierByName("RequirementUsage"));
    verifiedRequirement.setOptional(true);
    verifiedRequirement.setMultiple(true);
  }

  public Concept getUseCaseUsage() {
    return this.requireConceptByName("UseCaseUsage");
  }

  private void initUseCaseUsage() {
    Concept concept = this.requireConceptByName("UseCaseUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("CaseUsage"));
    Reference useCaseDefinition = new Reference("useCaseDefinition", concept, "sysml-UseCaseUsage-useCaseDefinition");
    useCaseDefinition.setKey("sysml-UseCaseUsage-useCaseDefinition");
    useCaseDefinition.setType(this.requireClassifierByName("UseCaseDefinition"));
    useCaseDefinition.setOptional(true);
    useCaseDefinition.setMultiple(false);
    Reference includedUseCase = new Reference("includedUseCase", concept, "sysml-UseCaseUsage-includedUseCase");
    includedUseCase.setKey("sysml-UseCaseUsage-includedUseCase");
    includedUseCase.setType(this.requireClassifierByName("UseCaseUsage"));
    includedUseCase.setOptional(true);
    includedUseCase.setMultiple(true);
  }

  public Concept getUseCaseDefinition() {
    return this.requireConceptByName("UseCaseDefinition");
  }

  private void initUseCaseDefinition() {
    Concept concept = this.requireConceptByName("UseCaseDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("CaseDefinition"));
    Reference includedUseCase = new Reference("includedUseCase", concept, "sysml-UseCaseDefinition-includedUseCase");
    includedUseCase.setKey("sysml-UseCaseDefinition-includedUseCase");
    includedUseCase.setType(this.requireClassifierByName("UseCaseUsage"));
    includedUseCase.setOptional(true);
    includedUseCase.setMultiple(true);
  }

  public Concept getViewUsage() {
    return this.requireConceptByName("ViewUsage");
  }

  private void initViewUsage() {
    Concept concept = this.requireConceptByName("ViewUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IPartUsage"));
    Reference viewDefinition = new Reference("viewDefinition", concept, "sysml-ViewUsage-viewDefinition");
    viewDefinition.setKey("sysml-ViewUsage-viewDefinition");
    viewDefinition.setType(this.requireClassifierByName("ViewDefinition"));
    viewDefinition.setOptional(true);
    viewDefinition.setMultiple(false);
    Reference satisfiedViewpoint = new Reference("satisfiedViewpoint", concept, "sysml-ViewUsage-satisfiedViewpoint");
    satisfiedViewpoint.setKey("sysml-ViewUsage-satisfiedViewpoint");
    satisfiedViewpoint.setType(this.requireClassifierByName("ViewpointUsage"));
    satisfiedViewpoint.setOptional(true);
    satisfiedViewpoint.setMultiple(true);
    Reference exposedElement = new Reference("exposedElement", concept, "sysml-ViewUsage-exposedElement");
    exposedElement.setKey("sysml-ViewUsage-exposedElement");
    exposedElement.setType(this.requireClassifierByName("IElement"));
    exposedElement.setOptional(true);
    exposedElement.setMultiple(true);
    Reference viewRendering = new Reference("viewRendering", concept, "sysml-ViewUsage-viewRendering");
    viewRendering.setKey("sysml-ViewUsage-viewRendering");
    viewRendering.setType(this.requireClassifierByName("RenderingUsage"));
    viewRendering.setOptional(true);
    viewRendering.setMultiple(false);
    Reference viewCondition = new Reference("viewCondition", concept, "sysml-ViewUsage-viewCondition");
    viewCondition.setKey("sysml-ViewUsage-viewCondition");
    viewCondition.setType(this.requireClassifierByName("IExpression"));
    viewCondition.setOptional(true);
    viewCondition.setMultiple(true);
  }

  public Concept getViewDefinition() {
    return this.requireConceptByName("ViewDefinition");
  }

  private void initViewDefinition() {
    Concept concept = this.requireConceptByName("ViewDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("PartDefinition"));
    Reference view = new Reference("view", concept, "sysml-ViewDefinition-view");
    view.setKey("sysml-ViewDefinition-view");
    view.setType(this.requireClassifierByName("ViewUsage"));
    view.setOptional(true);
    view.setMultiple(true);
    Reference satisfiedViewpoint = new Reference("satisfiedViewpoint", concept, "sysml-ViewDefinition-satisfiedViewpoint");
    satisfiedViewpoint.setKey("sysml-ViewDefinition-satisfiedViewpoint");
    satisfiedViewpoint.setType(this.requireClassifierByName("ViewpointUsage"));
    satisfiedViewpoint.setOptional(true);
    satisfiedViewpoint.setMultiple(true);
    Reference viewRendering = new Reference("viewRendering", concept, "sysml-ViewDefinition-viewRendering");
    viewRendering.setKey("sysml-ViewDefinition-viewRendering");
    viewRendering.setType(this.requireClassifierByName("RenderingUsage"));
    viewRendering.setOptional(true);
    viewRendering.setMultiple(false);
    Reference viewCondition = new Reference("viewCondition", concept, "sysml-ViewDefinition-viewCondition");
    viewCondition.setKey("sysml-ViewDefinition-viewCondition");
    viewCondition.setType(this.requireClassifierByName("IExpression"));
    viewCondition.setOptional(true);
    viewCondition.setMultiple(true);
  }

  public Concept getViewpointUsage() {
    return this.requireConceptByName("ViewpointUsage");
  }

  private void initViewpointUsage() {
    Concept concept = this.requireConceptByName("ViewpointUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("RequirementUsage"));
    Reference viewpointDefinition = new Reference("viewpointDefinition", concept, "sysml-ViewpointUsage-viewpointDefinition");
    viewpointDefinition.setKey("sysml-ViewpointUsage-viewpointDefinition");
    viewpointDefinition.setType(this.requireClassifierByName("ViewpointDefinition"));
    viewpointDefinition.setOptional(true);
    viewpointDefinition.setMultiple(false);
    Reference viewpointStakeholder = new Reference("viewpointStakeholder", concept, "sysml-ViewpointUsage-viewpointStakeholder");
    viewpointStakeholder.setKey("sysml-ViewpointUsage-viewpointStakeholder");
    viewpointStakeholder.setType(this.requireClassifierByName("IPartUsage"));
    viewpointStakeholder.setOptional(true);
    viewpointStakeholder.setMultiple(true);
  }

  public Concept getViewpointDefinition() {
    return this.requireConceptByName("ViewpointDefinition");
  }

  private void initViewpointDefinition() {
    Concept concept = this.requireConceptByName("ViewpointDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("RequirementDefinition"));
    Reference viewpointStakeholder = new Reference("viewpointStakeholder", concept, "sysml-ViewpointDefinition-viewpointStakeholder");
    viewpointStakeholder.setKey("sysml-ViewpointDefinition-viewpointStakeholder");
    viewpointStakeholder.setType(this.requireClassifierByName("IPartUsage"));
    viewpointStakeholder.setOptional(true);
    viewpointStakeholder.setMultiple(true);
  }

  public Concept getRenderingUsage() {
    return this.requireConceptByName("RenderingUsage");
  }

  private void initRenderingUsage() {
    Concept concept = this.requireConceptByName("RenderingUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IPartUsage"));
    Reference renderingDefinition = new Reference("renderingDefinition", concept, "sysml-RenderingUsage-renderingDefinition");
    renderingDefinition.setKey("sysml-RenderingUsage-renderingDefinition");
    renderingDefinition.setType(this.requireClassifierByName("RenderingDefinition"));
    renderingDefinition.setOptional(true);
    renderingDefinition.setMultiple(false);
  }

  public Concept getRenderingDefinition() {
    return this.requireConceptByName("RenderingDefinition");
  }

  private void initRenderingDefinition() {
    Concept concept = this.requireConceptByName("RenderingDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("PartDefinition"));
    Reference rendering = new Reference("rendering", concept, "sysml-RenderingDefinition-rendering");
    rendering.setKey("sysml-RenderingDefinition-rendering");
    rendering.setType(this.requireClassifierByName("RenderingUsage"));
    rendering.setOptional(true);
    rendering.setMultiple(true);
  }

  public Concept getMetadataUsage() {
    return this.requireConceptByName("MetadataUsage");
  }

  private void initMetadataUsage() {
    Concept concept = this.requireConceptByName("MetadataUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("MetadataFeature"));
    concept.addImplementedInterface(this.requireInterfaceByName("IItemUsage"));
    Reference metadataDefinition = new Reference("metadataDefinition", concept, "sysml-MetadataUsage-metadataDefinition");
    metadataDefinition.setKey("sysml-MetadataUsage-metadataDefinition");
    metadataDefinition.setType(this.requireClassifierByName("IMetaclass"));
    metadataDefinition.setOptional(true);
    metadataDefinition.setMultiple(false);
  }

  public Concept getInterfaceDefinition() {
    return this.requireConceptByName("InterfaceDefinition");
  }

  private void initInterfaceDefinition() {
    Concept concept = this.requireConceptByName("InterfaceDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ConnectionDefinition"));
    Reference interfaceEnd = new Reference("interfaceEnd", concept, "sysml-InterfaceDefinition-interfaceEnd");
    interfaceEnd.setKey("sysml-InterfaceDefinition-interfaceEnd");
    interfaceEnd.setType(this.requireClassifierByName("PortUsage"));
    interfaceEnd.setOptional(true);
    interfaceEnd.setMultiple(true);
  }

  public Concept getConjugatedPortTyping() {
    return this.requireConceptByName("ConjugatedPortTyping");
  }

  private void initConjugatedPortTyping() {
    Concept concept = this.requireConceptByName("ConjugatedPortTyping");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("FeatureTyping"));
    Reference portDefinition = new Reference("portDefinition", concept, "sysml-ConjugatedPortTyping-portDefinition");
    portDefinition.setKey("sysml-ConjugatedPortTyping-portDefinition");
    portDefinition.setType(this.requireClassifierByName("PortDefinition"));
    portDefinition.setOptional(false);
    portDefinition.setMultiple(false);
    Reference conjugatedPortDefinition = new Reference("conjugatedPortDefinition", concept, "sysml-ConjugatedPortTyping-conjugatedPortDefinition");
    conjugatedPortDefinition.setKey("sysml-ConjugatedPortTyping-conjugatedPortDefinition");
    conjugatedPortDefinition.setType(this.requireClassifierByName("ConjugatedPortDefinition"));
    conjugatedPortDefinition.setOptional(false);
    conjugatedPortDefinition.setMultiple(false);
  }

  public Concept getTransitionFeatureMembership() {
    return this.requireConceptByName("TransitionFeatureMembership");
  }

  private void initTransitionFeatureMembership() {
    Concept concept = this.requireConceptByName("TransitionFeatureMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("FeatureMembership"));
    Property kind = new Property("kind", concept, "sysml-TransitionFeatureMembership-kind");
    kind.setKey("sysml-TransitionFeatureMembership-kind");
    kind.setType(this.requireDataTypeByName("TransitionFeatureKind"));
    kind.setOptional(false);
    Reference transitionFeature = new Reference("transitionFeature", concept, "sysml-TransitionFeatureMembership-transitionFeature");
    transitionFeature.setKey("sysml-TransitionFeatureMembership-transitionFeature");
    transitionFeature.setType(this.requireClassifierByName("IStep"));
    transitionFeature.setOptional(false);
    transitionFeature.setMultiple(false);
  }

  public Concept getExhibitStateUsage() {
    return this.requireConceptByName("ExhibitStateUsage");
  }

  private void initExhibitStateUsage() {
    Concept concept = this.requireConceptByName("ExhibitStateUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("StateUsage"));
    concept.addImplementedInterface(this.requireInterfaceByName("IPerformActionUsage"));
    Reference exhibitedState = new Reference("exhibitedState", concept, "sysml-ExhibitStateUsage-exhibitedState");
    exhibitedState.setKey("sysml-ExhibitStateUsage-exhibitedState");
    exhibitedState.setType(this.requireClassifierByName("StateUsage"));
    exhibitedState.setOptional(false);
    exhibitedState.setMultiple(false);
  }

  public Concept getStateSubactionMembership() {
    return this.requireConceptByName("StateSubactionMembership");
  }

  private void initStateSubactionMembership() {
    Concept concept = this.requireConceptByName("StateSubactionMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("FeatureMembership"));
    Property kind = new Property("kind", concept, "sysml-StateSubactionMembership-kind");
    kind.setKey("sysml-StateSubactionMembership-kind");
    kind.setType(this.requireDataTypeByName("StateSubactionKind"));
    kind.setOptional(false);
    Reference action = new Reference("action", concept, "sysml-StateSubactionMembership-action");
    action.setKey("sysml-StateSubactionMembership-action");
    action.setType(this.requireClassifierByName("IActionUsage"));
    action.setOptional(false);
    action.setMultiple(false);
  }

  public Concept getStateDefinition() {
    return this.requireConceptByName("StateDefinition");
  }

  private void initStateDefinition() {
    Concept concept = this.requireConceptByName("StateDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ActionDefinition"));
    Reference state = new Reference("state", concept, "sysml-StateDefinition-state");
    state.setKey("sysml-StateDefinition-state");
    state.setType(this.requireClassifierByName("StateUsage"));
    state.setOptional(true);
    state.setMultiple(true);
    Reference entryAction = new Reference("entryAction", concept, "sysml-StateDefinition-entryAction");
    entryAction.setKey("sysml-StateDefinition-entryAction");
    entryAction.setType(this.requireClassifierByName("IActionUsage"));
    entryAction.setOptional(true);
    entryAction.setMultiple(false);
    Reference doAction = new Reference("doAction", concept, "sysml-StateDefinition-doAction");
    doAction.setKey("sysml-StateDefinition-doAction");
    doAction.setType(this.requireClassifierByName("IActionUsage"));
    doAction.setOptional(true);
    doAction.setMultiple(false);
    Reference exitAction = new Reference("exitAction", concept, "sysml-StateDefinition-exitAction");
    exitAction.setKey("sysml-StateDefinition-exitAction");
    exitAction.setType(this.requireClassifierByName("IActionUsage"));
    exitAction.setOptional(true);
    exitAction.setMultiple(false);
    Property isParallel = new Property("isParallel", concept, "sysml-StateDefinition-isParallel");
    isParallel.setKey("sysml-StateDefinition-isParallel");
    isParallel.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isParallel.setOptional(false);
  }

  public Concept getSuccessionFlowConnectionUsage() {
    return this.requireConceptByName("SuccessionFlowConnectionUsage");
  }

  private void initSuccessionFlowConnectionUsage() {
    Concept concept = this.requireConceptByName("SuccessionFlowConnectionUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("FlowConnectionUsage"));
    concept.addImplementedInterface(this.requireInterfaceByName("ISuccessionItemFlow"));
  }

  public Concept getFlowConnectionDefinition() {
    return this.requireConceptByName("FlowConnectionDefinition");
  }

  private void initFlowConnectionDefinition() {
    Concept concept = this.requireConceptByName("FlowConnectionDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ActionDefinition"));
    concept.addImplementedInterface(this.requireInterfaceByName("IInteraction"));
    Reference flowConnectionEnd = new Reference("flowConnectionEnd", concept, "sysml-FlowConnectionDefinition-flowConnectionEnd");
    flowConnectionEnd.setKey("sysml-FlowConnectionDefinition-flowConnectionEnd");
    flowConnectionEnd.setType(this.requireClassifierByName("IUsage"));
    flowConnectionEnd.setOptional(true);
    flowConnectionEnd.setMultiple(true);
  }

  public Concept getRequirementVerificationMembership() {
    return this.requireConceptByName("RequirementVerificationMembership");
  }

  private void initRequirementVerificationMembership() {
    Concept concept = this.requireConceptByName("RequirementVerificationMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("RequirementConstraintMembership"));
    Reference ownedRequirement = new Reference("ownedRequirement", concept, "sysml-RequirementVerificationMembership-ownedRequirement");
    ownedRequirement.setKey("sysml-RequirementVerificationMembership-ownedRequirement");
    ownedRequirement.setType(this.requireClassifierByName("RequirementUsage"));
    ownedRequirement.setOptional(false);
    ownedRequirement.setMultiple(false);
    Reference verifiedRequirement = new Reference("verifiedRequirement", concept, "sysml-RequirementVerificationMembership-verifiedRequirement");
    verifiedRequirement.setKey("sysml-RequirementVerificationMembership-verifiedRequirement");
    verifiedRequirement.setType(this.requireClassifierByName("RequirementUsage"));
    verifiedRequirement.setOptional(false);
    verifiedRequirement.setMultiple(false);
  }

  public Concept getRequirementConstraintMembership() {
    return this.requireConceptByName("RequirementConstraintMembership");
  }

  private void initRequirementConstraintMembership() {
    Concept concept = this.requireConceptByName("RequirementConstraintMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("FeatureMembership"));
    Property kind = new Property("kind", concept, "sysml-RequirementConstraintMembership-kind");
    kind.setKey("sysml-RequirementConstraintMembership-kind");
    kind.setType(this.requireDataTypeByName("RequirementConstraintKind"));
    kind.setOptional(false);
    Reference ownedConstraint = new Reference("ownedConstraint", concept, "sysml-RequirementConstraintMembership-ownedConstraint");
    ownedConstraint.setKey("sysml-RequirementConstraintMembership-ownedConstraint");
    ownedConstraint.setType(this.requireClassifierByName("IConstraintUsage"));
    ownedConstraint.setOptional(false);
    ownedConstraint.setMultiple(false);
    Reference referencedConstraint = new Reference("referencedConstraint", concept, "sysml-RequirementConstraintMembership-referencedConstraint");
    referencedConstraint.setKey("sysml-RequirementConstraintMembership-referencedConstraint");
    referencedConstraint.setType(this.requireClassifierByName("IConstraintUsage"));
    referencedConstraint.setOptional(false);
    referencedConstraint.setMultiple(false);
  }

  public Concept getIncludeUseCaseUsage() {
    return this.requireConceptByName("IncludeUseCaseUsage");
  }

  private void initIncludeUseCaseUsage() {
    Concept concept = this.requireConceptByName("IncludeUseCaseUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("UseCaseUsage"));
    concept.addImplementedInterface(this.requireInterfaceByName("IPerformActionUsage"));
    Reference useCaseIncluded = new Reference("useCaseIncluded", concept, "sysml-IncludeUseCaseUsage-useCaseIncluded");
    useCaseIncluded.setKey("sysml-IncludeUseCaseUsage-useCaseIncluded");
    useCaseIncluded.setType(this.requireClassifierByName("UseCaseUsage"));
    useCaseIncluded.setOptional(false);
    useCaseIncluded.setMultiple(false);
  }

  public Concept getObjectiveMembership() {
    return this.requireConceptByName("ObjectiveMembership");
  }

  private void initObjectiveMembership() {
    Concept concept = this.requireConceptByName("ObjectiveMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("FeatureMembership"));
    Reference ownedObjectiveRequirement = new Reference("ownedObjectiveRequirement", concept, "sysml-ObjectiveMembership-ownedObjectiveRequirement");
    ownedObjectiveRequirement.setKey("sysml-ObjectiveMembership-ownedObjectiveRequirement");
    ownedObjectiveRequirement.setType(this.requireClassifierByName("RequirementUsage"));
    ownedObjectiveRequirement.setOptional(false);
    ownedObjectiveRequirement.setMultiple(false);
  }

  public Concept getSatisfyRequirementUsage() {
    return this.requireConceptByName("SatisfyRequirementUsage");
  }

  private void initSatisfyRequirementUsage() {
    Concept concept = this.requireConceptByName("SatisfyRequirementUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("RequirementUsage"));
    concept.addImplementedInterface(this.requireInterfaceByName("IAssertConstraintUsage"));
    Reference satisfiedRequirement = new Reference("satisfiedRequirement", concept, "sysml-SatisfyRequirementUsage-satisfiedRequirement");
    satisfiedRequirement.setKey("sysml-SatisfyRequirementUsage-satisfiedRequirement");
    satisfiedRequirement.setType(this.requireClassifierByName("RequirementUsage"));
    satisfiedRequirement.setOptional(false);
    satisfiedRequirement.setMultiple(false);
    Reference satisfyingFeature = new Reference("satisfyingFeature", concept, "sysml-SatisfyRequirementUsage-satisfyingFeature");
    satisfyingFeature.setKey("sysml-SatisfyRequirementUsage-satisfyingFeature");
    satisfyingFeature.setType(this.requireClassifierByName("IFeature"));
    satisfyingFeature.setOptional(false);
    satisfyingFeature.setMultiple(false);
  }

  public Concept getSubjectMembership() {
    return this.requireConceptByName("SubjectMembership");
  }

  private void initSubjectMembership() {
    Concept concept = this.requireConceptByName("SubjectMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ParameterMembership"));
    Reference ownedSubjectParameter = new Reference("ownedSubjectParameter", concept, "sysml-SubjectMembership-ownedSubjectParameter");
    ownedSubjectParameter.setKey("sysml-SubjectMembership-ownedSubjectParameter");
    ownedSubjectParameter.setType(this.requireClassifierByName("IUsage"));
    ownedSubjectParameter.setOptional(false);
    ownedSubjectParameter.setMultiple(false);
  }

  public Concept getStakeholderMembership() {
    return this.requireConceptByName("StakeholderMembership");
  }

  private void initStakeholderMembership() {
    Concept concept = this.requireConceptByName("StakeholderMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ParameterMembership"));
    Reference ownedStakeholderParameter = new Reference("ownedStakeholderParameter", concept, "sysml-StakeholderMembership-ownedStakeholderParameter");
    ownedStakeholderParameter.setKey("sysml-StakeholderMembership-ownedStakeholderParameter");
    ownedStakeholderParameter.setType(this.requireClassifierByName("IPartUsage"));
    ownedStakeholderParameter.setOptional(false);
    ownedStakeholderParameter.setMultiple(false);
  }

  public Concept getFramedConcernMembership() {
    return this.requireConceptByName("FramedConcernMembership");
  }

  private void initFramedConcernMembership() {
    Concept concept = this.requireConceptByName("FramedConcernMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("RequirementConstraintMembership"));
    Reference ownedConcern = new Reference("ownedConcern", concept, "sysml-FramedConcernMembership-ownedConcern");
    ownedConcern.setKey("sysml-FramedConcernMembership-ownedConcern");
    ownedConcern.setType(this.requireClassifierByName("ConcernUsage"));
    ownedConcern.setOptional(false);
    ownedConcern.setMultiple(false);
    Reference referencedConcern = new Reference("referencedConcern", concept, "sysml-FramedConcernMembership-referencedConcern");
    referencedConcern.setKey("sysml-FramedConcernMembership-referencedConcern");
    referencedConcern.setType(this.requireClassifierByName("ConcernUsage"));
    referencedConcern.setOptional(false);
    referencedConcern.setMultiple(false);
  }

  public Concept getActorMembership() {
    return this.requireConceptByName("ActorMembership");
  }

  private void initActorMembership() {
    Concept concept = this.requireConceptByName("ActorMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ParameterMembership"));
    Reference ownedActorParameter = new Reference("ownedActorParameter", concept, "sysml-ActorMembership-ownedActorParameter");
    ownedActorParameter.setKey("sysml-ActorMembership-ownedActorParameter");
    ownedActorParameter.setType(this.requireClassifierByName("IPartUsage"));
    ownedActorParameter.setOptional(false);
    ownedActorParameter.setMultiple(false);
  }

  public Concept getViewRenderingMembership() {
    return this.requireConceptByName("ViewRenderingMembership");
  }

  private void initViewRenderingMembership() {
    Concept concept = this.requireConceptByName("ViewRenderingMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("FeatureMembership"));
    Reference ownedRendering = new Reference("ownedRendering", concept, "sysml-ViewRenderingMembership-ownedRendering");
    ownedRendering.setKey("sysml-ViewRenderingMembership-ownedRendering");
    ownedRendering.setType(this.requireClassifierByName("RenderingUsage"));
    ownedRendering.setOptional(false);
    ownedRendering.setMultiple(false);
    Reference referencedRendering = new Reference("referencedRendering", concept, "sysml-ViewRenderingMembership-referencedRendering");
    referencedRendering.setKey("sysml-ViewRenderingMembership-referencedRendering");
    referencedRendering.setType(this.requireClassifierByName("RenderingUsage"));
    referencedRendering.setOptional(false);
    referencedRendering.setMultiple(false);
  }

  public Concept getNamespaceExpose() {
    return this.requireConceptByName("NamespaceExpose");
  }

  private void initNamespaceExpose() {
    Concept concept = this.requireConceptByName("NamespaceExpose");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("NamespaceImport"));
    concept.addImplementedInterface(this.requireInterfaceByName("IExpose"));
  }

  public Concept getMembershipExpose() {
    return this.requireConceptByName("MembershipExpose");
  }

  private void initMembershipExpose() {
    Concept concept = this.requireConceptByName("MembershipExpose");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("MembershipImport"));
    concept.addImplementedInterface(this.requireInterfaceByName("IExpose"));
  }

  public Concept getBindingConnectorAsUsage() {
    return this.requireConceptByName("BindingConnectorAsUsage");
  }

  private void initBindingConnectorAsUsage() {
    Concept concept = this.requireConceptByName("BindingConnectorAsUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ConnectorAsUsage"));
    concept.addImplementedInterface(this.requireInterfaceByName("IBindingConnector"));
  }

  public Concept getSuccessionAsUsage() {
    return this.requireConceptByName("SuccessionAsUsage");
  }

  private void initSuccessionAsUsage() {
    Concept concept = this.requireConceptByName("SuccessionAsUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ConnectorAsUsage"));
    concept.addImplementedInterface(this.requireInterfaceByName("ISuccession"));
  }

  public Concept getForkNode() {
    return this.requireConceptByName("ForkNode");
  }

  private void initForkNode() {
    Concept concept = this.requireConceptByName("ForkNode");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ControlNode"));
  }

  public Concept getControlNode() {
    return this.requireConceptByName("ControlNode");
  }

  private void initControlNode() {
    Concept concept = this.requireConceptByName("ControlNode");
    concept.setAbstract(true);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IActionUsage"));
  }

  public Concept getJoinNode() {
    return this.requireConceptByName("JoinNode");
  }

  private void initJoinNode() {
    Concept concept = this.requireConceptByName("JoinNode");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ControlNode"));
  }

  public Concept getSendActionUsage() {
    return this.requireConceptByName("SendActionUsage");
  }

  private void initSendActionUsage() {
    Concept concept = this.requireConceptByName("SendActionUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IActionUsage"));
    Reference receiverArgument = new Reference("receiverArgument", concept, "sysml-SendActionUsage-receiverArgument");
    receiverArgument.setKey("sysml-SendActionUsage-receiverArgument");
    receiverArgument.setType(this.requireClassifierByName("IExpression"));
    receiverArgument.setOptional(true);
    receiverArgument.setMultiple(false);
    Reference payloadArgument = new Reference("payloadArgument", concept, "sysml-SendActionUsage-payloadArgument");
    payloadArgument.setKey("sysml-SendActionUsage-payloadArgument");
    payloadArgument.setType(this.requireClassifierByName("IExpression"));
    payloadArgument.setOptional(false);
    payloadArgument.setMultiple(false);
    Reference senderArgument = new Reference("senderArgument", concept, "sysml-SendActionUsage-senderArgument");
    senderArgument.setKey("sysml-SendActionUsage-senderArgument");
    senderArgument.setType(this.requireClassifierByName("IExpression"));
    senderArgument.setOptional(true);
    senderArgument.setMultiple(false);
  }

  public Concept getDecisionNode() {
    return this.requireConceptByName("DecisionNode");
  }

  private void initDecisionNode() {
    Concept concept = this.requireConceptByName("DecisionNode");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ControlNode"));
  }

  public Concept getMergeNode() {
    return this.requireConceptByName("MergeNode");
  }

  private void initMergeNode() {
    Concept concept = this.requireConceptByName("MergeNode");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ControlNode"));
  }

  public Concept getLoopActionUsage() {
    return this.requireConceptByName("LoopActionUsage");
  }

  private void initLoopActionUsage() {
    Concept concept = this.requireConceptByName("LoopActionUsage");
    concept.setAbstract(true);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IActionUsage"));
    Reference bodyAction = new Reference("bodyAction", concept, "sysml-LoopActionUsage-bodyAction");
    bodyAction.setKey("sysml-LoopActionUsage-bodyAction");
    bodyAction.setType(this.requireClassifierByName("IActionUsage"));
    bodyAction.setOptional(false);
    bodyAction.setMultiple(false);
  }

  public Concept getTriggerInvocationExpression() {
    return this.requireConceptByName("TriggerInvocationExpression");
  }

  private void initTriggerInvocationExpression() {
    Concept concept = this.requireConceptByName("TriggerInvocationExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("InvocationExpression"));
    Property kind = new Property("kind", concept, "sysml-TriggerInvocationExpression-kind");
    kind.setKey("sysml-TriggerInvocationExpression-kind");
    kind.setType(this.requireDataTypeByName("TriggerKind"));
    kind.setOptional(false);
  }

  public Concept getAssignmentActionUsage() {
    return this.requireConceptByName("AssignmentActionUsage");
  }

  private void initAssignmentActionUsage() {
    Concept concept = this.requireConceptByName("AssignmentActionUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IActionUsage"));
    Reference targetArgument = new Reference("targetArgument", concept, "sysml-AssignmentActionUsage-targetArgument");
    targetArgument.setKey("sysml-AssignmentActionUsage-targetArgument");
    targetArgument.setType(this.requireClassifierByName("IExpression"));
    targetArgument.setOptional(true);
    targetArgument.setMultiple(false);
    Reference valueExpression = new Reference("valueExpression", concept, "sysml-AssignmentActionUsage-valueExpression");
    valueExpression.setKey("sysml-AssignmentActionUsage-valueExpression");
    valueExpression.setType(this.requireClassifierByName("IExpression"));
    valueExpression.setOptional(true);
    valueExpression.setMultiple(false);
    Reference referent = new Reference("referent", concept, "sysml-AssignmentActionUsage-referent");
    referent.setKey("sysml-AssignmentActionUsage-referent");
    referent.setType(this.requireClassifierByName("IFeature"));
    referent.setOptional(false);
    referent.setMultiple(false);
  }

  public Concept getForLoopActionUsage() {
    return this.requireConceptByName("ForLoopActionUsage");
  }

  private void initForLoopActionUsage() {
    Concept concept = this.requireConceptByName("ForLoopActionUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("LoopActionUsage"));
    Reference seqArgument = new Reference("seqArgument", concept, "sysml-ForLoopActionUsage-seqArgument");
    seqArgument.setKey("sysml-ForLoopActionUsage-seqArgument");
    seqArgument.setType(this.requireClassifierByName("IExpression"));
    seqArgument.setOptional(false);
    seqArgument.setMultiple(false);
    Reference loopVariable = new Reference("loopVariable", concept, "sysml-ForLoopActionUsage-loopVariable");
    loopVariable.setKey("sysml-ForLoopActionUsage-loopVariable");
    loopVariable.setType(this.requireClassifierByName("ReferenceUsage"));
    loopVariable.setOptional(false);
    loopVariable.setMultiple(false);
  }

  public Concept getIfActionUsage() {
    return this.requireConceptByName("IfActionUsage");
  }

  private void initIfActionUsage() {
    Concept concept = this.requireConceptByName("IfActionUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IActionUsage"));
    Reference elseAction = new Reference("elseAction", concept, "sysml-IfActionUsage-elseAction");
    elseAction.setKey("sysml-IfActionUsage-elseAction");
    elseAction.setType(this.requireClassifierByName("IActionUsage"));
    elseAction.setOptional(true);
    elseAction.setMultiple(false);
    Reference thenAction = new Reference("thenAction", concept, "sysml-IfActionUsage-thenAction");
    thenAction.setKey("sysml-IfActionUsage-thenAction");
    thenAction.setType(this.requireClassifierByName("IActionUsage"));
    thenAction.setOptional(false);
    thenAction.setMultiple(false);
    Reference ifArgument = new Reference("ifArgument", concept, "sysml-IfActionUsage-ifArgument");
    ifArgument.setKey("sysml-IfActionUsage-ifArgument");
    ifArgument.setType(this.requireClassifierByName("IExpression"));
    ifArgument.setOptional(false);
    ifArgument.setMultiple(false);
  }

  public Concept getWhileLoopActionUsage() {
    return this.requireConceptByName("WhileLoopActionUsage");
  }

  private void initWhileLoopActionUsage() {
    Concept concept = this.requireConceptByName("WhileLoopActionUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("LoopActionUsage"));
    Reference whileArgument = new Reference("whileArgument", concept, "sysml-WhileLoopActionUsage-whileArgument");
    whileArgument.setKey("sysml-WhileLoopActionUsage-whileArgument");
    whileArgument.setType(this.requireClassifierByName("IExpression"));
    whileArgument.setOptional(false);
    whileArgument.setMultiple(false);
    Reference untilArgument = new Reference("untilArgument", concept, "sysml-WhileLoopActionUsage-untilArgument");
    untilArgument.setKey("sysml-WhileLoopActionUsage-untilArgument");
    untilArgument.setType(this.requireClassifierByName("IExpression"));
    untilArgument.setOptional(true);
    untilArgument.setMultiple(false);
  }

  public Concept getTerminateActionUsage() {
    return this.requireConceptByName("TerminateActionUsage");
  }

  private void initTerminateActionUsage() {
    Concept concept = this.requireConceptByName("TerminateActionUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IActionUsage"));
    Reference terminatedOccurrenceArgument = new Reference("terminatedOccurrenceArgument", concept, "sysml-TerminateActionUsage-terminatedOccurrenceArgument");
    terminatedOccurrenceArgument.setKey("sysml-TerminateActionUsage-terminatedOccurrenceArgument");
    terminatedOccurrenceArgument.setType(this.requireClassifierByName("IExpression"));
    terminatedOccurrenceArgument.setOptional(true);
    terminatedOccurrenceArgument.setMultiple(false);
  }

  public Concept getMetadataDefinition() {
    return this.requireConceptByName("MetadataDefinition");
  }

  private void initMetadataDefinition() {
    Concept concept = this.requireConceptByName("MetadataDefinition");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ItemDefinition"));
    concept.addImplementedInterface(this.requireInterfaceByName("IMetaclass"));
  }

  public Concept getAliasIdsContainer() {
    return this.requireConceptByName("AliasIdsContainer");
  }

  private void initAliasIdsContainer() {
    Concept concept = this.requireConceptByName("AliasIdsContainer");
    concept.setAbstract(false);
    concept.setPartition(false);
    Property aliasIds = new Property("aliasIds", concept, "sysml-AliasIdsContainer-aliasIds");
    aliasIds.setKey("sysml-AliasIdsContainer-aliasIds");
    aliasIds.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    aliasIds.setOptional(true);
  }

  public Concept getTextContainer() {
    return this.requireConceptByName("TextContainer");
  }

  private void initTextContainer() {
    Concept concept = this.requireConceptByName("TextContainer");
    concept.setAbstract(false);
    concept.setPartition(false);
    Property text = new Property("text", concept, "sysml-TextContainer-text");
    text.setKey("sysml-TextContainer-text");
    text.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    text.setOptional(true);
  }

  public Concept getFeaturing() {
    return this.requireConceptByName("Featuring");
  }

  private void initFeaturing() {
    Concept concept = this.requireConceptByName("Featuring");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IFeaturing"));
  }

  public Concept getRelationship() {
    return this.requireConceptByName("Relationship");
  }

  private void initRelationship() {
    Concept concept = this.requireConceptByName("Relationship");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
  }

  public Concept getElement() {
    return this.requireConceptByName("Element");
  }

  private void initElement() {
    Concept concept = this.requireConceptByName("Element");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IElement"));
  }

  public Concept getAnnotatingElement() {
    return this.requireConceptByName("AnnotatingElement");
  }

  private void initAnnotatingElement() {
    Concept concept = this.requireConceptByName("AnnotatingElement");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IAnnotatingElement"));
  }

  public Concept getStep() {
    return this.requireConceptByName("Step");
  }

  private void initStep() {
    Concept concept = this.requireConceptByName("Step");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IStep"));
  }

  public Concept getFeature() {
    return this.requireConceptByName("Feature");
  }

  private void initFeature() {
    Concept concept = this.requireConceptByName("Feature");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IFeature"));
  }

  public Concept getType() {
    return this.requireConceptByName("Type");
  }

  private void initType() {
    Concept concept = this.requireConceptByName("Type");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IType"));
  }

  public Concept getNamespace() {
    return this.requireConceptByName("Namespace");
  }

  private void initNamespace() {
    Concept concept = this.requireConceptByName("Namespace");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("INamespace"));
  }

  public Concept getBehavior() {
    return this.requireConceptByName("Behavior");
  }

  private void initBehavior() {
    Concept concept = this.requireConceptByName("Behavior");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IBehavior"));
  }

  public Concept getClass_() {
    return this.requireConceptByName("Class");
  }

  private void initClass() {
    Concept concept = this.requireConceptByName("Class");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IClass"));
  }

  public Concept getClassifier() {
    return this.requireConceptByName("Classifier");
  }

  private void initClassifier() {
    Concept concept = this.requireConceptByName("Classifier");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IClassifier"));
  }

  public Concept getSuccession() {
    return this.requireConceptByName("Succession");
  }

  private void initSuccession() {
    Concept concept = this.requireConceptByName("Succession");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("ISuccession"));
  }

  public Concept getConnector() {
    return this.requireConceptByName("Connector");
  }

  private void initConnector() {
    Concept concept = this.requireConceptByName("Connector");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IConnector"));
  }

  public Concept getStructure() {
    return this.requireConceptByName("Structure");
  }

  private void initStructure() {
    Concept concept = this.requireConceptByName("Structure");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IStructure"));
  }

  public Concept getPartUsage() {
    return this.requireConceptByName("PartUsage");
  }

  private void initPartUsage() {
    Concept concept = this.requireConceptByName("PartUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IPartUsage"));
  }

  public Concept getItemUsage() {
    return this.requireConceptByName("ItemUsage");
  }

  private void initItemUsage() {
    Concept concept = this.requireConceptByName("ItemUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IItemUsage"));
  }

  public Concept getOccurrenceUsage() {
    return this.requireConceptByName("OccurrenceUsage");
  }

  private void initOccurrenceUsage() {
    Concept concept = this.requireConceptByName("OccurrenceUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IOccurrenceUsage"));
  }

  public Concept getUsage() {
    return this.requireConceptByName("Usage");
  }

  private void initUsage() {
    Concept concept = this.requireConceptByName("Usage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IUsage"));
  }

  public Concept getDataType() {
    return this.requireConceptByName("DataType");
  }

  private void initDataType() {
    Concept concept = this.requireConceptByName("DataType");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IDataType"));
  }

  public Concept getActionUsage() {
    return this.requireConceptByName("ActionUsage");
  }

  private void initActionUsage() {
    Concept concept = this.requireConceptByName("ActionUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IActionUsage"));
  }

  public Concept getItemFlow() {
    return this.requireConceptByName("ItemFlow");
  }

  private void initItemFlow() {
    Concept concept = this.requireConceptByName("ItemFlow");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IItemFlow"));
  }

  public Concept getAssociationStructure() {
    return this.requireConceptByName("AssociationStructure");
  }

  private void initAssociationStructure() {
    Concept concept = this.requireConceptByName("AssociationStructure");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IAssociationStructure"));
  }

  public Concept getAssociation() {
    return this.requireConceptByName("Association");
  }

  private void initAssociation() {
    Concept concept = this.requireConceptByName("Association");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IAssociation"));
  }

  public Concept getPredicate() {
    return this.requireConceptByName("Predicate");
  }

  private void initPredicate() {
    Concept concept = this.requireConceptByName("Predicate");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IPredicate"));
  }

  public Concept getFunction() {
    return this.requireConceptByName("Function");
  }

  private void initFunction() {
    Concept concept = this.requireConceptByName("Function");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IFunction"));
  }

  public Concept getPerformActionUsage() {
    return this.requireConceptByName("PerformActionUsage");
  }

  private void initPerformActionUsage() {
    Concept concept = this.requireConceptByName("PerformActionUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IPerformActionUsage"));
  }

  public Concept getEventOccurrenceUsage() {
    return this.requireConceptByName("EventOccurrenceUsage");
  }

  private void initEventOccurrenceUsage() {
    Concept concept = this.requireConceptByName("EventOccurrenceUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IEventOccurrenceUsage"));
  }

  public Concept getSuccessionItemFlow() {
    return this.requireConceptByName("SuccessionItemFlow");
  }

  private void initSuccessionItemFlow() {
    Concept concept = this.requireConceptByName("SuccessionItemFlow");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("ISuccessionItemFlow"));
  }

  public Concept getInteraction() {
    return this.requireConceptByName("Interaction");
  }

  private void initInteraction() {
    Concept concept = this.requireConceptByName("Interaction");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IInteraction"));
  }

  public Concept getAssertConstraintUsage() {
    return this.requireConceptByName("AssertConstraintUsage");
  }

  private void initAssertConstraintUsage() {
    Concept concept = this.requireConceptByName("AssertConstraintUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IAssertConstraintUsage"));
  }

  public Concept getConstraintUsage() {
    return this.requireConceptByName("ConstraintUsage");
  }

  private void initConstraintUsage() {
    Concept concept = this.requireConceptByName("ConstraintUsage");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IConstraintUsage"));
  }

  public Concept getBooleanExpression() {
    return this.requireConceptByName("BooleanExpression");
  }

  private void initBooleanExpression() {
    Concept concept = this.requireConceptByName("BooleanExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IBooleanExpression"));
  }

  public Concept getExpression() {
    return this.requireConceptByName("Expression");
  }

  private void initExpression() {
    Concept concept = this.requireConceptByName("Expression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IExpression"));
  }

  public Concept getInvariant() {
    return this.requireConceptByName("Invariant");
  }

  private void initInvariant() {
    Concept concept = this.requireConceptByName("Invariant");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IInvariant"));
  }

  public Concept getExpose() {
    return this.requireConceptByName("Expose");
  }

  private void initExpose() {
    Concept concept = this.requireConceptByName("Expose");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IExpose"));
  }

  public Concept getImport() {
    return this.requireConceptByName("Import");
  }

  private void initImport() {
    Concept concept = this.requireConceptByName("Import");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IImport"));
  }

  public Concept getBindingConnector() {
    return this.requireConceptByName("BindingConnector");
  }

  private void initBindingConnector() {
    Concept concept = this.requireConceptByName("BindingConnector");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IBindingConnector"));
  }

  public Concept getMetaclass() {
    return this.requireConceptByName("Metaclass");
  }

  private void initMetaclass() {
    Concept concept = this.requireConceptByName("Metaclass");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IMetaclass"));
  }

  public Interface getIRelationship() {
    return this.requireInterfaceByName("IRelationship");
  }

  private void initIRelationship() {
    Interface interf = this.requireInterfaceByName("IRelationship");
    interf.addExtendedInterface(this.requireInterfaceByName("IElement"));
    Containment ownedRelatedElement = new Containment("ownedRelatedElement", interf, "sysml-IRelationship-ownedRelatedElement");
    ownedRelatedElement.setKey("sysml-IRelationship-ownedRelatedElement");
    ownedRelatedElement.setType(this.requireClassifierByName("IElement"));
    ownedRelatedElement.setOptional(true);
    ownedRelatedElement.setMultiple(true);
    Reference owningRelatedElement = new Reference("owningRelatedElement", interf, "sysml-IRelationship-owningRelatedElement");
    owningRelatedElement.setKey("sysml-IRelationship-owningRelatedElement");
    owningRelatedElement.setType(this.requireClassifierByName("IElement"));
    owningRelatedElement.setOptional(true);
    owningRelatedElement.setMultiple(false);
    Reference relatedElement = new Reference("relatedElement", interf, "sysml-IRelationship-relatedElement");
    relatedElement.setKey("sysml-IRelationship-relatedElement");
    relatedElement.setType(this.requireClassifierByName("IElement"));
    relatedElement.setOptional(true);
    relatedElement.setMultiple(true);
    Reference target = new Reference("target", interf, "sysml-IRelationship-target");
    target.setKey("sysml-IRelationship-target");
    target.setType(this.requireClassifierByName("IElement"));
    target.setOptional(true);
    target.setMultiple(true);
    Reference source = new Reference("source", interf, "sysml-IRelationship-source");
    source.setKey("sysml-IRelationship-source");
    source.setType(this.requireClassifierByName("IElement"));
    source.setOptional(true);
    source.setMultiple(true);
    Property isImplied = new Property("isImplied", interf, "sysml-IRelationship-isImplied");
    isImplied.setKey("sysml-IRelationship-isImplied");
    isImplied.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isImplied.setOptional(false);
  }

  public Interface getIElement() {
    return this.requireInterfaceByName("IElement");
  }

  private void initIElement() {
    Interface interf = this.requireInterfaceByName("IElement");
    Reference owningMembership = new Reference("owningMembership", interf, "sysml-IElement-owningMembership");
    owningMembership.setKey("sysml-IElement-owningMembership");
    owningMembership.setType(this.requireClassifierByName("OwningMembership"));
    owningMembership.setOptional(true);
    owningMembership.setMultiple(false);
    Reference owningNamespace = new Reference("owningNamespace", interf, "sysml-IElement-owningNamespace");
    owningNamespace.setKey("sysml-IElement-owningNamespace");
    owningNamespace.setType(this.requireClassifierByName("INamespace"));
    owningNamespace.setOptional(true);
    owningNamespace.setMultiple(false);
    Reference owningRelationship = new Reference("owningRelationship", interf, "sysml-IElement-owningRelationship");
    owningRelationship.setKey("sysml-IElement-owningRelationship");
    owningRelationship.setType(this.requireClassifierByName("IRelationship"));
    owningRelationship.setOptional(true);
    owningRelationship.setMultiple(false);
    Property elementId = new Property("elementId", interf, "sysml-IElement-elementId");
    elementId.setKey("sysml-IElement-elementId");
    elementId.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    elementId.setOptional(false);
    Containment ownedRelationship = new Containment("ownedRelationship", interf, "sysml-IElement-ownedRelationship");
    ownedRelationship.setKey("sysml-IElement-ownedRelationship");
    ownedRelationship.setType(this.requireClassifierByName("IRelationship"));
    ownedRelationship.setOptional(true);
    ownedRelationship.setMultiple(true);
    Reference owner = new Reference("owner", interf, "sysml-IElement-owner");
    owner.setKey("sysml-IElement-owner");
    owner.setType(this.requireClassifierByName("IElement"));
    owner.setOptional(true);
    owner.setMultiple(false);
    Reference ownedElement = new Reference("ownedElement", interf, "sysml-IElement-ownedElement");
    ownedElement.setKey("sysml-IElement-ownedElement");
    ownedElement.setType(this.requireClassifierByName("IElement"));
    ownedElement.setOptional(true);
    ownedElement.setMultiple(true);
    Reference documentation = new Reference("documentation", interf, "sysml-IElement-documentation");
    documentation.setKey("sysml-IElement-documentation");
    documentation.setType(this.requireClassifierByName("Documentation"));
    documentation.setOptional(true);
    documentation.setMultiple(true);
    Reference ownedAnnotation = new Reference("ownedAnnotation", interf, "sysml-IElement-ownedAnnotation");
    ownedAnnotation.setKey("sysml-IElement-ownedAnnotation");
    ownedAnnotation.setType(this.requireClassifierByName("Annotation"));
    ownedAnnotation.setOptional(true);
    ownedAnnotation.setMultiple(true);
    Reference textualRepresentation = new Reference("textualRepresentation", interf, "sysml-IElement-textualRepresentation");
    textualRepresentation.setKey("sysml-IElement-textualRepresentation");
    textualRepresentation.setType(this.requireClassifierByName("TextualRepresentation"));
    textualRepresentation.setOptional(true);
    textualRepresentation.setMultiple(true);
    Property declaredShortName = new Property("declaredShortName", interf, "sysml-IElement-declaredShortName");
    declaredShortName.setKey("sysml-IElement-declaredShortName");
    declaredShortName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    declaredShortName.setOptional(true);
    Property declaredName = new Property("declaredName", interf, "sysml-IElement-declaredName");
    declaredName.setKey("sysml-IElement-declaredName");
    declaredName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    declaredName.setOptional(true);
    Property shortName = new Property("shortName", interf, "sysml-IElement-shortName");
    shortName.setKey("sysml-IElement-shortName");
    shortName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    shortName.setOptional(true);
    Property name = new Property("name", interf, "sysml-IElement-name");
    name.setKey("sysml-IElement-name");
    name.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    name.setOptional(true);
    Property qualifiedName = new Property("qualifiedName", interf, "sysml-IElement-qualifiedName");
    qualifiedName.setKey("sysml-IElement-qualifiedName");
    qualifiedName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    qualifiedName.setOptional(true);
    Property isImpliedIncluded = new Property("isImpliedIncluded", interf, "sysml-IElement-isImpliedIncluded");
    isImpliedIncluded.setKey("sysml-IElement-isImpliedIncluded");
    isImpliedIncluded.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isImpliedIncluded.setOptional(false);
    Property isLibraryElement = new Property("isLibraryElement", interf, "sysml-IElement-isLibraryElement");
    isLibraryElement.setKey("sysml-IElement-isLibraryElement");
    isLibraryElement.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isLibraryElement.setOptional(false);
    Containment aliasIdsContainer = new Containment("aliasIdsContainer", interf, "sysml-IElement-aliasIdsContainer");
    aliasIdsContainer.setKey("sysml-IElement-aliasIdsContainer");
    aliasIdsContainer.setType(this.requireClassifierByName("AliasIdsContainer"));
    aliasIdsContainer.setOptional(true);
    aliasIdsContainer.setMultiple(true);
  }

  public Interface getINamespace() {
    return this.requireInterfaceByName("INamespace");
  }

  private void initINamespace() {
    Interface interf = this.requireInterfaceByName("INamespace");
    interf.addExtendedInterface(this.requireInterfaceByName("IElement"));
    Reference membership = new Reference("membership", interf, "sysml-INamespace-membership");
    membership.setKey("sysml-INamespace-membership");
    membership.setType(this.requireClassifierByName("Membership"));
    membership.setOptional(true);
    membership.setMultiple(true);
    Reference ownedImport = new Reference("ownedImport", interf, "sysml-INamespace-ownedImport");
    ownedImport.setKey("sysml-INamespace-ownedImport");
    ownedImport.setType(this.requireClassifierByName("IImport"));
    ownedImport.setOptional(true);
    ownedImport.setMultiple(true);
    Reference member = new Reference("member", interf, "sysml-INamespace-member");
    member.setKey("sysml-INamespace-member");
    member.setType(this.requireClassifierByName("IElement"));
    member.setOptional(true);
    member.setMultiple(true);
    Reference ownedMember = new Reference("ownedMember", interf, "sysml-INamespace-ownedMember");
    ownedMember.setKey("sysml-INamespace-ownedMember");
    ownedMember.setType(this.requireClassifierByName("IElement"));
    ownedMember.setOptional(true);
    ownedMember.setMultiple(true);
    Reference importedMembership = new Reference("importedMembership", interf, "sysml-INamespace-importedMembership");
    importedMembership.setKey("sysml-INamespace-importedMembership");
    importedMembership.setType(this.requireClassifierByName("Membership"));
    importedMembership.setOptional(true);
    importedMembership.setMultiple(true);
    Reference ownedMembership = new Reference("ownedMembership", interf, "sysml-INamespace-ownedMembership");
    ownedMembership.setKey("sysml-INamespace-ownedMembership");
    ownedMembership.setType(this.requireClassifierByName("Membership"));
    ownedMembership.setOptional(true);
    ownedMembership.setMultiple(true);
  }

  public Interface getIImport() {
    return this.requireInterfaceByName("IImport");
  }

  private void initIImport() {
    Interface interf = this.requireInterfaceByName("IImport");
    interf.addExtendedInterface(this.requireInterfaceByName("IRelationship"));
    Property visibility = new Property("visibility", interf, "sysml-IImport-visibility");
    visibility.setKey("sysml-IImport-visibility");
    visibility.setType(this.requireDataTypeByName("VisibilityKind"));
    visibility.setOptional(false);
    Property isRecursive = new Property("isRecursive", interf, "sysml-IImport-isRecursive");
    isRecursive.setKey("sysml-IImport-isRecursive");
    isRecursive.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isRecursive.setOptional(false);
    Property isImportAll = new Property("isImportAll", interf, "sysml-IImport-isImportAll");
    isImportAll.setKey("sysml-IImport-isImportAll");
    isImportAll.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isImportAll.setOptional(false);
    Reference importedElement = new Reference("importedElement", interf, "sysml-IImport-importedElement");
    importedElement.setKey("sysml-IImport-importedElement");
    importedElement.setType(this.requireClassifierByName("IElement"));
    importedElement.setOptional(false);
    importedElement.setMultiple(false);
    Reference importOwningNamespace = new Reference("importOwningNamespace", interf, "sysml-IImport-importOwningNamespace");
    importOwningNamespace.setKey("sysml-IImport-importOwningNamespace");
    importOwningNamespace.setType(this.requireClassifierByName("INamespace"));
    importOwningNamespace.setOptional(false);
    importOwningNamespace.setMultiple(false);
  }

  public Interface getIAnnotatingElement() {
    return this.requireInterfaceByName("IAnnotatingElement");
  }

  private void initIAnnotatingElement() {
    Interface interf = this.requireInterfaceByName("IAnnotatingElement");
    interf.addExtendedInterface(this.requireInterfaceByName("IElement"));
    Reference annotatedElement = new Reference("annotatedElement", interf, "sysml-IAnnotatingElement-annotatedElement");
    annotatedElement.setKey("sysml-IAnnotatingElement-annotatedElement");
    annotatedElement.setType(this.requireClassifierByName("IElement"));
    annotatedElement.setOptional(false);
    annotatedElement.setMultiple(true);
    Reference ownedAnnotatingRelationship = new Reference("ownedAnnotatingRelationship", interf, "sysml-IAnnotatingElement-ownedAnnotatingRelationship");
    ownedAnnotatingRelationship.setKey("sysml-IAnnotatingElement-ownedAnnotatingRelationship");
    ownedAnnotatingRelationship.setType(this.requireClassifierByName("Annotation"));
    ownedAnnotatingRelationship.setOptional(true);
    ownedAnnotatingRelationship.setMultiple(true);
    Reference annotation = new Reference("annotation", interf, "sysml-IAnnotatingElement-annotation");
    annotation.setKey("sysml-IAnnotatingElement-annotation");
    annotation.setType(this.requireClassifierByName("Annotation"));
    annotation.setOptional(true);
    annotation.setMultiple(true);
    Reference owningAnnotatingRelationship = new Reference("owningAnnotatingRelationship", interf, "sysml-IAnnotatingElement-owningAnnotatingRelationship");
    owningAnnotatingRelationship.setKey("sysml-IAnnotatingElement-owningAnnotatingRelationship");
    owningAnnotatingRelationship.setType(this.requireClassifierByName("Annotation"));
    owningAnnotatingRelationship.setOptional(true);
    owningAnnotatingRelationship.setMultiple(false);
  }

  public Interface getIType() {
    return this.requireInterfaceByName("IType");
  }

  private void initIType() {
    Interface interf = this.requireInterfaceByName("IType");
    interf.addExtendedInterface(this.requireInterfaceByName("INamespace"));
    Reference ownedFeatureMembership = new Reference("ownedFeatureMembership", interf, "sysml-IType-ownedFeatureMembership");
    ownedFeatureMembership.setKey("sysml-IType-ownedFeatureMembership");
    ownedFeatureMembership.setType(this.requireClassifierByName("FeatureMembership"));
    ownedFeatureMembership.setOptional(true);
    ownedFeatureMembership.setMultiple(true);
    Reference ownedFeature = new Reference("ownedFeature", interf, "sysml-IType-ownedFeature");
    ownedFeature.setKey("sysml-IType-ownedFeature");
    ownedFeature.setType(this.requireClassifierByName("IFeature"));
    ownedFeature.setOptional(true);
    ownedFeature.setMultiple(true);
    Reference ownedEndFeature = new Reference("ownedEndFeature", interf, "sysml-IType-ownedEndFeature");
    ownedEndFeature.setKey("sysml-IType-ownedEndFeature");
    ownedEndFeature.setType(this.requireClassifierByName("IFeature"));
    ownedEndFeature.setOptional(true);
    ownedEndFeature.setMultiple(true);
    Reference feature = new Reference("feature", interf, "sysml-IType-feature");
    feature.setKey("sysml-IType-feature");
    feature.setType(this.requireClassifierByName("IFeature"));
    feature.setOptional(true);
    feature.setMultiple(true);
    Reference input = new Reference("input", interf, "sysml-IType-input");
    input.setKey("sysml-IType-input");
    input.setType(this.requireClassifierByName("IFeature"));
    input.setOptional(true);
    input.setMultiple(true);
    Reference output = new Reference("output", interf, "sysml-IType-output");
    output.setKey("sysml-IType-output");
    output.setType(this.requireClassifierByName("IFeature"));
    output.setOptional(true);
    output.setMultiple(true);
    Property isAbstract = new Property("isAbstract", interf, "sysml-IType-isAbstract");
    isAbstract.setKey("sysml-IType-isAbstract");
    isAbstract.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isAbstract.setOptional(false);
    Reference inheritedMembership = new Reference("inheritedMembership", interf, "sysml-IType-inheritedMembership");
    inheritedMembership.setKey("sysml-IType-inheritedMembership");
    inheritedMembership.setType(this.requireClassifierByName("Membership"));
    inheritedMembership.setOptional(true);
    inheritedMembership.setMultiple(true);
    Reference endFeature = new Reference("endFeature", interf, "sysml-IType-endFeature");
    endFeature.setKey("sysml-IType-endFeature");
    endFeature.setType(this.requireClassifierByName("IFeature"));
    endFeature.setOptional(true);
    endFeature.setMultiple(true);
    Property isSufficient = new Property("isSufficient", interf, "sysml-IType-isSufficient");
    isSufficient.setKey("sysml-IType-isSufficient");
    isSufficient.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isSufficient.setOptional(false);
    Reference ownedConjugator = new Reference("ownedConjugator", interf, "sysml-IType-ownedConjugator");
    ownedConjugator.setKey("sysml-IType-ownedConjugator");
    ownedConjugator.setType(this.requireClassifierByName("Conjugation"));
    ownedConjugator.setOptional(true);
    ownedConjugator.setMultiple(false);
    Property isConjugated = new Property("isConjugated", interf, "sysml-IType-isConjugated");
    isConjugated.setKey("sysml-IType-isConjugated");
    isConjugated.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isConjugated.setOptional(false);
    Reference inheritedFeature = new Reference("inheritedFeature", interf, "sysml-IType-inheritedFeature");
    inheritedFeature.setKey("sysml-IType-inheritedFeature");
    inheritedFeature.setType(this.requireClassifierByName("IFeature"));
    inheritedFeature.setOptional(true);
    inheritedFeature.setMultiple(true);
    Reference multiplicity = new Reference("multiplicity", interf, "sysml-IType-multiplicity");
    multiplicity.setKey("sysml-IType-multiplicity");
    multiplicity.setType(this.requireClassifierByName("Multiplicity"));
    multiplicity.setOptional(true);
    multiplicity.setMultiple(false);
    Reference unioningType = new Reference("unioningType", interf, "sysml-IType-unioningType");
    unioningType.setKey("sysml-IType-unioningType");
    unioningType.setType(this.requireClassifierByName("IType"));
    unioningType.setOptional(true);
    unioningType.setMultiple(true);
    Reference ownedIntersecting = new Reference("ownedIntersecting", interf, "sysml-IType-ownedIntersecting");
    ownedIntersecting.setKey("sysml-IType-ownedIntersecting");
    ownedIntersecting.setType(this.requireClassifierByName("Intersecting"));
    ownedIntersecting.setOptional(true);
    ownedIntersecting.setMultiple(true);
    Reference intersectingType = new Reference("intersectingType", interf, "sysml-IType-intersectingType");
    intersectingType.setKey("sysml-IType-intersectingType");
    intersectingType.setType(this.requireClassifierByName("IType"));
    intersectingType.setOptional(true);
    intersectingType.setMultiple(true);
    Reference ownedUnioning = new Reference("ownedUnioning", interf, "sysml-IType-ownedUnioning");
    ownedUnioning.setKey("sysml-IType-ownedUnioning");
    ownedUnioning.setType(this.requireClassifierByName("Unioning"));
    ownedUnioning.setOptional(true);
    ownedUnioning.setMultiple(true);
    Reference ownedDisjoining = new Reference("ownedDisjoining", interf, "sysml-IType-ownedDisjoining");
    ownedDisjoining.setKey("sysml-IType-ownedDisjoining");
    ownedDisjoining.setType(this.requireClassifierByName("Disjoining"));
    ownedDisjoining.setOptional(true);
    ownedDisjoining.setMultiple(true);
    Reference featureMembership = new Reference("featureMembership", interf, "sysml-IType-featureMembership");
    featureMembership.setKey("sysml-IType-featureMembership");
    featureMembership.setType(this.requireClassifierByName("FeatureMembership"));
    featureMembership.setOptional(true);
    featureMembership.setMultiple(true);
    Reference differencingType = new Reference("differencingType", interf, "sysml-IType-differencingType");
    differencingType.setKey("sysml-IType-differencingType");
    differencingType.setType(this.requireClassifierByName("IType"));
    differencingType.setOptional(true);
    differencingType.setMultiple(true);
    Reference ownedDifferencing = new Reference("ownedDifferencing", interf, "sysml-IType-ownedDifferencing");
    ownedDifferencing.setKey("sysml-IType-ownedDifferencing");
    ownedDifferencing.setType(this.requireClassifierByName("Differencing"));
    ownedDifferencing.setOptional(true);
    ownedDifferencing.setMultiple(true);
    Reference directedFeature = new Reference("directedFeature", interf, "sysml-IType-directedFeature");
    directedFeature.setKey("sysml-IType-directedFeature");
    directedFeature.setType(this.requireClassifierByName("IFeature"));
    directedFeature.setOptional(true);
    directedFeature.setMultiple(true);
    Reference ownedSpecialization = new Reference("ownedSpecialization", interf, "sysml-IType-ownedSpecialization");
    ownedSpecialization.setKey("sysml-IType-ownedSpecialization");
    ownedSpecialization.setType(this.requireClassifierByName("Specialization"));
    ownedSpecialization.setOptional(true);
    ownedSpecialization.setMultiple(true);
  }

  public Interface getIFeaturing() {
    return this.requireInterfaceByName("IFeaturing");
  }

  private void initIFeaturing() {
    Interface interf = this.requireInterfaceByName("IFeaturing");
    interf.addExtendedInterface(this.requireInterfaceByName("IRelationship"));
    Reference type = new Reference("type", interf, "sysml-IFeaturing-type");
    type.setKey("sysml-IFeaturing-type");
    type.setType(this.requireClassifierByName("IType"));
    type.setOptional(false);
    type.setMultiple(false);
    Reference feature = new Reference("feature", interf, "sysml-IFeaturing-feature");
    feature.setKey("sysml-IFeaturing-feature");
    feature.setType(this.requireClassifierByName("IFeature"));
    feature.setOptional(false);
    feature.setMultiple(false);
  }

  public Interface getIFeature() {
    return this.requireInterfaceByName("IFeature");
  }

  private void initIFeature() {
    Interface interf = this.requireInterfaceByName("IFeature");
    interf.addExtendedInterface(this.requireInterfaceByName("IType"));
    Reference owningType = new Reference("owningType", interf, "sysml-IFeature-owningType");
    owningType.setKey("sysml-IFeature-owningType");
    owningType.setType(this.requireClassifierByName("IType"));
    owningType.setOptional(true);
    owningType.setMultiple(false);
    Property isUnique = new Property("isUnique", interf, "sysml-IFeature-isUnique");
    isUnique.setKey("sysml-IFeature-isUnique");
    isUnique.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isUnique.setOptional(false);
    Property isOrdered = new Property("isOrdered", interf, "sysml-IFeature-isOrdered");
    isOrdered.setKey("sysml-IFeature-isOrdered");
    isOrdered.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isOrdered.setOptional(false);
    Reference type = new Reference("type", interf, "sysml-IFeature-type");
    type.setKey("sysml-IFeature-type");
    type.setType(this.requireClassifierByName("IType"));
    type.setOptional(true);
    type.setMultiple(true);
    Reference ownedRedefinition = new Reference("ownedRedefinition", interf, "sysml-IFeature-ownedRedefinition");
    ownedRedefinition.setKey("sysml-IFeature-ownedRedefinition");
    ownedRedefinition.setType(this.requireClassifierByName("Redefinition"));
    ownedRedefinition.setOptional(true);
    ownedRedefinition.setMultiple(true);
    Reference ownedSubsetting = new Reference("ownedSubsetting", interf, "sysml-IFeature-ownedSubsetting");
    ownedSubsetting.setKey("sysml-IFeature-ownedSubsetting");
    ownedSubsetting.setType(this.requireClassifierByName("Subsetting"));
    ownedSubsetting.setOptional(true);
    ownedSubsetting.setMultiple(true);
    Reference owningFeatureMembership = new Reference("owningFeatureMembership", interf, "sysml-IFeature-owningFeatureMembership");
    owningFeatureMembership.setKey("sysml-IFeature-owningFeatureMembership");
    owningFeatureMembership.setType(this.requireClassifierByName("FeatureMembership"));
    owningFeatureMembership.setOptional(true);
    owningFeatureMembership.setMultiple(false);
    Property isComposite = new Property("isComposite", interf, "sysml-IFeature-isComposite");
    isComposite.setKey("sysml-IFeature-isComposite");
    isComposite.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isComposite.setOptional(false);
    Property isEnd = new Property("isEnd", interf, "sysml-IFeature-isEnd");
    isEnd.setKey("sysml-IFeature-isEnd");
    isEnd.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isEnd.setOptional(false);
    Reference endOwningType = new Reference("endOwningType", interf, "sysml-IFeature-endOwningType");
    endOwningType.setKey("sysml-IFeature-endOwningType");
    endOwningType.setType(this.requireClassifierByName("IType"));
    endOwningType.setOptional(true);
    endOwningType.setMultiple(false);
    Reference ownedTyping = new Reference("ownedTyping", interf, "sysml-IFeature-ownedTyping");
    ownedTyping.setKey("sysml-IFeature-ownedTyping");
    ownedTyping.setType(this.requireClassifierByName("FeatureTyping"));
    ownedTyping.setOptional(true);
    ownedTyping.setMultiple(true);
    Reference featuringType = new Reference("featuringType", interf, "sysml-IFeature-featuringType");
    featuringType.setKey("sysml-IFeature-featuringType");
    featuringType.setType(this.requireClassifierByName("IType"));
    featuringType.setOptional(true);
    featuringType.setMultiple(true);
    Reference ownedTypeFeaturing = new Reference("ownedTypeFeaturing", interf, "sysml-IFeature-ownedTypeFeaturing");
    ownedTypeFeaturing.setKey("sysml-IFeature-ownedTypeFeaturing");
    ownedTypeFeaturing.setType(this.requireClassifierByName("TypeFeaturing"));
    ownedTypeFeaturing.setOptional(true);
    ownedTypeFeaturing.setMultiple(true);
    Property isDerived = new Property("isDerived", interf, "sysml-IFeature-isDerived");
    isDerived.setKey("sysml-IFeature-isDerived");
    isDerived.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isDerived.setOptional(false);
    Reference chainingFeature = new Reference("chainingFeature", interf, "sysml-IFeature-chainingFeature");
    chainingFeature.setKey("sysml-IFeature-chainingFeature");
    chainingFeature.setType(this.requireClassifierByName("IFeature"));
    chainingFeature.setOptional(true);
    chainingFeature.setMultiple(true);
    Reference ownedFeatureInverting = new Reference("ownedFeatureInverting", interf, "sysml-IFeature-ownedFeatureInverting");
    ownedFeatureInverting.setKey("sysml-IFeature-ownedFeatureInverting");
    ownedFeatureInverting.setType(this.requireClassifierByName("FeatureInverting"));
    ownedFeatureInverting.setOptional(true);
    ownedFeatureInverting.setMultiple(true);
    Reference ownedFeatureChaining = new Reference("ownedFeatureChaining", interf, "sysml-IFeature-ownedFeatureChaining");
    ownedFeatureChaining.setKey("sysml-IFeature-ownedFeatureChaining");
    ownedFeatureChaining.setType(this.requireClassifierByName("FeatureChaining"));
    ownedFeatureChaining.setOptional(true);
    ownedFeatureChaining.setMultiple(true);
    Property isReadOnly = new Property("isReadOnly", interf, "sysml-IFeature-isReadOnly");
    isReadOnly.setKey("sysml-IFeature-isReadOnly");
    isReadOnly.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isReadOnly.setOptional(false);
    Property isPortion = new Property("isPortion", interf, "sysml-IFeature-isPortion");
    isPortion.setKey("sysml-IFeature-isPortion");
    isPortion.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isPortion.setOptional(false);
    Property direction = new Property("direction", interf, "sysml-IFeature-direction");
    direction.setKey("sysml-IFeature-direction");
    direction.setType(this.requireDataTypeByName("FeatureDirectionKind"));
    direction.setOptional(true);
    Reference ownedReferenceSubsetting = new Reference("ownedReferenceSubsetting", interf, "sysml-IFeature-ownedReferenceSubsetting");
    ownedReferenceSubsetting.setKey("sysml-IFeature-ownedReferenceSubsetting");
    ownedReferenceSubsetting.setType(this.requireClassifierByName("ReferenceSubsetting"));
    ownedReferenceSubsetting.setOptional(true);
    ownedReferenceSubsetting.setMultiple(false);
    Reference crossFeature = new Reference("crossFeature", interf, "sysml-IFeature-crossFeature");
    crossFeature.setKey("sysml-IFeature-crossFeature");
    crossFeature.setType(this.requireClassifierByName("IFeature"));
    crossFeature.setOptional(true);
    crossFeature.setMultiple(false);
    Reference ownedCrossSubsetting = new Reference("ownedCrossSubsetting", interf, "sysml-IFeature-ownedCrossSubsetting");
    ownedCrossSubsetting.setKey("sysml-IFeature-ownedCrossSubsetting");
    ownedCrossSubsetting.setType(this.requireClassifierByName("CrossSubsetting"));
    ownedCrossSubsetting.setOptional(true);
    ownedCrossSubsetting.setMultiple(false);
    Reference featureTarget = new Reference("featureTarget", interf, "sysml-IFeature-featureTarget");
    featureTarget.setKey("sysml-IFeature-featureTarget");
    featureTarget.setType(this.requireClassifierByName("IFeature"));
    featureTarget.setOptional(false);
    featureTarget.setMultiple(false);
    Property isNonunique = new Property("isNonunique", interf, "sysml-IFeature-isNonunique");
    isNonunique.setKey("sysml-IFeature-isNonunique");
    isNonunique.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isNonunique.setOptional(false);
  }

  public Interface getIClassifier() {
    return this.requireInterfaceByName("IClassifier");
  }

  private void initIClassifier() {
    Interface interf = this.requireInterfaceByName("IClassifier");
    interf.addExtendedInterface(this.requireInterfaceByName("IType"));
    Reference ownedSubclassification = new Reference("ownedSubclassification", interf, "sysml-IClassifier-ownedSubclassification");
    ownedSubclassification.setKey("sysml-IClassifier-ownedSubclassification");
    ownedSubclassification.setType(this.requireClassifierByName("Subclassification"));
    ownedSubclassification.setOptional(true);
    ownedSubclassification.setMultiple(true);
  }

  public Interface getIExpression() {
    return this.requireInterfaceByName("IExpression");
  }

  private void initIExpression() {
    Interface interf = this.requireInterfaceByName("IExpression");
    interf.addExtendedInterface(this.requireInterfaceByName("IStep"));
    Reference function = new Reference("function", interf, "sysml-IExpression-function");
    function.setKey("sysml-IExpression-function");
    function.setType(this.requireClassifierByName("IFunction"));
    function.setOptional(true);
    function.setMultiple(false);
    Reference result = new Reference("result", interf, "sysml-IExpression-result");
    result.setKey("sysml-IExpression-result");
    result.setType(this.requireClassifierByName("IFeature"));
    result.setOptional(false);
    result.setMultiple(false);
    Property isModelLevelEvaluable = new Property("isModelLevelEvaluable", interf, "sysml-IExpression-isModelLevelEvaluable");
    isModelLevelEvaluable.setKey("sysml-IExpression-isModelLevelEvaluable");
    isModelLevelEvaluable.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isModelLevelEvaluable.setOptional(false);
  }

  public Interface getIStep() {
    return this.requireInterfaceByName("IStep");
  }

  private void initIStep() {
    Interface interf = this.requireInterfaceByName("IStep");
    interf.addExtendedInterface(this.requireInterfaceByName("IFeature"));
    Reference behavior = new Reference("behavior", interf, "sysml-IStep-behavior");
    behavior.setKey("sysml-IStep-behavior");
    behavior.setType(this.requireClassifierByName("IBehavior"));
    behavior.setOptional(true);
    behavior.setMultiple(true);
    Reference parameter = new Reference("parameter", interf, "sysml-IStep-parameter");
    parameter.setKey("sysml-IStep-parameter");
    parameter.setType(this.requireClassifierByName("IFeature"));
    parameter.setOptional(true);
    parameter.setMultiple(true);
  }

  public Interface getIBehavior() {
    return this.requireInterfaceByName("IBehavior");
  }

  private void initIBehavior() {
    Interface interf = this.requireInterfaceByName("IBehavior");
    interf.addExtendedInterface(this.requireInterfaceByName("IClass"));
    Reference step = new Reference("step", interf, "sysml-IBehavior-step");
    step.setKey("sysml-IBehavior-step");
    step.setType(this.requireClassifierByName("IStep"));
    step.setOptional(true);
    step.setMultiple(true);
    Reference parameter = new Reference("parameter", interf, "sysml-IBehavior-parameter");
    parameter.setKey("sysml-IBehavior-parameter");
    parameter.setType(this.requireClassifierByName("IFeature"));
    parameter.setOptional(true);
    parameter.setMultiple(true);
  }

  public Interface getIClass() {
    return this.requireInterfaceByName("IClass");
  }

  private void initIClass() {
    Interface interf = this.requireInterfaceByName("IClass");
    interf.addExtendedInterface(this.requireInterfaceByName("IClassifier"));
  }

  public Interface getIFunction() {
    return this.requireInterfaceByName("IFunction");
  }

  private void initIFunction() {
    Interface interf = this.requireInterfaceByName("IFunction");
    interf.addExtendedInterface(this.requireInterfaceByName("IBehavior"));
    Reference expression = new Reference("expression", interf, "sysml-IFunction-expression");
    expression.setKey("sysml-IFunction-expression");
    expression.setType(this.requireClassifierByName("IExpression"));
    expression.setOptional(true);
    expression.setMultiple(true);
    Reference result = new Reference("result", interf, "sysml-IFunction-result");
    result.setKey("sysml-IFunction-result");
    result.setType(this.requireClassifierByName("IFeature"));
    result.setOptional(false);
    result.setMultiple(false);
    Property isModelLevelEvaluable = new Property("isModelLevelEvaluable", interf, "sysml-IFunction-isModelLevelEvaluable");
    isModelLevelEvaluable.setKey("sysml-IFunction-isModelLevelEvaluable");
    isModelLevelEvaluable.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isModelLevelEvaluable.setOptional(false);
  }

  public Interface getIInvariant() {
    return this.requireInterfaceByName("IInvariant");
  }

  private void initIInvariant() {
    Interface interf = this.requireInterfaceByName("IInvariant");
    interf.addExtendedInterface(this.requireInterfaceByName("IBooleanExpression"));
    Property isNegated = new Property("isNegated", interf, "sysml-IInvariant-isNegated");
    isNegated.setKey("sysml-IInvariant-isNegated");
    isNegated.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isNegated.setOptional(false);
  }

  public Interface getIBooleanExpression() {
    return this.requireInterfaceByName("IBooleanExpression");
  }

  private void initIBooleanExpression() {
    Interface interf = this.requireInterfaceByName("IBooleanExpression");
    interf.addExtendedInterface(this.requireInterfaceByName("IExpression"));
    Reference predicate = new Reference("predicate", interf, "sysml-IBooleanExpression-predicate");
    predicate.setKey("sysml-IBooleanExpression-predicate");
    predicate.setType(this.requireClassifierByName("IPredicate"));
    predicate.setOptional(true);
    predicate.setMultiple(false);
  }

  public Interface getIPredicate() {
    return this.requireInterfaceByName("IPredicate");
  }

  private void initIPredicate() {
    Interface interf = this.requireInterfaceByName("IPredicate");
    interf.addExtendedInterface(this.requireInterfaceByName("IFunction"));
  }

  public Interface getIStructure() {
    return this.requireInterfaceByName("IStructure");
  }

  private void initIStructure() {
    Interface interf = this.requireInterfaceByName("IStructure");
    interf.addExtendedInterface(this.requireInterfaceByName("IClass"));
  }

  public Interface getIMetaclass() {
    return this.requireInterfaceByName("IMetaclass");
  }

  private void initIMetaclass() {
    Interface interf = this.requireInterfaceByName("IMetaclass");
    interf.addExtendedInterface(this.requireInterfaceByName("IStructure"));
  }

  public Interface getIItemFlow() {
    return this.requireInterfaceByName("IItemFlow");
  }

  private void initIItemFlow() {
    Interface interf = this.requireInterfaceByName("IItemFlow");
    interf.addExtendedInterface(this.requireInterfaceByName("IConnector"));
    interf.addExtendedInterface(this.requireInterfaceByName("IStep"));
    Reference itemType = new Reference("itemType", interf, "sysml-IItemFlow-itemType");
    itemType.setKey("sysml-IItemFlow-itemType");
    itemType.setType(this.requireClassifierByName("IClassifier"));
    itemType.setOptional(true);
    itemType.setMultiple(true);
    Reference targetInputFeature = new Reference("targetInputFeature", interf, "sysml-IItemFlow-targetInputFeature");
    targetInputFeature.setKey("sysml-IItemFlow-targetInputFeature");
    targetInputFeature.setType(this.requireClassifierByName("IFeature"));
    targetInputFeature.setOptional(true);
    targetInputFeature.setMultiple(false);
    Reference sourceOutputFeature = new Reference("sourceOutputFeature", interf, "sysml-IItemFlow-sourceOutputFeature");
    sourceOutputFeature.setKey("sysml-IItemFlow-sourceOutputFeature");
    sourceOutputFeature.setType(this.requireClassifierByName("IFeature"));
    sourceOutputFeature.setOptional(true);
    sourceOutputFeature.setMultiple(false);
    Reference itemFlowEnd = new Reference("itemFlowEnd", interf, "sysml-IItemFlow-itemFlowEnd");
    itemFlowEnd.setKey("sysml-IItemFlow-itemFlowEnd");
    itemFlowEnd.setType(this.requireClassifierByName("ItemFlowEnd"));
    itemFlowEnd.setOptional(true);
    itemFlowEnd.setMultiple(true);
    Reference itemFeature = new Reference("itemFeature", interf, "sysml-IItemFlow-itemFeature");
    itemFeature.setKey("sysml-IItemFlow-itemFeature");
    itemFeature.setType(this.requireClassifierByName("ItemFeature"));
    itemFeature.setOptional(true);
    itemFeature.setMultiple(false);
    Reference interaction = new Reference("interaction", interf, "sysml-IItemFlow-interaction");
    interaction.setKey("sysml-IItemFlow-interaction");
    interaction.setType(this.requireClassifierByName("IInteraction"));
    interaction.setOptional(true);
    interaction.setMultiple(true);
  }

  public Interface getIConnector() {
    return this.requireInterfaceByName("IConnector");
  }

  private void initIConnector() {
    Interface interf = this.requireInterfaceByName("IConnector");
    interf.addExtendedInterface(this.requireInterfaceByName("IFeature"));
    interf.addExtendedInterface(this.requireInterfaceByName("IRelationship"));
    Reference relatedFeature = new Reference("relatedFeature", interf, "sysml-IConnector-relatedFeature");
    relatedFeature.setKey("sysml-IConnector-relatedFeature");
    relatedFeature.setType(this.requireClassifierByName("IFeature"));
    relatedFeature.setOptional(true);
    relatedFeature.setMultiple(true);
    Reference association = new Reference("association", interf, "sysml-IConnector-association");
    association.setKey("sysml-IConnector-association");
    association.setType(this.requireClassifierByName("IAssociation"));
    association.setOptional(true);
    association.setMultiple(true);
    Reference connectorEnd = new Reference("connectorEnd", interf, "sysml-IConnector-connectorEnd");
    connectorEnd.setKey("sysml-IConnector-connectorEnd");
    connectorEnd.setType(this.requireClassifierByName("IFeature"));
    connectorEnd.setOptional(true);
    connectorEnd.setMultiple(true);
    Reference sourceFeature = new Reference("sourceFeature", interf, "sysml-IConnector-sourceFeature");
    sourceFeature.setKey("sysml-IConnector-sourceFeature");
    sourceFeature.setType(this.requireClassifierByName("IFeature"));
    sourceFeature.setOptional(true);
    sourceFeature.setMultiple(false);
    Reference targetFeature = new Reference("targetFeature", interf, "sysml-IConnector-targetFeature");
    targetFeature.setKey("sysml-IConnector-targetFeature");
    targetFeature.setType(this.requireClassifierByName("IFeature"));
    targetFeature.setOptional(true);
    targetFeature.setMultiple(true);
  }

  public Interface getIAssociation() {
    return this.requireInterfaceByName("IAssociation");
  }

  private void initIAssociation() {
    Interface interf = this.requireInterfaceByName("IAssociation");
    interf.addExtendedInterface(this.requireInterfaceByName("IClassifier"));
    interf.addExtendedInterface(this.requireInterfaceByName("IRelationship"));
    Reference relatedType = new Reference("relatedType", interf, "sysml-IAssociation-relatedType");
    relatedType.setKey("sysml-IAssociation-relatedType");
    relatedType.setType(this.requireClassifierByName("IType"));
    relatedType.setOptional(true);
    relatedType.setMultiple(true);
    Reference sourceType = new Reference("sourceType", interf, "sysml-IAssociation-sourceType");
    sourceType.setKey("sysml-IAssociation-sourceType");
    sourceType.setType(this.requireClassifierByName("IType"));
    sourceType.setOptional(true);
    sourceType.setMultiple(false);
    Reference targetType = new Reference("targetType", interf, "sysml-IAssociation-targetType");
    targetType.setKey("sysml-IAssociation-targetType");
    targetType.setType(this.requireClassifierByName("IType"));
    targetType.setOptional(true);
    targetType.setMultiple(true);
    Reference associationEnd = new Reference("associationEnd", interf, "sysml-IAssociation-associationEnd");
    associationEnd.setKey("sysml-IAssociation-associationEnd");
    associationEnd.setType(this.requireClassifierByName("IFeature"));
    associationEnd.setOptional(true);
    associationEnd.setMultiple(true);
  }

  public Interface getIInteraction() {
    return this.requireInterfaceByName("IInteraction");
  }

  private void initIInteraction() {
    Interface interf = this.requireInterfaceByName("IInteraction");
    interf.addExtendedInterface(this.requireInterfaceByName("IAssociation"));
    interf.addExtendedInterface(this.requireInterfaceByName("IBehavior"));
  }

  public Interface getISuccessionItemFlow() {
    return this.requireInterfaceByName("ISuccessionItemFlow");
  }

  private void initISuccessionItemFlow() {
    Interface interf = this.requireInterfaceByName("ISuccessionItemFlow");
    interf.addExtendedInterface(this.requireInterfaceByName("IItemFlow"));
    interf.addExtendedInterface(this.requireInterfaceByName("ISuccession"));
  }

  public Interface getISuccession() {
    return this.requireInterfaceByName("ISuccession");
  }

  private void initISuccession() {
    Interface interf = this.requireInterfaceByName("ISuccession");
    interf.addExtendedInterface(this.requireInterfaceByName("IConnector"));
    Reference transitionStep = new Reference("transitionStep", interf, "sysml-ISuccession-transitionStep");
    transitionStep.setKey("sysml-ISuccession-transitionStep");
    transitionStep.setType(this.requireClassifierByName("IStep"));
    transitionStep.setOptional(true);
    transitionStep.setMultiple(false);
    Reference triggerStep = new Reference("triggerStep", interf, "sysml-ISuccession-triggerStep");
    triggerStep.setKey("sysml-ISuccession-triggerStep");
    triggerStep.setType(this.requireClassifierByName("IStep"));
    triggerStep.setOptional(true);
    triggerStep.setMultiple(true);
    Reference effectStep = new Reference("effectStep", interf, "sysml-ISuccession-effectStep");
    effectStep.setKey("sysml-ISuccession-effectStep");
    effectStep.setType(this.requireClassifierByName("IStep"));
    effectStep.setOptional(true);
    effectStep.setMultiple(true);
    Reference guardExpression = new Reference("guardExpression", interf, "sysml-ISuccession-guardExpression");
    guardExpression.setKey("sysml-ISuccession-guardExpression");
    guardExpression.setType(this.requireClassifierByName("IExpression"));
    guardExpression.setOptional(true);
    guardExpression.setMultiple(true);
  }

  public Interface getIDataType() {
    return this.requireInterfaceByName("IDataType");
  }

  private void initIDataType() {
    Interface interf = this.requireInterfaceByName("IDataType");
    interf.addExtendedInterface(this.requireInterfaceByName("IClassifier"));
  }

  public Interface getIBindingConnector() {
    return this.requireInterfaceByName("IBindingConnector");
  }

  private void initIBindingConnector() {
    Interface interf = this.requireInterfaceByName("IBindingConnector");
    interf.addExtendedInterface(this.requireInterfaceByName("IConnector"));
  }

  public Interface getIAssociationStructure() {
    return this.requireInterfaceByName("IAssociationStructure");
  }

  private void initIAssociationStructure() {
    Interface interf = this.requireInterfaceByName("IAssociationStructure");
    interf.addExtendedInterface(this.requireInterfaceByName("IAssociation"));
    interf.addExtendedInterface(this.requireInterfaceByName("IStructure"));
  }

  public Interface getIUsage() {
    return this.requireInterfaceByName("IUsage");
  }

  private void initIUsage() {
    Interface interf = this.requireInterfaceByName("IUsage");
    interf.addExtendedInterface(this.requireInterfaceByName("IFeature"));
    Property isReference = new Property("isReference", interf, "sysml-IUsage-isReference");
    isReference.setKey("sysml-IUsage-isReference");
    isReference.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isReference.setOptional(false);
    Property isVariation = new Property("isVariation", interf, "sysml-IUsage-isVariation");
    isVariation.setKey("sysml-IUsage-isVariation");
    isVariation.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isVariation.setOptional(false);
    Reference variant = new Reference("variant", interf, "sysml-IUsage-variant");
    variant.setKey("sysml-IUsage-variant");
    variant.setType(this.requireClassifierByName("IUsage"));
    variant.setOptional(true);
    variant.setMultiple(true);
    Reference variantMembership = new Reference("variantMembership", interf, "sysml-IUsage-variantMembership");
    variantMembership.setKey("sysml-IUsage-variantMembership");
    variantMembership.setType(this.requireClassifierByName("VariantMembership"));
    variantMembership.setOptional(true);
    variantMembership.setMultiple(true);
    Reference owningDefinition = new Reference("owningDefinition", interf, "sysml-IUsage-owningDefinition");
    owningDefinition.setKey("sysml-IUsage-owningDefinition");
    owningDefinition.setType(this.requireClassifierByName("Definition"));
    owningDefinition.setOptional(true);
    owningDefinition.setMultiple(false);
    Reference owningUsage = new Reference("owningUsage", interf, "sysml-IUsage-owningUsage");
    owningUsage.setKey("sysml-IUsage-owningUsage");
    owningUsage.setType(this.requireClassifierByName("IUsage"));
    owningUsage.setOptional(true);
    owningUsage.setMultiple(false);
    Reference nestedUsage = new Reference("nestedUsage", interf, "sysml-IUsage-nestedUsage");
    nestedUsage.setKey("sysml-IUsage-nestedUsage");
    nestedUsage.setType(this.requireClassifierByName("IUsage"));
    nestedUsage.setOptional(true);
    nestedUsage.setMultiple(true);
    Reference definition = new Reference("definition", interf, "sysml-IUsage-definition");
    definition.setKey("sysml-IUsage-definition");
    definition.setType(this.requireClassifierByName("IClassifier"));
    definition.setOptional(true);
    definition.setMultiple(true);
    Reference usage = new Reference("usage", interf, "sysml-IUsage-usage");
    usage.setKey("sysml-IUsage-usage");
    usage.setType(this.requireClassifierByName("IUsage"));
    usage.setOptional(true);
    usage.setMultiple(true);
    Reference directedUsage = new Reference("directedUsage", interf, "sysml-IUsage-directedUsage");
    directedUsage.setKey("sysml-IUsage-directedUsage");
    directedUsage.setType(this.requireClassifierByName("IUsage"));
    directedUsage.setOptional(true);
    directedUsage.setMultiple(true);
    Reference nestedReference = new Reference("nestedReference", interf, "sysml-IUsage-nestedReference");
    nestedReference.setKey("sysml-IUsage-nestedReference");
    nestedReference.setType(this.requireClassifierByName("ReferenceUsage"));
    nestedReference.setOptional(true);
    nestedReference.setMultiple(true);
    Reference nestedAttribute = new Reference("nestedAttribute", interf, "sysml-IUsage-nestedAttribute");
    nestedAttribute.setKey("sysml-IUsage-nestedAttribute");
    nestedAttribute.setType(this.requireClassifierByName("AttributeUsage"));
    nestedAttribute.setOptional(true);
    nestedAttribute.setMultiple(true);
    Reference nestedEnumeration = new Reference("nestedEnumeration", interf, "sysml-IUsage-nestedEnumeration");
    nestedEnumeration.setKey("sysml-IUsage-nestedEnumeration");
    nestedEnumeration.setType(this.requireClassifierByName("EnumerationUsage"));
    nestedEnumeration.setOptional(true);
    nestedEnumeration.setMultiple(true);
    Reference nestedOccurrence = new Reference("nestedOccurrence", interf, "sysml-IUsage-nestedOccurrence");
    nestedOccurrence.setKey("sysml-IUsage-nestedOccurrence");
    nestedOccurrence.setType(this.requireClassifierByName("IOccurrenceUsage"));
    nestedOccurrence.setOptional(true);
    nestedOccurrence.setMultiple(true);
    Reference nestedItem = new Reference("nestedItem", interf, "sysml-IUsage-nestedItem");
    nestedItem.setKey("sysml-IUsage-nestedItem");
    nestedItem.setType(this.requireClassifierByName("IItemUsage"));
    nestedItem.setOptional(true);
    nestedItem.setMultiple(true);
    Reference nestedPart = new Reference("nestedPart", interf, "sysml-IUsage-nestedPart");
    nestedPart.setKey("sysml-IUsage-nestedPart");
    nestedPart.setType(this.requireClassifierByName("IPartUsage"));
    nestedPart.setOptional(true);
    nestedPart.setMultiple(true);
    Reference nestedPort = new Reference("nestedPort", interf, "sysml-IUsage-nestedPort");
    nestedPort.setKey("sysml-IUsage-nestedPort");
    nestedPort.setType(this.requireClassifierByName("PortUsage"));
    nestedPort.setOptional(true);
    nestedPort.setMultiple(true);
    Reference nestedConnection = new Reference("nestedConnection", interf, "sysml-IUsage-nestedConnection");
    nestedConnection.setKey("sysml-IUsage-nestedConnection");
    nestedConnection.setType(this.requireClassifierByName("ConnectorAsUsage"));
    nestedConnection.setOptional(true);
    nestedConnection.setMultiple(true);
    Reference nestedFlow = new Reference("nestedFlow", interf, "sysml-IUsage-nestedFlow");
    nestedFlow.setKey("sysml-IUsage-nestedFlow");
    nestedFlow.setType(this.requireClassifierByName("FlowConnectionUsage"));
    nestedFlow.setOptional(true);
    nestedFlow.setMultiple(true);
    Reference nestedInterface = new Reference("nestedInterface", interf, "sysml-IUsage-nestedInterface");
    nestedInterface.setKey("sysml-IUsage-nestedInterface");
    nestedInterface.setType(this.requireClassifierByName("InterfaceUsage"));
    nestedInterface.setOptional(true);
    nestedInterface.setMultiple(true);
    Reference nestedAllocation = new Reference("nestedAllocation", interf, "sysml-IUsage-nestedAllocation");
    nestedAllocation.setKey("sysml-IUsage-nestedAllocation");
    nestedAllocation.setType(this.requireClassifierByName("AllocationUsage"));
    nestedAllocation.setOptional(true);
    nestedAllocation.setMultiple(true);
    Reference nestedAction = new Reference("nestedAction", interf, "sysml-IUsage-nestedAction");
    nestedAction.setKey("sysml-IUsage-nestedAction");
    nestedAction.setType(this.requireClassifierByName("IActionUsage"));
    nestedAction.setOptional(true);
    nestedAction.setMultiple(true);
    Reference nestedState = new Reference("nestedState", interf, "sysml-IUsage-nestedState");
    nestedState.setKey("sysml-IUsage-nestedState");
    nestedState.setType(this.requireClassifierByName("StateUsage"));
    nestedState.setOptional(true);
    nestedState.setMultiple(true);
    Reference nestedTransition = new Reference("nestedTransition", interf, "sysml-IUsage-nestedTransition");
    nestedTransition.setKey("sysml-IUsage-nestedTransition");
    nestedTransition.setType(this.requireClassifierByName("TransitionUsage"));
    nestedTransition.setOptional(true);
    nestedTransition.setMultiple(true);
    Reference nestedCalculation = new Reference("nestedCalculation", interf, "sysml-IUsage-nestedCalculation");
    nestedCalculation.setKey("sysml-IUsage-nestedCalculation");
    nestedCalculation.setType(this.requireClassifierByName("CalculationUsage"));
    nestedCalculation.setOptional(true);
    nestedCalculation.setMultiple(true);
    Reference nestedConstraint = new Reference("nestedConstraint", interf, "sysml-IUsage-nestedConstraint");
    nestedConstraint.setKey("sysml-IUsage-nestedConstraint");
    nestedConstraint.setType(this.requireClassifierByName("IConstraintUsage"));
    nestedConstraint.setOptional(true);
    nestedConstraint.setMultiple(true);
    Reference nestedRequirement = new Reference("nestedRequirement", interf, "sysml-IUsage-nestedRequirement");
    nestedRequirement.setKey("sysml-IUsage-nestedRequirement");
    nestedRequirement.setType(this.requireClassifierByName("RequirementUsage"));
    nestedRequirement.setOptional(true);
    nestedRequirement.setMultiple(true);
    Reference nestedConcern = new Reference("nestedConcern", interf, "sysml-IUsage-nestedConcern");
    nestedConcern.setKey("sysml-IUsage-nestedConcern");
    nestedConcern.setType(this.requireClassifierByName("ConcernUsage"));
    nestedConcern.setOptional(true);
    nestedConcern.setMultiple(true);
    Reference nestedCase = new Reference("nestedCase", interf, "sysml-IUsage-nestedCase");
    nestedCase.setKey("sysml-IUsage-nestedCase");
    nestedCase.setType(this.requireClassifierByName("CaseUsage"));
    nestedCase.setOptional(true);
    nestedCase.setMultiple(true);
    Reference nestedAnalysisCase = new Reference("nestedAnalysisCase", interf, "sysml-IUsage-nestedAnalysisCase");
    nestedAnalysisCase.setKey("sysml-IUsage-nestedAnalysisCase");
    nestedAnalysisCase.setType(this.requireClassifierByName("AnalysisCaseUsage"));
    nestedAnalysisCase.setOptional(true);
    nestedAnalysisCase.setMultiple(true);
    Reference nestedVerificationCase = new Reference("nestedVerificationCase", interf, "sysml-IUsage-nestedVerificationCase");
    nestedVerificationCase.setKey("sysml-IUsage-nestedVerificationCase");
    nestedVerificationCase.setType(this.requireClassifierByName("VerificationCaseUsage"));
    nestedVerificationCase.setOptional(true);
    nestedVerificationCase.setMultiple(true);
    Reference nestedUseCase = new Reference("nestedUseCase", interf, "sysml-IUsage-nestedUseCase");
    nestedUseCase.setKey("sysml-IUsage-nestedUseCase");
    nestedUseCase.setType(this.requireClassifierByName("UseCaseUsage"));
    nestedUseCase.setOptional(true);
    nestedUseCase.setMultiple(true);
    Reference nestedView = new Reference("nestedView", interf, "sysml-IUsage-nestedView");
    nestedView.setKey("sysml-IUsage-nestedView");
    nestedView.setType(this.requireClassifierByName("ViewUsage"));
    nestedView.setOptional(true);
    nestedView.setMultiple(true);
    Reference nestedViewpoint = new Reference("nestedViewpoint", interf, "sysml-IUsage-nestedViewpoint");
    nestedViewpoint.setKey("sysml-IUsage-nestedViewpoint");
    nestedViewpoint.setType(this.requireClassifierByName("ViewpointUsage"));
    nestedViewpoint.setOptional(true);
    nestedViewpoint.setMultiple(true);
    Reference nestedRendering = new Reference("nestedRendering", interf, "sysml-IUsage-nestedRendering");
    nestedRendering.setKey("sysml-IUsage-nestedRendering");
    nestedRendering.setType(this.requireClassifierByName("RenderingUsage"));
    nestedRendering.setOptional(true);
    nestedRendering.setMultiple(true);
    Reference nestedMetadata = new Reference("nestedMetadata", interf, "sysml-IUsage-nestedMetadata");
    nestedMetadata.setKey("sysml-IUsage-nestedMetadata");
    nestedMetadata.setType(this.requireClassifierByName("MetadataUsage"));
    nestedMetadata.setOptional(true);
    nestedMetadata.setMultiple(true);
  }

  public Interface getIOccurrenceUsage() {
    return this.requireInterfaceByName("IOccurrenceUsage");
  }

  private void initIOccurrenceUsage() {
    Interface interf = this.requireInterfaceByName("IOccurrenceUsage");
    interf.addExtendedInterface(this.requireInterfaceByName("IUsage"));
    Reference occurrenceDefinition = new Reference("occurrenceDefinition", interf, "sysml-IOccurrenceUsage-occurrenceDefinition");
    occurrenceDefinition.setKey("sysml-IOccurrenceUsage-occurrenceDefinition");
    occurrenceDefinition.setType(this.requireClassifierByName("IClass"));
    occurrenceDefinition.setOptional(true);
    occurrenceDefinition.setMultiple(true);
    Reference individualDefinition = new Reference("individualDefinition", interf, "sysml-IOccurrenceUsage-individualDefinition");
    individualDefinition.setKey("sysml-IOccurrenceUsage-individualDefinition");
    individualDefinition.setType(this.requireClassifierByName("OccurrenceDefinition"));
    individualDefinition.setOptional(true);
    individualDefinition.setMultiple(false);
    Property isIndividual = new Property("isIndividual", interf, "sysml-IOccurrenceUsage-isIndividual");
    isIndividual.setKey("sysml-IOccurrenceUsage-isIndividual");
    isIndividual.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isIndividual.setOptional(false);
    Property portionKind = new Property("portionKind", interf, "sysml-IOccurrenceUsage-portionKind");
    portionKind.setKey("sysml-IOccurrenceUsage-portionKind");
    portionKind.setType(this.requireDataTypeByName("PortionKind"));
    portionKind.setOptional(true);
  }

  public Interface getIItemUsage() {
    return this.requireInterfaceByName("IItemUsage");
  }

  private void initIItemUsage() {
    Interface interf = this.requireInterfaceByName("IItemUsage");
    interf.addExtendedInterface(this.requireInterfaceByName("IOccurrenceUsage"));
    Reference itemDefinition = new Reference("itemDefinition", interf, "sysml-IItemUsage-itemDefinition");
    itemDefinition.setKey("sysml-IItemUsage-itemDefinition");
    itemDefinition.setType(this.requireClassifierByName("IStructure"));
    itemDefinition.setOptional(true);
    itemDefinition.setMultiple(true);
  }

  public Interface getIPartUsage() {
    return this.requireInterfaceByName("IPartUsage");
  }

  private void initIPartUsage() {
    Interface interf = this.requireInterfaceByName("IPartUsage");
    interf.addExtendedInterface(this.requireInterfaceByName("IItemUsage"));
    Reference partDefinition = new Reference("partDefinition", interf, "sysml-IPartUsage-partDefinition");
    partDefinition.setKey("sysml-IPartUsage-partDefinition");
    partDefinition.setType(this.requireClassifierByName("PartDefinition"));
    partDefinition.setOptional(true);
    partDefinition.setMultiple(true);
  }

  public Interface getIActionUsage() {
    return this.requireInterfaceByName("IActionUsage");
  }

  private void initIActionUsage() {
    Interface interf = this.requireInterfaceByName("IActionUsage");
    interf.addExtendedInterface(this.requireInterfaceByName("IOccurrenceUsage"));
    interf.addExtendedInterface(this.requireInterfaceByName("IStep"));
    Reference actionDefinition = new Reference("actionDefinition", interf, "sysml-IActionUsage-actionDefinition");
    actionDefinition.setKey("sysml-IActionUsage-actionDefinition");
    actionDefinition.setType(this.requireClassifierByName("IBehavior"));
    actionDefinition.setOptional(true);
    actionDefinition.setMultiple(true);
  }

  public Interface getIConstraintUsage() {
    return this.requireInterfaceByName("IConstraintUsage");
  }

  private void initIConstraintUsage() {
    Interface interf = this.requireInterfaceByName("IConstraintUsage");
    interf.addExtendedInterface(this.requireInterfaceByName("IOccurrenceUsage"));
    interf.addExtendedInterface(this.requireInterfaceByName("IBooleanExpression"));
    Reference constraintDefinition = new Reference("constraintDefinition", interf, "sysml-IConstraintUsage-constraintDefinition");
    constraintDefinition.setKey("sysml-IConstraintUsage-constraintDefinition");
    constraintDefinition.setType(this.requireClassifierByName("IPredicate"));
    constraintDefinition.setOptional(true);
    constraintDefinition.setMultiple(false);
  }

  public Interface getIPerformActionUsage() {
    return this.requireInterfaceByName("IPerformActionUsage");
  }

  private void initIPerformActionUsage() {
    Interface interf = this.requireInterfaceByName("IPerformActionUsage");
    interf.addExtendedInterface(this.requireInterfaceByName("IActionUsage"));
    interf.addExtendedInterface(this.requireInterfaceByName("IEventOccurrenceUsage"));
    Reference performedAction = new Reference("performedAction", interf, "sysml-IPerformActionUsage-performedAction");
    performedAction.setKey("sysml-IPerformActionUsage-performedAction");
    performedAction.setType(this.requireClassifierByName("IActionUsage"));
    performedAction.setOptional(false);
    performedAction.setMultiple(false);
  }

  public Interface getIEventOccurrenceUsage() {
    return this.requireInterfaceByName("IEventOccurrenceUsage");
  }

  private void initIEventOccurrenceUsage() {
    Interface interf = this.requireInterfaceByName("IEventOccurrenceUsage");
    interf.addExtendedInterface(this.requireInterfaceByName("IOccurrenceUsage"));
    Reference eventOccurrence = new Reference("eventOccurrence", interf, "sysml-IEventOccurrenceUsage-eventOccurrence");
    eventOccurrence.setKey("sysml-IEventOccurrenceUsage-eventOccurrence");
    eventOccurrence.setType(this.requireClassifierByName("IOccurrenceUsage"));
    eventOccurrence.setOptional(false);
    eventOccurrence.setMultiple(false);
  }

  public Interface getIAssertConstraintUsage() {
    return this.requireInterfaceByName("IAssertConstraintUsage");
  }

  private void initIAssertConstraintUsage() {
    Interface interf = this.requireInterfaceByName("IAssertConstraintUsage");
    interf.addExtendedInterface(this.requireInterfaceByName("IConstraintUsage"));
    interf.addExtendedInterface(this.requireInterfaceByName("IInvariant"));
    Reference assertedConstraint = new Reference("assertedConstraint", interf, "sysml-IAssertConstraintUsage-assertedConstraint");
    assertedConstraint.setKey("sysml-IAssertConstraintUsage-assertedConstraint");
    assertedConstraint.setType(this.requireClassifierByName("IConstraintUsage"));
    assertedConstraint.setOptional(false);
    assertedConstraint.setMultiple(false);
  }

  public Interface getIExpose() {
    return this.requireInterfaceByName("IExpose");
  }

  private void initIExpose() {
    Interface interf = this.requireInterfaceByName("IExpose");
    interf.addExtendedInterface(this.requireInterfaceByName("IImport"));
  }

  public Enumeration getVisibilityKind() {
    return this.requireEnumerationByName("VisibilityKind");
  }

  public Enumeration getFeatureDirectionKind() {
    return this.requireEnumerationByName("FeatureDirectionKind");
  }

  public Enumeration getPortionKind() {
    return this.requireEnumerationByName("PortionKind");
  }

  public Enumeration getTransitionFeatureKind() {
    return this.requireEnumerationByName("TransitionFeatureKind");
  }

  public Enumeration getStateSubactionKind() {
    return this.requireEnumerationByName("StateSubactionKind");
  }

  public Enumeration getRequirementConstraintKind() {
    return this.requireEnumerationByName("RequirementConstraintKind");
  }

  public Enumeration getTriggerKind() {
    return this.requireEnumerationByName("TriggerKind");
  }

  private void createElements() {
    new Concept(this, "Subclassification", "sysml-Subclassification", "sysml-Subclassification");;
    new Concept(this, "Specialization", "sysml-Specialization", "sysml-Specialization");;
    new Concept(this, "OwningMembership", "sysml-OwningMembership", "sysml-OwningMembership");;
    new Concept(this, "Membership", "sysml-Membership", "sysml-Membership");;
    new Concept(this, "Documentation", "sysml-Documentation", "sysml-Documentation");;
    new Concept(this, "Comment", "sysml-Comment", "sysml-Comment");;
    new Concept(this, "Annotation", "sysml-Annotation", "sysml-Annotation");;
    new Concept(this, "TextualRepresentation", "sysml-TextualRepresentation", "sysml-TextualRepresentation");;
    new Concept(this, "FeatureMembership", "sysml-FeatureMembership", "sysml-FeatureMembership");;
    new Concept(this, "Redefinition", "sysml-Redefinition", "sysml-Redefinition");;
    new Concept(this, "Subsetting", "sysml-Subsetting", "sysml-Subsetting");;
    new Concept(this, "FeatureTyping", "sysml-FeatureTyping", "sysml-FeatureTyping");;
    new Concept(this, "TypeFeaturing", "sysml-TypeFeaturing", "sysml-TypeFeaturing");;
    new Concept(this, "FeatureInverting", "sysml-FeatureInverting", "sysml-FeatureInverting");;
    new Concept(this, "FeatureChaining", "sysml-FeatureChaining", "sysml-FeatureChaining");;
    new Concept(this, "ReferenceSubsetting", "sysml-ReferenceSubsetting", "sysml-ReferenceSubsetting");;
    new Concept(this, "CrossSubsetting", "sysml-CrossSubsetting", "sysml-CrossSubsetting");;
    new Concept(this, "Conjugation", "sysml-Conjugation", "sysml-Conjugation");;
    new Concept(this, "Multiplicity", "sysml-Multiplicity", "sysml-Multiplicity");;
    new Concept(this, "Intersecting", "sysml-Intersecting", "sysml-Intersecting");;
    new Concept(this, "Unioning", "sysml-Unioning", "sysml-Unioning");;
    new Concept(this, "Disjoining", "sysml-Disjoining", "sysml-Disjoining");;
    new Concept(this, "Differencing", "sysml-Differencing", "sysml-Differencing");;
    new Concept(this, "EndFeatureMembership", "sysml-EndFeatureMembership", "sysml-EndFeatureMembership");;
    new Concept(this, "ResultExpressionMembership", "sysml-ResultExpressionMembership", "sysml-ResultExpressionMembership");;
    new Concept(this, "ReturnParameterMembership", "sysml-ReturnParameterMembership", "sysml-ReturnParameterMembership");;
    new Concept(this, "ParameterMembership", "sysml-ParameterMembership", "sysml-ParameterMembership");;
    new Concept(this, "MultiplicityRange", "sysml-MultiplicityRange", "sysml-MultiplicityRange");;
    new Concept(this, "FeatureValue", "sysml-FeatureValue", "sysml-FeatureValue");;
    new Concept(this, "MetadataFeature", "sysml-MetadataFeature", "sysml-MetadataFeature");;
    new Concept(this, "ItemFlowEnd", "sysml-ItemFlowEnd", "sysml-ItemFlowEnd");;
    new Concept(this, "ItemFeature", "sysml-ItemFeature", "sysml-ItemFeature");;
    new Concept(this, "ElementFilterMembership", "sysml-ElementFilterMembership", "sysml-ElementFilterMembership");;
    new Concept(this, "Package", "sysml-Package", "sysml-Package");;
    new Concept(this, "LibraryPackage", "sysml-LibraryPackage", "sysml-LibraryPackage");;
    new Concept(this, "FeatureReferenceExpression", "sysml-FeatureReferenceExpression", "sysml-FeatureReferenceExpression");;
    new Concept(this, "MetadataAccessExpression", "sysml-MetadataAccessExpression", "sysml-MetadataAccessExpression");;
    new Concept(this, "NullExpression", "sysml-NullExpression", "sysml-NullExpression");;
    new Concept(this, "IndexExpression", "sysml-IndexExpression", "sysml-IndexExpression");;
    new Concept(this, "OperatorExpression", "sysml-OperatorExpression", "sysml-OperatorExpression");;
    new Concept(this, "InvocationExpression", "sysml-InvocationExpression", "sysml-InvocationExpression");;
    new Concept(this, "CollectExpression", "sysml-CollectExpression", "sysml-CollectExpression");;
    new Concept(this, "LiteralInfinity", "sysml-LiteralInfinity", "sysml-LiteralInfinity");;
    new Concept(this, "LiteralExpression", "sysml-LiteralExpression", "sysml-LiteralExpression");;
    new Concept(this, "LiteralInteger", "sysml-LiteralInteger", "sysml-LiteralInteger");;
    new Concept(this, "SelectExpression", "sysml-SelectExpression", "sysml-SelectExpression");;
    new Concept(this, "LiteralRational", "sysml-LiteralRational", "sysml-LiteralRational");;
    new Concept(this, "LiteralBoolean", "sysml-LiteralBoolean", "sysml-LiteralBoolean");;
    new Concept(this, "LiteralString", "sysml-LiteralString", "sysml-LiteralString");;
    new Concept(this, "FeatureChainExpression", "sysml-FeatureChainExpression", "sysml-FeatureChainExpression");;
    new Concept(this, "Dependency", "sysml-Dependency", "sysml-Dependency");;
    new Concept(this, "NamespaceImport", "sysml-NamespaceImport", "sysml-NamespaceImport");;
    new Concept(this, "MembershipImport", "sysml-MembershipImport", "sysml-MembershipImport");;
    new Concept(this, "InterfaceUsage", "sysml-InterfaceUsage", "sysml-InterfaceUsage");;
    new Concept(this, "ConnectionUsage", "sysml-ConnectionUsage", "sysml-ConnectionUsage");;
    new Concept(this, "ConnectorAsUsage", "sysml-ConnectorAsUsage", "sysml-ConnectorAsUsage");;
    new Concept(this, "VariantMembership", "sysml-VariantMembership", "sysml-VariantMembership");;
    new Concept(this, "Definition", "sysml-Definition", "sysml-Definition");;
    new Concept(this, "ReferenceUsage", "sysml-ReferenceUsage", "sysml-ReferenceUsage");;
    new Concept(this, "AttributeUsage", "sysml-AttributeUsage", "sysml-AttributeUsage");;
    new Concept(this, "EnumerationUsage", "sysml-EnumerationUsage", "sysml-EnumerationUsage");;
    new Concept(this, "EnumerationDefinition", "sysml-EnumerationDefinition", "sysml-EnumerationDefinition");;
    new Concept(this, "AttributeDefinition", "sysml-AttributeDefinition", "sysml-AttributeDefinition");;
    new Concept(this, "OccurrenceDefinition", "sysml-OccurrenceDefinition", "sysml-OccurrenceDefinition");;
    new Concept(this, "LifeClass", "sysml-LifeClass", "sysml-LifeClass");;
    new Concept(this, "PartDefinition", "sysml-PartDefinition", "sysml-PartDefinition");;
    new Concept(this, "ItemDefinition", "sysml-ItemDefinition", "sysml-ItemDefinition");;
    new Concept(this, "PortUsage", "sysml-PortUsage", "sysml-PortUsage");;
    new Concept(this, "PortDefinition", "sysml-PortDefinition", "sysml-PortDefinition");;
    new Concept(this, "ConjugatedPortDefinition", "sysml-ConjugatedPortDefinition", "sysml-ConjugatedPortDefinition");;
    new Concept(this, "PortConjugation", "sysml-PortConjugation", "sysml-PortConjugation");;
    new Concept(this, "FlowConnectionUsage", "sysml-FlowConnectionUsage", "sysml-FlowConnectionUsage");;
    new Concept(this, "AllocationUsage", "sysml-AllocationUsage", "sysml-AllocationUsage");;
    new Concept(this, "AllocationDefinition", "sysml-AllocationDefinition", "sysml-AllocationDefinition");;
    new Concept(this, "ConnectionDefinition", "sysml-ConnectionDefinition", "sysml-ConnectionDefinition");;
    new Concept(this, "StateUsage", "sysml-StateUsage", "sysml-StateUsage");;
    new Concept(this, "TransitionUsage", "sysml-TransitionUsage", "sysml-TransitionUsage");;
    new Concept(this, "AcceptActionUsage", "sysml-AcceptActionUsage", "sysml-AcceptActionUsage");;
    new Concept(this, "CalculationUsage", "sysml-CalculationUsage", "sysml-CalculationUsage");;
    new Concept(this, "RequirementUsage", "sysml-RequirementUsage", "sysml-RequirementUsage");;
    new Concept(this, "RequirementDefinition", "sysml-RequirementDefinition", "sysml-RequirementDefinition");;
    new Concept(this, "ConstraintDefinition", "sysml-ConstraintDefinition", "sysml-ConstraintDefinition");;
    new Concept(this, "ConcernUsage", "sysml-ConcernUsage", "sysml-ConcernUsage");;
    new Concept(this, "ConcernDefinition", "sysml-ConcernDefinition", "sysml-ConcernDefinition");;
    new Concept(this, "CaseUsage", "sysml-CaseUsage", "sysml-CaseUsage");;
    new Concept(this, "CaseDefinition", "sysml-CaseDefinition", "sysml-CaseDefinition");;
    new Concept(this, "CalculationDefinition", "sysml-CalculationDefinition", "sysml-CalculationDefinition");;
    new Concept(this, "ActionDefinition", "sysml-ActionDefinition", "sysml-ActionDefinition");;
    new Concept(this, "AnalysisCaseUsage", "sysml-AnalysisCaseUsage", "sysml-AnalysisCaseUsage");;
    new Concept(this, "AnalysisCaseDefinition", "sysml-AnalysisCaseDefinition", "sysml-AnalysisCaseDefinition");;
    new Concept(this, "VerificationCaseUsage", "sysml-VerificationCaseUsage", "sysml-VerificationCaseUsage");;
    new Concept(this, "VerificationCaseDefinition", "sysml-VerificationCaseDefinition", "sysml-VerificationCaseDefinition");;
    new Concept(this, "UseCaseUsage", "sysml-UseCaseUsage", "sysml-UseCaseUsage");;
    new Concept(this, "UseCaseDefinition", "sysml-UseCaseDefinition", "sysml-UseCaseDefinition");;
    new Concept(this, "ViewUsage", "sysml-ViewUsage", "sysml-ViewUsage");;
    new Concept(this, "ViewDefinition", "sysml-ViewDefinition", "sysml-ViewDefinition");;
    new Concept(this, "ViewpointUsage", "sysml-ViewpointUsage", "sysml-ViewpointUsage");;
    new Concept(this, "ViewpointDefinition", "sysml-ViewpointDefinition", "sysml-ViewpointDefinition");;
    new Concept(this, "RenderingUsage", "sysml-RenderingUsage", "sysml-RenderingUsage");;
    new Concept(this, "RenderingDefinition", "sysml-RenderingDefinition", "sysml-RenderingDefinition");;
    new Concept(this, "MetadataUsage", "sysml-MetadataUsage", "sysml-MetadataUsage");;
    new Concept(this, "InterfaceDefinition", "sysml-InterfaceDefinition", "sysml-InterfaceDefinition");;
    new Concept(this, "ConjugatedPortTyping", "sysml-ConjugatedPortTyping", "sysml-ConjugatedPortTyping");;
    new Concept(this, "TransitionFeatureMembership", "sysml-TransitionFeatureMembership", "sysml-TransitionFeatureMembership");;
    new Concept(this, "ExhibitStateUsage", "sysml-ExhibitStateUsage", "sysml-ExhibitStateUsage");;
    new Concept(this, "StateSubactionMembership", "sysml-StateSubactionMembership", "sysml-StateSubactionMembership");;
    new Concept(this, "StateDefinition", "sysml-StateDefinition", "sysml-StateDefinition");;
    new Concept(this, "SuccessionFlowConnectionUsage", "sysml-SuccessionFlowConnectionUsage", "sysml-SuccessionFlowConnectionUsage");;
    new Concept(this, "FlowConnectionDefinition", "sysml-FlowConnectionDefinition", "sysml-FlowConnectionDefinition");;
    new Concept(this, "RequirementVerificationMembership", "sysml-RequirementVerificationMembership", "sysml-RequirementVerificationMembership");;
    new Concept(this, "RequirementConstraintMembership", "sysml-RequirementConstraintMembership", "sysml-RequirementConstraintMembership");;
    new Concept(this, "IncludeUseCaseUsage", "sysml-IncludeUseCaseUsage", "sysml-IncludeUseCaseUsage");;
    new Concept(this, "ObjectiveMembership", "sysml-ObjectiveMembership", "sysml-ObjectiveMembership");;
    new Concept(this, "SatisfyRequirementUsage", "sysml-SatisfyRequirementUsage", "sysml-SatisfyRequirementUsage");;
    new Concept(this, "SubjectMembership", "sysml-SubjectMembership", "sysml-SubjectMembership");;
    new Concept(this, "StakeholderMembership", "sysml-StakeholderMembership", "sysml-StakeholderMembership");;
    new Concept(this, "FramedConcernMembership", "sysml-FramedConcernMembership", "sysml-FramedConcernMembership");;
    new Concept(this, "ActorMembership", "sysml-ActorMembership", "sysml-ActorMembership");;
    new Concept(this, "ViewRenderingMembership", "sysml-ViewRenderingMembership", "sysml-ViewRenderingMembership");;
    new Concept(this, "NamespaceExpose", "sysml-NamespaceExpose", "sysml-NamespaceExpose");;
    new Concept(this, "MembershipExpose", "sysml-MembershipExpose", "sysml-MembershipExpose");;
    new Concept(this, "BindingConnectorAsUsage", "sysml-BindingConnectorAsUsage", "sysml-BindingConnectorAsUsage");;
    new Concept(this, "SuccessionAsUsage", "sysml-SuccessionAsUsage", "sysml-SuccessionAsUsage");;
    new Concept(this, "ForkNode", "sysml-ForkNode", "sysml-ForkNode");;
    new Concept(this, "ControlNode", "sysml-ControlNode", "sysml-ControlNode");;
    new Concept(this, "JoinNode", "sysml-JoinNode", "sysml-JoinNode");;
    new Concept(this, "SendActionUsage", "sysml-SendActionUsage", "sysml-SendActionUsage");;
    new Concept(this, "DecisionNode", "sysml-DecisionNode", "sysml-DecisionNode");;
    new Concept(this, "MergeNode", "sysml-MergeNode", "sysml-MergeNode");;
    new Concept(this, "LoopActionUsage", "sysml-LoopActionUsage", "sysml-LoopActionUsage");;
    new Concept(this, "TriggerInvocationExpression", "sysml-TriggerInvocationExpression", "sysml-TriggerInvocationExpression");;
    new Concept(this, "AssignmentActionUsage", "sysml-AssignmentActionUsage", "sysml-AssignmentActionUsage");;
    new Concept(this, "ForLoopActionUsage", "sysml-ForLoopActionUsage", "sysml-ForLoopActionUsage");;
    new Concept(this, "IfActionUsage", "sysml-IfActionUsage", "sysml-IfActionUsage");;
    new Concept(this, "WhileLoopActionUsage", "sysml-WhileLoopActionUsage", "sysml-WhileLoopActionUsage");;
    new Concept(this, "TerminateActionUsage", "sysml-TerminateActionUsage", "sysml-TerminateActionUsage");;
    new Concept(this, "MetadataDefinition", "sysml-MetadataDefinition", "sysml-MetadataDefinition");;
    new Concept(this, "AliasIdsContainer", "sysml-AliasIdsContainer", "sysml-AliasIdsContainer");;
    new Concept(this, "TextContainer", "sysml-TextContainer", "sysml-TextContainer");;
    new Concept(this, "Featuring", "sysml-Featuring", "sysml-Featuring");;
    new Concept(this, "Relationship", "sysml-Relationship", "sysml-Relationship");;
    new Concept(this, "Element", "sysml-Element", "sysml-Element");;
    new Concept(this, "AnnotatingElement", "sysml-AnnotatingElement", "sysml-AnnotatingElement");;
    new Concept(this, "Step", "sysml-Step", "sysml-Step");;
    new Concept(this, "Feature", "sysml-Feature", "sysml-Feature");;
    new Concept(this, "Type", "sysml-Type", "sysml-Type");;
    new Concept(this, "Namespace", "sysml-Namespace", "sysml-Namespace");;
    new Concept(this, "Behavior", "sysml-Behavior", "sysml-Behavior");;
    new Concept(this, "Class", "sysml-Class", "sysml-Class");;
    new Concept(this, "Classifier", "sysml-Classifier", "sysml-Classifier");;
    new Concept(this, "Succession", "sysml-Succession", "sysml-Succession");;
    new Concept(this, "Connector", "sysml-Connector", "sysml-Connector");;
    new Concept(this, "Structure", "sysml-Structure", "sysml-Structure");;
    new Concept(this, "PartUsage", "sysml-PartUsage", "sysml-PartUsage");;
    new Concept(this, "ItemUsage", "sysml-ItemUsage", "sysml-ItemUsage");;
    new Concept(this, "OccurrenceUsage", "sysml-OccurrenceUsage", "sysml-OccurrenceUsage");;
    new Concept(this, "Usage", "sysml-Usage", "sysml-Usage");;
    new Concept(this, "DataType", "sysml-DataType", "sysml-DataType");;
    new Concept(this, "ActionUsage", "sysml-ActionUsage", "sysml-ActionUsage");;
    new Concept(this, "ItemFlow", "sysml-ItemFlow", "sysml-ItemFlow");;
    new Concept(this, "AssociationStructure", "sysml-AssociationStructure", "sysml-AssociationStructure");;
    new Concept(this, "Association", "sysml-Association", "sysml-Association");;
    new Concept(this, "Predicate", "sysml-Predicate", "sysml-Predicate");;
    new Concept(this, "Function", "sysml-Function", "sysml-Function");;
    new Concept(this, "PerformActionUsage", "sysml-PerformActionUsage", "sysml-PerformActionUsage");;
    new Concept(this, "EventOccurrenceUsage", "sysml-EventOccurrenceUsage", "sysml-EventOccurrenceUsage");;
    new Concept(this, "SuccessionItemFlow", "sysml-SuccessionItemFlow", "sysml-SuccessionItemFlow");;
    new Concept(this, "Interaction", "sysml-Interaction", "sysml-Interaction");;
    new Concept(this, "AssertConstraintUsage", "sysml-AssertConstraintUsage", "sysml-AssertConstraintUsage");;
    new Concept(this, "ConstraintUsage", "sysml-ConstraintUsage", "sysml-ConstraintUsage");;
    new Concept(this, "BooleanExpression", "sysml-BooleanExpression", "sysml-BooleanExpression");;
    new Concept(this, "Expression", "sysml-Expression", "sysml-Expression");;
    new Concept(this, "Invariant", "sysml-Invariant", "sysml-Invariant");;
    new Concept(this, "Expose", "sysml-Expose", "sysml-Expose");;
    new Concept(this, "Import", "sysml-Import", "sysml-Import");;
    new Concept(this, "BindingConnector", "sysml-BindingConnector", "sysml-BindingConnector");;
    new Concept(this, "Metaclass", "sysml-Metaclass", "sysml-Metaclass");;
    new Interface(this, "IRelationship", "sysml-IRelationship", "sysml-IRelationship");;
    new Interface(this, "IElement", "sysml-IElement", "sysml-IElement");;
    new Interface(this, "INamespace", "sysml-INamespace", "sysml-INamespace");;
    new Interface(this, "IImport", "sysml-IImport", "sysml-IImport");;
    new Interface(this, "IAnnotatingElement", "sysml-IAnnotatingElement", "sysml-IAnnotatingElement");;
    new Interface(this, "IType", "sysml-IType", "sysml-IType");;
    new Interface(this, "IFeaturing", "sysml-IFeaturing", "sysml-IFeaturing");;
    new Interface(this, "IFeature", "sysml-IFeature", "sysml-IFeature");;
    new Interface(this, "IClassifier", "sysml-IClassifier", "sysml-IClassifier");;
    new Interface(this, "IExpression", "sysml-IExpression", "sysml-IExpression");;
    new Interface(this, "IStep", "sysml-IStep", "sysml-IStep");;
    new Interface(this, "IBehavior", "sysml-IBehavior", "sysml-IBehavior");;
    new Interface(this, "IClass", "sysml-IClass", "sysml-IClass");;
    new Interface(this, "IFunction", "sysml-IFunction", "sysml-IFunction");;
    new Interface(this, "IInvariant", "sysml-IInvariant", "sysml-IInvariant");;
    new Interface(this, "IBooleanExpression", "sysml-IBooleanExpression", "sysml-IBooleanExpression");;
    new Interface(this, "IPredicate", "sysml-IPredicate", "sysml-IPredicate");;
    new Interface(this, "IStructure", "sysml-IStructure", "sysml-IStructure");;
    new Interface(this, "IMetaclass", "sysml-IMetaclass", "sysml-IMetaclass");;
    new Interface(this, "IItemFlow", "sysml-IItemFlow", "sysml-IItemFlow");;
    new Interface(this, "IConnector", "sysml-IConnector", "sysml-IConnector");;
    new Interface(this, "IAssociation", "sysml-IAssociation", "sysml-IAssociation");;
    new Interface(this, "IInteraction", "sysml-IInteraction", "sysml-IInteraction");;
    new Interface(this, "ISuccessionItemFlow", "sysml-ISuccessionItemFlow", "sysml-ISuccessionItemFlow");;
    new Interface(this, "ISuccession", "sysml-ISuccession", "sysml-ISuccession");;
    new Interface(this, "IDataType", "sysml-IDataType", "sysml-IDataType");;
    new Interface(this, "IBindingConnector", "sysml-IBindingConnector", "sysml-IBindingConnector");;
    new Interface(this, "IAssociationStructure", "sysml-IAssociationStructure", "sysml-IAssociationStructure");;
    new Interface(this, "IUsage", "sysml-IUsage", "sysml-IUsage");;
    new Interface(this, "IOccurrenceUsage", "sysml-IOccurrenceUsage", "sysml-IOccurrenceUsage");;
    new Interface(this, "IItemUsage", "sysml-IItemUsage", "sysml-IItemUsage");;
    new Interface(this, "IPartUsage", "sysml-IPartUsage", "sysml-IPartUsage");;
    new Interface(this, "IActionUsage", "sysml-IActionUsage", "sysml-IActionUsage");;
    new Interface(this, "IConstraintUsage", "sysml-IConstraintUsage", "sysml-IConstraintUsage");;
    new Interface(this, "IPerformActionUsage", "sysml-IPerformActionUsage", "sysml-IPerformActionUsage");;
    new Interface(this, "IEventOccurrenceUsage", "sysml-IEventOccurrenceUsage", "sysml-IEventOccurrenceUsage");;
    new Interface(this, "IAssertConstraintUsage", "sysml-IAssertConstraintUsage", "sysml-IAssertConstraintUsage");;
    new Interface(this, "IExpose", "sysml-IExpose", "sysml-IExpose");;
    Enumeration visibilityKind = new Enumeration(this, "VisibilityKind", "sysml-VisibilityKind");;
    visibilityKind.setKey("sysml-VisibilityKind");
    visibilityKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "private").setID("sysml-VisibilityKind-private").setKey("sysml-VisibilityKind-private"));
    visibilityKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "protected").setID("sysml-VisibilityKind-protected").setKey("sysml-VisibilityKind-protected"));
    visibilityKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "public").setID("sysml-VisibilityKind-public").setKey("sysml-VisibilityKind-public"));
    Enumeration featureDirectionKind = new Enumeration(this, "FeatureDirectionKind", "sysml-FeatureDirectionKind");;
    featureDirectionKind.setKey("sysml-FeatureDirectionKind");
    featureDirectionKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "in").setID("sysml-FeatureDirectionKind-in").setKey("sysml-FeatureDirectionKind-in"));
    featureDirectionKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "inout").setID("sysml-FeatureDirectionKind-inout").setKey("sysml-FeatureDirectionKind-inout"));
    featureDirectionKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "out").setID("sysml-FeatureDirectionKind-out").setKey("sysml-FeatureDirectionKind-out"));
    Enumeration portionKind = new Enumeration(this, "PortionKind", "sysml-PortionKind");;
    portionKind.setKey("sysml-PortionKind");
    portionKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "timeslice").setID("sysml-PortionKind-timeslice").setKey("sysml-PortionKind-timeslice"));
    portionKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "snapshot").setID("sysml-PortionKind-snapshot").setKey("sysml-PortionKind-snapshot"));
    Enumeration transitionFeatureKind = new Enumeration(this, "TransitionFeatureKind", "sysml-TransitionFeatureKind");;
    transitionFeatureKind.setKey("sysml-TransitionFeatureKind");
    transitionFeatureKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "trigger").setID("sysml-TransitionFeatureKind-trigger").setKey("sysml-TransitionFeatureKind-trigger"));
    transitionFeatureKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "guard").setID("sysml-TransitionFeatureKind-guard").setKey("sysml-TransitionFeatureKind-guard"));
    transitionFeatureKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "effect").setID("sysml-TransitionFeatureKind-effect").setKey("sysml-TransitionFeatureKind-effect"));
    Enumeration stateSubactionKind = new Enumeration(this, "StateSubactionKind", "sysml-StateSubactionKind");;
    stateSubactionKind.setKey("sysml-StateSubactionKind");
    stateSubactionKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "entry").setID("sysml-StateSubactionKind-entry").setKey("sysml-StateSubactionKind-entry"));
    stateSubactionKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "do").setID("sysml-StateSubactionKind-do").setKey("sysml-StateSubactionKind-do"));
    stateSubactionKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "exit").setID("sysml-StateSubactionKind-exit").setKey("sysml-StateSubactionKind-exit"));
    Enumeration requirementConstraintKind = new Enumeration(this, "RequirementConstraintKind", "sysml-RequirementConstraintKind");;
    requirementConstraintKind.setKey("sysml-RequirementConstraintKind");
    requirementConstraintKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "assumption").setID("sysml-RequirementConstraintKind-assumption").setKey("sysml-RequirementConstraintKind-assumption"));
    requirementConstraintKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "requirement").setID("sysml-RequirementConstraintKind-requirement").setKey("sysml-RequirementConstraintKind-requirement"));
    Enumeration triggerKind = new Enumeration(this, "TriggerKind", "sysml-TriggerKind");;
    triggerKind.setKey("sysml-TriggerKind");
    triggerKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "when").setID("sysml-TriggerKind-when").setKey("sysml-TriggerKind-when"));
    triggerKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "at").setID("sysml-TriggerKind-at").setKey("sysml-TriggerKind-at"));
    triggerKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "after").setID("sysml-TriggerKind-after").setKey("sysml-TriggerKind-after"));
  }
}
