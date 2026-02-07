package io.lionweb.sysml2;

import io.lionweb.language.Concept;
import io.lionweb.language.Containment;
import io.lionweb.language.Property;
import io.lionweb.language.Reference;
import io.lionweb.model.ClassifierInstance;
import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;
import java.lang.IllegalStateException;
import java.lang.Object;
import java.lang.Override;
import java.lang.String;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

public class AllocationDefinition extends ConnectionDefinition {
  @NotNull
  private String id;

  @Nullable
  private ClassifierInstance<?> parent;

  protected List<ReferenceValue> allocation = new ArrayList<>();

  public AllocationDefinition(@NotNull String id) {
    super(id);
  }

  @NotNull
  public String getID() {
    return this.id;
  }

  @Override
  public ClassifierInstance<?> getParent() {
    return this.parent;
  }

  @Override
  public ClassifierInstance setParent(@Nullable ClassifierInstance<?> parent) {
    this.parent = parent;
    return this;
  }

  @Override
  public Concept getClassifier() {
    return SysmlLanguage.getInstance().getAllocationDefinition();
  }

  public int addToAllocation(ReferenceValue referenceValue, int index) {
    if (index > allocation.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("allocation"), index, referenceValue);
    }
    allocation.add(index, referenceValue);
    return allocation.size() - 1;
  }

  public List<ReferenceValue> getAllocation() {
    return allocation;
  }

  public int addToAllocation(AllocationUsage referred) {
    return addToAllocation(new ReferenceValue(referred, null), allocation.size());
  }

  public int addToAllocation(AllocationUsage referred, int index) {
    return addToAllocation(new ReferenceValue(referred, null), index);
  }

  public void clearAllocation() {
    while (!allocation.isEmpty()) {
            removeFromAllocation(0);
        };
  }

  public void removeFromAllocation(@NotNull ReferenceValue child) {
    int index = allocation.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromAllocation(index);;
  }

  public void removeFromAllocation(int index) {
    if (allocation.size() > index) {

            ReferenceValue removed = allocation.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("allocation"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + allocation.size());
          }
  }

  public void setAllocation(@NotNull List<? extends ReferenceValue> newValue) {
    clearAllocation();
          for (ReferenceValue referenceValue : newValue) {
              addToAllocation(referenceValue, allocation.size());
          }
  }

  @Override
  public Object getPropertyValue(Property property) {
    throw new IllegalStateException("Property " + property + " not found.");
  }

  @Override
  public void setPropertyValue(Property property, Object value) {
    Objects.requireNonNull(property, "Property should not be null");;
    Objects.requireNonNull(property.getKey(), "Cannot assign a property with no Key specified");;
    throw new IllegalStateException("Property " + property + " not found.");
  }

  @Override
  public List<? extends Node> getChildren(Containment containment) {
    throw new IllegalStateException("Containment " + containment + " not found.");
  }

  @Override
  public void addChild(@NotNull Containment containment, @NotNull Node child) {
    Objects.requireNonNull(containment, "Containment should not be null");
    Objects.requireNonNull(child, "Child should not be null");
    throw new IllegalStateException("Containment " + containment + " not found.");
  }

  @Override
  public void addChild(@NotNull Containment containment, @NotNull Node child, int index) {
    Objects.requireNonNull(containment, "containment must not be null");
    Objects.requireNonNull(child, "child must not be null");
    if (index < 0) throw new IllegalArgumentException("index should be non-negative");;
    throw new IllegalStateException("Containment " + containment + " not found.");
  }

  @Override
  public List<ReferenceValue> getReferenceValues(@NotNull Reference reference) {
    Objects.requireNonNull(reference, "reference should not be null");;
    if (Objects.equals(reference.getKey(), "sysml-AllocationDefinition-allocation")) {
      return allocation;
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public int addReferenceValue(Reference reference, ReferenceValue referredNode) {
    if (Objects.equals(reference.getKey(), "sysml-AllocationDefinition-allocation")) {
      return addToAllocation(referredNode, allocation.size());
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public int addReferenceValue(Reference reference, int index, ReferenceValue referredNode) {
    if (Objects.equals(reference.getKey(), "sysml-AllocationDefinition-allocation")) {
      return addToAllocation(referredNode, index);
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public void setReferenceValues(@NotNull Reference reference,
      @NotNull List<? extends ReferenceValue> values) {
    Objects.requireNonNull(reference, "reference cannot be null");
    Objects.requireNonNull(values, "values cannot be null");
    if (Objects.equals(reference.getKey(), "sysml-AllocationDefinition-allocation")) {
      setAllocation(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ConnectionDefinition-connectionEnd")) {
      setConnectionEnd(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAssociation-relatedType")) {
      setRelatedType(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAssociation-sourceType")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setSourceType(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAssociation-targetType")) {
      setTargetType(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAssociation-associationEnd")) {
      setAssociationEnd(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-OccurrenceDefinition-lifeClass")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setLifeClass(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IClassifier-ownedSubclassification")) {
      setOwnedSubclassification(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-owningRelatedElement")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwningRelatedElement(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-relatedElement")) {
      setRelatedElement(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-target")) {
      setTarget(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-source")) {
      setSource(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owningMembership")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwningMembership(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owningNamespace")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwningNamespace(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owningRelationship")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwningRelationship(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owner")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwner(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-ownedElement")) {
      setOwnedElement(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-documentation")) {
      setDocumentation(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-ownedAnnotation")) {
      setOwnedAnnotation(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-textualRepresentation")) {
      setTextualRepresentation(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-variant")) {
      setVariant(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-variantMembership")) {
      setVariantMembership(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-usage")) {
      setUsage(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-directedUsage")) {
      setDirectedUsage(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedReference")) {
      setOwnedReference(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAttribute")) {
      setOwnedAttribute(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedEnumeration")) {
      setOwnedEnumeration(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedOccurrence")) {
      setOwnedOccurrence(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedItem")) {
      setOwnedItem(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedPart")) {
      setOwnedPart(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedPort")) {
      setOwnedPort(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConnection")) {
      setOwnedConnection(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedFlow")) {
      setOwnedFlow(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedInterface")) {
      setOwnedInterface(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAllocation")) {
      setOwnedAllocation(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAction")) {
      setOwnedAction(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedState")) {
      setOwnedState(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedTransition")) {
      setOwnedTransition(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedCalculation")) {
      setOwnedCalculation(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConstraint")) {
      setOwnedConstraint(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedRequirement")) {
      setOwnedRequirement(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConcern")) {
      setOwnedConcern(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedCase")) {
      setOwnedCase(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAnalysisCase")) {
      setOwnedAnalysisCase(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedVerificationCase")) {
      setOwnedVerificationCase(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedUseCase")) {
      setOwnedUseCase(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedView")) {
      setOwnedView(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedViewpoint")) {
      setOwnedViewpoint(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedRendering")) {
      setOwnedRendering(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedMetadata")) {
      setOwnedMetadata(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedUsage")) {
      setOwnedUsage(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedFeatureMembership")) {
      setOwnedFeatureMembership(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedFeature")) {
      setOwnedFeature(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedEndFeature")) {
      setOwnedEndFeature(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-feature")) {
      setFeature(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-input")) {
      setInput(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-output")) {
      setOutput(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-inheritedMembership")) {
      setInheritedMembership(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-endFeature")) {
      setEndFeature(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedConjugator")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwnedConjugator(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-inheritedFeature")) {
      setInheritedFeature(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-multiplicity")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setMultiplicity(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-unioningType")) {
      setUnioningType(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedIntersecting")) {
      setOwnedIntersecting(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-intersectingType")) {
      setIntersectingType(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedUnioning")) {
      setOwnedUnioning(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedDisjoining")) {
      setOwnedDisjoining(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-featureMembership")) {
      setFeatureMembership(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-differencingType")) {
      setDifferencingType(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedDifferencing")) {
      setOwnedDifferencing(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-directedFeature")) {
      setDirectedFeature(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedSpecialization")) {
      setOwnedSpecialization(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-membership")) {
      setMembership(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedImport")) {
      setOwnedImport(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-member")) {
      setMember(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedMember")) {
      setOwnedMember(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-importedMembership")) {
      setImportedMembership(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedMembership")) {
      setOwnedMembership(values);
      return;
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public void setReferred(@NotNull Reference reference, int index, @Nullable Node referredNode) {
    Objects.requireNonNull(reference, "reference cannot be null");
    if (index < 0) throw new IllegalArgumentException("index should be non-negative");;
    if (Objects.equals(reference.getKey(), "sysml-AllocationDefinition-allocation")) {
      if (index >= allocation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = allocation.get(index);
      allocation.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ConnectionDefinition-connectionEnd")) {
      if (index >= connectionEnd.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = connectionEnd.get(index);
      connectionEnd.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAssociation-relatedType")) {
      if (index >= relatedType.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = relatedType.get(index);
      relatedType.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAssociation-sourceType")) {
      if (index >= 1 || sourceType == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      sourceType = sourceType.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAssociation-targetType")) {
      if (index >= targetType.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = targetType.get(index);
      targetType.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAssociation-associationEnd")) {
      if (index >= associationEnd.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = associationEnd.get(index);
      associationEnd.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-OccurrenceDefinition-lifeClass")) {
      if (index >= 1 || lifeClass == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      lifeClass = lifeClass.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IClassifier-ownedSubclassification")) {
      if (index >= ownedSubclassification.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedSubclassification.get(index);
      ownedSubclassification.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-owningRelatedElement")) {
      if (index >= 1 || owningRelatedElement == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningRelatedElement = owningRelatedElement.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-relatedElement")) {
      if (index >= relatedElement.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = relatedElement.get(index);
      relatedElement.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-target")) {
      if (index >= target.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = target.get(index);
      target.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-source")) {
      if (index >= source.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = source.get(index);
      source.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owningMembership")) {
      if (index >= 1 || owningMembership == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningMembership = owningMembership.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owningNamespace")) {
      if (index >= 1 || owningNamespace == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningNamespace = owningNamespace.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owningRelationship")) {
      if (index >= 1 || owningRelationship == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningRelationship = owningRelationship.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owner")) {
      if (index >= 1 || owner == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owner = owner.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-ownedElement")) {
      if (index >= ownedElement.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedElement.get(index);
      ownedElement.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-documentation")) {
      if (index >= documentation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = documentation.get(index);
      documentation.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-ownedAnnotation")) {
      if (index >= ownedAnnotation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedAnnotation.get(index);
      ownedAnnotation.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-textualRepresentation")) {
      if (index >= textualRepresentation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = textualRepresentation.get(index);
      textualRepresentation.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-variant")) {
      if (index >= variant.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = variant.get(index);
      variant.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-variantMembership")) {
      if (index >= variantMembership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = variantMembership.get(index);
      variantMembership.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-usage")) {
      if (index >= usage.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = usage.get(index);
      usage.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-directedUsage")) {
      if (index >= directedUsage.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = directedUsage.get(index);
      directedUsage.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedReference")) {
      if (index >= ownedReference.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedReference.get(index);
      ownedReference.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAttribute")) {
      if (index >= ownedAttribute.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedAttribute.get(index);
      ownedAttribute.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedEnumeration")) {
      if (index >= ownedEnumeration.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedEnumeration.get(index);
      ownedEnumeration.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedOccurrence")) {
      if (index >= ownedOccurrence.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedOccurrence.get(index);
      ownedOccurrence.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedItem")) {
      if (index >= ownedItem.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedItem.get(index);
      ownedItem.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedPart")) {
      if (index >= ownedPart.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedPart.get(index);
      ownedPart.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedPort")) {
      if (index >= ownedPort.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedPort.get(index);
      ownedPort.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConnection")) {
      if (index >= ownedConnection.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedConnection.get(index);
      ownedConnection.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedFlow")) {
      if (index >= ownedFlow.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedFlow.get(index);
      ownedFlow.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedInterface")) {
      if (index >= ownedInterface.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedInterface.get(index);
      ownedInterface.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAllocation")) {
      if (index >= ownedAllocation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedAllocation.get(index);
      ownedAllocation.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAction")) {
      if (index >= ownedAction.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedAction.get(index);
      ownedAction.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedState")) {
      if (index >= ownedState.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedState.get(index);
      ownedState.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedTransition")) {
      if (index >= ownedTransition.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedTransition.get(index);
      ownedTransition.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedCalculation")) {
      if (index >= ownedCalculation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedCalculation.get(index);
      ownedCalculation.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConstraint")) {
      if (index >= ownedConstraint.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedConstraint.get(index);
      ownedConstraint.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedRequirement")) {
      if (index >= ownedRequirement.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedRequirement.get(index);
      ownedRequirement.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConcern")) {
      if (index >= ownedConcern.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedConcern.get(index);
      ownedConcern.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedCase")) {
      if (index >= ownedCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedCase.get(index);
      ownedCase.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAnalysisCase")) {
      if (index >= ownedAnalysisCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedAnalysisCase.get(index);
      ownedAnalysisCase.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedVerificationCase")) {
      if (index >= ownedVerificationCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedVerificationCase.get(index);
      ownedVerificationCase.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedUseCase")) {
      if (index >= ownedUseCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedUseCase.get(index);
      ownedUseCase.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedView")) {
      if (index >= ownedView.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedView.get(index);
      ownedView.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedViewpoint")) {
      if (index >= ownedViewpoint.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedViewpoint.get(index);
      ownedViewpoint.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedRendering")) {
      if (index >= ownedRendering.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedRendering.get(index);
      ownedRendering.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedMetadata")) {
      if (index >= ownedMetadata.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedMetadata.get(index);
      ownedMetadata.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedUsage")) {
      if (index >= ownedUsage.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedUsage.get(index);
      ownedUsage.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedFeatureMembership")) {
      if (index >= ownedFeatureMembership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedFeatureMembership.get(index);
      ownedFeatureMembership.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedFeature")) {
      if (index >= ownedFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedFeature.get(index);
      ownedFeature.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedEndFeature")) {
      if (index >= ownedEndFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedEndFeature.get(index);
      ownedEndFeature.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-feature")) {
      if (index >= feature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = feature.get(index);
      feature.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-input")) {
      if (index >= input.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = input.get(index);
      input.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-output")) {
      if (index >= output.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = output.get(index);
      output.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-inheritedMembership")) {
      if (index >= inheritedMembership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = inheritedMembership.get(index);
      inheritedMembership.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-endFeature")) {
      if (index >= endFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = endFeature.get(index);
      endFeature.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedConjugator")) {
      if (index >= 1 || ownedConjugator == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      ownedConjugator = ownedConjugator.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-inheritedFeature")) {
      if (index >= inheritedFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = inheritedFeature.get(index);
      inheritedFeature.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-multiplicity")) {
      if (index >= 1 || multiplicity == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      multiplicity = multiplicity.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-unioningType")) {
      if (index >= unioningType.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = unioningType.get(index);
      unioningType.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedIntersecting")) {
      if (index >= ownedIntersecting.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedIntersecting.get(index);
      ownedIntersecting.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-intersectingType")) {
      if (index >= intersectingType.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = intersectingType.get(index);
      intersectingType.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedUnioning")) {
      if (index >= ownedUnioning.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedUnioning.get(index);
      ownedUnioning.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedDisjoining")) {
      if (index >= ownedDisjoining.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedDisjoining.get(index);
      ownedDisjoining.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-featureMembership")) {
      if (index >= featureMembership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = featureMembership.get(index);
      featureMembership.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-differencingType")) {
      if (index >= differencingType.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = differencingType.get(index);
      differencingType.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedDifferencing")) {
      if (index >= ownedDifferencing.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedDifferencing.get(index);
      ownedDifferencing.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-directedFeature")) {
      if (index >= directedFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = directedFeature.get(index);
      directedFeature.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedSpecialization")) {
      if (index >= ownedSpecialization.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedSpecialization.get(index);
      ownedSpecialization.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-membership")) {
      if (index >= membership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = membership.get(index);
      membership.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedImport")) {
      if (index >= ownedImport.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedImport.get(index);
      ownedImport.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-member")) {
      if (index >= member.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = member.get(index);
      member.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedMember")) {
      if (index >= ownedMember.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedMember.get(index);
      ownedMember.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-importedMembership")) {
      if (index >= importedMembership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = importedMembership.get(index);
      importedMembership.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedMembership")) {
      if (index >= ownedMembership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedMembership.get(index);
      ownedMembership.set(index, original.withReferred(referredNode));
      return;
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public void setResolveInfo(@NotNull Reference reference, int index,
      @Nullable String resolveInfo) {
    Objects.requireNonNull(reference, "reference cannot be null");
    if (index < 0) throw new IllegalArgumentException("index should be non-negative");;
    if (Objects.equals(reference.getKey(), "sysml-AllocationDefinition-allocation")) {
      if (index >= allocation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = allocation.get(index);
      allocation.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ConnectionDefinition-connectionEnd")) {
      if (index >= connectionEnd.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = connectionEnd.get(index);
      connectionEnd.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAssociation-relatedType")) {
      if (index >= relatedType.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = relatedType.get(index);
      relatedType.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAssociation-sourceType")) {
      if (index >= 1 || sourceType == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      sourceType = sourceType.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAssociation-targetType")) {
      if (index >= targetType.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = targetType.get(index);
      targetType.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAssociation-associationEnd")) {
      if (index >= associationEnd.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = associationEnd.get(index);
      associationEnd.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-OccurrenceDefinition-lifeClass")) {
      if (index >= 1 || lifeClass == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      lifeClass = lifeClass.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IClassifier-ownedSubclassification")) {
      if (index >= ownedSubclassification.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedSubclassification.get(index);
      ownedSubclassification.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-owningRelatedElement")) {
      if (index >= 1 || owningRelatedElement == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningRelatedElement = owningRelatedElement.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-relatedElement")) {
      if (index >= relatedElement.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = relatedElement.get(index);
      relatedElement.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-target")) {
      if (index >= target.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = target.get(index);
      target.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-source")) {
      if (index >= source.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = source.get(index);
      source.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owningMembership")) {
      if (index >= 1 || owningMembership == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningMembership = owningMembership.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owningNamespace")) {
      if (index >= 1 || owningNamespace == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningNamespace = owningNamespace.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owningRelationship")) {
      if (index >= 1 || owningRelationship == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningRelationship = owningRelationship.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owner")) {
      if (index >= 1 || owner == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owner = owner.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-ownedElement")) {
      if (index >= ownedElement.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedElement.get(index);
      ownedElement.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-documentation")) {
      if (index >= documentation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = documentation.get(index);
      documentation.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-ownedAnnotation")) {
      if (index >= ownedAnnotation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedAnnotation.get(index);
      ownedAnnotation.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-textualRepresentation")) {
      if (index >= textualRepresentation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = textualRepresentation.get(index);
      textualRepresentation.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-variant")) {
      if (index >= variant.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = variant.get(index);
      variant.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-variantMembership")) {
      if (index >= variantMembership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = variantMembership.get(index);
      variantMembership.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-usage")) {
      if (index >= usage.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = usage.get(index);
      usage.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-directedUsage")) {
      if (index >= directedUsage.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = directedUsage.get(index);
      directedUsage.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedReference")) {
      if (index >= ownedReference.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedReference.get(index);
      ownedReference.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAttribute")) {
      if (index >= ownedAttribute.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedAttribute.get(index);
      ownedAttribute.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedEnumeration")) {
      if (index >= ownedEnumeration.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedEnumeration.get(index);
      ownedEnumeration.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedOccurrence")) {
      if (index >= ownedOccurrence.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedOccurrence.get(index);
      ownedOccurrence.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedItem")) {
      if (index >= ownedItem.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedItem.get(index);
      ownedItem.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedPart")) {
      if (index >= ownedPart.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedPart.get(index);
      ownedPart.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedPort")) {
      if (index >= ownedPort.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedPort.get(index);
      ownedPort.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConnection")) {
      if (index >= ownedConnection.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedConnection.get(index);
      ownedConnection.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedFlow")) {
      if (index >= ownedFlow.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedFlow.get(index);
      ownedFlow.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedInterface")) {
      if (index >= ownedInterface.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedInterface.get(index);
      ownedInterface.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAllocation")) {
      if (index >= ownedAllocation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedAllocation.get(index);
      ownedAllocation.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAction")) {
      if (index >= ownedAction.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedAction.get(index);
      ownedAction.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedState")) {
      if (index >= ownedState.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedState.get(index);
      ownedState.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedTransition")) {
      if (index >= ownedTransition.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedTransition.get(index);
      ownedTransition.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedCalculation")) {
      if (index >= ownedCalculation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedCalculation.get(index);
      ownedCalculation.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConstraint")) {
      if (index >= ownedConstraint.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedConstraint.get(index);
      ownedConstraint.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedRequirement")) {
      if (index >= ownedRequirement.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedRequirement.get(index);
      ownedRequirement.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConcern")) {
      if (index >= ownedConcern.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedConcern.get(index);
      ownedConcern.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedCase")) {
      if (index >= ownedCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedCase.get(index);
      ownedCase.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAnalysisCase")) {
      if (index >= ownedAnalysisCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedAnalysisCase.get(index);
      ownedAnalysisCase.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedVerificationCase")) {
      if (index >= ownedVerificationCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedVerificationCase.get(index);
      ownedVerificationCase.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedUseCase")) {
      if (index >= ownedUseCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedUseCase.get(index);
      ownedUseCase.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedView")) {
      if (index >= ownedView.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedView.get(index);
      ownedView.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedViewpoint")) {
      if (index >= ownedViewpoint.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedViewpoint.get(index);
      ownedViewpoint.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedRendering")) {
      if (index >= ownedRendering.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedRendering.get(index);
      ownedRendering.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedMetadata")) {
      if (index >= ownedMetadata.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedMetadata.get(index);
      ownedMetadata.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedUsage")) {
      if (index >= ownedUsage.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedUsage.get(index);
      ownedUsage.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedFeatureMembership")) {
      if (index >= ownedFeatureMembership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedFeatureMembership.get(index);
      ownedFeatureMembership.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedFeature")) {
      if (index >= ownedFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedFeature.get(index);
      ownedFeature.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedEndFeature")) {
      if (index >= ownedEndFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedEndFeature.get(index);
      ownedEndFeature.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-feature")) {
      if (index >= feature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = feature.get(index);
      feature.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-input")) {
      if (index >= input.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = input.get(index);
      input.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-output")) {
      if (index >= output.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = output.get(index);
      output.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-inheritedMembership")) {
      if (index >= inheritedMembership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = inheritedMembership.get(index);
      inheritedMembership.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-endFeature")) {
      if (index >= endFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = endFeature.get(index);
      endFeature.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedConjugator")) {
      if (index >= 1 || ownedConjugator == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      ownedConjugator = ownedConjugator.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-inheritedFeature")) {
      if (index >= inheritedFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = inheritedFeature.get(index);
      inheritedFeature.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-multiplicity")) {
      if (index >= 1 || multiplicity == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      multiplicity = multiplicity.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-unioningType")) {
      if (index >= unioningType.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = unioningType.get(index);
      unioningType.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedIntersecting")) {
      if (index >= ownedIntersecting.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedIntersecting.get(index);
      ownedIntersecting.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-intersectingType")) {
      if (index >= intersectingType.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = intersectingType.get(index);
      intersectingType.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedUnioning")) {
      if (index >= ownedUnioning.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedUnioning.get(index);
      ownedUnioning.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedDisjoining")) {
      if (index >= ownedDisjoining.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedDisjoining.get(index);
      ownedDisjoining.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-featureMembership")) {
      if (index >= featureMembership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = featureMembership.get(index);
      featureMembership.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-differencingType")) {
      if (index >= differencingType.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = differencingType.get(index);
      differencingType.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedDifferencing")) {
      if (index >= ownedDifferencing.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedDifferencing.get(index);
      ownedDifferencing.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-directedFeature")) {
      if (index >= directedFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = directedFeature.get(index);
      directedFeature.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedSpecialization")) {
      if (index >= ownedSpecialization.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedSpecialization.get(index);
      ownedSpecialization.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-membership")) {
      if (index >= membership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = membership.get(index);
      membership.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedImport")) {
      if (index >= ownedImport.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedImport.get(index);
      ownedImport.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-member")) {
      if (index >= member.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = member.get(index);
      member.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedMember")) {
      if (index >= ownedMember.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedMember.get(index);
      ownedMember.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-importedMembership")) {
      if (index >= importedMembership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = importedMembership.get(index);
      importedMembership.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedMembership")) {
      if (index >= ownedMembership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedMembership.get(index);
      ownedMembership.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }
}
