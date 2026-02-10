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
import java.util.Collections;
import java.util.List;
import java.util.Objects;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

public class CaseDefinition extends CalculationDefinition {
  @NotNull
  private String id;

  @Nullable
  private ClassifierInstance<?> parent;

  protected ReferenceValue objectiveRequirement = null;

  protected ReferenceValue subjectParameter = null;

  protected List<ReferenceValue> actorParameter = new ArrayList<>();

  public CaseDefinition(@NotNull String id) {
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
    return SysmlLanguage.getInstance().getCaseDefinition();
  }

  public void setObjectiveRequirement(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("objectiveRequirement"), 0, objectiveRequirement);
      }
      objectiveRequirement = null;
    } else {
      if (partitionObserverCache != null) {
        if (objectiveRequirement != null) {
          ReferenceValue oldValue = objectiveRequirement;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("objectiveRequirement"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("objectiveRequirement"), 0, value);
        }
      }
      this.objectiveRequirement = value;
    }
  }

  public ReferenceValue getObjectiveRequirement() {
    return objectiveRequirement;
  }

  public void setSubjectParameter(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("subjectParameter"), 0, subjectParameter);
      }
      subjectParameter = null;
    } else {
      if (partitionObserverCache != null) {
        if (subjectParameter != null) {
          ReferenceValue oldValue = subjectParameter;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("subjectParameter"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("subjectParameter"), 0, value);
        }
      }
      this.subjectParameter = value;
    }
  }

  public ReferenceValue getSubjectParameter() {
    return subjectParameter;
  }

  public int addToActorParameter(ReferenceValue referenceValue, int index) {
    if (index > actorParameter.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("actorParameter"), index, referenceValue);
    }
    actorParameter.add(index, referenceValue);
    return actorParameter.size() - 1;
  }

  public List<ReferenceValue> getActorParameter() {
    return actorParameter;
  }

  public int addToActorParameter(IPartUsage referred) {
    return addToActorParameter(new ReferenceValue(referred, null), actorParameter.size());
  }

  public int addToActorParameter(IPartUsage referred, int index) {
    return addToActorParameter(new ReferenceValue(referred, null), index);
  }

  public void clearActorParameter() {
    while (!actorParameter.isEmpty()) {
            removeFromActorParameter(0);
        };
  }

  public void removeFromActorParameter(@NotNull ReferenceValue child) {
    int index = actorParameter.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromActorParameter(index);;
  }

  public void removeFromActorParameter(int index) {
    if (actorParameter.size() > index) {

            ReferenceValue removed = actorParameter.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("actorParameter"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + actorParameter.size());
          }
  }

  public void setActorParameter(@NotNull List<? extends ReferenceValue> newValue) {
    clearActorParameter();
          for (ReferenceValue referenceValue : newValue) {
              addToActorParameter(referenceValue, actorParameter.size());
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
    if (Objects.equals(reference.getKey(), "sysml-CaseDefinition-objectiveRequirement")) {
      return Collections.singletonList(objectiveRequirement);
    }
    if (Objects.equals(reference.getKey(), "sysml-CaseDefinition-subjectParameter")) {
      return Collections.singletonList(subjectParameter);
    }
    if (Objects.equals(reference.getKey(), "sysml-CaseDefinition-actorParameter")) {
      return actorParameter;
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public int addReferenceValue(Reference reference, ReferenceValue referredNode) {
    if (Objects.equals(reference.getKey(), "sysml-CaseDefinition-actorParameter")) {
      return addToActorParameter(referredNode, actorParameter.size());
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public int addReferenceValue(Reference reference, int index, ReferenceValue referredNode) {
    if (Objects.equals(reference.getKey(), "sysml-CaseDefinition-actorParameter")) {
      return addToActorParameter(referredNode, index);
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public void setReferenceValues(@NotNull Reference reference,
      @NotNull List<? extends ReferenceValue> values) {
    Objects.requireNonNull(reference, "reference cannot be null");
    Objects.requireNonNull(values, "values cannot be null");
    if (Objects.equals(reference.getKey(), "sysml-CaseDefinition-objectiveRequirement")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setObjectiveRequirement(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-CaseDefinition-subjectParameter")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setSubjectParameter(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-CaseDefinition-actorParameter")) {
      setActorParameter(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-CalculationDefinition-calculation")) {
      setCalculation(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ActionDefinition-action")) {
      setAction(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFunction-expression")) {
      setExpression(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFunction-result")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setResult(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-OccurrenceDefinition-lifeClass")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setLifeClass(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IBehavior-step")) {
      setStep(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IBehavior-parameter")) {
      setParameter(values);
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
    if (Objects.equals(reference.getKey(), "sysml-IClassifier-ownedSubclassification")) {
      setOwnedSubclassification(values);
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
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public void setReferred(@NotNull Reference reference, int index, @Nullable Node referredNode) {
    Objects.requireNonNull(reference, "reference cannot be null");
    if (index < 0) throw new IllegalArgumentException("index should be non-negative");;
    if (Objects.equals(reference.getKey(), "sysml-CaseDefinition-objectiveRequirement")) {
      if (index >= 1 || objectiveRequirement == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      objectiveRequirement = objectiveRequirement.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-CaseDefinition-subjectParameter")) {
      if (index >= 1 || subjectParameter == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      subjectParameter = subjectParameter.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-CaseDefinition-actorParameter")) {
      if (index >= actorParameter.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = actorParameter.get(index);
      actorParameter.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-CalculationDefinition-calculation")) {
      if (index >= calculation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = calculation.get(index);
      calculation.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ActionDefinition-action")) {
      if (index >= action.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = action.get(index);
      action.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFunction-expression")) {
      if (index >= expression.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = expression.get(index);
      expression.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFunction-result")) {
      if (index >= 1 || result == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      result = result.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-OccurrenceDefinition-lifeClass")) {
      if (index >= 1 || lifeClass == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      lifeClass = lifeClass.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IBehavior-step")) {
      if (index >= step.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = step.get(index);
      step.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IBehavior-parameter")) {
      if (index >= parameter.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = parameter.get(index);
      parameter.set(index, original.withReferred(referredNode));
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
    if (Objects.equals(reference.getKey(), "sysml-IClassifier-ownedSubclassification")) {
      if (index >= ownedSubclassification.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedSubclassification.get(index);
      ownedSubclassification.set(index, original.withReferred(referredNode));
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
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public void setResolveInfo(@NotNull Reference reference, int index,
      @Nullable String resolveInfo) {
    Objects.requireNonNull(reference, "reference cannot be null");
    if (index < 0) throw new IllegalArgumentException("index should be non-negative");;
    if (Objects.equals(reference.getKey(), "sysml-CaseDefinition-objectiveRequirement")) {
      if (index >= 1 || objectiveRequirement == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      objectiveRequirement = objectiveRequirement.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-CaseDefinition-subjectParameter")) {
      if (index >= 1 || subjectParameter == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      subjectParameter = subjectParameter.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-CaseDefinition-actorParameter")) {
      if (index >= actorParameter.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = actorParameter.get(index);
      actorParameter.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-CalculationDefinition-calculation")) {
      if (index >= calculation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = calculation.get(index);
      calculation.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ActionDefinition-action")) {
      if (index >= action.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = action.get(index);
      action.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFunction-expression")) {
      if (index >= expression.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = expression.get(index);
      expression.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFunction-result")) {
      if (index >= 1 || result == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      result = result.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-OccurrenceDefinition-lifeClass")) {
      if (index >= 1 || lifeClass == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      lifeClass = lifeClass.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IBehavior-step")) {
      if (index >= step.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = step.get(index);
      step.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IBehavior-parameter")) {
      if (index >= parameter.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = parameter.get(index);
      parameter.set(index, original.withResolveInfo(resolveInfo));
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
    if (Objects.equals(reference.getKey(), "sysml-IClassifier-ownedSubclassification")) {
      if (index >= ownedSubclassification.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedSubclassification.get(index);
      ownedSubclassification.set(index, original.withResolveInfo(resolveInfo));
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
    throw new IllegalStateException("Reference " + reference + " not found.");
  }
}
