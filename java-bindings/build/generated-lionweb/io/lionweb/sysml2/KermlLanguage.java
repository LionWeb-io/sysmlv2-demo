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

public class KermlLanguage extends Language {
  private static KermlLanguage INSTANCE;

  private KermlLanguage() {
    super(LionWebVersion.v2023_1);
    this.setName("kerml");
    this.setVersion("1");
    this.setID("kerml");
    this.setKey("kerml");
    this.addDependency(TypesLanguage.getInstance());
    createElements();
    initOwningMembership();
    initMembership();
    initImport();
    initDocumentation();
    initComment();
    initAnnotation();
    initTextualRepresentation();
    initDependency();
    initMembershipImport();
    initNamespaceImport();
    initSubclassification();
    initSpecialization();
    initFeatureMembership();
    initRedefinition();
    initSubsetting();
    initFeatureTyping();
    initTypeFeaturing();
    initFeatureInverting();
    initFeatureChaining();
    initReferenceSubsetting();
    initConjugation();
    initMultiplicity();
    initIntersecting();
    initUnioning();
    initDisjoining();
    initDifferencing();
    initEndFeatureMembership();
    initElementFilterMembership();
    initExpression();
    initFunction();
    initPackage();
    initLibraryPackage();
    initInvocationExpression();
    initFeatureReferenceExpression();
    initOperatorExpression();
    initLiteralString();
    initLiteralExpression();
    initLiteralBoolean();
    initLiteralInteger();
    initNullExpression();
    initMetadataAccessExpression();
    initMetadataFeature();
    initMetaclass();
    initSelectExpression();
    initFeatureChainExpression();
    initCollectExpression();
    initLiteralInfinity();
    initLiteralRational();
    initMultiplicityRange();
    initFeatureValue();
    initBindingConnector();
    initAssociation();
    initInvariant();
    initBooleanExpression();
    initPredicate();
    initReturnParameterMembership();
    initParameterMembership();
    initResultExpressionMembership();
    initDataType();
    initInteraction();
    initItemFlowEnd();
    initItemFlow();
    initItemFeature();
    initSuccessionItemFlow();
    initAssociationStructure();
    initAliasIdsContainer();
    initFeaturing();
    initRelationship();
    initElement();
    initAnnotatingElement();
    initBehavior();
    initClass();
    initClassifier();
    initType();
    initNamespace();
    initStep();
    initFeature();
    initSuccession();
    initConnector();
    initStructure();
    initIElement();
    initIRelationship();
    initINamespace();
    initIAnnotatingElement();
    initIType();
    initIFeaturing();
    initIFeature();
    initIClassifier();
    initIStep();
    initIBehavior();
    initIClass();
    initIStructure();
    initIConnector();
    initISuccession();
  }

  public static KermlLanguage getInstance() {
    if (INSTANCE == null) {
      INSTANCE = new KermlLanguage();
    }
    return INSTANCE;
  }

  public Concept getOwningMembership() {
    return this.requireConceptByName("OwningMembership");
  }

  private void initOwningMembership() {
    Concept concept = this.requireConceptByName("OwningMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Membership"));
    Property ownedMemberElementId = new Property("ownedMemberElementId", concept, "kerml-OwningMembership-ownedMemberElementId");
    ownedMemberElementId.setKey("kerml-OwningMembership-ownedMemberElementId");
    ownedMemberElementId.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    ownedMemberElementId.setOptional(false);
    Property ownedMemberShortName = new Property("ownedMemberShortName", concept, "kerml-OwningMembership-ownedMemberShortName");
    ownedMemberShortName.setKey("kerml-OwningMembership-ownedMemberShortName");
    ownedMemberShortName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    ownedMemberShortName.setOptional(true);
    Property ownedMemberName = new Property("ownedMemberName", concept, "kerml-OwningMembership-ownedMemberName");
    ownedMemberName.setKey("kerml-OwningMembership-ownedMemberName");
    ownedMemberName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    ownedMemberName.setOptional(true);
    Reference ownedMemberElement = new Reference("ownedMemberElement", concept, "kerml-OwningMembership-ownedMemberElement");
    ownedMemberElement.setKey("kerml-OwningMembership-ownedMemberElement");
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
    Reference membershipOwningNamespace = new Reference("membershipOwningNamespace", concept, "kerml-Membership-membershipOwningNamespace");
    membershipOwningNamespace.setKey("kerml-Membership-membershipOwningNamespace");
    membershipOwningNamespace.setType(this.requireClassifierByName("INamespace"));
    membershipOwningNamespace.setOptional(false);
    membershipOwningNamespace.setMultiple(false);
    Property memberElementId = new Property("memberElementId", concept, "kerml-Membership-memberElementId");
    memberElementId.setKey("kerml-Membership-memberElementId");
    memberElementId.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    memberElementId.setOptional(false);
    Property memberShortName = new Property("memberShortName", concept, "kerml-Membership-memberShortName");
    memberShortName.setKey("kerml-Membership-memberShortName");
    memberShortName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    memberShortName.setOptional(true);
    Reference memberElement = new Reference("memberElement", concept, "kerml-Membership-memberElement");
    memberElement.setKey("kerml-Membership-memberElement");
    memberElement.setType(this.requireClassifierByName("IElement"));
    memberElement.setOptional(false);
    memberElement.setMultiple(false);
    Property memberName = new Property("memberName", concept, "kerml-Membership-memberName");
    memberName.setKey("kerml-Membership-memberName");
    memberName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    memberName.setOptional(true);
    Property visibility = new Property("visibility", concept, "kerml-Membership-visibility");
    visibility.setKey("kerml-Membership-visibility");
    visibility.setType(this.requireDataTypeByName("VisibilityKind"));
    visibility.setOptional(false);
  }

  public Concept getImport() {
    return this.requireConceptByName("Import");
  }

  private void initImport() {
    Concept concept = this.requireConceptByName("Import");
    concept.setAbstract(true);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Property visibility = new Property("visibility", concept, "kerml-Import-visibility");
    visibility.setKey("kerml-Import-visibility");
    visibility.setType(this.requireDataTypeByName("VisibilityKind"));
    visibility.setOptional(false);
    Property isRecursive = new Property("isRecursive", concept, "kerml-Import-isRecursive");
    isRecursive.setKey("kerml-Import-isRecursive");
    isRecursive.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isRecursive.setOptional(false);
    Property isImportAll = new Property("isImportAll", concept, "kerml-Import-isImportAll");
    isImportAll.setKey("kerml-Import-isImportAll");
    isImportAll.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isImportAll.setOptional(false);
    Reference importedElement = new Reference("importedElement", concept, "kerml-Import-importedElement");
    importedElement.setKey("kerml-Import-importedElement");
    importedElement.setType(this.requireClassifierByName("IElement"));
    importedElement.setOptional(false);
    importedElement.setMultiple(false);
    Reference importOwningNamespace = new Reference("importOwningNamespace", concept, "kerml-Import-importOwningNamespace");
    importOwningNamespace.setKey("kerml-Import-importOwningNamespace");
    importOwningNamespace.setType(this.requireClassifierByName("INamespace"));
    importOwningNamespace.setOptional(false);
    importOwningNamespace.setMultiple(false);
  }

  public Concept getDocumentation() {
    return this.requireConceptByName("Documentation");
  }

  private void initDocumentation() {
    Concept concept = this.requireConceptByName("Documentation");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Comment"));
    Reference documentedElement = new Reference("documentedElement", concept, "kerml-Documentation-documentedElement");
    documentedElement.setKey("kerml-Documentation-documentedElement");
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
    Property locale = new Property("locale", concept, "kerml-Comment-locale");
    locale.setKey("kerml-Comment-locale");
    locale.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    locale.setOptional(true);
    Property body = new Property("body", concept, "kerml-Comment-body");
    body.setKey("kerml-Comment-body");
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
    Reference annotatingElement = new Reference("annotatingElement", concept, "kerml-Annotation-annotatingElement");
    annotatingElement.setKey("kerml-Annotation-annotatingElement");
    annotatingElement.setType(this.requireClassifierByName("IAnnotatingElement"));
    annotatingElement.setOptional(false);
    annotatingElement.setMultiple(false);
    Reference annotatedElement = new Reference("annotatedElement", concept, "kerml-Annotation-annotatedElement");
    annotatedElement.setKey("kerml-Annotation-annotatedElement");
    annotatedElement.setType(this.requireClassifierByName("IElement"));
    annotatedElement.setOptional(false);
    annotatedElement.setMultiple(false);
    Reference owningAnnotatedElement = new Reference("owningAnnotatedElement", concept, "kerml-Annotation-owningAnnotatedElement");
    owningAnnotatedElement.setKey("kerml-Annotation-owningAnnotatedElement");
    owningAnnotatedElement.setType(this.requireClassifierByName("IElement"));
    owningAnnotatedElement.setOptional(true);
    owningAnnotatedElement.setMultiple(false);
    Reference owningAnnotatingElement = new Reference("owningAnnotatingElement", concept, "kerml-Annotation-owningAnnotatingElement");
    owningAnnotatingElement.setKey("kerml-Annotation-owningAnnotatingElement");
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
    Property language = new Property("language", concept, "kerml-TextualRepresentation-language");
    language.setKey("kerml-TextualRepresentation-language");
    language.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    language.setOptional(false);
    Property body = new Property("body", concept, "kerml-TextualRepresentation-body");
    body.setKey("kerml-TextualRepresentation-body");
    body.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    body.setOptional(false);
    Reference representedElement = new Reference("representedElement", concept, "kerml-TextualRepresentation-representedElement");
    representedElement.setKey("kerml-TextualRepresentation-representedElement");
    representedElement.setType(this.requireClassifierByName("IElement"));
    representedElement.setOptional(false);
    representedElement.setMultiple(false);
  }

  public Concept getDependency() {
    return this.requireConceptByName("Dependency");
  }

  private void initDependency() {
    Concept concept = this.requireConceptByName("Dependency");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Reference client = new Reference("client", concept, "kerml-Dependency-client");
    client.setKey("kerml-Dependency-client");
    client.setType(this.requireClassifierByName("IElement"));
    client.setOptional(false);
    client.setMultiple(true);
    Reference supplier = new Reference("supplier", concept, "kerml-Dependency-supplier");
    supplier.setKey("kerml-Dependency-supplier");
    supplier.setType(this.requireClassifierByName("IElement"));
    supplier.setOptional(false);
    supplier.setMultiple(true);
  }

  public Concept getMembershipImport() {
    return this.requireConceptByName("MembershipImport");
  }

  private void initMembershipImport() {
    Concept concept = this.requireConceptByName("MembershipImport");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Import"));
    Reference importedMembership = new Reference("importedMembership", concept, "kerml-MembershipImport-importedMembership");
    importedMembership.setKey("kerml-MembershipImport-importedMembership");
    importedMembership.setType(this.requireClassifierByName("Membership"));
    importedMembership.setOptional(false);
    importedMembership.setMultiple(false);
  }

  public Concept getNamespaceImport() {
    return this.requireConceptByName("NamespaceImport");
  }

  private void initNamespaceImport() {
    Concept concept = this.requireConceptByName("NamespaceImport");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Import"));
    Reference importedNamespace = new Reference("importedNamespace", concept, "kerml-NamespaceImport-importedNamespace");
    importedNamespace.setKey("kerml-NamespaceImport-importedNamespace");
    importedNamespace.setType(this.requireClassifierByName("INamespace"));
    importedNamespace.setOptional(false);
    importedNamespace.setMultiple(false);
  }

  public Concept getSubclassification() {
    return this.requireConceptByName("Subclassification");
  }

  private void initSubclassification() {
    Concept concept = this.requireConceptByName("Subclassification");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Specialization"));
    Reference superclassifier = new Reference("superclassifier", concept, "kerml-Subclassification-superclassifier");
    superclassifier.setKey("kerml-Subclassification-superclassifier");
    superclassifier.setType(this.requireClassifierByName("IClassifier"));
    superclassifier.setOptional(false);
    superclassifier.setMultiple(false);
    Reference owningClassifier = new Reference("owningClassifier", concept, "kerml-Subclassification-owningClassifier");
    owningClassifier.setKey("kerml-Subclassification-owningClassifier");
    owningClassifier.setType(this.requireClassifierByName("IClassifier"));
    owningClassifier.setOptional(true);
    owningClassifier.setMultiple(false);
    Reference subclassifier = new Reference("subclassifier", concept, "kerml-Subclassification-subclassifier");
    subclassifier.setKey("kerml-Subclassification-subclassifier");
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
    Reference owningType = new Reference("owningType", concept, "kerml-Specialization-owningType");
    owningType.setKey("kerml-Specialization-owningType");
    owningType.setType(this.requireClassifierByName("IType"));
    owningType.setOptional(true);
    owningType.setMultiple(false);
    Reference general = new Reference("general", concept, "kerml-Specialization-general");
    general.setKey("kerml-Specialization-general");
    general.setType(this.requireClassifierByName("IType"));
    general.setOptional(false);
    general.setMultiple(false);
    Reference specific = new Reference("specific", concept, "kerml-Specialization-specific");
    specific.setKey("kerml-Specialization-specific");
    specific.setType(this.requireClassifierByName("IType"));
    specific.setOptional(false);
    specific.setMultiple(false);
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
    Reference ownedMemberFeature = new Reference("ownedMemberFeature", concept, "kerml-FeatureMembership-ownedMemberFeature");
    ownedMemberFeature.setKey("kerml-FeatureMembership-ownedMemberFeature");
    ownedMemberFeature.setType(this.requireClassifierByName("IFeature"));
    ownedMemberFeature.setOptional(false);
    ownedMemberFeature.setMultiple(false);
    Reference owningType = new Reference("owningType", concept, "kerml-FeatureMembership-owningType");
    owningType.setKey("kerml-FeatureMembership-owningType");
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
    Reference redefiningFeature = new Reference("redefiningFeature", concept, "kerml-Redefinition-redefiningFeature");
    redefiningFeature.setKey("kerml-Redefinition-redefiningFeature");
    redefiningFeature.setType(this.requireClassifierByName("IFeature"));
    redefiningFeature.setOptional(false);
    redefiningFeature.setMultiple(false);
    Reference redefinedFeature = new Reference("redefinedFeature", concept, "kerml-Redefinition-redefinedFeature");
    redefinedFeature.setKey("kerml-Redefinition-redefinedFeature");
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
    Reference subsettedFeature = new Reference("subsettedFeature", concept, "kerml-Subsetting-subsettedFeature");
    subsettedFeature.setKey("kerml-Subsetting-subsettedFeature");
    subsettedFeature.setType(this.requireClassifierByName("IFeature"));
    subsettedFeature.setOptional(false);
    subsettedFeature.setMultiple(false);
    Reference subsettingFeature = new Reference("subsettingFeature", concept, "kerml-Subsetting-subsettingFeature");
    subsettingFeature.setKey("kerml-Subsetting-subsettingFeature");
    subsettingFeature.setType(this.requireClassifierByName("IFeature"));
    subsettingFeature.setOptional(false);
    subsettingFeature.setMultiple(false);
    Reference owningFeature = new Reference("owningFeature", concept, "kerml-Subsetting-owningFeature");
    owningFeature.setKey("kerml-Subsetting-owningFeature");
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
    Reference typedFeature = new Reference("typedFeature", concept, "kerml-FeatureTyping-typedFeature");
    typedFeature.setKey("kerml-FeatureTyping-typedFeature");
    typedFeature.setType(this.requireClassifierByName("IFeature"));
    typedFeature.setOptional(false);
    typedFeature.setMultiple(false);
    Reference type = new Reference("type", concept, "kerml-FeatureTyping-type");
    type.setKey("kerml-FeatureTyping-type");
    type.setType(this.requireClassifierByName("IType"));
    type.setOptional(false);
    type.setMultiple(false);
    Reference owningFeature = new Reference("owningFeature", concept, "kerml-FeatureTyping-owningFeature");
    owningFeature.setKey("kerml-FeatureTyping-owningFeature");
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
    Reference featureOfType = new Reference("featureOfType", concept, "kerml-TypeFeaturing-featureOfType");
    featureOfType.setKey("kerml-TypeFeaturing-featureOfType");
    featureOfType.setType(this.requireClassifierByName("IFeature"));
    featureOfType.setOptional(false);
    featureOfType.setMultiple(false);
    Reference featuringType = new Reference("featuringType", concept, "kerml-TypeFeaturing-featuringType");
    featuringType.setKey("kerml-TypeFeaturing-featuringType");
    featuringType.setType(this.requireClassifierByName("IType"));
    featuringType.setOptional(false);
    featuringType.setMultiple(false);
    Reference owningFeatureOfType = new Reference("owningFeatureOfType", concept, "kerml-TypeFeaturing-owningFeatureOfType");
    owningFeatureOfType.setKey("kerml-TypeFeaturing-owningFeatureOfType");
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
    Reference featureInverted = new Reference("featureInverted", concept, "kerml-FeatureInverting-featureInverted");
    featureInverted.setKey("kerml-FeatureInverting-featureInverted");
    featureInverted.setType(this.requireClassifierByName("IFeature"));
    featureInverted.setOptional(false);
    featureInverted.setMultiple(false);
    Reference invertingFeature = new Reference("invertingFeature", concept, "kerml-FeatureInverting-invertingFeature");
    invertingFeature.setKey("kerml-FeatureInverting-invertingFeature");
    invertingFeature.setType(this.requireClassifierByName("IFeature"));
    invertingFeature.setOptional(false);
    invertingFeature.setMultiple(false);
    Reference owningFeature = new Reference("owningFeature", concept, "kerml-FeatureInverting-owningFeature");
    owningFeature.setKey("kerml-FeatureInverting-owningFeature");
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
    Reference chainingFeature = new Reference("chainingFeature", concept, "kerml-FeatureChaining-chainingFeature");
    chainingFeature.setKey("kerml-FeatureChaining-chainingFeature");
    chainingFeature.setType(this.requireClassifierByName("IFeature"));
    chainingFeature.setOptional(false);
    chainingFeature.setMultiple(false);
    Reference featureChained = new Reference("featureChained", concept, "kerml-FeatureChaining-featureChained");
    featureChained.setKey("kerml-FeatureChaining-featureChained");
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
    Reference referencedFeature = new Reference("referencedFeature", concept, "kerml-ReferenceSubsetting-referencedFeature");
    referencedFeature.setKey("kerml-ReferenceSubsetting-referencedFeature");
    referencedFeature.setType(this.requireClassifierByName("IFeature"));
    referencedFeature.setOptional(false);
    referencedFeature.setMultiple(false);
    Reference referencingFeature = new Reference("referencingFeature", concept, "kerml-ReferenceSubsetting-referencingFeature");
    referencingFeature.setKey("kerml-ReferenceSubsetting-referencingFeature");
    referencingFeature.setType(this.requireClassifierByName("IFeature"));
    referencingFeature.setOptional(false);
    referencingFeature.setMultiple(false);
  }

  public Concept getConjugation() {
    return this.requireConceptByName("Conjugation");
  }

  private void initConjugation() {
    Concept concept = this.requireConceptByName("Conjugation");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Reference originalType = new Reference("originalType", concept, "kerml-Conjugation-originalType");
    originalType.setKey("kerml-Conjugation-originalType");
    originalType.setType(this.requireClassifierByName("IType"));
    originalType.setOptional(false);
    originalType.setMultiple(false);
    Reference conjugatedType = new Reference("conjugatedType", concept, "kerml-Conjugation-conjugatedType");
    conjugatedType.setKey("kerml-Conjugation-conjugatedType");
    conjugatedType.setType(this.requireClassifierByName("IType"));
    conjugatedType.setOptional(false);
    conjugatedType.setMultiple(false);
    Reference owningType = new Reference("owningType", concept, "kerml-Conjugation-owningType");
    owningType.setKey("kerml-Conjugation-owningType");
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
    Reference intersectingType = new Reference("intersectingType", concept, "kerml-Intersecting-intersectingType");
    intersectingType.setKey("kerml-Intersecting-intersectingType");
    intersectingType.setType(this.requireClassifierByName("IType"));
    intersectingType.setOptional(false);
    intersectingType.setMultiple(false);
    Reference typeIntersected = new Reference("typeIntersected", concept, "kerml-Intersecting-typeIntersected");
    typeIntersected.setKey("kerml-Intersecting-typeIntersected");
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
    Reference unioningType = new Reference("unioningType", concept, "kerml-Unioning-unioningType");
    unioningType.setKey("kerml-Unioning-unioningType");
    unioningType.setType(this.requireClassifierByName("IType"));
    unioningType.setOptional(false);
    unioningType.setMultiple(false);
    Reference typeUnioned = new Reference("typeUnioned", concept, "kerml-Unioning-typeUnioned");
    typeUnioned.setKey("kerml-Unioning-typeUnioned");
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
    Reference typeDisjoined = new Reference("typeDisjoined", concept, "kerml-Disjoining-typeDisjoined");
    typeDisjoined.setKey("kerml-Disjoining-typeDisjoined");
    typeDisjoined.setType(this.requireClassifierByName("IType"));
    typeDisjoined.setOptional(false);
    typeDisjoined.setMultiple(false);
    Reference disjoiningType = new Reference("disjoiningType", concept, "kerml-Disjoining-disjoiningType");
    disjoiningType.setKey("kerml-Disjoining-disjoiningType");
    disjoiningType.setType(this.requireClassifierByName("IType"));
    disjoiningType.setOptional(false);
    disjoiningType.setMultiple(false);
    Reference owningType = new Reference("owningType", concept, "kerml-Disjoining-owningType");
    owningType.setKey("kerml-Disjoining-owningType");
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
    Reference differencingType = new Reference("differencingType", concept, "kerml-Differencing-differencingType");
    differencingType.setKey("kerml-Differencing-differencingType");
    differencingType.setType(this.requireClassifierByName("IType"));
    differencingType.setOptional(false);
    differencingType.setMultiple(false);
    Reference typeDifferenced = new Reference("typeDifferenced", concept, "kerml-Differencing-typeDifferenced");
    typeDifferenced.setKey("kerml-Differencing-typeDifferenced");
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

  public Concept getElementFilterMembership() {
    return this.requireConceptByName("ElementFilterMembership");
  }

  private void initElementFilterMembership() {
    Concept concept = this.requireConceptByName("ElementFilterMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("OwningMembership"));
    Reference condition = new Reference("condition", concept, "kerml-ElementFilterMembership-condition");
    condition.setKey("kerml-ElementFilterMembership-condition");
    condition.setType(this.requireClassifierByName("Expression"));
    condition.setOptional(false);
    condition.setMultiple(false);
  }

  public Concept getExpression() {
    return this.requireConceptByName("Expression");
  }

  private void initExpression() {
    Concept concept = this.requireConceptByName("Expression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IStep"));
    Reference function = new Reference("function", concept, "kerml-Expression-function");
    function.setKey("kerml-Expression-function");
    function.setType(this.requireClassifierByName("Function"));
    function.setOptional(true);
    function.setMultiple(false);
    Reference result = new Reference("result", concept, "kerml-Expression-result");
    result.setKey("kerml-Expression-result");
    result.setType(this.requireClassifierByName("IFeature"));
    result.setOptional(false);
    result.setMultiple(false);
    Property isModelLevelEvaluable = new Property("isModelLevelEvaluable", concept, "kerml-Expression-isModelLevelEvaluable");
    isModelLevelEvaluable.setKey("kerml-Expression-isModelLevelEvaluable");
    isModelLevelEvaluable.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isModelLevelEvaluable.setOptional(false);
  }

  public Concept getFunction() {
    return this.requireConceptByName("Function");
  }

  private void initFunction() {
    Concept concept = this.requireConceptByName("Function");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IBehavior"));
    Reference expression = new Reference("expression", concept, "kerml-Function-expression");
    expression.setKey("kerml-Function-expression");
    expression.setType(this.requireClassifierByName("Expression"));
    expression.setOptional(true);
    expression.setMultiple(true);
    Reference result = new Reference("result", concept, "kerml-Function-result");
    result.setKey("kerml-Function-result");
    result.setType(this.requireClassifierByName("IFeature"));
    result.setOptional(false);
    result.setMultiple(false);
    Property isModelLevelEvaluable = new Property("isModelLevelEvaluable", concept, "kerml-Function-isModelLevelEvaluable");
    isModelLevelEvaluable.setKey("kerml-Function-isModelLevelEvaluable");
    isModelLevelEvaluable.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isModelLevelEvaluable.setOptional(false);
  }

  public Concept getPackage() {
    return this.requireConceptByName("Package");
  }

  private void initPackage() {
    Concept concept = this.requireConceptByName("Package");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("INamespace"));
    Reference filterCondition = new Reference("filterCondition", concept, "kerml-Package-filterCondition");
    filterCondition.setKey("kerml-Package-filterCondition");
    filterCondition.setType(this.requireClassifierByName("Expression"));
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
    Property isStandard = new Property("isStandard", concept, "kerml-LibraryPackage-isStandard");
    isStandard.setKey("kerml-LibraryPackage-isStandard");
    isStandard.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isStandard.setOptional(false);
  }

  public Concept getInvocationExpression() {
    return this.requireConceptByName("InvocationExpression");
  }

  private void initInvocationExpression() {
    Concept concept = this.requireConceptByName("InvocationExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Expression"));
    Reference argument = new Reference("argument", concept, "kerml-InvocationExpression-argument");
    argument.setKey("kerml-InvocationExpression-argument");
    argument.setType(this.requireClassifierByName("Expression"));
    argument.setOptional(true);
    argument.setMultiple(true);
    Containment operand = new Containment("operand", concept, "kerml-InvocationExpression-operand");
    operand.setKey("kerml-InvocationExpression-operand");
    operand.setType(this.requireClassifierByName("Expression"));
    operand.setOptional(true);
    operand.setMultiple(true);
  }

  public Concept getFeatureReferenceExpression() {
    return this.requireConceptByName("FeatureReferenceExpression");
  }

  private void initFeatureReferenceExpression() {
    Concept concept = this.requireConceptByName("FeatureReferenceExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Expression"));
    Reference referent = new Reference("referent", concept, "kerml-FeatureReferenceExpression-referent");
    referent.setKey("kerml-FeatureReferenceExpression-referent");
    referent.setType(this.requireClassifierByName("IFeature"));
    referent.setOptional(false);
    referent.setMultiple(false);
  }

  public Concept getOperatorExpression() {
    return this.requireConceptByName("OperatorExpression");
  }

  private void initOperatorExpression() {
    Concept concept = this.requireConceptByName("OperatorExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("InvocationExpression"));
    Property operator = new Property("operator", concept, "kerml-OperatorExpression-operator");
    operator.setKey("kerml-OperatorExpression-operator");
    operator.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    operator.setOptional(false);
  }

  public Concept getLiteralString() {
    return this.requireConceptByName("LiteralString");
  }

  private void initLiteralString() {
    Concept concept = this.requireConceptByName("LiteralString");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("LiteralExpression"));
    Property value = new Property("value", concept, "kerml-LiteralString-value");
    value.setKey("kerml-LiteralString-value");
    value.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    value.setOptional(false);
  }

  public Concept getLiteralExpression() {
    return this.requireConceptByName("LiteralExpression");
  }

  private void initLiteralExpression() {
    Concept concept = this.requireConceptByName("LiteralExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Expression"));
  }

  public Concept getLiteralBoolean() {
    return this.requireConceptByName("LiteralBoolean");
  }

  private void initLiteralBoolean() {
    Concept concept = this.requireConceptByName("LiteralBoolean");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("LiteralExpression"));
    Property value = new Property("value", concept, "kerml-LiteralBoolean-value");
    value.setKey("kerml-LiteralBoolean-value");
    value.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    value.setOptional(false);
  }

  public Concept getLiteralInteger() {
    return this.requireConceptByName("LiteralInteger");
  }

  private void initLiteralInteger() {
    Concept concept = this.requireConceptByName("LiteralInteger");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("LiteralExpression"));
    Property value = new Property("value", concept, "kerml-LiteralInteger-value");
    value.setKey("kerml-LiteralInteger-value");
    value.setType(TypesLanguage.getInstance().requireDataTypeByName("Integer"));
    value.setOptional(false);
  }

  public Concept getNullExpression() {
    return this.requireConceptByName("NullExpression");
  }

  private void initNullExpression() {
    Concept concept = this.requireConceptByName("NullExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Expression"));
  }

  public Concept getMetadataAccessExpression() {
    return this.requireConceptByName("MetadataAccessExpression");
  }

  private void initMetadataAccessExpression() {
    Concept concept = this.requireConceptByName("MetadataAccessExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Expression"));
    Reference referencedElement = new Reference("referencedElement", concept, "kerml-MetadataAccessExpression-referencedElement");
    referencedElement.setKey("kerml-MetadataAccessExpression-referencedElement");
    referencedElement.setType(this.requireClassifierByName("IElement"));
    referencedElement.setOptional(false);
    referencedElement.setMultiple(false);
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
    Reference metaclass = new Reference("metaclass", concept, "kerml-MetadataFeature-metaclass");
    metaclass.setKey("kerml-MetadataFeature-metaclass");
    metaclass.setType(this.requireClassifierByName("Metaclass"));
    metaclass.setOptional(true);
    metaclass.setMultiple(false);
  }

  public Concept getMetaclass() {
    return this.requireConceptByName("Metaclass");
  }

  private void initMetaclass() {
    Concept concept = this.requireConceptByName("Metaclass");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IStructure"));
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

  public Concept getFeatureChainExpression() {
    return this.requireConceptByName("FeatureChainExpression");
  }

  private void initFeatureChainExpression() {
    Concept concept = this.requireConceptByName("FeatureChainExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("OperatorExpression"));
    Reference targetFeature = new Reference("targetFeature", concept, "kerml-FeatureChainExpression-targetFeature");
    targetFeature.setKey("kerml-FeatureChainExpression-targetFeature");
    targetFeature.setType(this.requireClassifierByName("IFeature"));
    targetFeature.setOptional(false);
    targetFeature.setMultiple(false);
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

  public Concept getLiteralRational() {
    return this.requireConceptByName("LiteralRational");
  }

  private void initLiteralRational() {
    Concept concept = this.requireConceptByName("LiteralRational");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("LiteralExpression"));
    Property value = new Property("value", concept, "kerml-LiteralRational-value");
    value.setKey("kerml-LiteralRational-value");
    value.setType(TypesLanguage.getInstance().requireDataTypeByName("Real"));
    value.setOptional(false);
  }

  public Concept getMultiplicityRange() {
    return this.requireConceptByName("MultiplicityRange");
  }

  private void initMultiplicityRange() {
    Concept concept = this.requireConceptByName("MultiplicityRange");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Multiplicity"));
    Reference lowerBound = new Reference("lowerBound", concept, "kerml-MultiplicityRange-lowerBound");
    lowerBound.setKey("kerml-MultiplicityRange-lowerBound");
    lowerBound.setType(this.requireClassifierByName("Expression"));
    lowerBound.setOptional(true);
    lowerBound.setMultiple(false);
    Reference upperBound = new Reference("upperBound", concept, "kerml-MultiplicityRange-upperBound");
    upperBound.setKey("kerml-MultiplicityRange-upperBound");
    upperBound.setType(this.requireClassifierByName("Expression"));
    upperBound.setOptional(false);
    upperBound.setMultiple(false);
    Reference bound = new Reference("bound", concept, "kerml-MultiplicityRange-bound");
    bound.setKey("kerml-MultiplicityRange-bound");
    bound.setType(this.requireClassifierByName("Expression"));
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
    Reference featureWithValue = new Reference("featureWithValue", concept, "kerml-FeatureValue-featureWithValue");
    featureWithValue.setKey("kerml-FeatureValue-featureWithValue");
    featureWithValue.setType(this.requireClassifierByName("IFeature"));
    featureWithValue.setOptional(false);
    featureWithValue.setMultiple(false);
    Reference value = new Reference("value", concept, "kerml-FeatureValue-value");
    value.setKey("kerml-FeatureValue-value");
    value.setType(this.requireClassifierByName("Expression"));
    value.setOptional(false);
    value.setMultiple(false);
    Property isInitial = new Property("isInitial", concept, "kerml-FeatureValue-isInitial");
    isInitial.setKey("kerml-FeatureValue-isInitial");
    isInitial.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isInitial.setOptional(false);
    Property isDefault = new Property("isDefault", concept, "kerml-FeatureValue-isDefault");
    isDefault.setKey("kerml-FeatureValue-isDefault");
    isDefault.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isDefault.setOptional(false);
  }

  public Concept getBindingConnector() {
    return this.requireConceptByName("BindingConnector");
  }

  private void initBindingConnector() {
    Concept concept = this.requireConceptByName("BindingConnector");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IConnector"));
  }

  public Concept getAssociation() {
    return this.requireConceptByName("Association");
  }

  private void initAssociation() {
    Concept concept = this.requireConceptByName("Association");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IClassifier"));
    concept.addImplementedInterface(this.requireInterfaceByName("IRelationship"));
    Reference relatedType = new Reference("relatedType", concept, "kerml-Association-relatedType");
    relatedType.setKey("kerml-Association-relatedType");
    relatedType.setType(this.requireClassifierByName("IType"));
    relatedType.setOptional(true);
    relatedType.setMultiple(true);
    Reference sourceType = new Reference("sourceType", concept, "kerml-Association-sourceType");
    sourceType.setKey("kerml-Association-sourceType");
    sourceType.setType(this.requireClassifierByName("IType"));
    sourceType.setOptional(true);
    sourceType.setMultiple(false);
    Reference targetType = new Reference("targetType", concept, "kerml-Association-targetType");
    targetType.setKey("kerml-Association-targetType");
    targetType.setType(this.requireClassifierByName("IType"));
    targetType.setOptional(true);
    targetType.setMultiple(true);
    Reference associationEnd = new Reference("associationEnd", concept, "kerml-Association-associationEnd");
    associationEnd.setKey("kerml-Association-associationEnd");
    associationEnd.setType(this.requireClassifierByName("IFeature"));
    associationEnd.setOptional(true);
    associationEnd.setMultiple(true);
  }

  public Concept getInvariant() {
    return this.requireConceptByName("Invariant");
  }

  private void initInvariant() {
    Concept concept = this.requireConceptByName("Invariant");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("BooleanExpression"));
    Property isNegated = new Property("isNegated", concept, "kerml-Invariant-isNegated");
    isNegated.setKey("kerml-Invariant-isNegated");
    isNegated.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isNegated.setOptional(false);
  }

  public Concept getBooleanExpression() {
    return this.requireConceptByName("BooleanExpression");
  }

  private void initBooleanExpression() {
    Concept concept = this.requireConceptByName("BooleanExpression");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Expression"));
    Reference predicate = new Reference("predicate", concept, "kerml-BooleanExpression-predicate");
    predicate.setKey("kerml-BooleanExpression-predicate");
    predicate.setType(this.requireClassifierByName("Predicate"));
    predicate.setOptional(true);
    predicate.setMultiple(false);
  }

  public Concept getPredicate() {
    return this.requireConceptByName("Predicate");
  }

  private void initPredicate() {
    Concept concept = this.requireConceptByName("Predicate");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Function"));
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
    Reference ownedMemberParameter = new Reference("ownedMemberParameter", concept, "kerml-ParameterMembership-ownedMemberParameter");
    ownedMemberParameter.setKey("kerml-ParameterMembership-ownedMemberParameter");
    ownedMemberParameter.setType(this.requireClassifierByName("IFeature"));
    ownedMemberParameter.setOptional(false);
    ownedMemberParameter.setMultiple(false);
  }

  public Concept getResultExpressionMembership() {
    return this.requireConceptByName("ResultExpressionMembership");
  }

  private void initResultExpressionMembership() {
    Concept concept = this.requireConceptByName("ResultExpressionMembership");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("FeatureMembership"));
    Reference ownedResultExpression = new Reference("ownedResultExpression", concept, "kerml-ResultExpressionMembership-ownedResultExpression");
    ownedResultExpression.setKey("kerml-ResultExpressionMembership-ownedResultExpression");
    ownedResultExpression.setType(this.requireClassifierByName("Expression"));
    ownedResultExpression.setOptional(false);
    ownedResultExpression.setMultiple(false);
  }

  public Concept getDataType() {
    return this.requireConceptByName("DataType");
  }

  private void initDataType() {
    Concept concept = this.requireConceptByName("DataType");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IClassifier"));
  }

  public Concept getInteraction() {
    return this.requireConceptByName("Interaction");
  }

  private void initInteraction() {
    Concept concept = this.requireConceptByName("Interaction");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Association"));
    concept.addImplementedInterface(this.requireInterfaceByName("IBehavior"));
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

  public Concept getItemFlow() {
    return this.requireConceptByName("ItemFlow");
  }

  private void initItemFlow() {
    Concept concept = this.requireConceptByName("ItemFlow");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.addImplementedInterface(this.requireInterfaceByName("IConnector"));
    concept.addImplementedInterface(this.requireInterfaceByName("IStep"));
    Reference itemType = new Reference("itemType", concept, "kerml-ItemFlow-itemType");
    itemType.setKey("kerml-ItemFlow-itemType");
    itemType.setType(this.requireClassifierByName("IClassifier"));
    itemType.setOptional(true);
    itemType.setMultiple(true);
    Reference targetInputFeature = new Reference("targetInputFeature", concept, "kerml-ItemFlow-targetInputFeature");
    targetInputFeature.setKey("kerml-ItemFlow-targetInputFeature");
    targetInputFeature.setType(this.requireClassifierByName("IFeature"));
    targetInputFeature.setOptional(true);
    targetInputFeature.setMultiple(false);
    Reference sourceOutputFeature = new Reference("sourceOutputFeature", concept, "kerml-ItemFlow-sourceOutputFeature");
    sourceOutputFeature.setKey("kerml-ItemFlow-sourceOutputFeature");
    sourceOutputFeature.setType(this.requireClassifierByName("IFeature"));
    sourceOutputFeature.setOptional(true);
    sourceOutputFeature.setMultiple(false);
    Reference itemFlowEnd = new Reference("itemFlowEnd", concept, "kerml-ItemFlow-itemFlowEnd");
    itemFlowEnd.setKey("kerml-ItemFlow-itemFlowEnd");
    itemFlowEnd.setType(this.requireClassifierByName("ItemFlowEnd"));
    itemFlowEnd.setOptional(true);
    itemFlowEnd.setMultiple(true);
    Reference itemFeature = new Reference("itemFeature", concept, "kerml-ItemFlow-itemFeature");
    itemFeature.setKey("kerml-ItemFlow-itemFeature");
    itemFeature.setType(this.requireClassifierByName("ItemFeature"));
    itemFeature.setOptional(true);
    itemFeature.setMultiple(false);
    Reference interaction = new Reference("interaction", concept, "kerml-ItemFlow-interaction");
    interaction.setKey("kerml-ItemFlow-interaction");
    interaction.setType(this.requireClassifierByName("Interaction"));
    interaction.setOptional(true);
    interaction.setMultiple(true);
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

  public Concept getSuccessionItemFlow() {
    return this.requireConceptByName("SuccessionItemFlow");
  }

  private void initSuccessionItemFlow() {
    Concept concept = this.requireConceptByName("SuccessionItemFlow");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("ItemFlow"));
    concept.addImplementedInterface(this.requireInterfaceByName("ISuccession"));
  }

  public Concept getAssociationStructure() {
    return this.requireConceptByName("AssociationStructure");
  }

  private void initAssociationStructure() {
    Concept concept = this.requireConceptByName("AssociationStructure");
    concept.setAbstract(false);
    concept.setPartition(false);
    concept.setExtendedConcept(this.requireConceptByName("Association"));
    concept.addImplementedInterface(this.requireInterfaceByName("IStructure"));
  }

  public Concept getAliasIdsContainer() {
    return this.requireConceptByName("AliasIdsContainer");
  }

  private void initAliasIdsContainer() {
    Concept concept = this.requireConceptByName("AliasIdsContainer");
    concept.setAbstract(false);
    concept.setPartition(false);
    Property aliasIds = new Property("aliasIds", concept, "kerml-AliasIdsContainer-aliasIds");
    aliasIds.setKey("kerml-AliasIdsContainer-aliasIds");
    aliasIds.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    aliasIds.setOptional(true);
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

  public Interface getIElement() {
    return this.requireInterfaceByName("IElement");
  }

  private void initIElement() {
    Interface interf = this.requireInterfaceByName("IElement");
    Reference owningMembership = new Reference("owningMembership", interf, "kerml-IElement-owningMembership");
    owningMembership.setKey("kerml-IElement-owningMembership");
    owningMembership.setType(this.requireClassifierByName("OwningMembership"));
    owningMembership.setOptional(true);
    owningMembership.setMultiple(false);
    Containment ownedRelationship = new Containment("ownedRelationship", interf, "kerml-IElement-ownedRelationship");
    ownedRelationship.setKey("kerml-IElement-ownedRelationship");
    ownedRelationship.setType(this.requireClassifierByName("IRelationship"));
    ownedRelationship.setOptional(true);
    ownedRelationship.setMultiple(true);
    Reference owningRelationship = new Reference("owningRelationship", interf, "kerml-IElement-owningRelationship");
    owningRelationship.setKey("kerml-IElement-owningRelationship");
    owningRelationship.setType(this.requireClassifierByName("IRelationship"));
    owningRelationship.setOptional(true);
    owningRelationship.setMultiple(false);
    Reference owningNamespace = new Reference("owningNamespace", interf, "kerml-IElement-owningNamespace");
    owningNamespace.setKey("kerml-IElement-owningNamespace");
    owningNamespace.setType(this.requireClassifierByName("INamespace"));
    owningNamespace.setOptional(true);
    owningNamespace.setMultiple(false);
    Property elementId = new Property("elementId", interf, "kerml-IElement-elementId");
    elementId.setKey("kerml-IElement-elementId");
    elementId.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    elementId.setOptional(false);
    Reference owner = new Reference("owner", interf, "kerml-IElement-owner");
    owner.setKey("kerml-IElement-owner");
    owner.setType(this.requireClassifierByName("IElement"));
    owner.setOptional(true);
    owner.setMultiple(false);
    Reference ownedElement = new Reference("ownedElement", interf, "kerml-IElement-ownedElement");
    ownedElement.setKey("kerml-IElement-ownedElement");
    ownedElement.setType(this.requireClassifierByName("IElement"));
    ownedElement.setOptional(true);
    ownedElement.setMultiple(true);
    Reference documentation = new Reference("documentation", interf, "kerml-IElement-documentation");
    documentation.setKey("kerml-IElement-documentation");
    documentation.setType(this.requireClassifierByName("Documentation"));
    documentation.setOptional(true);
    documentation.setMultiple(true);
    Reference ownedAnnotation = new Reference("ownedAnnotation", interf, "kerml-IElement-ownedAnnotation");
    ownedAnnotation.setKey("kerml-IElement-ownedAnnotation");
    ownedAnnotation.setType(this.requireClassifierByName("Annotation"));
    ownedAnnotation.setOptional(true);
    ownedAnnotation.setMultiple(true);
    Reference textualRepresentation = new Reference("textualRepresentation", interf, "kerml-IElement-textualRepresentation");
    textualRepresentation.setKey("kerml-IElement-textualRepresentation");
    textualRepresentation.setType(this.requireClassifierByName("TextualRepresentation"));
    textualRepresentation.setOptional(true);
    textualRepresentation.setMultiple(true);
    Property declaredShortName = new Property("declaredShortName", interf, "kerml-IElement-declaredShortName");
    declaredShortName.setKey("kerml-IElement-declaredShortName");
    declaredShortName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    declaredShortName.setOptional(true);
    Property declaredName = new Property("declaredName", interf, "kerml-IElement-declaredName");
    declaredName.setKey("kerml-IElement-declaredName");
    declaredName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    declaredName.setOptional(true);
    Property shortName = new Property("shortName", interf, "kerml-IElement-shortName");
    shortName.setKey("kerml-IElement-shortName");
    shortName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    shortName.setOptional(true);
    Property name = new Property("name", interf, "kerml-IElement-name");
    name.setKey("kerml-IElement-name");
    name.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    name.setOptional(true);
    Property qualifiedName = new Property("qualifiedName", interf, "kerml-IElement-qualifiedName");
    qualifiedName.setKey("kerml-IElement-qualifiedName");
    qualifiedName.setType(TypesLanguage.getInstance().requireDataTypeByName("String"));
    qualifiedName.setOptional(true);
    Property isImpliedIncluded = new Property("isImpliedIncluded", interf, "kerml-IElement-isImpliedIncluded");
    isImpliedIncluded.setKey("kerml-IElement-isImpliedIncluded");
    isImpliedIncluded.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isImpliedIncluded.setOptional(false);
    Property isLibraryElement = new Property("isLibraryElement", interf, "kerml-IElement-isLibraryElement");
    isLibraryElement.setKey("kerml-IElement-isLibraryElement");
    isLibraryElement.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isLibraryElement.setOptional(false);
    Containment aliasIdsContainer = new Containment("aliasIdsContainer", interf, "kerml-IElement-aliasIdsContainer");
    aliasIdsContainer.setKey("kerml-IElement-aliasIdsContainer");
    aliasIdsContainer.setType(this.requireClassifierByName("AliasIdsContainer"));
    aliasIdsContainer.setOptional(true);
    aliasIdsContainer.setMultiple(true);
  }

  public Interface getIRelationship() {
    return this.requireInterfaceByName("IRelationship");
  }

  private void initIRelationship() {
    Interface interf = this.requireInterfaceByName("IRelationship");
    interf.addExtendedInterface(this.requireInterfaceByName("IElement"));
    Reference relatedElement = new Reference("relatedElement", interf, "kerml-IRelationship-relatedElement");
    relatedElement.setKey("kerml-IRelationship-relatedElement");
    relatedElement.setType(this.requireClassifierByName("IElement"));
    relatedElement.setOptional(true);
    relatedElement.setMultiple(true);
    Reference target = new Reference("target", interf, "kerml-IRelationship-target");
    target.setKey("kerml-IRelationship-target");
    target.setType(this.requireClassifierByName("IElement"));
    target.setOptional(true);
    target.setMultiple(true);
    Reference source = new Reference("source", interf, "kerml-IRelationship-source");
    source.setKey("kerml-IRelationship-source");
    source.setType(this.requireClassifierByName("IElement"));
    source.setOptional(true);
    source.setMultiple(true);
    Reference owningRelatedElement = new Reference("owningRelatedElement", interf, "kerml-IRelationship-owningRelatedElement");
    owningRelatedElement.setKey("kerml-IRelationship-owningRelatedElement");
    owningRelatedElement.setType(this.requireClassifierByName("IElement"));
    owningRelatedElement.setOptional(true);
    owningRelatedElement.setMultiple(false);
    Containment ownedRelatedElement = new Containment("ownedRelatedElement", interf, "kerml-IRelationship-ownedRelatedElement");
    ownedRelatedElement.setKey("kerml-IRelationship-ownedRelatedElement");
    ownedRelatedElement.setType(this.requireClassifierByName("IElement"));
    ownedRelatedElement.setOptional(true);
    ownedRelatedElement.setMultiple(true);
    Property isImplied = new Property("isImplied", interf, "kerml-IRelationship-isImplied");
    isImplied.setKey("kerml-IRelationship-isImplied");
    isImplied.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isImplied.setOptional(false);
  }

  public Interface getINamespace() {
    return this.requireInterfaceByName("INamespace");
  }

  private void initINamespace() {
    Interface interf = this.requireInterfaceByName("INamespace");
    interf.addExtendedInterface(this.requireInterfaceByName("IElement"));
    Reference membership = new Reference("membership", interf, "kerml-INamespace-membership");
    membership.setKey("kerml-INamespace-membership");
    membership.setType(this.requireClassifierByName("Membership"));
    membership.setOptional(true);
    membership.setMultiple(true);
    Reference ownedImport = new Reference("ownedImport", interf, "kerml-INamespace-ownedImport");
    ownedImport.setKey("kerml-INamespace-ownedImport");
    ownedImport.setType(this.requireClassifierByName("Import"));
    ownedImport.setOptional(true);
    ownedImport.setMultiple(true);
    Reference member = new Reference("member", interf, "kerml-INamespace-member");
    member.setKey("kerml-INamespace-member");
    member.setType(this.requireClassifierByName("IElement"));
    member.setOptional(true);
    member.setMultiple(true);
    Reference ownedMember = new Reference("ownedMember", interf, "kerml-INamespace-ownedMember");
    ownedMember.setKey("kerml-INamespace-ownedMember");
    ownedMember.setType(this.requireClassifierByName("IElement"));
    ownedMember.setOptional(true);
    ownedMember.setMultiple(true);
    Reference ownedMembership = new Reference("ownedMembership", interf, "kerml-INamespace-ownedMembership");
    ownedMembership.setKey("kerml-INamespace-ownedMembership");
    ownedMembership.setType(this.requireClassifierByName("Membership"));
    ownedMembership.setOptional(true);
    ownedMembership.setMultiple(true);
    Reference importedMembership = new Reference("importedMembership", interf, "kerml-INamespace-importedMembership");
    importedMembership.setKey("kerml-INamespace-importedMembership");
    importedMembership.setType(this.requireClassifierByName("Membership"));
    importedMembership.setOptional(true);
    importedMembership.setMultiple(true);
  }

  public Interface getIAnnotatingElement() {
    return this.requireInterfaceByName("IAnnotatingElement");
  }

  private void initIAnnotatingElement() {
    Interface interf = this.requireInterfaceByName("IAnnotatingElement");
    interf.addExtendedInterface(this.requireInterfaceByName("IElement"));
    Reference annotatedElement = new Reference("annotatedElement", interf, "kerml-IAnnotatingElement-annotatedElement");
    annotatedElement.setKey("kerml-IAnnotatingElement-annotatedElement");
    annotatedElement.setType(this.requireClassifierByName("IElement"));
    annotatedElement.setOptional(false);
    annotatedElement.setMultiple(true);
    Reference ownedAnnotatingRelationship = new Reference("ownedAnnotatingRelationship", interf, "kerml-IAnnotatingElement-ownedAnnotatingRelationship");
    ownedAnnotatingRelationship.setKey("kerml-IAnnotatingElement-ownedAnnotatingRelationship");
    ownedAnnotatingRelationship.setType(this.requireClassifierByName("Annotation"));
    ownedAnnotatingRelationship.setOptional(true);
    ownedAnnotatingRelationship.setMultiple(true);
    Reference annotation = new Reference("annotation", interf, "kerml-IAnnotatingElement-annotation");
    annotation.setKey("kerml-IAnnotatingElement-annotation");
    annotation.setType(this.requireClassifierByName("Annotation"));
    annotation.setOptional(true);
    annotation.setMultiple(true);
  }

  public Interface getIType() {
    return this.requireInterfaceByName("IType");
  }

  private void initIType() {
    Interface interf = this.requireInterfaceByName("IType");
    interf.addExtendedInterface(this.requireInterfaceByName("INamespace"));
    Reference ownedFeatureMembership = new Reference("ownedFeatureMembership", interf, "kerml-IType-ownedFeatureMembership");
    ownedFeatureMembership.setKey("kerml-IType-ownedFeatureMembership");
    ownedFeatureMembership.setType(this.requireClassifierByName("FeatureMembership"));
    ownedFeatureMembership.setOptional(true);
    ownedFeatureMembership.setMultiple(true);
    Reference ownedFeature = new Reference("ownedFeature", interf, "kerml-IType-ownedFeature");
    ownedFeature.setKey("kerml-IType-ownedFeature");
    ownedFeature.setType(this.requireClassifierByName("IFeature"));
    ownedFeature.setOptional(true);
    ownedFeature.setMultiple(true);
    Reference ownedEndFeature = new Reference("ownedEndFeature", interf, "kerml-IType-ownedEndFeature");
    ownedEndFeature.setKey("kerml-IType-ownedEndFeature");
    ownedEndFeature.setType(this.requireClassifierByName("IFeature"));
    ownedEndFeature.setOptional(true);
    ownedEndFeature.setMultiple(true);
    Reference feature = new Reference("feature", interf, "kerml-IType-feature");
    feature.setKey("kerml-IType-feature");
    feature.setType(this.requireClassifierByName("IFeature"));
    feature.setOptional(true);
    feature.setMultiple(true);
    Reference input = new Reference("input", interf, "kerml-IType-input");
    input.setKey("kerml-IType-input");
    input.setType(this.requireClassifierByName("IFeature"));
    input.setOptional(true);
    input.setMultiple(true);
    Reference output = new Reference("output", interf, "kerml-IType-output");
    output.setKey("kerml-IType-output");
    output.setType(this.requireClassifierByName("IFeature"));
    output.setOptional(true);
    output.setMultiple(true);
    Property isAbstract = new Property("isAbstract", interf, "kerml-IType-isAbstract");
    isAbstract.setKey("kerml-IType-isAbstract");
    isAbstract.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isAbstract.setOptional(false);
    Reference inheritedMembership = new Reference("inheritedMembership", interf, "kerml-IType-inheritedMembership");
    inheritedMembership.setKey("kerml-IType-inheritedMembership");
    inheritedMembership.setType(this.requireClassifierByName("Membership"));
    inheritedMembership.setOptional(true);
    inheritedMembership.setMultiple(true);
    Reference endFeature = new Reference("endFeature", interf, "kerml-IType-endFeature");
    endFeature.setKey("kerml-IType-endFeature");
    endFeature.setType(this.requireClassifierByName("IFeature"));
    endFeature.setOptional(true);
    endFeature.setMultiple(true);
    Property isSufficient = new Property("isSufficient", interf, "kerml-IType-isSufficient");
    isSufficient.setKey("kerml-IType-isSufficient");
    isSufficient.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isSufficient.setOptional(false);
    Reference ownedConjugator = new Reference("ownedConjugator", interf, "kerml-IType-ownedConjugator");
    ownedConjugator.setKey("kerml-IType-ownedConjugator");
    ownedConjugator.setType(this.requireClassifierByName("Conjugation"));
    ownedConjugator.setOptional(true);
    ownedConjugator.setMultiple(false);
    Property isConjugated = new Property("isConjugated", interf, "kerml-IType-isConjugated");
    isConjugated.setKey("kerml-IType-isConjugated");
    isConjugated.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isConjugated.setOptional(false);
    Reference inheritedFeature = new Reference("inheritedFeature", interf, "kerml-IType-inheritedFeature");
    inheritedFeature.setKey("kerml-IType-inheritedFeature");
    inheritedFeature.setType(this.requireClassifierByName("IFeature"));
    inheritedFeature.setOptional(true);
    inheritedFeature.setMultiple(true);
    Reference multiplicity = new Reference("multiplicity", interf, "kerml-IType-multiplicity");
    multiplicity.setKey("kerml-IType-multiplicity");
    multiplicity.setType(this.requireClassifierByName("Multiplicity"));
    multiplicity.setOptional(true);
    multiplicity.setMultiple(false);
    Reference unioningType = new Reference("unioningType", interf, "kerml-IType-unioningType");
    unioningType.setKey("kerml-IType-unioningType");
    unioningType.setType(this.requireClassifierByName("IType"));
    unioningType.setOptional(true);
    unioningType.setMultiple(true);
    Reference ownedIntersecting = new Reference("ownedIntersecting", interf, "kerml-IType-ownedIntersecting");
    ownedIntersecting.setKey("kerml-IType-ownedIntersecting");
    ownedIntersecting.setType(this.requireClassifierByName("Intersecting"));
    ownedIntersecting.setOptional(true);
    ownedIntersecting.setMultiple(true);
    Reference intersectingType = new Reference("intersectingType", interf, "kerml-IType-intersectingType");
    intersectingType.setKey("kerml-IType-intersectingType");
    intersectingType.setType(this.requireClassifierByName("IType"));
    intersectingType.setOptional(true);
    intersectingType.setMultiple(true);
    Reference ownedUnioning = new Reference("ownedUnioning", interf, "kerml-IType-ownedUnioning");
    ownedUnioning.setKey("kerml-IType-ownedUnioning");
    ownedUnioning.setType(this.requireClassifierByName("Unioning"));
    ownedUnioning.setOptional(true);
    ownedUnioning.setMultiple(true);
    Reference ownedDisjoining = new Reference("ownedDisjoining", interf, "kerml-IType-ownedDisjoining");
    ownedDisjoining.setKey("kerml-IType-ownedDisjoining");
    ownedDisjoining.setType(this.requireClassifierByName("Disjoining"));
    ownedDisjoining.setOptional(true);
    ownedDisjoining.setMultiple(true);
    Reference featureMembership = new Reference("featureMembership", interf, "kerml-IType-featureMembership");
    featureMembership.setKey("kerml-IType-featureMembership");
    featureMembership.setType(this.requireClassifierByName("FeatureMembership"));
    featureMembership.setOptional(true);
    featureMembership.setMultiple(true);
    Reference differencingType = new Reference("differencingType", interf, "kerml-IType-differencingType");
    differencingType.setKey("kerml-IType-differencingType");
    differencingType.setType(this.requireClassifierByName("IType"));
    differencingType.setOptional(true);
    differencingType.setMultiple(true);
    Reference ownedDifferencing = new Reference("ownedDifferencing", interf, "kerml-IType-ownedDifferencing");
    ownedDifferencing.setKey("kerml-IType-ownedDifferencing");
    ownedDifferencing.setType(this.requireClassifierByName("Differencing"));
    ownedDifferencing.setOptional(true);
    ownedDifferencing.setMultiple(true);
    Reference directedFeature = new Reference("directedFeature", interf, "kerml-IType-directedFeature");
    directedFeature.setKey("kerml-IType-directedFeature");
    directedFeature.setType(this.requireClassifierByName("IFeature"));
    directedFeature.setOptional(true);
    directedFeature.setMultiple(true);
    Reference ownedSpecialization = new Reference("ownedSpecialization", interf, "kerml-IType-ownedSpecialization");
    ownedSpecialization.setKey("kerml-IType-ownedSpecialization");
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
    Reference type = new Reference("type", interf, "kerml-IFeaturing-type");
    type.setKey("kerml-IFeaturing-type");
    type.setType(this.requireClassifierByName("IType"));
    type.setOptional(false);
    type.setMultiple(false);
    Reference feature = new Reference("feature", interf, "kerml-IFeaturing-feature");
    feature.setKey("kerml-IFeaturing-feature");
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
    Reference owningType = new Reference("owningType", interf, "kerml-IFeature-owningType");
    owningType.setKey("kerml-IFeature-owningType");
    owningType.setType(this.requireClassifierByName("IType"));
    owningType.setOptional(true);
    owningType.setMultiple(false);
    Property isUnique = new Property("isUnique", interf, "kerml-IFeature-isUnique");
    isUnique.setKey("kerml-IFeature-isUnique");
    isUnique.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isUnique.setOptional(false);
    Property isOrdered = new Property("isOrdered", interf, "kerml-IFeature-isOrdered");
    isOrdered.setKey("kerml-IFeature-isOrdered");
    isOrdered.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isOrdered.setOptional(false);
    Reference type = new Reference("type", interf, "kerml-IFeature-type");
    type.setKey("kerml-IFeature-type");
    type.setType(this.requireClassifierByName("IType"));
    type.setOptional(true);
    type.setMultiple(true);
    Reference ownedRedefinition = new Reference("ownedRedefinition", interf, "kerml-IFeature-ownedRedefinition");
    ownedRedefinition.setKey("kerml-IFeature-ownedRedefinition");
    ownedRedefinition.setType(this.requireClassifierByName("Redefinition"));
    ownedRedefinition.setOptional(true);
    ownedRedefinition.setMultiple(true);
    Reference ownedSubsetting = new Reference("ownedSubsetting", interf, "kerml-IFeature-ownedSubsetting");
    ownedSubsetting.setKey("kerml-IFeature-ownedSubsetting");
    ownedSubsetting.setType(this.requireClassifierByName("Subsetting"));
    ownedSubsetting.setOptional(true);
    ownedSubsetting.setMultiple(true);
    Reference owningFeatureMembership = new Reference("owningFeatureMembership", interf, "kerml-IFeature-owningFeatureMembership");
    owningFeatureMembership.setKey("kerml-IFeature-owningFeatureMembership");
    owningFeatureMembership.setType(this.requireClassifierByName("FeatureMembership"));
    owningFeatureMembership.setOptional(true);
    owningFeatureMembership.setMultiple(false);
    Property isComposite = new Property("isComposite", interf, "kerml-IFeature-isComposite");
    isComposite.setKey("kerml-IFeature-isComposite");
    isComposite.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isComposite.setOptional(false);
    Property isEnd = new Property("isEnd", interf, "kerml-IFeature-isEnd");
    isEnd.setKey("kerml-IFeature-isEnd");
    isEnd.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isEnd.setOptional(false);
    Reference endOwningType = new Reference("endOwningType", interf, "kerml-IFeature-endOwningType");
    endOwningType.setKey("kerml-IFeature-endOwningType");
    endOwningType.setType(this.requireClassifierByName("IType"));
    endOwningType.setOptional(true);
    endOwningType.setMultiple(false);
    Reference ownedTyping = new Reference("ownedTyping", interf, "kerml-IFeature-ownedTyping");
    ownedTyping.setKey("kerml-IFeature-ownedTyping");
    ownedTyping.setType(this.requireClassifierByName("FeatureTyping"));
    ownedTyping.setOptional(true);
    ownedTyping.setMultiple(true);
    Reference featuringType = new Reference("featuringType", interf, "kerml-IFeature-featuringType");
    featuringType.setKey("kerml-IFeature-featuringType");
    featuringType.setType(this.requireClassifierByName("IType"));
    featuringType.setOptional(true);
    featuringType.setMultiple(true);
    Reference ownedTypeFeaturing = new Reference("ownedTypeFeaturing", interf, "kerml-IFeature-ownedTypeFeaturing");
    ownedTypeFeaturing.setKey("kerml-IFeature-ownedTypeFeaturing");
    ownedTypeFeaturing.setType(this.requireClassifierByName("TypeFeaturing"));
    ownedTypeFeaturing.setOptional(true);
    ownedTypeFeaturing.setMultiple(true);
    Property isDerived = new Property("isDerived", interf, "kerml-IFeature-isDerived");
    isDerived.setKey("kerml-IFeature-isDerived");
    isDerived.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isDerived.setOptional(false);
    Reference chainingFeature = new Reference("chainingFeature", interf, "kerml-IFeature-chainingFeature");
    chainingFeature.setKey("kerml-IFeature-chainingFeature");
    chainingFeature.setType(this.requireClassifierByName("IFeature"));
    chainingFeature.setOptional(true);
    chainingFeature.setMultiple(true);
    Reference ownedFeatureInverting = new Reference("ownedFeatureInverting", interf, "kerml-IFeature-ownedFeatureInverting");
    ownedFeatureInverting.setKey("kerml-IFeature-ownedFeatureInverting");
    ownedFeatureInverting.setType(this.requireClassifierByName("FeatureInverting"));
    ownedFeatureInverting.setOptional(true);
    ownedFeatureInverting.setMultiple(true);
    Reference ownedFeatureChaining = new Reference("ownedFeatureChaining", interf, "kerml-IFeature-ownedFeatureChaining");
    ownedFeatureChaining.setKey("kerml-IFeature-ownedFeatureChaining");
    ownedFeatureChaining.setType(this.requireClassifierByName("FeatureChaining"));
    ownedFeatureChaining.setOptional(true);
    ownedFeatureChaining.setMultiple(true);
    Property isReadOnly = new Property("isReadOnly", interf, "kerml-IFeature-isReadOnly");
    isReadOnly.setKey("kerml-IFeature-isReadOnly");
    isReadOnly.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isReadOnly.setOptional(false);
    Property isPortion = new Property("isPortion", interf, "kerml-IFeature-isPortion");
    isPortion.setKey("kerml-IFeature-isPortion");
    isPortion.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isPortion.setOptional(false);
    Property direction = new Property("direction", interf, "kerml-IFeature-direction");
    direction.setKey("kerml-IFeature-direction");
    direction.setType(this.requireDataTypeByName("FeatureDirectionKind"));
    direction.setOptional(true);
    Reference ownedReferenceSubsetting = new Reference("ownedReferenceSubsetting", interf, "kerml-IFeature-ownedReferenceSubsetting");
    ownedReferenceSubsetting.setKey("kerml-IFeature-ownedReferenceSubsetting");
    ownedReferenceSubsetting.setType(this.requireClassifierByName("ReferenceSubsetting"));
    ownedReferenceSubsetting.setOptional(true);
    ownedReferenceSubsetting.setMultiple(false);
    Reference featureTarget = new Reference("featureTarget", interf, "kerml-IFeature-featureTarget");
    featureTarget.setKey("kerml-IFeature-featureTarget");
    featureTarget.setType(this.requireClassifierByName("IFeature"));
    featureTarget.setOptional(false);
    featureTarget.setMultiple(false);
    Property isNonunique = new Property("isNonunique", interf, "kerml-IFeature-isNonunique");
    isNonunique.setKey("kerml-IFeature-isNonunique");
    isNonunique.setType(TypesLanguage.getInstance().requireDataTypeByName("Boolean"));
    isNonunique.setOptional(false);
  }

  public Interface getIClassifier() {
    return this.requireInterfaceByName("IClassifier");
  }

  private void initIClassifier() {
    Interface interf = this.requireInterfaceByName("IClassifier");
    interf.addExtendedInterface(this.requireInterfaceByName("IType"));
    Reference ownedSubclassification = new Reference("ownedSubclassification", interf, "kerml-IClassifier-ownedSubclassification");
    ownedSubclassification.setKey("kerml-IClassifier-ownedSubclassification");
    ownedSubclassification.setType(this.requireClassifierByName("Subclassification"));
    ownedSubclassification.setOptional(true);
    ownedSubclassification.setMultiple(true);
  }

  public Interface getIStep() {
    return this.requireInterfaceByName("IStep");
  }

  private void initIStep() {
    Interface interf = this.requireInterfaceByName("IStep");
    interf.addExtendedInterface(this.requireInterfaceByName("IFeature"));
    Reference behavior = new Reference("behavior", interf, "kerml-IStep-behavior");
    behavior.setKey("kerml-IStep-behavior");
    behavior.setType(this.requireClassifierByName("IBehavior"));
    behavior.setOptional(true);
    behavior.setMultiple(true);
    Reference parameter = new Reference("parameter", interf, "kerml-IStep-parameter");
    parameter.setKey("kerml-IStep-parameter");
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
    Reference step = new Reference("step", interf, "kerml-IBehavior-step");
    step.setKey("kerml-IBehavior-step");
    step.setType(this.requireClassifierByName("IStep"));
    step.setOptional(true);
    step.setMultiple(true);
    Reference parameter = new Reference("parameter", interf, "kerml-IBehavior-parameter");
    parameter.setKey("kerml-IBehavior-parameter");
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

  public Interface getIStructure() {
    return this.requireInterfaceByName("IStructure");
  }

  private void initIStructure() {
    Interface interf = this.requireInterfaceByName("IStructure");
    interf.addExtendedInterface(this.requireInterfaceByName("IClass"));
  }

  public Interface getIConnector() {
    return this.requireInterfaceByName("IConnector");
  }

  private void initIConnector() {
    Interface interf = this.requireInterfaceByName("IConnector");
    interf.addExtendedInterface(this.requireInterfaceByName("IFeature"));
    interf.addExtendedInterface(this.requireInterfaceByName("IRelationship"));
    Reference relatedFeature = new Reference("relatedFeature", interf, "kerml-IConnector-relatedFeature");
    relatedFeature.setKey("kerml-IConnector-relatedFeature");
    relatedFeature.setType(this.requireClassifierByName("IFeature"));
    relatedFeature.setOptional(true);
    relatedFeature.setMultiple(true);
    Reference association = new Reference("association", interf, "kerml-IConnector-association");
    association.setKey("kerml-IConnector-association");
    association.setType(this.requireClassifierByName("Association"));
    association.setOptional(true);
    association.setMultiple(true);
    Reference connectorEnd = new Reference("connectorEnd", interf, "kerml-IConnector-connectorEnd");
    connectorEnd.setKey("kerml-IConnector-connectorEnd");
    connectorEnd.setType(this.requireClassifierByName("IFeature"));
    connectorEnd.setOptional(true);
    connectorEnd.setMultiple(true);
    Reference sourceFeature = new Reference("sourceFeature", interf, "kerml-IConnector-sourceFeature");
    sourceFeature.setKey("kerml-IConnector-sourceFeature");
    sourceFeature.setType(this.requireClassifierByName("IFeature"));
    sourceFeature.setOptional(true);
    sourceFeature.setMultiple(false);
    Reference targetFeature = new Reference("targetFeature", interf, "kerml-IConnector-targetFeature");
    targetFeature.setKey("kerml-IConnector-targetFeature");
    targetFeature.setType(this.requireClassifierByName("IFeature"));
    targetFeature.setOptional(true);
    targetFeature.setMultiple(true);
  }

  public Interface getISuccession() {
    return this.requireInterfaceByName("ISuccession");
  }

  private void initISuccession() {
    Interface interf = this.requireInterfaceByName("ISuccession");
    interf.addExtendedInterface(this.requireInterfaceByName("IConnector"));
    Reference transitionStep = new Reference("transitionStep", interf, "kerml-ISuccession-transitionStep");
    transitionStep.setKey("kerml-ISuccession-transitionStep");
    transitionStep.setType(this.requireClassifierByName("IStep"));
    transitionStep.setOptional(true);
    transitionStep.setMultiple(false);
    Reference triggerStep = new Reference("triggerStep", interf, "kerml-ISuccession-triggerStep");
    triggerStep.setKey("kerml-ISuccession-triggerStep");
    triggerStep.setType(this.requireClassifierByName("IStep"));
    triggerStep.setOptional(true);
    triggerStep.setMultiple(true);
    Reference effectStep = new Reference("effectStep", interf, "kerml-ISuccession-effectStep");
    effectStep.setKey("kerml-ISuccession-effectStep");
    effectStep.setType(this.requireClassifierByName("IStep"));
    effectStep.setOptional(true);
    effectStep.setMultiple(true);
    Reference guardExpression = new Reference("guardExpression", interf, "kerml-ISuccession-guardExpression");
    guardExpression.setKey("kerml-ISuccession-guardExpression");
    guardExpression.setType(this.requireClassifierByName("Expression"));
    guardExpression.setOptional(true);
    guardExpression.setMultiple(true);
  }

  public Enumeration getVisibilityKind() {
    return this.requireEnumerationByName("VisibilityKind");
  }

  public Enumeration getFeatureDirectionKind() {
    return this.requireEnumerationByName("FeatureDirectionKind");
  }

  private void createElements() {
    new Concept(this, "OwningMembership", "kerml-OwningMembership", "kerml-OwningMembership");;
    new Concept(this, "Membership", "kerml-Membership", "kerml-Membership");;
    new Concept(this, "Import", "kerml-Import", "kerml-Import");;
    new Concept(this, "Documentation", "kerml-Documentation", "kerml-Documentation");;
    new Concept(this, "Comment", "kerml-Comment", "kerml-Comment");;
    new Concept(this, "Annotation", "kerml-Annotation", "kerml-Annotation");;
    new Concept(this, "TextualRepresentation", "kerml-TextualRepresentation", "kerml-TextualRepresentation");;
    new Concept(this, "Dependency", "kerml-Dependency", "kerml-Dependency");;
    new Concept(this, "MembershipImport", "kerml-MembershipImport", "kerml-MembershipImport");;
    new Concept(this, "NamespaceImport", "kerml-NamespaceImport", "kerml-NamespaceImport");;
    new Concept(this, "Subclassification", "kerml-Subclassification", "kerml-Subclassification");;
    new Concept(this, "Specialization", "kerml-Specialization", "kerml-Specialization");;
    new Concept(this, "FeatureMembership", "kerml-FeatureMembership", "kerml-FeatureMembership");;
    new Concept(this, "Redefinition", "kerml-Redefinition", "kerml-Redefinition");;
    new Concept(this, "Subsetting", "kerml-Subsetting", "kerml-Subsetting");;
    new Concept(this, "FeatureTyping", "kerml-FeatureTyping", "kerml-FeatureTyping");;
    new Concept(this, "TypeFeaturing", "kerml-TypeFeaturing", "kerml-TypeFeaturing");;
    new Concept(this, "FeatureInverting", "kerml-FeatureInverting", "kerml-FeatureInverting");;
    new Concept(this, "FeatureChaining", "kerml-FeatureChaining", "kerml-FeatureChaining");;
    new Concept(this, "ReferenceSubsetting", "kerml-ReferenceSubsetting", "kerml-ReferenceSubsetting");;
    new Concept(this, "Conjugation", "kerml-Conjugation", "kerml-Conjugation");;
    new Concept(this, "Multiplicity", "kerml-Multiplicity", "kerml-Multiplicity");;
    new Concept(this, "Intersecting", "kerml-Intersecting", "kerml-Intersecting");;
    new Concept(this, "Unioning", "kerml-Unioning", "kerml-Unioning");;
    new Concept(this, "Disjoining", "kerml-Disjoining", "kerml-Disjoining");;
    new Concept(this, "Differencing", "kerml-Differencing", "kerml-Differencing");;
    new Concept(this, "EndFeatureMembership", "kerml-EndFeatureMembership", "kerml-EndFeatureMembership");;
    new Concept(this, "ElementFilterMembership", "kerml-ElementFilterMembership", "kerml-ElementFilterMembership");;
    new Concept(this, "Expression", "kerml-Expression", "kerml-Expression");;
    new Concept(this, "Function", "kerml-Function", "kerml-Function");;
    new Concept(this, "Package", "kerml-Package", "kerml-Package");;
    new Concept(this, "LibraryPackage", "kerml-LibraryPackage", "kerml-LibraryPackage");;
    new Concept(this, "InvocationExpression", "kerml-InvocationExpression", "kerml-InvocationExpression");;
    new Concept(this, "FeatureReferenceExpression", "kerml-FeatureReferenceExpression", "kerml-FeatureReferenceExpression");;
    new Concept(this, "OperatorExpression", "kerml-OperatorExpression", "kerml-OperatorExpression");;
    new Concept(this, "LiteralString", "kerml-LiteralString", "kerml-LiteralString");;
    new Concept(this, "LiteralExpression", "kerml-LiteralExpression", "kerml-LiteralExpression");;
    new Concept(this, "LiteralBoolean", "kerml-LiteralBoolean", "kerml-LiteralBoolean");;
    new Concept(this, "LiteralInteger", "kerml-LiteralInteger", "kerml-LiteralInteger");;
    new Concept(this, "NullExpression", "kerml-NullExpression", "kerml-NullExpression");;
    new Concept(this, "MetadataAccessExpression", "kerml-MetadataAccessExpression", "kerml-MetadataAccessExpression");;
    new Concept(this, "MetadataFeature", "kerml-MetadataFeature", "kerml-MetadataFeature");;
    new Concept(this, "Metaclass", "kerml-Metaclass", "kerml-Metaclass");;
    new Concept(this, "SelectExpression", "kerml-SelectExpression", "kerml-SelectExpression");;
    new Concept(this, "FeatureChainExpression", "kerml-FeatureChainExpression", "kerml-FeatureChainExpression");;
    new Concept(this, "CollectExpression", "kerml-CollectExpression", "kerml-CollectExpression");;
    new Concept(this, "LiteralInfinity", "kerml-LiteralInfinity", "kerml-LiteralInfinity");;
    new Concept(this, "LiteralRational", "kerml-LiteralRational", "kerml-LiteralRational");;
    new Concept(this, "MultiplicityRange", "kerml-MultiplicityRange", "kerml-MultiplicityRange");;
    new Concept(this, "FeatureValue", "kerml-FeatureValue", "kerml-FeatureValue");;
    new Concept(this, "BindingConnector", "kerml-BindingConnector", "kerml-BindingConnector");;
    new Concept(this, "Association", "kerml-Association", "kerml-Association");;
    new Concept(this, "Invariant", "kerml-Invariant", "kerml-Invariant");;
    new Concept(this, "BooleanExpression", "kerml-BooleanExpression", "kerml-BooleanExpression");;
    new Concept(this, "Predicate", "kerml-Predicate", "kerml-Predicate");;
    new Concept(this, "ReturnParameterMembership", "kerml-ReturnParameterMembership", "kerml-ReturnParameterMembership");;
    new Concept(this, "ParameterMembership", "kerml-ParameterMembership", "kerml-ParameterMembership");;
    new Concept(this, "ResultExpressionMembership", "kerml-ResultExpressionMembership", "kerml-ResultExpressionMembership");;
    new Concept(this, "DataType", "kerml-DataType", "kerml-DataType");;
    new Concept(this, "Interaction", "kerml-Interaction", "kerml-Interaction");;
    new Concept(this, "ItemFlowEnd", "kerml-ItemFlowEnd", "kerml-ItemFlowEnd");;
    new Concept(this, "ItemFlow", "kerml-ItemFlow", "kerml-ItemFlow");;
    new Concept(this, "ItemFeature", "kerml-ItemFeature", "kerml-ItemFeature");;
    new Concept(this, "SuccessionItemFlow", "kerml-SuccessionItemFlow", "kerml-SuccessionItemFlow");;
    new Concept(this, "AssociationStructure", "kerml-AssociationStructure", "kerml-AssociationStructure");;
    new Concept(this, "AliasIdsContainer", "kerml-AliasIdsContainer", "kerml-AliasIdsContainer");;
    new Concept(this, "Featuring", "kerml-Featuring", "kerml-Featuring");;
    new Concept(this, "Relationship", "kerml-Relationship", "kerml-Relationship");;
    new Concept(this, "Element", "kerml-Element", "kerml-Element");;
    new Concept(this, "AnnotatingElement", "kerml-AnnotatingElement", "kerml-AnnotatingElement");;
    new Concept(this, "Behavior", "kerml-Behavior", "kerml-Behavior");;
    new Concept(this, "Class", "kerml-Class", "kerml-Class");;
    new Concept(this, "Classifier", "kerml-Classifier", "kerml-Classifier");;
    new Concept(this, "Type", "kerml-Type", "kerml-Type");;
    new Concept(this, "Namespace", "kerml-Namespace", "kerml-Namespace");;
    new Concept(this, "Step", "kerml-Step", "kerml-Step");;
    new Concept(this, "Feature", "kerml-Feature", "kerml-Feature");;
    new Concept(this, "Succession", "kerml-Succession", "kerml-Succession");;
    new Concept(this, "Connector", "kerml-Connector", "kerml-Connector");;
    new Concept(this, "Structure", "kerml-Structure", "kerml-Structure");;
    new Interface(this, "IElement", "kerml-IElement", "kerml-IElement");;
    new Interface(this, "IRelationship", "kerml-IRelationship", "kerml-IRelationship");;
    new Interface(this, "INamespace", "kerml-INamespace", "kerml-INamespace");;
    new Interface(this, "IAnnotatingElement", "kerml-IAnnotatingElement", "kerml-IAnnotatingElement");;
    new Interface(this, "IType", "kerml-IType", "kerml-IType");;
    new Interface(this, "IFeaturing", "kerml-IFeaturing", "kerml-IFeaturing");;
    new Interface(this, "IFeature", "kerml-IFeature", "kerml-IFeature");;
    new Interface(this, "IClassifier", "kerml-IClassifier", "kerml-IClassifier");;
    new Interface(this, "IStep", "kerml-IStep", "kerml-IStep");;
    new Interface(this, "IBehavior", "kerml-IBehavior", "kerml-IBehavior");;
    new Interface(this, "IClass", "kerml-IClass", "kerml-IClass");;
    new Interface(this, "IStructure", "kerml-IStructure", "kerml-IStructure");;
    new Interface(this, "IConnector", "kerml-IConnector", "kerml-IConnector");;
    new Interface(this, "ISuccession", "kerml-ISuccession", "kerml-ISuccession");;
    Enumeration visibilityKind = new Enumeration(this, "VisibilityKind", "kerml-VisibilityKind");;
    visibilityKind.setKey("kerml-VisibilityKind");
    visibilityKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "private").setID("kerml-VisibilityKind-private").setKey("kerml-VisibilityKind-private"));
    visibilityKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "protected").setID("kerml-VisibilityKind-protected").setKey("kerml-VisibilityKind-protected"));
    visibilityKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "public").setID("kerml-VisibilityKind-public").setKey("kerml-VisibilityKind-public"));
    Enumeration featureDirectionKind = new Enumeration(this, "FeatureDirectionKind", "kerml-FeatureDirectionKind");;
    featureDirectionKind.setKey("kerml-FeatureDirectionKind");
    featureDirectionKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "in").setID("kerml-FeatureDirectionKind-in").setKey("kerml-FeatureDirectionKind-in"));
    featureDirectionKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "inout").setID("kerml-FeatureDirectionKind-inout").setKey("kerml-FeatureDirectionKind-inout"));
    featureDirectionKind.addLiteral(new EnumerationLiteral(this.getLionWebVersion(), "out").setID("kerml-FeatureDirectionKind-out").setKey("kerml-FeatureDirectionKind-out"));
  }
}
