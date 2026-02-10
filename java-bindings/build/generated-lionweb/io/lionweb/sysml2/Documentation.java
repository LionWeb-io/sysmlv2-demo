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

public class Documentation extends Comment {
  @NotNull
  private String id;

  @Nullable
  private ClassifierInstance<?> parent;

  protected ReferenceValue documentedElement = null;

  public Documentation(@NotNull String id) {
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
    return SysmlLanguage.getInstance().getDocumentation();
  }

  public void setDocumentedElement(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("documentedElement"), 0, documentedElement);
      }
      documentedElement = null;
    } else {
      if (partitionObserverCache != null) {
        if (documentedElement != null) {
          ReferenceValue oldValue = documentedElement;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("documentedElement"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("documentedElement"), 0, value);
        }
      }
      this.documentedElement = value;
    }
  }

  public ReferenceValue getDocumentedElement() {
    return documentedElement;
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
    if (Objects.equals(reference.getKey(), "sysml-Documentation-documentedElement")) {
      return Collections.singletonList(documentedElement);
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
    if (Objects.equals(reference.getKey(), "sysml-Documentation-documentedElement")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setDocumentedElement(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAnnotatingElement-annotatedElement")) {
      setAnnotatedElement(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAnnotatingElement-ownedAnnotatingRelationship")) {
      setOwnedAnnotatingRelationship(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAnnotatingElement-annotation")) {
      setAnnotation(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAnnotatingElement-owningAnnotatingRelationship")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwningAnnotatingRelationship(values.isEmpty() ? null : values.get(0));
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
    if (Objects.equals(reference.getKey(), "sysml-Documentation-documentedElement")) {
      if (index >= 1 || documentedElement == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      documentedElement = documentedElement.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAnnotatingElement-annotatedElement")) {
      if (index >= annotatedElement.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = annotatedElement.get(index);
      annotatedElement.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAnnotatingElement-ownedAnnotatingRelationship")) {
      if (index >= ownedAnnotatingRelationship.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedAnnotatingRelationship.get(index);
      ownedAnnotatingRelationship.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAnnotatingElement-annotation")) {
      if (index >= annotation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = annotation.get(index);
      annotation.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAnnotatingElement-owningAnnotatingRelationship")) {
      if (index >= 1 || owningAnnotatingRelationship == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningAnnotatingRelationship = owningAnnotatingRelationship.withReferred(referredNode);
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
    if (Objects.equals(reference.getKey(), "sysml-Documentation-documentedElement")) {
      if (index >= 1 || documentedElement == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      documentedElement = documentedElement.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAnnotatingElement-annotatedElement")) {
      if (index >= annotatedElement.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = annotatedElement.get(index);
      annotatedElement.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAnnotatingElement-ownedAnnotatingRelationship")) {
      if (index >= ownedAnnotatingRelationship.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedAnnotatingRelationship.get(index);
      ownedAnnotatingRelationship.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAnnotatingElement-annotation")) {
      if (index >= annotation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = annotation.get(index);
      annotation.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IAnnotatingElement-owningAnnotatingRelationship")) {
      if (index >= 1 || owningAnnotatingRelationship == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningAnnotatingRelationship = owningAnnotatingRelationship.withResolveInfo(resolveInfo);
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
