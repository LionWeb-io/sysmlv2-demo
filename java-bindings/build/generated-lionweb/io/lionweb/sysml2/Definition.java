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

public class Definition extends AbstractNode implements HasSettableParent, IClassifier {
  @NotNull
  private String id;

  @Nullable
  private ClassifierInstance<?> parent;

  protected Boolean isVariation;

  protected List<ReferenceValue> variant = new ArrayList<>();

  protected List<ReferenceValue> variantMembership = new ArrayList<>();

  protected List<ReferenceValue> usage = new ArrayList<>();

  protected List<ReferenceValue> directedUsage = new ArrayList<>();

  protected List<ReferenceValue> ownedReference = new ArrayList<>();

  protected List<ReferenceValue> ownedAttribute = new ArrayList<>();

  protected List<ReferenceValue> ownedEnumeration = new ArrayList<>();

  protected List<ReferenceValue> ownedOccurrence = new ArrayList<>();

  protected List<ReferenceValue> ownedItem = new ArrayList<>();

  protected List<ReferenceValue> ownedPart = new ArrayList<>();

  protected List<ReferenceValue> ownedPort = new ArrayList<>();

  protected List<ReferenceValue> ownedConnection = new ArrayList<>();

  protected List<ReferenceValue> ownedFlow = new ArrayList<>();

  protected List<ReferenceValue> ownedInterface = new ArrayList<>();

  protected List<ReferenceValue> ownedAllocation = new ArrayList<>();

  protected List<ReferenceValue> ownedAction = new ArrayList<>();

  protected List<ReferenceValue> ownedState = new ArrayList<>();

  protected List<ReferenceValue> ownedTransition = new ArrayList<>();

  protected List<ReferenceValue> ownedCalculation = new ArrayList<>();

  protected List<ReferenceValue> ownedConstraint = new ArrayList<>();

  protected List<ReferenceValue> ownedRequirement = new ArrayList<>();

  protected List<ReferenceValue> ownedConcern = new ArrayList<>();

  protected List<ReferenceValue> ownedCase = new ArrayList<>();

  protected List<ReferenceValue> ownedAnalysisCase = new ArrayList<>();

  protected List<ReferenceValue> ownedVerificationCase = new ArrayList<>();

  protected List<ReferenceValue> ownedUseCase = new ArrayList<>();

  protected List<ReferenceValue> ownedView = new ArrayList<>();

  protected List<ReferenceValue> ownedViewpoint = new ArrayList<>();

  protected List<ReferenceValue> ownedRendering = new ArrayList<>();

  protected List<ReferenceValue> ownedMetadata = new ArrayList<>();

  protected List<ReferenceValue> ownedUsage = new ArrayList<>();

  protected List<ReferenceValue> ownedSubclassification = new ArrayList<>();

  protected List<ReferenceValue> ownedFeatureMembership = new ArrayList<>();

  protected List<ReferenceValue> ownedFeature = new ArrayList<>();

  protected List<ReferenceValue> ownedEndFeature = new ArrayList<>();

  protected List<ReferenceValue> feature = new ArrayList<>();

  protected List<ReferenceValue> input = new ArrayList<>();

  protected List<ReferenceValue> output = new ArrayList<>();

  protected Boolean isAbstract;

  protected List<ReferenceValue> inheritedMembership = new ArrayList<>();

  protected List<ReferenceValue> endFeature = new ArrayList<>();

  protected Boolean isSufficient;

  protected ReferenceValue ownedConjugator = null;

  protected Boolean isConjugated;

  protected List<ReferenceValue> inheritedFeature = new ArrayList<>();

  protected ReferenceValue multiplicity = null;

  protected List<ReferenceValue> unioningType = new ArrayList<>();

  protected List<ReferenceValue> ownedIntersecting = new ArrayList<>();

  protected List<ReferenceValue> intersectingType = new ArrayList<>();

  protected List<ReferenceValue> ownedUnioning = new ArrayList<>();

  protected List<ReferenceValue> ownedDisjoining = new ArrayList<>();

  protected List<ReferenceValue> featureMembership = new ArrayList<>();

  protected List<ReferenceValue> differencingType = new ArrayList<>();

  protected List<ReferenceValue> ownedDifferencing = new ArrayList<>();

  protected List<ReferenceValue> directedFeature = new ArrayList<>();

  protected List<ReferenceValue> ownedSpecialization = new ArrayList<>();

  protected List<ReferenceValue> membership = new ArrayList<>();

  protected List<ReferenceValue> ownedImport = new ArrayList<>();

  protected List<ReferenceValue> member = new ArrayList<>();

  protected List<ReferenceValue> ownedMember = new ArrayList<>();

  protected List<ReferenceValue> importedMembership = new ArrayList<>();

  protected List<ReferenceValue> ownedMembership = new ArrayList<>();

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

  public Definition(@NotNull String id) {
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
    return SysmlLanguage.getInstance().getDefinition();
  }

  public Boolean getIsVariation() {
    return isVariation;
  }

  public void setIsVariation(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isVariation"), getIsVariation(), value);
        }
    this.isVariation = value;
  }

  public int addToVariant(ReferenceValue referenceValue, int index) {
    if (index > variant.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("variant"), index, referenceValue);
    }
    variant.add(index, referenceValue);
    return variant.size() - 1;
  }

  public List<ReferenceValue> getVariant() {
    return variant;
  }

  public int addToVariant(IUsage referred) {
    return addToVariant(new ReferenceValue(referred, null), variant.size());
  }

  public int addToVariant(IUsage referred, int index) {
    return addToVariant(new ReferenceValue(referred, null), index);
  }

  public void clearVariant() {
    while (!variant.isEmpty()) {
            removeFromVariant(0);
        };
  }

  public void removeFromVariant(@NotNull ReferenceValue child) {
    int index = variant.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromVariant(index);;
  }

  public void removeFromVariant(int index) {
    if (variant.size() > index) {

            ReferenceValue removed = variant.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("variant"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + variant.size());
          }
  }

  public void setVariant(@NotNull List<? extends ReferenceValue> newValue) {
    clearVariant();
          for (ReferenceValue referenceValue : newValue) {
              addToVariant(referenceValue, variant.size());
          }
  }

  public int addToVariantMembership(ReferenceValue referenceValue, int index) {
    if (index > variantMembership.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("variantMembership"), index, referenceValue);
    }
    variantMembership.add(index, referenceValue);
    return variantMembership.size() - 1;
  }

  public List<ReferenceValue> getVariantMembership() {
    return variantMembership;
  }

  public int addToVariantMembership(VariantMembership referred) {
    return addToVariantMembership(new ReferenceValue(referred, null), variantMembership.size());
  }

  public int addToVariantMembership(VariantMembership referred, int index) {
    return addToVariantMembership(new ReferenceValue(referred, null), index);
  }

  public void clearVariantMembership() {
    while (!variantMembership.isEmpty()) {
            removeFromVariantMembership(0);
        };
  }

  public void removeFromVariantMembership(@NotNull ReferenceValue child) {
    int index = variantMembership.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromVariantMembership(index);;
  }

  public void removeFromVariantMembership(int index) {
    if (variantMembership.size() > index) {

            ReferenceValue removed = variantMembership.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("variantMembership"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + variantMembership.size());
          }
  }

  public void setVariantMembership(@NotNull List<? extends ReferenceValue> newValue) {
    clearVariantMembership();
          for (ReferenceValue referenceValue : newValue) {
              addToVariantMembership(referenceValue, variantMembership.size());
          }
  }

  public int addToUsage(ReferenceValue referenceValue, int index) {
    if (index > usage.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("usage"), index, referenceValue);
    }
    usage.add(index, referenceValue);
    return usage.size() - 1;
  }

  public List<ReferenceValue> getUsage() {
    return usage;
  }

  public int addToUsage(IUsage referred) {
    return addToUsage(new ReferenceValue(referred, null), usage.size());
  }

  public int addToUsage(IUsage referred, int index) {
    return addToUsage(new ReferenceValue(referred, null), index);
  }

  public void clearUsage() {
    while (!usage.isEmpty()) {
            removeFromUsage(0);
        };
  }

  public void removeFromUsage(@NotNull ReferenceValue child) {
    int index = usage.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromUsage(index);;
  }

  public void removeFromUsage(int index) {
    if (usage.size() > index) {

            ReferenceValue removed = usage.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("usage"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + usage.size());
          }
  }

  public void setUsage(@NotNull List<? extends ReferenceValue> newValue) {
    clearUsage();
          for (ReferenceValue referenceValue : newValue) {
              addToUsage(referenceValue, usage.size());
          }
  }

  public int addToDirectedUsage(ReferenceValue referenceValue, int index) {
    if (index > directedUsage.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("directedUsage"), index, referenceValue);
    }
    directedUsage.add(index, referenceValue);
    return directedUsage.size() - 1;
  }

  public List<ReferenceValue> getDirectedUsage() {
    return directedUsage;
  }

  public int addToDirectedUsage(IUsage referred) {
    return addToDirectedUsage(new ReferenceValue(referred, null), directedUsage.size());
  }

  public int addToDirectedUsage(IUsage referred, int index) {
    return addToDirectedUsage(new ReferenceValue(referred, null), index);
  }

  public void clearDirectedUsage() {
    while (!directedUsage.isEmpty()) {
            removeFromDirectedUsage(0);
        };
  }

  public void removeFromDirectedUsage(@NotNull ReferenceValue child) {
    int index = directedUsage.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromDirectedUsage(index);;
  }

  public void removeFromDirectedUsage(int index) {
    if (directedUsage.size() > index) {

            ReferenceValue removed = directedUsage.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("directedUsage"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + directedUsage.size());
          }
  }

  public void setDirectedUsage(@NotNull List<? extends ReferenceValue> newValue) {
    clearDirectedUsage();
          for (ReferenceValue referenceValue : newValue) {
              addToDirectedUsage(referenceValue, directedUsage.size());
          }
  }

  public int addToOwnedReference(ReferenceValue referenceValue, int index) {
    if (index > ownedReference.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedReference"), index, referenceValue);
    }
    ownedReference.add(index, referenceValue);
    return ownedReference.size() - 1;
  }

  public List<ReferenceValue> getOwnedReference() {
    return ownedReference;
  }

  public int addToOwnedReference(ReferenceUsage referred) {
    return addToOwnedReference(new ReferenceValue(referred, null), ownedReference.size());
  }

  public int addToOwnedReference(ReferenceUsage referred, int index) {
    return addToOwnedReference(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedReference() {
    while (!ownedReference.isEmpty()) {
            removeFromOwnedReference(0);
        };
  }

  public void removeFromOwnedReference(@NotNull ReferenceValue child) {
    int index = ownedReference.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedReference(index);;
  }

  public void removeFromOwnedReference(int index) {
    if (ownedReference.size() > index) {

            ReferenceValue removed = ownedReference.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedReference"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedReference.size());
          }
  }

  public void setOwnedReference(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedReference();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedReference(referenceValue, ownedReference.size());
          }
  }

  public int addToOwnedAttribute(ReferenceValue referenceValue, int index) {
    if (index > ownedAttribute.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedAttribute"), index, referenceValue);
    }
    ownedAttribute.add(index, referenceValue);
    return ownedAttribute.size() - 1;
  }

  public List<ReferenceValue> getOwnedAttribute() {
    return ownedAttribute;
  }

  public int addToOwnedAttribute(AttributeUsage referred) {
    return addToOwnedAttribute(new ReferenceValue(referred, null), ownedAttribute.size());
  }

  public int addToOwnedAttribute(AttributeUsage referred, int index) {
    return addToOwnedAttribute(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedAttribute() {
    while (!ownedAttribute.isEmpty()) {
            removeFromOwnedAttribute(0);
        };
  }

  public void removeFromOwnedAttribute(@NotNull ReferenceValue child) {
    int index = ownedAttribute.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedAttribute(index);;
  }

  public void removeFromOwnedAttribute(int index) {
    if (ownedAttribute.size() > index) {

            ReferenceValue removed = ownedAttribute.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedAttribute"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedAttribute.size());
          }
  }

  public void setOwnedAttribute(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedAttribute();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedAttribute(referenceValue, ownedAttribute.size());
          }
  }

  public int addToOwnedEnumeration(ReferenceValue referenceValue, int index) {
    if (index > ownedEnumeration.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedEnumeration"), index, referenceValue);
    }
    ownedEnumeration.add(index, referenceValue);
    return ownedEnumeration.size() - 1;
  }

  public List<ReferenceValue> getOwnedEnumeration() {
    return ownedEnumeration;
  }

  public int addToOwnedEnumeration(EnumerationUsage referred) {
    return addToOwnedEnumeration(new ReferenceValue(referred, null), ownedEnumeration.size());
  }

  public int addToOwnedEnumeration(EnumerationUsage referred, int index) {
    return addToOwnedEnumeration(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedEnumeration() {
    while (!ownedEnumeration.isEmpty()) {
            removeFromOwnedEnumeration(0);
        };
  }

  public void removeFromOwnedEnumeration(@NotNull ReferenceValue child) {
    int index = ownedEnumeration.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedEnumeration(index);;
  }

  public void removeFromOwnedEnumeration(int index) {
    if (ownedEnumeration.size() > index) {

            ReferenceValue removed = ownedEnumeration.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedEnumeration"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedEnumeration.size());
          }
  }

  public void setOwnedEnumeration(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedEnumeration();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedEnumeration(referenceValue, ownedEnumeration.size());
          }
  }

  public int addToOwnedOccurrence(ReferenceValue referenceValue, int index) {
    if (index > ownedOccurrence.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedOccurrence"), index, referenceValue);
    }
    ownedOccurrence.add(index, referenceValue);
    return ownedOccurrence.size() - 1;
  }

  public List<ReferenceValue> getOwnedOccurrence() {
    return ownedOccurrence;
  }

  public int addToOwnedOccurrence(IOccurrenceUsage referred) {
    return addToOwnedOccurrence(new ReferenceValue(referred, null), ownedOccurrence.size());
  }

  public int addToOwnedOccurrence(IOccurrenceUsage referred, int index) {
    return addToOwnedOccurrence(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedOccurrence() {
    while (!ownedOccurrence.isEmpty()) {
            removeFromOwnedOccurrence(0);
        };
  }

  public void removeFromOwnedOccurrence(@NotNull ReferenceValue child) {
    int index = ownedOccurrence.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedOccurrence(index);;
  }

  public void removeFromOwnedOccurrence(int index) {
    if (ownedOccurrence.size() > index) {

            ReferenceValue removed = ownedOccurrence.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedOccurrence"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedOccurrence.size());
          }
  }

  public void setOwnedOccurrence(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedOccurrence();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedOccurrence(referenceValue, ownedOccurrence.size());
          }
  }

  public int addToOwnedItem(ReferenceValue referenceValue, int index) {
    if (index > ownedItem.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedItem"), index, referenceValue);
    }
    ownedItem.add(index, referenceValue);
    return ownedItem.size() - 1;
  }

  public List<ReferenceValue> getOwnedItem() {
    return ownedItem;
  }

  public int addToOwnedItem(IItemUsage referred) {
    return addToOwnedItem(new ReferenceValue(referred, null), ownedItem.size());
  }

  public int addToOwnedItem(IItemUsage referred, int index) {
    return addToOwnedItem(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedItem() {
    while (!ownedItem.isEmpty()) {
            removeFromOwnedItem(0);
        };
  }

  public void removeFromOwnedItem(@NotNull ReferenceValue child) {
    int index = ownedItem.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedItem(index);;
  }

  public void removeFromOwnedItem(int index) {
    if (ownedItem.size() > index) {

            ReferenceValue removed = ownedItem.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedItem"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedItem.size());
          }
  }

  public void setOwnedItem(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedItem();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedItem(referenceValue, ownedItem.size());
          }
  }

  public int addToOwnedPart(ReferenceValue referenceValue, int index) {
    if (index > ownedPart.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedPart"), index, referenceValue);
    }
    ownedPart.add(index, referenceValue);
    return ownedPart.size() - 1;
  }

  public List<ReferenceValue> getOwnedPart() {
    return ownedPart;
  }

  public int addToOwnedPart(IPartUsage referred) {
    return addToOwnedPart(new ReferenceValue(referred, null), ownedPart.size());
  }

  public int addToOwnedPart(IPartUsage referred, int index) {
    return addToOwnedPart(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedPart() {
    while (!ownedPart.isEmpty()) {
            removeFromOwnedPart(0);
        };
  }

  public void removeFromOwnedPart(@NotNull ReferenceValue child) {
    int index = ownedPart.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedPart(index);;
  }

  public void removeFromOwnedPart(int index) {
    if (ownedPart.size() > index) {

            ReferenceValue removed = ownedPart.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedPart"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedPart.size());
          }
  }

  public void setOwnedPart(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedPart();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedPart(referenceValue, ownedPart.size());
          }
  }

  public int addToOwnedPort(ReferenceValue referenceValue, int index) {
    if (index > ownedPort.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedPort"), index, referenceValue);
    }
    ownedPort.add(index, referenceValue);
    return ownedPort.size() - 1;
  }

  public List<ReferenceValue> getOwnedPort() {
    return ownedPort;
  }

  public int addToOwnedPort(PortUsage referred) {
    return addToOwnedPort(new ReferenceValue(referred, null), ownedPort.size());
  }

  public int addToOwnedPort(PortUsage referred, int index) {
    return addToOwnedPort(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedPort() {
    while (!ownedPort.isEmpty()) {
            removeFromOwnedPort(0);
        };
  }

  public void removeFromOwnedPort(@NotNull ReferenceValue child) {
    int index = ownedPort.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedPort(index);;
  }

  public void removeFromOwnedPort(int index) {
    if (ownedPort.size() > index) {

            ReferenceValue removed = ownedPort.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedPort"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedPort.size());
          }
  }

  public void setOwnedPort(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedPort();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedPort(referenceValue, ownedPort.size());
          }
  }

  public int addToOwnedConnection(ReferenceValue referenceValue, int index) {
    if (index > ownedConnection.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedConnection"), index, referenceValue);
    }
    ownedConnection.add(index, referenceValue);
    return ownedConnection.size() - 1;
  }

  public List<ReferenceValue> getOwnedConnection() {
    return ownedConnection;
  }

  public int addToOwnedConnection(ConnectorAsUsage referred) {
    return addToOwnedConnection(new ReferenceValue(referred, null), ownedConnection.size());
  }

  public int addToOwnedConnection(ConnectorAsUsage referred, int index) {
    return addToOwnedConnection(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedConnection() {
    while (!ownedConnection.isEmpty()) {
            removeFromOwnedConnection(0);
        };
  }

  public void removeFromOwnedConnection(@NotNull ReferenceValue child) {
    int index = ownedConnection.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedConnection(index);;
  }

  public void removeFromOwnedConnection(int index) {
    if (ownedConnection.size() > index) {

            ReferenceValue removed = ownedConnection.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedConnection"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedConnection.size());
          }
  }

  public void setOwnedConnection(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedConnection();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedConnection(referenceValue, ownedConnection.size());
          }
  }

  public int addToOwnedFlow(ReferenceValue referenceValue, int index) {
    if (index > ownedFlow.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedFlow"), index, referenceValue);
    }
    ownedFlow.add(index, referenceValue);
    return ownedFlow.size() - 1;
  }

  public List<ReferenceValue> getOwnedFlow() {
    return ownedFlow;
  }

  public int addToOwnedFlow(FlowConnectionUsage referred) {
    return addToOwnedFlow(new ReferenceValue(referred, null), ownedFlow.size());
  }

  public int addToOwnedFlow(FlowConnectionUsage referred, int index) {
    return addToOwnedFlow(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedFlow() {
    while (!ownedFlow.isEmpty()) {
            removeFromOwnedFlow(0);
        };
  }

  public void removeFromOwnedFlow(@NotNull ReferenceValue child) {
    int index = ownedFlow.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedFlow(index);;
  }

  public void removeFromOwnedFlow(int index) {
    if (ownedFlow.size() > index) {

            ReferenceValue removed = ownedFlow.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedFlow"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedFlow.size());
          }
  }

  public void setOwnedFlow(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedFlow();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedFlow(referenceValue, ownedFlow.size());
          }
  }

  public int addToOwnedInterface(ReferenceValue referenceValue, int index) {
    if (index > ownedInterface.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedInterface"), index, referenceValue);
    }
    ownedInterface.add(index, referenceValue);
    return ownedInterface.size() - 1;
  }

  public List<ReferenceValue> getOwnedInterface() {
    return ownedInterface;
  }

  public int addToOwnedInterface(InterfaceUsage referred) {
    return addToOwnedInterface(new ReferenceValue(referred, null), ownedInterface.size());
  }

  public int addToOwnedInterface(InterfaceUsage referred, int index) {
    return addToOwnedInterface(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedInterface() {
    while (!ownedInterface.isEmpty()) {
            removeFromOwnedInterface(0);
        };
  }

  public void removeFromOwnedInterface(@NotNull ReferenceValue child) {
    int index = ownedInterface.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedInterface(index);;
  }

  public void removeFromOwnedInterface(int index) {
    if (ownedInterface.size() > index) {

            ReferenceValue removed = ownedInterface.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedInterface"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedInterface.size());
          }
  }

  public void setOwnedInterface(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedInterface();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedInterface(referenceValue, ownedInterface.size());
          }
  }

  public int addToOwnedAllocation(ReferenceValue referenceValue, int index) {
    if (index > ownedAllocation.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedAllocation"), index, referenceValue);
    }
    ownedAllocation.add(index, referenceValue);
    return ownedAllocation.size() - 1;
  }

  public List<ReferenceValue> getOwnedAllocation() {
    return ownedAllocation;
  }

  public int addToOwnedAllocation(AllocationUsage referred) {
    return addToOwnedAllocation(new ReferenceValue(referred, null), ownedAllocation.size());
  }

  public int addToOwnedAllocation(AllocationUsage referred, int index) {
    return addToOwnedAllocation(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedAllocation() {
    while (!ownedAllocation.isEmpty()) {
            removeFromOwnedAllocation(0);
        };
  }

  public void removeFromOwnedAllocation(@NotNull ReferenceValue child) {
    int index = ownedAllocation.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedAllocation(index);;
  }

  public void removeFromOwnedAllocation(int index) {
    if (ownedAllocation.size() > index) {

            ReferenceValue removed = ownedAllocation.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedAllocation"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedAllocation.size());
          }
  }

  public void setOwnedAllocation(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedAllocation();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedAllocation(referenceValue, ownedAllocation.size());
          }
  }

  public int addToOwnedAction(ReferenceValue referenceValue, int index) {
    if (index > ownedAction.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedAction"), index, referenceValue);
    }
    ownedAction.add(index, referenceValue);
    return ownedAction.size() - 1;
  }

  public List<ReferenceValue> getOwnedAction() {
    return ownedAction;
  }

  public int addToOwnedAction(IActionUsage referred) {
    return addToOwnedAction(new ReferenceValue(referred, null), ownedAction.size());
  }

  public int addToOwnedAction(IActionUsage referred, int index) {
    return addToOwnedAction(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedAction() {
    while (!ownedAction.isEmpty()) {
            removeFromOwnedAction(0);
        };
  }

  public void removeFromOwnedAction(@NotNull ReferenceValue child) {
    int index = ownedAction.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedAction(index);;
  }

  public void removeFromOwnedAction(int index) {
    if (ownedAction.size() > index) {

            ReferenceValue removed = ownedAction.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedAction"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedAction.size());
          }
  }

  public void setOwnedAction(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedAction();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedAction(referenceValue, ownedAction.size());
          }
  }

  public int addToOwnedState(ReferenceValue referenceValue, int index) {
    if (index > ownedState.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedState"), index, referenceValue);
    }
    ownedState.add(index, referenceValue);
    return ownedState.size() - 1;
  }

  public List<ReferenceValue> getOwnedState() {
    return ownedState;
  }

  public int addToOwnedState(StateUsage referred) {
    return addToOwnedState(new ReferenceValue(referred, null), ownedState.size());
  }

  public int addToOwnedState(StateUsage referred, int index) {
    return addToOwnedState(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedState() {
    while (!ownedState.isEmpty()) {
            removeFromOwnedState(0);
        };
  }

  public void removeFromOwnedState(@NotNull ReferenceValue child) {
    int index = ownedState.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedState(index);;
  }

  public void removeFromOwnedState(int index) {
    if (ownedState.size() > index) {

            ReferenceValue removed = ownedState.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedState"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedState.size());
          }
  }

  public void setOwnedState(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedState();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedState(referenceValue, ownedState.size());
          }
  }

  public int addToOwnedTransition(ReferenceValue referenceValue, int index) {
    if (index > ownedTransition.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedTransition"), index, referenceValue);
    }
    ownedTransition.add(index, referenceValue);
    return ownedTransition.size() - 1;
  }

  public List<ReferenceValue> getOwnedTransition() {
    return ownedTransition;
  }

  public int addToOwnedTransition(TransitionUsage referred) {
    return addToOwnedTransition(new ReferenceValue(referred, null), ownedTransition.size());
  }

  public int addToOwnedTransition(TransitionUsage referred, int index) {
    return addToOwnedTransition(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedTransition() {
    while (!ownedTransition.isEmpty()) {
            removeFromOwnedTransition(0);
        };
  }

  public void removeFromOwnedTransition(@NotNull ReferenceValue child) {
    int index = ownedTransition.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedTransition(index);;
  }

  public void removeFromOwnedTransition(int index) {
    if (ownedTransition.size() > index) {

            ReferenceValue removed = ownedTransition.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedTransition"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedTransition.size());
          }
  }

  public void setOwnedTransition(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedTransition();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedTransition(referenceValue, ownedTransition.size());
          }
  }

  public int addToOwnedCalculation(ReferenceValue referenceValue, int index) {
    if (index > ownedCalculation.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedCalculation"), index, referenceValue);
    }
    ownedCalculation.add(index, referenceValue);
    return ownedCalculation.size() - 1;
  }

  public List<ReferenceValue> getOwnedCalculation() {
    return ownedCalculation;
  }

  public int addToOwnedCalculation(CalculationUsage referred) {
    return addToOwnedCalculation(new ReferenceValue(referred, null), ownedCalculation.size());
  }

  public int addToOwnedCalculation(CalculationUsage referred, int index) {
    return addToOwnedCalculation(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedCalculation() {
    while (!ownedCalculation.isEmpty()) {
            removeFromOwnedCalculation(0);
        };
  }

  public void removeFromOwnedCalculation(@NotNull ReferenceValue child) {
    int index = ownedCalculation.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedCalculation(index);;
  }

  public void removeFromOwnedCalculation(int index) {
    if (ownedCalculation.size() > index) {

            ReferenceValue removed = ownedCalculation.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedCalculation"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedCalculation.size());
          }
  }

  public void setOwnedCalculation(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedCalculation();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedCalculation(referenceValue, ownedCalculation.size());
          }
  }

  public int addToOwnedConstraint(ReferenceValue referenceValue, int index) {
    if (index > ownedConstraint.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedConstraint"), index, referenceValue);
    }
    ownedConstraint.add(index, referenceValue);
    return ownedConstraint.size() - 1;
  }

  public List<ReferenceValue> getOwnedConstraint() {
    return ownedConstraint;
  }

  public int addToOwnedConstraint(IConstraintUsage referred) {
    return addToOwnedConstraint(new ReferenceValue(referred, null), ownedConstraint.size());
  }

  public int addToOwnedConstraint(IConstraintUsage referred, int index) {
    return addToOwnedConstraint(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedConstraint() {
    while (!ownedConstraint.isEmpty()) {
            removeFromOwnedConstraint(0);
        };
  }

  public void removeFromOwnedConstraint(@NotNull ReferenceValue child) {
    int index = ownedConstraint.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedConstraint(index);;
  }

  public void removeFromOwnedConstraint(int index) {
    if (ownedConstraint.size() > index) {

            ReferenceValue removed = ownedConstraint.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedConstraint"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedConstraint.size());
          }
  }

  public void setOwnedConstraint(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedConstraint();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedConstraint(referenceValue, ownedConstraint.size());
          }
  }

  public int addToOwnedRequirement(ReferenceValue referenceValue, int index) {
    if (index > ownedRequirement.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedRequirement"), index, referenceValue);
    }
    ownedRequirement.add(index, referenceValue);
    return ownedRequirement.size() - 1;
  }

  public List<ReferenceValue> getOwnedRequirement() {
    return ownedRequirement;
  }

  public int addToOwnedRequirement(RequirementUsage referred) {
    return addToOwnedRequirement(new ReferenceValue(referred, null), ownedRequirement.size());
  }

  public int addToOwnedRequirement(RequirementUsage referred, int index) {
    return addToOwnedRequirement(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedRequirement() {
    while (!ownedRequirement.isEmpty()) {
            removeFromOwnedRequirement(0);
        };
  }

  public void removeFromOwnedRequirement(@NotNull ReferenceValue child) {
    int index = ownedRequirement.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedRequirement(index);;
  }

  public void removeFromOwnedRequirement(int index) {
    if (ownedRequirement.size() > index) {

            ReferenceValue removed = ownedRequirement.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedRequirement"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedRequirement.size());
          }
  }

  public void setOwnedRequirement(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedRequirement();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedRequirement(referenceValue, ownedRequirement.size());
          }
  }

  public int addToOwnedConcern(ReferenceValue referenceValue, int index) {
    if (index > ownedConcern.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedConcern"), index, referenceValue);
    }
    ownedConcern.add(index, referenceValue);
    return ownedConcern.size() - 1;
  }

  public List<ReferenceValue> getOwnedConcern() {
    return ownedConcern;
  }

  public int addToOwnedConcern(ConcernUsage referred) {
    return addToOwnedConcern(new ReferenceValue(referred, null), ownedConcern.size());
  }

  public int addToOwnedConcern(ConcernUsage referred, int index) {
    return addToOwnedConcern(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedConcern() {
    while (!ownedConcern.isEmpty()) {
            removeFromOwnedConcern(0);
        };
  }

  public void removeFromOwnedConcern(@NotNull ReferenceValue child) {
    int index = ownedConcern.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedConcern(index);;
  }

  public void removeFromOwnedConcern(int index) {
    if (ownedConcern.size() > index) {

            ReferenceValue removed = ownedConcern.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedConcern"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedConcern.size());
          }
  }

  public void setOwnedConcern(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedConcern();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedConcern(referenceValue, ownedConcern.size());
          }
  }

  public int addToOwnedCase(ReferenceValue referenceValue, int index) {
    if (index > ownedCase.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedCase"), index, referenceValue);
    }
    ownedCase.add(index, referenceValue);
    return ownedCase.size() - 1;
  }

  public List<ReferenceValue> getOwnedCase() {
    return ownedCase;
  }

  public int addToOwnedCase(CaseUsage referred) {
    return addToOwnedCase(new ReferenceValue(referred, null), ownedCase.size());
  }

  public int addToOwnedCase(CaseUsage referred, int index) {
    return addToOwnedCase(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedCase() {
    while (!ownedCase.isEmpty()) {
            removeFromOwnedCase(0);
        };
  }

  public void removeFromOwnedCase(@NotNull ReferenceValue child) {
    int index = ownedCase.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedCase(index);;
  }

  public void removeFromOwnedCase(int index) {
    if (ownedCase.size() > index) {

            ReferenceValue removed = ownedCase.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedCase"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedCase.size());
          }
  }

  public void setOwnedCase(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedCase();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedCase(referenceValue, ownedCase.size());
          }
  }

  public int addToOwnedAnalysisCase(ReferenceValue referenceValue, int index) {
    if (index > ownedAnalysisCase.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedAnalysisCase"), index, referenceValue);
    }
    ownedAnalysisCase.add(index, referenceValue);
    return ownedAnalysisCase.size() - 1;
  }

  public List<ReferenceValue> getOwnedAnalysisCase() {
    return ownedAnalysisCase;
  }

  public int addToOwnedAnalysisCase(AnalysisCaseUsage referred) {
    return addToOwnedAnalysisCase(new ReferenceValue(referred, null), ownedAnalysisCase.size());
  }

  public int addToOwnedAnalysisCase(AnalysisCaseUsage referred, int index) {
    return addToOwnedAnalysisCase(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedAnalysisCase() {
    while (!ownedAnalysisCase.isEmpty()) {
            removeFromOwnedAnalysisCase(0);
        };
  }

  public void removeFromOwnedAnalysisCase(@NotNull ReferenceValue child) {
    int index = ownedAnalysisCase.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedAnalysisCase(index);;
  }

  public void removeFromOwnedAnalysisCase(int index) {
    if (ownedAnalysisCase.size() > index) {

            ReferenceValue removed = ownedAnalysisCase.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedAnalysisCase"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedAnalysisCase.size());
          }
  }

  public void setOwnedAnalysisCase(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedAnalysisCase();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedAnalysisCase(referenceValue, ownedAnalysisCase.size());
          }
  }

  public int addToOwnedVerificationCase(ReferenceValue referenceValue, int index) {
    if (index > ownedVerificationCase.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedVerificationCase"), index, referenceValue);
    }
    ownedVerificationCase.add(index, referenceValue);
    return ownedVerificationCase.size() - 1;
  }

  public List<ReferenceValue> getOwnedVerificationCase() {
    return ownedVerificationCase;
  }

  public int addToOwnedVerificationCase(VerificationCaseUsage referred) {
    return addToOwnedVerificationCase(new ReferenceValue(referred, null), ownedVerificationCase.size());
  }

  public int addToOwnedVerificationCase(VerificationCaseUsage referred, int index) {
    return addToOwnedVerificationCase(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedVerificationCase() {
    while (!ownedVerificationCase.isEmpty()) {
            removeFromOwnedVerificationCase(0);
        };
  }

  public void removeFromOwnedVerificationCase(@NotNull ReferenceValue child) {
    int index = ownedVerificationCase.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedVerificationCase(index);;
  }

  public void removeFromOwnedVerificationCase(int index) {
    if (ownedVerificationCase.size() > index) {

            ReferenceValue removed = ownedVerificationCase.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedVerificationCase"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedVerificationCase.size());
          }
  }

  public void setOwnedVerificationCase(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedVerificationCase();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedVerificationCase(referenceValue, ownedVerificationCase.size());
          }
  }

  public int addToOwnedUseCase(ReferenceValue referenceValue, int index) {
    if (index > ownedUseCase.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedUseCase"), index, referenceValue);
    }
    ownedUseCase.add(index, referenceValue);
    return ownedUseCase.size() - 1;
  }

  public List<ReferenceValue> getOwnedUseCase() {
    return ownedUseCase;
  }

  public int addToOwnedUseCase(UseCaseUsage referred) {
    return addToOwnedUseCase(new ReferenceValue(referred, null), ownedUseCase.size());
  }

  public int addToOwnedUseCase(UseCaseUsage referred, int index) {
    return addToOwnedUseCase(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedUseCase() {
    while (!ownedUseCase.isEmpty()) {
            removeFromOwnedUseCase(0);
        };
  }

  public void removeFromOwnedUseCase(@NotNull ReferenceValue child) {
    int index = ownedUseCase.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedUseCase(index);;
  }

  public void removeFromOwnedUseCase(int index) {
    if (ownedUseCase.size() > index) {

            ReferenceValue removed = ownedUseCase.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedUseCase"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedUseCase.size());
          }
  }

  public void setOwnedUseCase(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedUseCase();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedUseCase(referenceValue, ownedUseCase.size());
          }
  }

  public int addToOwnedView(ReferenceValue referenceValue, int index) {
    if (index > ownedView.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedView"), index, referenceValue);
    }
    ownedView.add(index, referenceValue);
    return ownedView.size() - 1;
  }

  public List<ReferenceValue> getOwnedView() {
    return ownedView;
  }

  public int addToOwnedView(ViewUsage referred) {
    return addToOwnedView(new ReferenceValue(referred, null), ownedView.size());
  }

  public int addToOwnedView(ViewUsage referred, int index) {
    return addToOwnedView(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedView() {
    while (!ownedView.isEmpty()) {
            removeFromOwnedView(0);
        };
  }

  public void removeFromOwnedView(@NotNull ReferenceValue child) {
    int index = ownedView.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedView(index);;
  }

  public void removeFromOwnedView(int index) {
    if (ownedView.size() > index) {

            ReferenceValue removed = ownedView.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedView"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedView.size());
          }
  }

  public void setOwnedView(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedView();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedView(referenceValue, ownedView.size());
          }
  }

  public int addToOwnedViewpoint(ReferenceValue referenceValue, int index) {
    if (index > ownedViewpoint.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedViewpoint"), index, referenceValue);
    }
    ownedViewpoint.add(index, referenceValue);
    return ownedViewpoint.size() - 1;
  }

  public List<ReferenceValue> getOwnedViewpoint() {
    return ownedViewpoint;
  }

  public int addToOwnedViewpoint(ViewpointUsage referred) {
    return addToOwnedViewpoint(new ReferenceValue(referred, null), ownedViewpoint.size());
  }

  public int addToOwnedViewpoint(ViewpointUsage referred, int index) {
    return addToOwnedViewpoint(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedViewpoint() {
    while (!ownedViewpoint.isEmpty()) {
            removeFromOwnedViewpoint(0);
        };
  }

  public void removeFromOwnedViewpoint(@NotNull ReferenceValue child) {
    int index = ownedViewpoint.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedViewpoint(index);;
  }

  public void removeFromOwnedViewpoint(int index) {
    if (ownedViewpoint.size() > index) {

            ReferenceValue removed = ownedViewpoint.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedViewpoint"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedViewpoint.size());
          }
  }

  public void setOwnedViewpoint(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedViewpoint();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedViewpoint(referenceValue, ownedViewpoint.size());
          }
  }

  public int addToOwnedRendering(ReferenceValue referenceValue, int index) {
    if (index > ownedRendering.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedRendering"), index, referenceValue);
    }
    ownedRendering.add(index, referenceValue);
    return ownedRendering.size() - 1;
  }

  public List<ReferenceValue> getOwnedRendering() {
    return ownedRendering;
  }

  public int addToOwnedRendering(RenderingUsage referred) {
    return addToOwnedRendering(new ReferenceValue(referred, null), ownedRendering.size());
  }

  public int addToOwnedRendering(RenderingUsage referred, int index) {
    return addToOwnedRendering(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedRendering() {
    while (!ownedRendering.isEmpty()) {
            removeFromOwnedRendering(0);
        };
  }

  public void removeFromOwnedRendering(@NotNull ReferenceValue child) {
    int index = ownedRendering.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedRendering(index);;
  }

  public void removeFromOwnedRendering(int index) {
    if (ownedRendering.size() > index) {

            ReferenceValue removed = ownedRendering.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedRendering"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedRendering.size());
          }
  }

  public void setOwnedRendering(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedRendering();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedRendering(referenceValue, ownedRendering.size());
          }
  }

  public int addToOwnedMetadata(ReferenceValue referenceValue, int index) {
    if (index > ownedMetadata.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedMetadata"), index, referenceValue);
    }
    ownedMetadata.add(index, referenceValue);
    return ownedMetadata.size() - 1;
  }

  public List<ReferenceValue> getOwnedMetadata() {
    return ownedMetadata;
  }

  public int addToOwnedMetadata(MetadataUsage referred) {
    return addToOwnedMetadata(new ReferenceValue(referred, null), ownedMetadata.size());
  }

  public int addToOwnedMetadata(MetadataUsage referred, int index) {
    return addToOwnedMetadata(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedMetadata() {
    while (!ownedMetadata.isEmpty()) {
            removeFromOwnedMetadata(0);
        };
  }

  public void removeFromOwnedMetadata(@NotNull ReferenceValue child) {
    int index = ownedMetadata.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedMetadata(index);;
  }

  public void removeFromOwnedMetadata(int index) {
    if (ownedMetadata.size() > index) {

            ReferenceValue removed = ownedMetadata.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedMetadata"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedMetadata.size());
          }
  }

  public void setOwnedMetadata(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedMetadata();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedMetadata(referenceValue, ownedMetadata.size());
          }
  }

  public int addToOwnedUsage(ReferenceValue referenceValue, int index) {
    if (index > ownedUsage.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedUsage"), index, referenceValue);
    }
    ownedUsage.add(index, referenceValue);
    return ownedUsage.size() - 1;
  }

  public List<ReferenceValue> getOwnedUsage() {
    return ownedUsage;
  }

  public int addToOwnedUsage(IUsage referred) {
    return addToOwnedUsage(new ReferenceValue(referred, null), ownedUsage.size());
  }

  public int addToOwnedUsage(IUsage referred, int index) {
    return addToOwnedUsage(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedUsage() {
    while (!ownedUsage.isEmpty()) {
            removeFromOwnedUsage(0);
        };
  }

  public void removeFromOwnedUsage(@NotNull ReferenceValue child) {
    int index = ownedUsage.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedUsage(index);;
  }

  public void removeFromOwnedUsage(int index) {
    if (ownedUsage.size() > index) {

            ReferenceValue removed = ownedUsage.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedUsage"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedUsage.size());
          }
  }

  public void setOwnedUsage(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedUsage();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedUsage(referenceValue, ownedUsage.size());
          }
  }

  public int addToOwnedSubclassification(ReferenceValue referenceValue, int index) {
    if (index > ownedSubclassification.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedSubclassification"), index, referenceValue);
    }
    ownedSubclassification.add(index, referenceValue);
    return ownedSubclassification.size() - 1;
  }

  public List<ReferenceValue> getOwnedSubclassification() {
    return ownedSubclassification;
  }

  public int addToOwnedSubclassification(Subclassification referred) {
    return addToOwnedSubclassification(new ReferenceValue(referred, null), ownedSubclassification.size());
  }

  public int addToOwnedSubclassification(Subclassification referred, int index) {
    return addToOwnedSubclassification(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedSubclassification() {
    while (!ownedSubclassification.isEmpty()) {
            removeFromOwnedSubclassification(0);
        };
  }

  public void removeFromOwnedSubclassification(@NotNull ReferenceValue child) {
    int index = ownedSubclassification.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedSubclassification(index);;
  }

  public void removeFromOwnedSubclassification(int index) {
    if (ownedSubclassification.size() > index) {

            ReferenceValue removed = ownedSubclassification.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedSubclassification"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedSubclassification.size());
          }
  }

  public void setOwnedSubclassification(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedSubclassification();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedSubclassification(referenceValue, ownedSubclassification.size());
          }
  }

  public int addToOwnedFeatureMembership(ReferenceValue referenceValue, int index) {
    if (index > ownedFeatureMembership.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedFeatureMembership"), index, referenceValue);
    }
    ownedFeatureMembership.add(index, referenceValue);
    return ownedFeatureMembership.size() - 1;
  }

  public List<ReferenceValue> getOwnedFeatureMembership() {
    return ownedFeatureMembership;
  }

  public int addToOwnedFeatureMembership(FeatureMembership referred) {
    return addToOwnedFeatureMembership(new ReferenceValue(referred, null), ownedFeatureMembership.size());
  }

  public int addToOwnedFeatureMembership(FeatureMembership referred, int index) {
    return addToOwnedFeatureMembership(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedFeatureMembership() {
    while (!ownedFeatureMembership.isEmpty()) {
            removeFromOwnedFeatureMembership(0);
        };
  }

  public void removeFromOwnedFeatureMembership(@NotNull ReferenceValue child) {
    int index = ownedFeatureMembership.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedFeatureMembership(index);;
  }

  public void removeFromOwnedFeatureMembership(int index) {
    if (ownedFeatureMembership.size() > index) {

            ReferenceValue removed = ownedFeatureMembership.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedFeatureMembership"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedFeatureMembership.size());
          }
  }

  public void setOwnedFeatureMembership(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedFeatureMembership();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedFeatureMembership(referenceValue, ownedFeatureMembership.size());
          }
  }

  public int addToOwnedFeature(ReferenceValue referenceValue, int index) {
    if (index > ownedFeature.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedFeature"), index, referenceValue);
    }
    ownedFeature.add(index, referenceValue);
    return ownedFeature.size() - 1;
  }

  public List<ReferenceValue> getOwnedFeature() {
    return ownedFeature;
  }

  public int addToOwnedFeature(IFeature referred) {
    return addToOwnedFeature(new ReferenceValue(referred, null), ownedFeature.size());
  }

  public int addToOwnedFeature(IFeature referred, int index) {
    return addToOwnedFeature(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedFeature() {
    while (!ownedFeature.isEmpty()) {
            removeFromOwnedFeature(0);
        };
  }

  public void removeFromOwnedFeature(@NotNull ReferenceValue child) {
    int index = ownedFeature.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedFeature(index);;
  }

  public void removeFromOwnedFeature(int index) {
    if (ownedFeature.size() > index) {

            ReferenceValue removed = ownedFeature.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedFeature"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedFeature.size());
          }
  }

  public void setOwnedFeature(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedFeature();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedFeature(referenceValue, ownedFeature.size());
          }
  }

  public int addToOwnedEndFeature(ReferenceValue referenceValue, int index) {
    if (index > ownedEndFeature.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedEndFeature"), index, referenceValue);
    }
    ownedEndFeature.add(index, referenceValue);
    return ownedEndFeature.size() - 1;
  }

  public List<ReferenceValue> getOwnedEndFeature() {
    return ownedEndFeature;
  }

  public int addToOwnedEndFeature(IFeature referred) {
    return addToOwnedEndFeature(new ReferenceValue(referred, null), ownedEndFeature.size());
  }

  public int addToOwnedEndFeature(IFeature referred, int index) {
    return addToOwnedEndFeature(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedEndFeature() {
    while (!ownedEndFeature.isEmpty()) {
            removeFromOwnedEndFeature(0);
        };
  }

  public void removeFromOwnedEndFeature(@NotNull ReferenceValue child) {
    int index = ownedEndFeature.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedEndFeature(index);;
  }

  public void removeFromOwnedEndFeature(int index) {
    if (ownedEndFeature.size() > index) {

            ReferenceValue removed = ownedEndFeature.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedEndFeature"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedEndFeature.size());
          }
  }

  public void setOwnedEndFeature(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedEndFeature();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedEndFeature(referenceValue, ownedEndFeature.size());
          }
  }

  public int addToFeature(ReferenceValue referenceValue, int index) {
    if (index > feature.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("feature"), index, referenceValue);
    }
    feature.add(index, referenceValue);
    return feature.size() - 1;
  }

  public List<ReferenceValue> getFeature() {
    return feature;
  }

  public int addToFeature(IFeature referred) {
    return addToFeature(new ReferenceValue(referred, null), feature.size());
  }

  public int addToFeature(IFeature referred, int index) {
    return addToFeature(new ReferenceValue(referred, null), index);
  }

  public void clearFeature() {
    while (!feature.isEmpty()) {
            removeFromFeature(0);
        };
  }

  public void removeFromFeature(@NotNull ReferenceValue child) {
    int index = feature.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromFeature(index);;
  }

  public void removeFromFeature(int index) {
    if (feature.size() > index) {

            ReferenceValue removed = feature.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("feature"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + feature.size());
          }
  }

  public void setFeature(@NotNull List<? extends ReferenceValue> newValue) {
    clearFeature();
          for (ReferenceValue referenceValue : newValue) {
              addToFeature(referenceValue, feature.size());
          }
  }

  public int addToInput(ReferenceValue referenceValue, int index) {
    if (index > input.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("input"), index, referenceValue);
    }
    input.add(index, referenceValue);
    return input.size() - 1;
  }

  public List<ReferenceValue> getInput() {
    return input;
  }

  public int addToInput(IFeature referred) {
    return addToInput(new ReferenceValue(referred, null), input.size());
  }

  public int addToInput(IFeature referred, int index) {
    return addToInput(new ReferenceValue(referred, null), index);
  }

  public void clearInput() {
    while (!input.isEmpty()) {
            removeFromInput(0);
        };
  }

  public void removeFromInput(@NotNull ReferenceValue child) {
    int index = input.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromInput(index);;
  }

  public void removeFromInput(int index) {
    if (input.size() > index) {

            ReferenceValue removed = input.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("input"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + input.size());
          }
  }

  public void setInput(@NotNull List<? extends ReferenceValue> newValue) {
    clearInput();
          for (ReferenceValue referenceValue : newValue) {
              addToInput(referenceValue, input.size());
          }
  }

  public int addToOutput(ReferenceValue referenceValue, int index) {
    if (index > output.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("output"), index, referenceValue);
    }
    output.add(index, referenceValue);
    return output.size() - 1;
  }

  public List<ReferenceValue> getOutput() {
    return output;
  }

  public int addToOutput(IFeature referred) {
    return addToOutput(new ReferenceValue(referred, null), output.size());
  }

  public int addToOutput(IFeature referred, int index) {
    return addToOutput(new ReferenceValue(referred, null), index);
  }

  public void clearOutput() {
    while (!output.isEmpty()) {
            removeFromOutput(0);
        };
  }

  public void removeFromOutput(@NotNull ReferenceValue child) {
    int index = output.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOutput(index);;
  }

  public void removeFromOutput(int index) {
    if (output.size() > index) {

            ReferenceValue removed = output.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("output"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + output.size());
          }
  }

  public void setOutput(@NotNull List<? extends ReferenceValue> newValue) {
    clearOutput();
          for (ReferenceValue referenceValue : newValue) {
              addToOutput(referenceValue, output.size());
          }
  }

  public Boolean getIsAbstract() {
    return isAbstract;
  }

  public void setIsAbstract(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isAbstract"), getIsAbstract(), value);
        }
    this.isAbstract = value;
  }

  public int addToInheritedMembership(ReferenceValue referenceValue, int index) {
    if (index > inheritedMembership.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("inheritedMembership"), index, referenceValue);
    }
    inheritedMembership.add(index, referenceValue);
    return inheritedMembership.size() - 1;
  }

  public List<ReferenceValue> getInheritedMembership() {
    return inheritedMembership;
  }

  public int addToInheritedMembership(Membership referred) {
    return addToInheritedMembership(new ReferenceValue(referred, null), inheritedMembership.size());
  }

  public int addToInheritedMembership(Membership referred, int index) {
    return addToInheritedMembership(new ReferenceValue(referred, null), index);
  }

  public void clearInheritedMembership() {
    while (!inheritedMembership.isEmpty()) {
            removeFromInheritedMembership(0);
        };
  }

  public void removeFromInheritedMembership(@NotNull ReferenceValue child) {
    int index = inheritedMembership.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromInheritedMembership(index);;
  }

  public void removeFromInheritedMembership(int index) {
    if (inheritedMembership.size() > index) {

            ReferenceValue removed = inheritedMembership.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("inheritedMembership"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + inheritedMembership.size());
          }
  }

  public void setInheritedMembership(@NotNull List<? extends ReferenceValue> newValue) {
    clearInheritedMembership();
          for (ReferenceValue referenceValue : newValue) {
              addToInheritedMembership(referenceValue, inheritedMembership.size());
          }
  }

  public int addToEndFeature(ReferenceValue referenceValue, int index) {
    if (index > endFeature.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("endFeature"), index, referenceValue);
    }
    endFeature.add(index, referenceValue);
    return endFeature.size() - 1;
  }

  public List<ReferenceValue> getEndFeature() {
    return endFeature;
  }

  public int addToEndFeature(IFeature referred) {
    return addToEndFeature(new ReferenceValue(referred, null), endFeature.size());
  }

  public int addToEndFeature(IFeature referred, int index) {
    return addToEndFeature(new ReferenceValue(referred, null), index);
  }

  public void clearEndFeature() {
    while (!endFeature.isEmpty()) {
            removeFromEndFeature(0);
        };
  }

  public void removeFromEndFeature(@NotNull ReferenceValue child) {
    int index = endFeature.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromEndFeature(index);;
  }

  public void removeFromEndFeature(int index) {
    if (endFeature.size() > index) {

            ReferenceValue removed = endFeature.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("endFeature"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + endFeature.size());
          }
  }

  public void setEndFeature(@NotNull List<? extends ReferenceValue> newValue) {
    clearEndFeature();
          for (ReferenceValue referenceValue : newValue) {
              addToEndFeature(referenceValue, endFeature.size());
          }
  }

  public Boolean getIsSufficient() {
    return isSufficient;
  }

  public void setIsSufficient(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isSufficient"), getIsSufficient(), value);
        }
    this.isSufficient = value;
  }

  public void setOwnedConjugator(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("ownedConjugator"), 0, ownedConjugator);
      }
      ownedConjugator = null;
    } else {
      if (partitionObserverCache != null) {
        if (ownedConjugator != null) {
          ReferenceValue oldValue = ownedConjugator;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("ownedConjugator"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedConjugator"), 0, value);
        }
      }
      this.ownedConjugator = value;
    }
  }

  public ReferenceValue getOwnedConjugator() {
    return ownedConjugator;
  }

  public Boolean getIsConjugated() {
    return isConjugated;
  }

  public void setIsConjugated(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isConjugated"), getIsConjugated(), value);
        }
    this.isConjugated = value;
  }

  public int addToInheritedFeature(ReferenceValue referenceValue, int index) {
    if (index > inheritedFeature.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("inheritedFeature"), index, referenceValue);
    }
    inheritedFeature.add(index, referenceValue);
    return inheritedFeature.size() - 1;
  }

  public List<ReferenceValue> getInheritedFeature() {
    return inheritedFeature;
  }

  public int addToInheritedFeature(IFeature referred) {
    return addToInheritedFeature(new ReferenceValue(referred, null), inheritedFeature.size());
  }

  public int addToInheritedFeature(IFeature referred, int index) {
    return addToInheritedFeature(new ReferenceValue(referred, null), index);
  }

  public void clearInheritedFeature() {
    while (!inheritedFeature.isEmpty()) {
            removeFromInheritedFeature(0);
        };
  }

  public void removeFromInheritedFeature(@NotNull ReferenceValue child) {
    int index = inheritedFeature.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromInheritedFeature(index);;
  }

  public void removeFromInheritedFeature(int index) {
    if (inheritedFeature.size() > index) {

            ReferenceValue removed = inheritedFeature.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("inheritedFeature"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + inheritedFeature.size());
          }
  }

  public void setInheritedFeature(@NotNull List<? extends ReferenceValue> newValue) {
    clearInheritedFeature();
          for (ReferenceValue referenceValue : newValue) {
              addToInheritedFeature(referenceValue, inheritedFeature.size());
          }
  }

  public void setMultiplicity(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("multiplicity"), 0, multiplicity);
      }
      multiplicity = null;
    } else {
      if (partitionObserverCache != null) {
        if (multiplicity != null) {
          ReferenceValue oldValue = multiplicity;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("multiplicity"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("multiplicity"), 0, value);
        }
      }
      this.multiplicity = value;
    }
  }

  public ReferenceValue getMultiplicity() {
    return multiplicity;
  }

  public int addToUnioningType(ReferenceValue referenceValue, int index) {
    if (index > unioningType.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("unioningType"), index, referenceValue);
    }
    unioningType.add(index, referenceValue);
    return unioningType.size() - 1;
  }

  public List<ReferenceValue> getUnioningType() {
    return unioningType;
  }

  public int addToUnioningType(IType referred) {
    return addToUnioningType(new ReferenceValue(referred, null), unioningType.size());
  }

  public int addToUnioningType(IType referred, int index) {
    return addToUnioningType(new ReferenceValue(referred, null), index);
  }

  public void clearUnioningType() {
    while (!unioningType.isEmpty()) {
            removeFromUnioningType(0);
        };
  }

  public void removeFromUnioningType(@NotNull ReferenceValue child) {
    int index = unioningType.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromUnioningType(index);;
  }

  public void removeFromUnioningType(int index) {
    if (unioningType.size() > index) {

            ReferenceValue removed = unioningType.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("unioningType"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + unioningType.size());
          }
  }

  public void setUnioningType(@NotNull List<? extends ReferenceValue> newValue) {
    clearUnioningType();
          for (ReferenceValue referenceValue : newValue) {
              addToUnioningType(referenceValue, unioningType.size());
          }
  }

  public int addToOwnedIntersecting(ReferenceValue referenceValue, int index) {
    if (index > ownedIntersecting.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedIntersecting"), index, referenceValue);
    }
    ownedIntersecting.add(index, referenceValue);
    return ownedIntersecting.size() - 1;
  }

  public List<ReferenceValue> getOwnedIntersecting() {
    return ownedIntersecting;
  }

  public int addToOwnedIntersecting(Intersecting referred) {
    return addToOwnedIntersecting(new ReferenceValue(referred, null), ownedIntersecting.size());
  }

  public int addToOwnedIntersecting(Intersecting referred, int index) {
    return addToOwnedIntersecting(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedIntersecting() {
    while (!ownedIntersecting.isEmpty()) {
            removeFromOwnedIntersecting(0);
        };
  }

  public void removeFromOwnedIntersecting(@NotNull ReferenceValue child) {
    int index = ownedIntersecting.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedIntersecting(index);;
  }

  public void removeFromOwnedIntersecting(int index) {
    if (ownedIntersecting.size() > index) {

            ReferenceValue removed = ownedIntersecting.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedIntersecting"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedIntersecting.size());
          }
  }

  public void setOwnedIntersecting(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedIntersecting();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedIntersecting(referenceValue, ownedIntersecting.size());
          }
  }

  public int addToIntersectingType(ReferenceValue referenceValue, int index) {
    if (index > intersectingType.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("intersectingType"), index, referenceValue);
    }
    intersectingType.add(index, referenceValue);
    return intersectingType.size() - 1;
  }

  public List<ReferenceValue> getIntersectingType() {
    return intersectingType;
  }

  public int addToIntersectingType(IType referred) {
    return addToIntersectingType(new ReferenceValue(referred, null), intersectingType.size());
  }

  public int addToIntersectingType(IType referred, int index) {
    return addToIntersectingType(new ReferenceValue(referred, null), index);
  }

  public void clearIntersectingType() {
    while (!intersectingType.isEmpty()) {
            removeFromIntersectingType(0);
        };
  }

  public void removeFromIntersectingType(@NotNull ReferenceValue child) {
    int index = intersectingType.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromIntersectingType(index);;
  }

  public void removeFromIntersectingType(int index) {
    if (intersectingType.size() > index) {

            ReferenceValue removed = intersectingType.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("intersectingType"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + intersectingType.size());
          }
  }

  public void setIntersectingType(@NotNull List<? extends ReferenceValue> newValue) {
    clearIntersectingType();
          for (ReferenceValue referenceValue : newValue) {
              addToIntersectingType(referenceValue, intersectingType.size());
          }
  }

  public int addToOwnedUnioning(ReferenceValue referenceValue, int index) {
    if (index > ownedUnioning.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedUnioning"), index, referenceValue);
    }
    ownedUnioning.add(index, referenceValue);
    return ownedUnioning.size() - 1;
  }

  public List<ReferenceValue> getOwnedUnioning() {
    return ownedUnioning;
  }

  public int addToOwnedUnioning(Unioning referred) {
    return addToOwnedUnioning(new ReferenceValue(referred, null), ownedUnioning.size());
  }

  public int addToOwnedUnioning(Unioning referred, int index) {
    return addToOwnedUnioning(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedUnioning() {
    while (!ownedUnioning.isEmpty()) {
            removeFromOwnedUnioning(0);
        };
  }

  public void removeFromOwnedUnioning(@NotNull ReferenceValue child) {
    int index = ownedUnioning.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedUnioning(index);;
  }

  public void removeFromOwnedUnioning(int index) {
    if (ownedUnioning.size() > index) {

            ReferenceValue removed = ownedUnioning.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedUnioning"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedUnioning.size());
          }
  }

  public void setOwnedUnioning(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedUnioning();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedUnioning(referenceValue, ownedUnioning.size());
          }
  }

  public int addToOwnedDisjoining(ReferenceValue referenceValue, int index) {
    if (index > ownedDisjoining.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedDisjoining"), index, referenceValue);
    }
    ownedDisjoining.add(index, referenceValue);
    return ownedDisjoining.size() - 1;
  }

  public List<ReferenceValue> getOwnedDisjoining() {
    return ownedDisjoining;
  }

  public int addToOwnedDisjoining(Disjoining referred) {
    return addToOwnedDisjoining(new ReferenceValue(referred, null), ownedDisjoining.size());
  }

  public int addToOwnedDisjoining(Disjoining referred, int index) {
    return addToOwnedDisjoining(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedDisjoining() {
    while (!ownedDisjoining.isEmpty()) {
            removeFromOwnedDisjoining(0);
        };
  }

  public void removeFromOwnedDisjoining(@NotNull ReferenceValue child) {
    int index = ownedDisjoining.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedDisjoining(index);;
  }

  public void removeFromOwnedDisjoining(int index) {
    if (ownedDisjoining.size() > index) {

            ReferenceValue removed = ownedDisjoining.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedDisjoining"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedDisjoining.size());
          }
  }

  public void setOwnedDisjoining(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedDisjoining();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedDisjoining(referenceValue, ownedDisjoining.size());
          }
  }

  public int addToFeatureMembership(ReferenceValue referenceValue, int index) {
    if (index > featureMembership.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("featureMembership"), index, referenceValue);
    }
    featureMembership.add(index, referenceValue);
    return featureMembership.size() - 1;
  }

  public List<ReferenceValue> getFeatureMembership() {
    return featureMembership;
  }

  public int addToFeatureMembership(FeatureMembership referred) {
    return addToFeatureMembership(new ReferenceValue(referred, null), featureMembership.size());
  }

  public int addToFeatureMembership(FeatureMembership referred, int index) {
    return addToFeatureMembership(new ReferenceValue(referred, null), index);
  }

  public void clearFeatureMembership() {
    while (!featureMembership.isEmpty()) {
            removeFromFeatureMembership(0);
        };
  }

  public void removeFromFeatureMembership(@NotNull ReferenceValue child) {
    int index = featureMembership.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromFeatureMembership(index);;
  }

  public void removeFromFeatureMembership(int index) {
    if (featureMembership.size() > index) {

            ReferenceValue removed = featureMembership.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("featureMembership"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + featureMembership.size());
          }
  }

  public void setFeatureMembership(@NotNull List<? extends ReferenceValue> newValue) {
    clearFeatureMembership();
          for (ReferenceValue referenceValue : newValue) {
              addToFeatureMembership(referenceValue, featureMembership.size());
          }
  }

  public int addToDifferencingType(ReferenceValue referenceValue, int index) {
    if (index > differencingType.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("differencingType"), index, referenceValue);
    }
    differencingType.add(index, referenceValue);
    return differencingType.size() - 1;
  }

  public List<ReferenceValue> getDifferencingType() {
    return differencingType;
  }

  public int addToDifferencingType(IType referred) {
    return addToDifferencingType(new ReferenceValue(referred, null), differencingType.size());
  }

  public int addToDifferencingType(IType referred, int index) {
    return addToDifferencingType(new ReferenceValue(referred, null), index);
  }

  public void clearDifferencingType() {
    while (!differencingType.isEmpty()) {
            removeFromDifferencingType(0);
        };
  }

  public void removeFromDifferencingType(@NotNull ReferenceValue child) {
    int index = differencingType.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromDifferencingType(index);;
  }

  public void removeFromDifferencingType(int index) {
    if (differencingType.size() > index) {

            ReferenceValue removed = differencingType.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("differencingType"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + differencingType.size());
          }
  }

  public void setDifferencingType(@NotNull List<? extends ReferenceValue> newValue) {
    clearDifferencingType();
          for (ReferenceValue referenceValue : newValue) {
              addToDifferencingType(referenceValue, differencingType.size());
          }
  }

  public int addToOwnedDifferencing(ReferenceValue referenceValue, int index) {
    if (index > ownedDifferencing.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedDifferencing"), index, referenceValue);
    }
    ownedDifferencing.add(index, referenceValue);
    return ownedDifferencing.size() - 1;
  }

  public List<ReferenceValue> getOwnedDifferencing() {
    return ownedDifferencing;
  }

  public int addToOwnedDifferencing(Differencing referred) {
    return addToOwnedDifferencing(new ReferenceValue(referred, null), ownedDifferencing.size());
  }

  public int addToOwnedDifferencing(Differencing referred, int index) {
    return addToOwnedDifferencing(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedDifferencing() {
    while (!ownedDifferencing.isEmpty()) {
            removeFromOwnedDifferencing(0);
        };
  }

  public void removeFromOwnedDifferencing(@NotNull ReferenceValue child) {
    int index = ownedDifferencing.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedDifferencing(index);;
  }

  public void removeFromOwnedDifferencing(int index) {
    if (ownedDifferencing.size() > index) {

            ReferenceValue removed = ownedDifferencing.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedDifferencing"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedDifferencing.size());
          }
  }

  public void setOwnedDifferencing(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedDifferencing();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedDifferencing(referenceValue, ownedDifferencing.size());
          }
  }

  public int addToDirectedFeature(ReferenceValue referenceValue, int index) {
    if (index > directedFeature.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("directedFeature"), index, referenceValue);
    }
    directedFeature.add(index, referenceValue);
    return directedFeature.size() - 1;
  }

  public List<ReferenceValue> getDirectedFeature() {
    return directedFeature;
  }

  public int addToDirectedFeature(IFeature referred) {
    return addToDirectedFeature(new ReferenceValue(referred, null), directedFeature.size());
  }

  public int addToDirectedFeature(IFeature referred, int index) {
    return addToDirectedFeature(new ReferenceValue(referred, null), index);
  }

  public void clearDirectedFeature() {
    while (!directedFeature.isEmpty()) {
            removeFromDirectedFeature(0);
        };
  }

  public void removeFromDirectedFeature(@NotNull ReferenceValue child) {
    int index = directedFeature.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromDirectedFeature(index);;
  }

  public void removeFromDirectedFeature(int index) {
    if (directedFeature.size() > index) {

            ReferenceValue removed = directedFeature.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("directedFeature"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + directedFeature.size());
          }
  }

  public void setDirectedFeature(@NotNull List<? extends ReferenceValue> newValue) {
    clearDirectedFeature();
          for (ReferenceValue referenceValue : newValue) {
              addToDirectedFeature(referenceValue, directedFeature.size());
          }
  }

  public int addToOwnedSpecialization(ReferenceValue referenceValue, int index) {
    if (index > ownedSpecialization.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedSpecialization"), index, referenceValue);
    }
    ownedSpecialization.add(index, referenceValue);
    return ownedSpecialization.size() - 1;
  }

  public List<ReferenceValue> getOwnedSpecialization() {
    return ownedSpecialization;
  }

  public int addToOwnedSpecialization(Specialization referred) {
    return addToOwnedSpecialization(new ReferenceValue(referred, null), ownedSpecialization.size());
  }

  public int addToOwnedSpecialization(Specialization referred, int index) {
    return addToOwnedSpecialization(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedSpecialization() {
    while (!ownedSpecialization.isEmpty()) {
            removeFromOwnedSpecialization(0);
        };
  }

  public void removeFromOwnedSpecialization(@NotNull ReferenceValue child) {
    int index = ownedSpecialization.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedSpecialization(index);;
  }

  public void removeFromOwnedSpecialization(int index) {
    if (ownedSpecialization.size() > index) {

            ReferenceValue removed = ownedSpecialization.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedSpecialization"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedSpecialization.size());
          }
  }

  public void setOwnedSpecialization(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedSpecialization();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedSpecialization(referenceValue, ownedSpecialization.size());
          }
  }

  public int addToMembership(ReferenceValue referenceValue, int index) {
    if (index > membership.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("membership"), index, referenceValue);
    }
    membership.add(index, referenceValue);
    return membership.size() - 1;
  }

  public List<ReferenceValue> getMembership() {
    return membership;
  }

  public int addToMembership(Membership referred) {
    return addToMembership(new ReferenceValue(referred, null), membership.size());
  }

  public int addToMembership(Membership referred, int index) {
    return addToMembership(new ReferenceValue(referred, null), index);
  }

  public void clearMembership() {
    while (!membership.isEmpty()) {
            removeFromMembership(0);
        };
  }

  public void removeFromMembership(@NotNull ReferenceValue child) {
    int index = membership.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromMembership(index);;
  }

  public void removeFromMembership(int index) {
    if (membership.size() > index) {

            ReferenceValue removed = membership.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("membership"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + membership.size());
          }
  }

  public void setMembership(@NotNull List<? extends ReferenceValue> newValue) {
    clearMembership();
          for (ReferenceValue referenceValue : newValue) {
              addToMembership(referenceValue, membership.size());
          }
  }

  public int addToOwnedImport(ReferenceValue referenceValue, int index) {
    if (index > ownedImport.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedImport"), index, referenceValue);
    }
    ownedImport.add(index, referenceValue);
    return ownedImport.size() - 1;
  }

  public List<ReferenceValue> getOwnedImport() {
    return ownedImport;
  }

  public int addToOwnedImport(IImport referred) {
    return addToOwnedImport(new ReferenceValue(referred, null), ownedImport.size());
  }

  public int addToOwnedImport(IImport referred, int index) {
    return addToOwnedImport(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedImport() {
    while (!ownedImport.isEmpty()) {
            removeFromOwnedImport(0);
        };
  }

  public void removeFromOwnedImport(@NotNull ReferenceValue child) {
    int index = ownedImport.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedImport(index);;
  }

  public void removeFromOwnedImport(int index) {
    if (ownedImport.size() > index) {

            ReferenceValue removed = ownedImport.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedImport"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedImport.size());
          }
  }

  public void setOwnedImport(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedImport();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedImport(referenceValue, ownedImport.size());
          }
  }

  public int addToMember(ReferenceValue referenceValue, int index) {
    if (index > member.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("member"), index, referenceValue);
    }
    member.add(index, referenceValue);
    return member.size() - 1;
  }

  public List<ReferenceValue> getMember() {
    return member;
  }

  public int addToMember(IElement referred) {
    return addToMember(new ReferenceValue(referred, null), member.size());
  }

  public int addToMember(IElement referred, int index) {
    return addToMember(new ReferenceValue(referred, null), index);
  }

  public void clearMember() {
    while (!member.isEmpty()) {
            removeFromMember(0);
        };
  }

  public void removeFromMember(@NotNull ReferenceValue child) {
    int index = member.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromMember(index);;
  }

  public void removeFromMember(int index) {
    if (member.size() > index) {

            ReferenceValue removed = member.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("member"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + member.size());
          }
  }

  public void setMember(@NotNull List<? extends ReferenceValue> newValue) {
    clearMember();
          for (ReferenceValue referenceValue : newValue) {
              addToMember(referenceValue, member.size());
          }
  }

  public int addToOwnedMember(ReferenceValue referenceValue, int index) {
    if (index > ownedMember.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedMember"), index, referenceValue);
    }
    ownedMember.add(index, referenceValue);
    return ownedMember.size() - 1;
  }

  public List<ReferenceValue> getOwnedMember() {
    return ownedMember;
  }

  public int addToOwnedMember(IElement referred) {
    return addToOwnedMember(new ReferenceValue(referred, null), ownedMember.size());
  }

  public int addToOwnedMember(IElement referred, int index) {
    return addToOwnedMember(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedMember() {
    while (!ownedMember.isEmpty()) {
            removeFromOwnedMember(0);
        };
  }

  public void removeFromOwnedMember(@NotNull ReferenceValue child) {
    int index = ownedMember.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedMember(index);;
  }

  public void removeFromOwnedMember(int index) {
    if (ownedMember.size() > index) {

            ReferenceValue removed = ownedMember.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedMember"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedMember.size());
          }
  }

  public void setOwnedMember(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedMember();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedMember(referenceValue, ownedMember.size());
          }
  }

  public int addToImportedMembership(ReferenceValue referenceValue, int index) {
    if (index > importedMembership.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("importedMembership"), index, referenceValue);
    }
    importedMembership.add(index, referenceValue);
    return importedMembership.size() - 1;
  }

  public List<ReferenceValue> getImportedMembership() {
    return importedMembership;
  }

  public int addToImportedMembership(Membership referred) {
    return addToImportedMembership(new ReferenceValue(referred, null), importedMembership.size());
  }

  public int addToImportedMembership(Membership referred, int index) {
    return addToImportedMembership(new ReferenceValue(referred, null), index);
  }

  public void clearImportedMembership() {
    while (!importedMembership.isEmpty()) {
            removeFromImportedMembership(0);
        };
  }

  public void removeFromImportedMembership(@NotNull ReferenceValue child) {
    int index = importedMembership.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromImportedMembership(index);;
  }

  public void removeFromImportedMembership(int index) {
    if (importedMembership.size() > index) {

            ReferenceValue removed = importedMembership.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("importedMembership"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + importedMembership.size());
          }
  }

  public void setImportedMembership(@NotNull List<? extends ReferenceValue> newValue) {
    clearImportedMembership();
          for (ReferenceValue referenceValue : newValue) {
              addToImportedMembership(referenceValue, importedMembership.size());
          }
  }

  public int addToOwnedMembership(ReferenceValue referenceValue, int index) {
    if (index > ownedMembership.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedMembership"), index, referenceValue);
    }
    ownedMembership.add(index, referenceValue);
    return ownedMembership.size() - 1;
  }

  public List<ReferenceValue> getOwnedMembership() {
    return ownedMembership;
  }

  public int addToOwnedMembership(Membership referred) {
    return addToOwnedMembership(new ReferenceValue(referred, null), ownedMembership.size());
  }

  public int addToOwnedMembership(Membership referred, int index) {
    return addToOwnedMembership(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedMembership() {
    while (!ownedMembership.isEmpty()) {
            removeFromOwnedMembership(0);
        };
  }

  public void removeFromOwnedMembership(@NotNull ReferenceValue child) {
    int index = ownedMembership.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedMembership(index);;
  }

  public void removeFromOwnedMembership(int index) {
    if (ownedMembership.size() > index) {

            ReferenceValue removed = ownedMembership.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedMembership"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedMembership.size());
          }
  }

  public void setOwnedMembership(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedMembership();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedMembership(referenceValue, ownedMembership.size());
          }
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
    if (Objects.equals(property.getKey(), "sysml-Definition-isVariation")) {
      return isVariation;
    }
    if (Objects.equals(property.getKey(), "sysml-IType-isAbstract")) {
      return isAbstract;
    }
    if (Objects.equals(property.getKey(), "sysml-IType-isSufficient")) {
      return isSufficient;
    }
    if (Objects.equals(property.getKey(), "sysml-IType-isConjugated")) {
      return isConjugated;
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
    if (Objects.equals(property.getKey(), "sysml-Definition-isVariation")) {
      setIsVariation((Boolean) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IType-isAbstract")) {
      setIsAbstract((Boolean) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IType-isSufficient")) {
      setIsSufficient((Boolean) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IType-isConjugated")) {
      setIsConjugated((Boolean) value);
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
    if (Objects.equals(reference.getKey(), "sysml-Definition-variant")) {
      return variant;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-variantMembership")) {
      return variantMembership;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-usage")) {
      return usage;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-directedUsage")) {
      return directedUsage;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedReference")) {
      return ownedReference;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAttribute")) {
      return ownedAttribute;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedEnumeration")) {
      return ownedEnumeration;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedOccurrence")) {
      return ownedOccurrence;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedItem")) {
      return ownedItem;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedPart")) {
      return ownedPart;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedPort")) {
      return ownedPort;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConnection")) {
      return ownedConnection;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedFlow")) {
      return ownedFlow;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedInterface")) {
      return ownedInterface;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAllocation")) {
      return ownedAllocation;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAction")) {
      return ownedAction;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedState")) {
      return ownedState;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedTransition")) {
      return ownedTransition;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedCalculation")) {
      return ownedCalculation;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConstraint")) {
      return ownedConstraint;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedRequirement")) {
      return ownedRequirement;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConcern")) {
      return ownedConcern;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedCase")) {
      return ownedCase;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAnalysisCase")) {
      return ownedAnalysisCase;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedVerificationCase")) {
      return ownedVerificationCase;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedUseCase")) {
      return ownedUseCase;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedView")) {
      return ownedView;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedViewpoint")) {
      return ownedViewpoint;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedRendering")) {
      return ownedRendering;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedMetadata")) {
      return ownedMetadata;
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedUsage")) {
      return ownedUsage;
    }
    if (Objects.equals(reference.getKey(), "sysml-IClassifier-ownedSubclassification")) {
      return ownedSubclassification;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedFeatureMembership")) {
      return ownedFeatureMembership;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedFeature")) {
      return ownedFeature;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedEndFeature")) {
      return ownedEndFeature;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-feature")) {
      return feature;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-input")) {
      return input;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-output")) {
      return output;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-inheritedMembership")) {
      return inheritedMembership;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-endFeature")) {
      return endFeature;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedConjugator")) {
      return Collections.singletonList(ownedConjugator);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-inheritedFeature")) {
      return inheritedFeature;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-multiplicity")) {
      return Collections.singletonList(multiplicity);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-unioningType")) {
      return unioningType;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedIntersecting")) {
      return ownedIntersecting;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-intersectingType")) {
      return intersectingType;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedUnioning")) {
      return ownedUnioning;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedDisjoining")) {
      return ownedDisjoining;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-featureMembership")) {
      return featureMembership;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-differencingType")) {
      return differencingType;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedDifferencing")) {
      return ownedDifferencing;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-directedFeature")) {
      return directedFeature;
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedSpecialization")) {
      return ownedSpecialization;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-membership")) {
      return membership;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedImport")) {
      return ownedImport;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-member")) {
      return member;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedMember")) {
      return ownedMember;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-importedMembership")) {
      return importedMembership;
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedMembership")) {
      return ownedMembership;
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
    if (Objects.equals(reference.getKey(), "sysml-Definition-variant")) {
      return addToVariant(referredNode, variant.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-variantMembership")) {
      return addToVariantMembership(referredNode, variantMembership.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-usage")) {
      return addToUsage(referredNode, usage.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-directedUsage")) {
      return addToDirectedUsage(referredNode, directedUsage.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedReference")) {
      return addToOwnedReference(referredNode, ownedReference.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAttribute")) {
      return addToOwnedAttribute(referredNode, ownedAttribute.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedEnumeration")) {
      return addToOwnedEnumeration(referredNode, ownedEnumeration.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedOccurrence")) {
      return addToOwnedOccurrence(referredNode, ownedOccurrence.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedItem")) {
      return addToOwnedItem(referredNode, ownedItem.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedPart")) {
      return addToOwnedPart(referredNode, ownedPart.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedPort")) {
      return addToOwnedPort(referredNode, ownedPort.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConnection")) {
      return addToOwnedConnection(referredNode, ownedConnection.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedFlow")) {
      return addToOwnedFlow(referredNode, ownedFlow.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedInterface")) {
      return addToOwnedInterface(referredNode, ownedInterface.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAllocation")) {
      return addToOwnedAllocation(referredNode, ownedAllocation.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAction")) {
      return addToOwnedAction(referredNode, ownedAction.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedState")) {
      return addToOwnedState(referredNode, ownedState.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedTransition")) {
      return addToOwnedTransition(referredNode, ownedTransition.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedCalculation")) {
      return addToOwnedCalculation(referredNode, ownedCalculation.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConstraint")) {
      return addToOwnedConstraint(referredNode, ownedConstraint.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedRequirement")) {
      return addToOwnedRequirement(referredNode, ownedRequirement.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConcern")) {
      return addToOwnedConcern(referredNode, ownedConcern.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedCase")) {
      return addToOwnedCase(referredNode, ownedCase.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAnalysisCase")) {
      return addToOwnedAnalysisCase(referredNode, ownedAnalysisCase.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedVerificationCase")) {
      return addToOwnedVerificationCase(referredNode, ownedVerificationCase.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedUseCase")) {
      return addToOwnedUseCase(referredNode, ownedUseCase.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedView")) {
      return addToOwnedView(referredNode, ownedView.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedViewpoint")) {
      return addToOwnedViewpoint(referredNode, ownedViewpoint.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedRendering")) {
      return addToOwnedRendering(referredNode, ownedRendering.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedMetadata")) {
      return addToOwnedMetadata(referredNode, ownedMetadata.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedUsage")) {
      return addToOwnedUsage(referredNode, ownedUsage.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IClassifier-ownedSubclassification")) {
      return addToOwnedSubclassification(referredNode, ownedSubclassification.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedFeatureMembership")) {
      return addToOwnedFeatureMembership(referredNode, ownedFeatureMembership.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedFeature")) {
      return addToOwnedFeature(referredNode, ownedFeature.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedEndFeature")) {
      return addToOwnedEndFeature(referredNode, ownedEndFeature.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-feature")) {
      return addToFeature(referredNode, feature.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-input")) {
      return addToInput(referredNode, input.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-output")) {
      return addToOutput(referredNode, output.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-inheritedMembership")) {
      return addToInheritedMembership(referredNode, inheritedMembership.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-endFeature")) {
      return addToEndFeature(referredNode, endFeature.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-inheritedFeature")) {
      return addToInheritedFeature(referredNode, inheritedFeature.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-unioningType")) {
      return addToUnioningType(referredNode, unioningType.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedIntersecting")) {
      return addToOwnedIntersecting(referredNode, ownedIntersecting.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-intersectingType")) {
      return addToIntersectingType(referredNode, intersectingType.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedUnioning")) {
      return addToOwnedUnioning(referredNode, ownedUnioning.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedDisjoining")) {
      return addToOwnedDisjoining(referredNode, ownedDisjoining.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-featureMembership")) {
      return addToFeatureMembership(referredNode, featureMembership.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-differencingType")) {
      return addToDifferencingType(referredNode, differencingType.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedDifferencing")) {
      return addToOwnedDifferencing(referredNode, ownedDifferencing.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-directedFeature")) {
      return addToDirectedFeature(referredNode, directedFeature.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedSpecialization")) {
      return addToOwnedSpecialization(referredNode, ownedSpecialization.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-membership")) {
      return addToMembership(referredNode, membership.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedImport")) {
      return addToOwnedImport(referredNode, ownedImport.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-member")) {
      return addToMember(referredNode, member.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedMember")) {
      return addToOwnedMember(referredNode, ownedMember.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-importedMembership")) {
      return addToImportedMembership(referredNode, importedMembership.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedMembership")) {
      return addToOwnedMembership(referredNode, ownedMembership.size());
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
    if (Objects.equals(reference.getKey(), "sysml-Definition-variant")) {
      return addToVariant(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-variantMembership")) {
      return addToVariantMembership(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-usage")) {
      return addToUsage(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-directedUsage")) {
      return addToDirectedUsage(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedReference")) {
      return addToOwnedReference(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAttribute")) {
      return addToOwnedAttribute(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedEnumeration")) {
      return addToOwnedEnumeration(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedOccurrence")) {
      return addToOwnedOccurrence(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedItem")) {
      return addToOwnedItem(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedPart")) {
      return addToOwnedPart(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedPort")) {
      return addToOwnedPort(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConnection")) {
      return addToOwnedConnection(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedFlow")) {
      return addToOwnedFlow(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedInterface")) {
      return addToOwnedInterface(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAllocation")) {
      return addToOwnedAllocation(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAction")) {
      return addToOwnedAction(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedState")) {
      return addToOwnedState(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedTransition")) {
      return addToOwnedTransition(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedCalculation")) {
      return addToOwnedCalculation(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConstraint")) {
      return addToOwnedConstraint(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedRequirement")) {
      return addToOwnedRequirement(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedConcern")) {
      return addToOwnedConcern(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedCase")) {
      return addToOwnedCase(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedAnalysisCase")) {
      return addToOwnedAnalysisCase(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedVerificationCase")) {
      return addToOwnedVerificationCase(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedUseCase")) {
      return addToOwnedUseCase(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedView")) {
      return addToOwnedView(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedViewpoint")) {
      return addToOwnedViewpoint(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedRendering")) {
      return addToOwnedRendering(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedMetadata")) {
      return addToOwnedMetadata(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-Definition-ownedUsage")) {
      return addToOwnedUsage(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IClassifier-ownedSubclassification")) {
      return addToOwnedSubclassification(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedFeatureMembership")) {
      return addToOwnedFeatureMembership(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedFeature")) {
      return addToOwnedFeature(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedEndFeature")) {
      return addToOwnedEndFeature(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-feature")) {
      return addToFeature(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-input")) {
      return addToInput(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-output")) {
      return addToOutput(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-inheritedMembership")) {
      return addToInheritedMembership(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-endFeature")) {
      return addToEndFeature(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-inheritedFeature")) {
      return addToInheritedFeature(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-unioningType")) {
      return addToUnioningType(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedIntersecting")) {
      return addToOwnedIntersecting(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-intersectingType")) {
      return addToIntersectingType(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedUnioning")) {
      return addToOwnedUnioning(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedDisjoining")) {
      return addToOwnedDisjoining(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-featureMembership")) {
      return addToFeatureMembership(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-differencingType")) {
      return addToDifferencingType(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedDifferencing")) {
      return addToOwnedDifferencing(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-directedFeature")) {
      return addToDirectedFeature(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IType-ownedSpecialization")) {
      return addToOwnedSpecialization(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-membership")) {
      return addToMembership(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedImport")) {
      return addToOwnedImport(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-member")) {
      return addToMember(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedMember")) {
      return addToOwnedMember(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-importedMembership")) {
      return addToImportedMembership(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-INamespace-ownedMembership")) {
      return addToOwnedMembership(referredNode, index);
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
