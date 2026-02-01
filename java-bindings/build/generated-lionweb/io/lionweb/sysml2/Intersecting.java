package io.lionweb.sysml2;

import io.lionweb.language.Concept;
import io.lionweb.language.Containment;
import io.lionweb.language.Property;
import io.lionweb.language.Reference;
import io.lionweb.model.ClassifierInstance;
import io.lionweb.model.HasSettableParent;
import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;
import io.lionweb.model.impl.AbstractNode;
import java.lang.Boolean;
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

public class Intersecting extends AbstractNode implements HasSettableParent, IRelationship {
  @NotNull
  private String id;

  @Nullable
  private ClassifierInstance<?> parent;

  protected ReferenceValue intersectingType = null;

  protected ReferenceValue typeIntersected = null;

  protected List<IElement> ownedRelatedElement = new ArrayList<>();

  protected ReferenceValue owningRelatedElement = null;

  protected List<ReferenceValue> relatedElement = new ArrayList<>();

  protected List<ReferenceValue> target = new ArrayList<>();

  protected List<ReferenceValue> source = new ArrayList<>();

  protected Boolean isImplied;

  protected ReferenceValue owningMembership = null;

  protected ReferenceValue owningNamespace = null;

  protected ReferenceValue owningRelationship = null;

  protected String elementId;

  protected List<IRelationship> ownedRelationship = new ArrayList<>();

  protected ReferenceValue owner = null;

  protected List<ReferenceValue> ownedElement = new ArrayList<>();

  protected List<ReferenceValue> documentation = new ArrayList<>();

  protected List<ReferenceValue> ownedAnnotation = new ArrayList<>();

  protected List<ReferenceValue> textualRepresentation = new ArrayList<>();

  protected String declaredShortName;

  protected String declaredName;

  protected String shortName;

  protected String name;

  protected String qualifiedName;

  protected Boolean isImpliedIncluded;

  protected Boolean isLibraryElement;

  protected List<AliasIdsContainer> aliasIdsContainer = new ArrayList<>();

  public Intersecting(@NotNull String id) {
    Objects.requireNonNull(id, "id must not be null");
    this.id = id;
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
    return SysmlLanguage.getInstance().getIntersecting();
  }

  public void setIntersectingType(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("intersectingType"), 0, intersectingType);
      }
      intersectingType = null;
    } else {
      if (partitionObserverCache != null) {
        if (intersectingType != null) {
          ReferenceValue oldValue = intersectingType;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("intersectingType"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("intersectingType"), 0, value);
        }
      }
      this.intersectingType = value;
    }
  }

  public ReferenceValue getIntersectingType() {
    return intersectingType;
  }

  public void setTypeIntersected(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("typeIntersected"), 0, typeIntersected);
      }
      typeIntersected = null;
    } else {
      if (partitionObserverCache != null) {
        if (typeIntersected != null) {
          ReferenceValue oldValue = typeIntersected;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("typeIntersected"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("typeIntersected"), 0, value);
        }
      }
      this.typeIntersected = value;
    }
  }

  public ReferenceValue getTypeIntersected() {
    return typeIntersected;
  }

  public @NotNull List<IElement> getOwnedRelatedElement() {
    return Collections.unmodifiableList(ownedRelatedElement);
  }

  public void clearOwnedRelatedElement() {
    while (!ownedRelatedElement.isEmpty()) {
            removeFromOwnedRelatedElement(0);
        };
  }

  public int addToOwnedRelatedElement(@NotNull IElement child) {
    return addToOwnedRelatedElement(child, ownedRelatedElement.size());
  }

  public int addToOwnedRelatedElement(@NotNull IElement child, int index) {
    if (child instanceof HasSettableParent) {
      ((HasSettableParent) child).setParent(this);
    }
    ownedRelatedElement.add(index, (IElement)child);
    if (partitionObserverCache != null) {
      partitionObserverCache.childAdded(this, this.getClassifier().requireContainmentByName("ownedRelatedElement"), ownedRelatedElement.size() - 1, child);
    }
    return ownedRelatedElement.size() - 1;
  }

  public void removeFromOwnedRelatedElement(@NotNull IElement child) {
    int index = ownedRelatedElement.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedRelatedElement(index);;
  }

  public void removeFromOwnedRelatedElement(int index) {
    if (ownedRelatedElement.size() > index) {
                Node removed = ownedRelatedElement.remove(index);
                if (removed instanceof HasSettableParent) { ((HasSettableParent) removed).setParent(null); }
                if (partitionObserverCache != null) {
                  partitionObserverCache.childRemoved(this, this.getClassifier().requireContainmentByName("ownedRelatedElement"), index, removed);
                }
              } else {
                throw new IllegalArgumentException(
                    "Invalid index " + index + " when children are " + ownedRelatedElement.size());
              };
  }

  public void setOwnedRelatedElement(@NotNull List<IElement> newValue) {
    clearOwnedRelatedElement();
              for (IElement child : newValue) { addToOwnedRelatedElement(child); };
  }

  public void setOwningRelatedElement(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("owningRelatedElement"), 0, owningRelatedElement);
      }
      owningRelatedElement = null;
    } else {
      if (partitionObserverCache != null) {
        if (owningRelatedElement != null) {
          ReferenceValue oldValue = owningRelatedElement;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("owningRelatedElement"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("owningRelatedElement"), 0, value);
        }
      }
      this.owningRelatedElement = value;
    }
  }

  public ReferenceValue getOwningRelatedElement() {
    return owningRelatedElement;
  }

  public int addToRelatedElement(ReferenceValue referenceValue, int index) {
    if (index > relatedElement.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("relatedElement"), index, referenceValue);
    }
    relatedElement.add(index, referenceValue);
    return relatedElement.size() - 1;
  }

  public List<ReferenceValue> getRelatedElement() {
    return relatedElement;
  }

  public int addToRelatedElement(IElement referred) {
    return addToRelatedElement(new ReferenceValue(referred, null), relatedElement.size());
  }

  public int addToRelatedElement(IElement referred, int index) {
    return addToRelatedElement(new ReferenceValue(referred, null), index);
  }

  public void clearRelatedElement() {
    while (!relatedElement.isEmpty()) {
            removeFromRelatedElement(0);
        };
  }

  public void removeFromRelatedElement(@NotNull ReferenceValue child) {
    int index = relatedElement.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromRelatedElement(index);;
  }

  public void removeFromRelatedElement(int index) {
    if (relatedElement.size() > index) {

            ReferenceValue removed = relatedElement.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("relatedElement"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + relatedElement.size());
          }
  }

  public void setRelatedElement(@NotNull List<? extends ReferenceValue> newValue) {
    clearRelatedElement();
          for (ReferenceValue referenceValue : newValue) {
              addToRelatedElement(referenceValue, relatedElement.size());
          }
  }

  public int addToTarget(ReferenceValue referenceValue, int index) {
    if (index > target.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("target"), index, referenceValue);
    }
    target.add(index, referenceValue);
    return target.size() - 1;
  }

  public List<ReferenceValue> getTarget() {
    return target;
  }

  public int addToTarget(IElement referred) {
    return addToTarget(new ReferenceValue(referred, null), target.size());
  }

  public int addToTarget(IElement referred, int index) {
    return addToTarget(new ReferenceValue(referred, null), index);
  }

  public void clearTarget() {
    while (!target.isEmpty()) {
            removeFromTarget(0);
        };
  }

  public void removeFromTarget(@NotNull ReferenceValue child) {
    int index = target.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromTarget(index);;
  }

  public void removeFromTarget(int index) {
    if (target.size() > index) {

            ReferenceValue removed = target.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("target"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + target.size());
          }
  }

  public void setTarget(@NotNull List<? extends ReferenceValue> newValue) {
    clearTarget();
          for (ReferenceValue referenceValue : newValue) {
              addToTarget(referenceValue, target.size());
          }
  }

  public int addToSource(ReferenceValue referenceValue, int index) {
    if (index > source.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("source"), index, referenceValue);
    }
    source.add(index, referenceValue);
    return source.size() - 1;
  }

  public List<ReferenceValue> getSource() {
    return source;
  }

  public int addToSource(IElement referred) {
    return addToSource(new ReferenceValue(referred, null), source.size());
  }

  public int addToSource(IElement referred, int index) {
    return addToSource(new ReferenceValue(referred, null), index);
  }

  public void clearSource() {
    while (!source.isEmpty()) {
            removeFromSource(0);
        };
  }

  public void removeFromSource(@NotNull ReferenceValue child) {
    int index = source.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromSource(index);;
  }

  public void removeFromSource(int index) {
    if (source.size() > index) {

            ReferenceValue removed = source.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("source"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + source.size());
          }
  }

  public void setSource(@NotNull List<? extends ReferenceValue> newValue) {
    clearSource();
          for (ReferenceValue referenceValue : newValue) {
              addToSource(referenceValue, source.size());
          }
  }

  public Boolean getIsImplied() {
    return isImplied;
  }

  public void setIsImplied(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isImplied"), getIsImplied(), value);
        }
    this.isImplied = value;
  }

  public void setOwningMembership(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("owningMembership"), 0, owningMembership);
      }
      owningMembership = null;
    } else {
      if (partitionObserverCache != null) {
        if (owningMembership != null) {
          ReferenceValue oldValue = owningMembership;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("owningMembership"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("owningMembership"), 0, value);
        }
      }
      this.owningMembership = value;
    }
  }

  public ReferenceValue getOwningMembership() {
    return owningMembership;
  }

  public void setOwningNamespace(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("owningNamespace"), 0, owningNamespace);
      }
      owningNamespace = null;
    } else {
      if (partitionObserverCache != null) {
        if (owningNamespace != null) {
          ReferenceValue oldValue = owningNamespace;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("owningNamespace"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("owningNamespace"), 0, value);
        }
      }
      this.owningNamespace = value;
    }
  }

  public ReferenceValue getOwningNamespace() {
    return owningNamespace;
  }

  public void setOwningRelationship(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("owningRelationship"), 0, owningRelationship);
      }
      owningRelationship = null;
    } else {
      if (partitionObserverCache != null) {
        if (owningRelationship != null) {
          ReferenceValue oldValue = owningRelationship;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("owningRelationship"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("owningRelationship"), 0, value);
        }
      }
      this.owningRelationship = value;
    }
  }

  public ReferenceValue getOwningRelationship() {
    return owningRelationship;
  }

  public String getElementId() {
    return elementId;
  }

  public void setElementId(String value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("elementId"), getElementId(), value);
        }
    this.elementId = value;
  }

  public @NotNull List<IRelationship> getOwnedRelationship() {
    return Collections.unmodifiableList(ownedRelationship);
  }

  public void clearOwnedRelationship() {
    while (!ownedRelationship.isEmpty()) {
            removeFromOwnedRelationship(0);
        };
  }

  public int addToOwnedRelationship(@NotNull IRelationship child) {
    return addToOwnedRelationship(child, ownedRelationship.size());
  }

  public int addToOwnedRelationship(@NotNull IRelationship child, int index) {
    if (child instanceof HasSettableParent) {
      ((HasSettableParent) child).setParent(this);
    }
    ownedRelationship.add(index, (IRelationship)child);
    if (partitionObserverCache != null) {
      partitionObserverCache.childAdded(this, this.getClassifier().requireContainmentByName("ownedRelationship"), ownedRelationship.size() - 1, child);
    }
    return ownedRelationship.size() - 1;
  }

  public void removeFromOwnedRelationship(@NotNull IRelationship child) {
    int index = ownedRelationship.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedRelationship(index);;
  }

  public void removeFromOwnedRelationship(int index) {
    if (ownedRelationship.size() > index) {
                Node removed = ownedRelationship.remove(index);
                if (removed instanceof HasSettableParent) { ((HasSettableParent) removed).setParent(null); }
                if (partitionObserverCache != null) {
                  partitionObserverCache.childRemoved(this, this.getClassifier().requireContainmentByName("ownedRelationship"), index, removed);
                }
              } else {
                throw new IllegalArgumentException(
                    "Invalid index " + index + " when children are " + ownedRelationship.size());
              };
  }

  public void setOwnedRelationship(@NotNull List<IRelationship> newValue) {
    clearOwnedRelationship();
              for (IRelationship child : newValue) { addToOwnedRelationship(child); };
  }

  public void setOwner(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("owner"), 0, owner);
      }
      owner = null;
    } else {
      if (partitionObserverCache != null) {
        if (owner != null) {
          ReferenceValue oldValue = owner;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("owner"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("owner"), 0, value);
        }
      }
      this.owner = value;
    }
  }

  public ReferenceValue getOwner() {
    return owner;
  }

  public int addToOwnedElement(ReferenceValue referenceValue, int index) {
    if (index > ownedElement.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedElement"), index, referenceValue);
    }
    ownedElement.add(index, referenceValue);
    return ownedElement.size() - 1;
  }

  public List<ReferenceValue> getOwnedElement() {
    return ownedElement;
  }

  public int addToOwnedElement(IElement referred) {
    return addToOwnedElement(new ReferenceValue(referred, null), ownedElement.size());
  }

  public int addToOwnedElement(IElement referred, int index) {
    return addToOwnedElement(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedElement() {
    while (!ownedElement.isEmpty()) {
            removeFromOwnedElement(0);
        };
  }

  public void removeFromOwnedElement(@NotNull ReferenceValue child) {
    int index = ownedElement.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedElement(index);;
  }

  public void removeFromOwnedElement(int index) {
    if (ownedElement.size() > index) {

            ReferenceValue removed = ownedElement.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedElement"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedElement.size());
          }
  }

  public void setOwnedElement(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedElement();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedElement(referenceValue, ownedElement.size());
          }
  }

  public int addToDocumentation(ReferenceValue referenceValue, int index) {
    if (index > documentation.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("documentation"), index, referenceValue);
    }
    documentation.add(index, referenceValue);
    return documentation.size() - 1;
  }

  public List<ReferenceValue> getDocumentation() {
    return documentation;
  }

  public int addToDocumentation(Documentation referred) {
    return addToDocumentation(new ReferenceValue(referred, null), documentation.size());
  }

  public int addToDocumentation(Documentation referred, int index) {
    return addToDocumentation(new ReferenceValue(referred, null), index);
  }

  public void clearDocumentation() {
    while (!documentation.isEmpty()) {
            removeFromDocumentation(0);
        };
  }

  public void removeFromDocumentation(@NotNull ReferenceValue child) {
    int index = documentation.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromDocumentation(index);;
  }

  public void removeFromDocumentation(int index) {
    if (documentation.size() > index) {

            ReferenceValue removed = documentation.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("documentation"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + documentation.size());
          }
  }

  public void setDocumentation(@NotNull List<? extends ReferenceValue> newValue) {
    clearDocumentation();
          for (ReferenceValue referenceValue : newValue) {
              addToDocumentation(referenceValue, documentation.size());
          }
  }

  public int addToOwnedAnnotation(ReferenceValue referenceValue, int index) {
    if (index > ownedAnnotation.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedAnnotation"), index, referenceValue);
    }
    ownedAnnotation.add(index, referenceValue);
    return ownedAnnotation.size() - 1;
  }

  public List<ReferenceValue> getOwnedAnnotation() {
    return ownedAnnotation;
  }

  public int addToOwnedAnnotation(Annotation referred) {
    return addToOwnedAnnotation(new ReferenceValue(referred, null), ownedAnnotation.size());
  }

  public int addToOwnedAnnotation(Annotation referred, int index) {
    return addToOwnedAnnotation(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedAnnotation() {
    while (!ownedAnnotation.isEmpty()) {
            removeFromOwnedAnnotation(0);
        };
  }

  public void removeFromOwnedAnnotation(@NotNull ReferenceValue child) {
    int index = ownedAnnotation.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedAnnotation(index);;
  }

  public void removeFromOwnedAnnotation(int index) {
    if (ownedAnnotation.size() > index) {

            ReferenceValue removed = ownedAnnotation.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedAnnotation"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedAnnotation.size());
          }
  }

  public void setOwnedAnnotation(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedAnnotation();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedAnnotation(referenceValue, ownedAnnotation.size());
          }
  }

  public int addToTextualRepresentation(ReferenceValue referenceValue, int index) {
    if (index > textualRepresentation.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("textualRepresentation"), index, referenceValue);
    }
    textualRepresentation.add(index, referenceValue);
    return textualRepresentation.size() - 1;
  }

  public List<ReferenceValue> getTextualRepresentation() {
    return textualRepresentation;
  }

  public int addToTextualRepresentation(TextualRepresentation referred) {
    return addToTextualRepresentation(new ReferenceValue(referred, null), textualRepresentation.size());
  }

  public int addToTextualRepresentation(TextualRepresentation referred, int index) {
    return addToTextualRepresentation(new ReferenceValue(referred, null), index);
  }

  public void clearTextualRepresentation() {
    while (!textualRepresentation.isEmpty()) {
            removeFromTextualRepresentation(0);
        };
  }

  public void removeFromTextualRepresentation(@NotNull ReferenceValue child) {
    int index = textualRepresentation.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromTextualRepresentation(index);;
  }

  public void removeFromTextualRepresentation(int index) {
    if (textualRepresentation.size() > index) {

            ReferenceValue removed = textualRepresentation.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("textualRepresentation"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + textualRepresentation.size());
          }
  }

  public void setTextualRepresentation(@NotNull List<? extends ReferenceValue> newValue) {
    clearTextualRepresentation();
          for (ReferenceValue referenceValue : newValue) {
              addToTextualRepresentation(referenceValue, textualRepresentation.size());
          }
  }

  public String getDeclaredShortName() {
    return declaredShortName;
  }

  public void setDeclaredShortName(String value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("declaredShortName"), getDeclaredShortName(), value);
        }
    this.declaredShortName = value;
  }

  public String getDeclaredName() {
    return declaredName;
  }

  public void setDeclaredName(String value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("declaredName"), getDeclaredName(), value);
        }
    this.declaredName = value;
  }

  public String getShortName() {
    return shortName;
  }

  public void setShortName(String value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("shortName"), getShortName(), value);
        }
    this.shortName = value;
  }

  public String getName() {
    return name;
  }

  public void setName(String value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("name"), getName(), value);
        }
    this.name = value;
  }

  public String getQualifiedName() {
    return qualifiedName;
  }

  public void setQualifiedName(String value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("qualifiedName"), getQualifiedName(), value);
        }
    this.qualifiedName = value;
  }

  public Boolean getIsImpliedIncluded() {
    return isImpliedIncluded;
  }

  public void setIsImpliedIncluded(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isImpliedIncluded"), getIsImpliedIncluded(), value);
        }
    this.isImpliedIncluded = value;
  }

  public Boolean getIsLibraryElement() {
    return isLibraryElement;
  }

  public void setIsLibraryElement(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isLibraryElement"), getIsLibraryElement(), value);
        }
    this.isLibraryElement = value;
  }

  public @NotNull List<AliasIdsContainer> getAliasIdsContainer() {
    return Collections.unmodifiableList(aliasIdsContainer);
  }

  public void clearAliasIdsContainer() {
    while (!aliasIdsContainer.isEmpty()) {
            removeFromAliasIdsContainer(0);
        };
  }

  public int addToAliasIdsContainer(@NotNull AliasIdsContainer child) {
    return addToAliasIdsContainer(child, aliasIdsContainer.size());
  }

  public int addToAliasIdsContainer(@NotNull AliasIdsContainer child, int index) {
    if (child instanceof HasSettableParent) {
      ((HasSettableParent) child).setParent(this);
    }
    aliasIdsContainer.add(index, (AliasIdsContainer)child);
    if (partitionObserverCache != null) {
      partitionObserverCache.childAdded(this, this.getClassifier().requireContainmentByName("aliasIdsContainer"), aliasIdsContainer.size() - 1, child);
    }
    return aliasIdsContainer.size() - 1;
  }

  public void removeFromAliasIdsContainer(@NotNull AliasIdsContainer child) {
    int index = aliasIdsContainer.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromAliasIdsContainer(index);;
  }

  public void removeFromAliasIdsContainer(int index) {
    if (aliasIdsContainer.size() > index) {
                Node removed = aliasIdsContainer.remove(index);
                if (removed instanceof HasSettableParent) { ((HasSettableParent) removed).setParent(null); }
                if (partitionObserverCache != null) {
                  partitionObserverCache.childRemoved(this, this.getClassifier().requireContainmentByName("aliasIdsContainer"), index, removed);
                }
              } else {
                throw new IllegalArgumentException(
                    "Invalid index " + index + " when children are " + aliasIdsContainer.size());
              };
  }

  public void setAliasIdsContainer(@NotNull List<AliasIdsContainer> newValue) {
    clearAliasIdsContainer();
              for (AliasIdsContainer child : newValue) { addToAliasIdsContainer(child); };
  }

  @Override
  public Object getPropertyValue(Property property) {
    if (Objects.equals(property.getKey(), "sysml-IRelationship-isImplied")) {
      return isImplied;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-elementId")) {
      return elementId;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-declaredShortName")) {
      return declaredShortName;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-declaredName")) {
      return declaredName;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-shortName")) {
      return shortName;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-name")) {
      return name;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-qualifiedName")) {
      return qualifiedName;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-isImpliedIncluded")) {
      return isImpliedIncluded;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-isLibraryElement")) {
      return isLibraryElement;
    }
    throw new IllegalStateException("Property " + property + " not found.");
  }

  @Override
  public void setPropertyValue(Property property, Object value) {
    Objects.requireNonNull(property, "Property should not be null");;
    Objects.requireNonNull(property.getKey(), "Cannot assign a property with no Key specified");;
    if (Objects.equals(property.getKey(), "sysml-IRelationship-isImplied")) {
      setIsImplied((Boolean) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-elementId")) {
      setElementId((String) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-declaredShortName")) {
      setDeclaredShortName((String) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-declaredName")) {
      setDeclaredName((String) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-shortName")) {
      setShortName((String) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-name")) {
      setName((String) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-qualifiedName")) {
      setQualifiedName((String) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-isImpliedIncluded")) {
      setIsImpliedIncluded((Boolean) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IElement-isLibraryElement")) {
      setIsLibraryElement((Boolean) value);
      return;
    }
    throw new IllegalStateException("Property " + property + " not found.");
  }

  @Override
  public List<? extends Node> getChildren(Containment containment) {
    if (Objects.equals(containment.getKey(), "sysml-IRelationship-ownedRelatedElement")) {
      return ownedRelatedElement;
    }
    if (Objects.equals(containment.getKey(), "sysml-IElement-ownedRelationship")) {
      return ownedRelationship;
    }
    if (Objects.equals(containment.getKey(), "sysml-IElement-aliasIdsContainer")) {
      return aliasIdsContainer;
    }
    throw new IllegalStateException("Containment " + containment + " not found.");
  }

  @Override
  public void addChild(@NotNull Containment containment, @NotNull Node child) {
    Objects.requireNonNull(containment, "Containment should not be null");
    Objects.requireNonNull(child, "Child should not be null");
    if (containment.getKey().equals("sysml-IRelationship-ownedRelatedElement")) {
      addToOwnedRelatedElement((IElement) child);
      return;
    }
    if (containment.getKey().equals("sysml-IElement-ownedRelationship")) {
      addToOwnedRelationship((IRelationship) child);
      return;
    }
    if (containment.getKey().equals("sysml-IElement-aliasIdsContainer")) {
      addToAliasIdsContainer((AliasIdsContainer) child);
      return;
    }
    throw new IllegalStateException("Containment " + containment + " not found.");
  }

  @Override
  public void addChild(@NotNull Containment containment, @NotNull Node child, int index) {
    Objects.requireNonNull(containment, "containment must not be null");
    Objects.requireNonNull(child, "child must not be null");
    if (index < 0) throw new IllegalArgumentException("index should be non-negative");;
    if (containment.getKey().equals("sysml-IRelationship-ownedRelatedElement")) {
      addToOwnedRelatedElement((IElement) child, index);
      return;
    }
    if (containment.getKey().equals("sysml-IElement-ownedRelationship")) {
      addToOwnedRelationship((IRelationship) child, index);
      return;
    }
    if (containment.getKey().equals("sysml-IElement-aliasIdsContainer")) {
      addToAliasIdsContainer((AliasIdsContainer) child, index);
      return;
    }
    throw new IllegalStateException("Containment " + containment + " not found.");
  }

  @Override
  public List<ReferenceValue> getReferenceValues(@NotNull Reference reference) {
    Objects.requireNonNull(reference, "reference should not be null");;
    if (Objects.equals(reference.getKey(), "sysml-Intersecting-intersectingType")) {
      return Collections.singletonList(intersectingType);
    }
    if (Objects.equals(reference.getKey(), "sysml-Intersecting-typeIntersected")) {
      return Collections.singletonList(typeIntersected);
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-owningRelatedElement")) {
      return Collections.singletonList(owningRelatedElement);
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-relatedElement")) {
      return relatedElement;
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-target")) {
      return target;
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-source")) {
      return source;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owningMembership")) {
      return Collections.singletonList(owningMembership);
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owningNamespace")) {
      return Collections.singletonList(owningNamespace);
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owningRelationship")) {
      return Collections.singletonList(owningRelationship);
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-owner")) {
      return Collections.singletonList(owner);
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-ownedElement")) {
      return ownedElement;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-documentation")) {
      return documentation;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-ownedAnnotation")) {
      return ownedAnnotation;
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-textualRepresentation")) {
      return textualRepresentation;
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public int addReferenceValue(Reference reference, ReferenceValue referredNode) {
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-relatedElement")) {
      return addToRelatedElement(referredNode, relatedElement.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-target")) {
      return addToTarget(referredNode, target.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-source")) {
      return addToSource(referredNode, source.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-ownedElement")) {
      return addToOwnedElement(referredNode, ownedElement.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-documentation")) {
      return addToDocumentation(referredNode, documentation.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-ownedAnnotation")) {
      return addToOwnedAnnotation(referredNode, ownedAnnotation.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-textualRepresentation")) {
      return addToTextualRepresentation(referredNode, textualRepresentation.size());
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public int addReferenceValue(Reference reference, int index, ReferenceValue referredNode) {
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-relatedElement")) {
      return addToRelatedElement(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-target")) {
      return addToTarget(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-source")) {
      return addToSource(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-ownedElement")) {
      return addToOwnedElement(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-documentation")) {
      return addToDocumentation(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-ownedAnnotation")) {
      return addToOwnedAnnotation(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IElement-textualRepresentation")) {
      return addToTextualRepresentation(referredNode, index);
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public void setReferenceValues(@NotNull Reference reference,
      @NotNull List<? extends ReferenceValue> values) {
    Objects.requireNonNull(reference, "reference cannot be null");
    Objects.requireNonNull(values, "values cannot be null");
    if (Objects.equals(reference.getKey(), "sysml-Intersecting-intersectingType")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setIntersectingType(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Intersecting-typeIntersected")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setTypeIntersected(values.isEmpty() ? null : values.get(0));
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
    if (Objects.equals(reference.getKey(), "sysml-Intersecting-intersectingType")) {
      if (index >= 1 || intersectingType == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      intersectingType = intersectingType.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Intersecting-typeIntersected")) {
      if (index >= 1 || typeIntersected == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      typeIntersected = typeIntersected.withReferred(referredNode);
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
    if (Objects.equals(reference.getKey(), "sysml-Intersecting-intersectingType")) {
      if (index >= 1 || intersectingType == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      intersectingType = intersectingType.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-Intersecting-typeIntersected")) {
      if (index >= 1 || typeIntersected == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      typeIntersected = typeIntersected.withResolveInfo(resolveInfo);
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
