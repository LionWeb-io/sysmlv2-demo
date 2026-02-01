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
import java.util.Collections;
import java.util.List;
import java.util.Objects;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

public class Subsetting extends Specialization {
  @NotNull
  private String id;

  @Nullable
  private ClassifierInstance<?> parent;

  protected ReferenceValue subsettedFeature = null;

  protected ReferenceValue subsettingFeature = null;

  protected ReferenceValue owningFeature = null;

  public Subsetting(@NotNull String id) {
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
    return SysmlLanguage.getInstance().getSubsetting();
  }

  public void setSubsettedFeature(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("subsettedFeature"), 0, subsettedFeature);
      }
      subsettedFeature = null;
    } else {
      if (partitionObserverCache != null) {
        if (subsettedFeature != null) {
          ReferenceValue oldValue = subsettedFeature;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("subsettedFeature"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("subsettedFeature"), 0, value);
        }
      }
      this.subsettedFeature = value;
    }
  }

  public ReferenceValue getSubsettedFeature() {
    return subsettedFeature;
  }

  public void setSubsettingFeature(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("subsettingFeature"), 0, subsettingFeature);
      }
      subsettingFeature = null;
    } else {
      if (partitionObserverCache != null) {
        if (subsettingFeature != null) {
          ReferenceValue oldValue = subsettingFeature;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("subsettingFeature"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("subsettingFeature"), 0, value);
        }
      }
      this.subsettingFeature = value;
    }
  }

  public ReferenceValue getSubsettingFeature() {
    return subsettingFeature;
  }

  public void setOwningFeature(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("owningFeature"), 0, owningFeature);
      }
      owningFeature = null;
    } else {
      if (partitionObserverCache != null) {
        if (owningFeature != null) {
          ReferenceValue oldValue = owningFeature;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("owningFeature"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("owningFeature"), 0, value);
        }
      }
      this.owningFeature = value;
    }
  }

  public ReferenceValue getOwningFeature() {
    return owningFeature;
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
    if (Objects.equals(reference.getKey(), "sysml-Subsetting-subsettedFeature")) {
      return Collections.singletonList(subsettedFeature);
    }
    if (Objects.equals(reference.getKey(), "sysml-Subsetting-subsettingFeature")) {
      return Collections.singletonList(subsettingFeature);
    }
    if (Objects.equals(reference.getKey(), "sysml-Subsetting-owningFeature")) {
      return Collections.singletonList(owningFeature);
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public int addReferenceValue(Reference reference, ReferenceValue referredNode) {
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public int addReferenceValue(Reference reference, int index, ReferenceValue referredNode) {
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public void setReferenceValues(@NotNull Reference reference,
      @NotNull List<? extends ReferenceValue> values) {
    Objects.requireNonNull(reference, "reference cannot be null");
    Objects.requireNonNull(values, "values cannot be null");
    if (Objects.equals(reference.getKey(), "sysml-Subsetting-subsettedFeature")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setSubsettedFeature(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Subsetting-subsettingFeature")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setSubsettingFeature(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Subsetting-owningFeature")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwningFeature(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Specialization-owningType")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwningType(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Specialization-general")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setGeneral(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Specialization-specific")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setSpecific(values.isEmpty() ? null : values.get(0));
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
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public void setReferred(@NotNull Reference reference, int index, @Nullable Node referredNode) {
    Objects.requireNonNull(reference, "reference cannot be null");
    if (index < 0) throw new IllegalArgumentException("index should be non-negative");;
    if (Objects.equals(reference.getKey(), "sysml-Subsetting-subsettedFeature")) {
      if (index >= 1 || subsettedFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      subsettedFeature = subsettedFeature.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Subsetting-subsettingFeature")) {
      if (index >= 1 || subsettingFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      subsettingFeature = subsettingFeature.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Subsetting-owningFeature")) {
      if (index >= 1 || owningFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningFeature = owningFeature.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Specialization-owningType")) {
      if (index >= 1 || owningType == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningType = owningType.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Specialization-general")) {
      if (index >= 1 || general == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      general = general.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Specialization-specific")) {
      if (index >= 1 || specific == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      specific = specific.withReferred(referredNode);
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
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public void setResolveInfo(@NotNull Reference reference, int index,
      @Nullable String resolveInfo) {
    Objects.requireNonNull(reference, "reference cannot be null");
    if (index < 0) throw new IllegalArgumentException("index should be non-negative");;
    if (Objects.equals(reference.getKey(), "sysml-Subsetting-subsettedFeature")) {
      if (index >= 1 || subsettedFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      subsettedFeature = subsettedFeature.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Subsetting-subsettingFeature")) {
      if (index >= 1 || subsettingFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      subsettingFeature = subsettingFeature.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Subsetting-owningFeature")) {
      if (index >= 1 || owningFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningFeature = owningFeature.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Specialization-owningType")) {
      if (index >= 1 || owningType == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningType = owningType.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Specialization-general")) {
      if (index >= 1 || general == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      general = general.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Specialization-specific")) {
      if (index >= 1 || specific == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      specific = specific.withResolveInfo(resolveInfo);
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
    throw new IllegalStateException("Reference " + reference + " not found.");
  }
}
