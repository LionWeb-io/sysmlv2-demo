package io.lionweb.sysml2;

import io.lionweb.language.Concept;
import io.lionweb.language.Containment;
import io.lionweb.language.Property;
import io.lionweb.language.Reference;
import io.lionweb.model.ClassifierInstance;
import io.lionweb.model.HasSettableParent;
import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;
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

public class SuccessionFlowConnectionUsage extends FlowConnectionUsage implements ISuccessionItemFlow {
  @NotNull
  private String id;

  @Nullable
  private ClassifierInstance<?> parent;

  protected ReferenceValue transitionStep = null;

  protected List<ReferenceValue> triggerStep = new ArrayList<>();

  protected List<ReferenceValue> effectStep = new ArrayList<>();

  protected List<ReferenceValue> guardExpression = new ArrayList<>();

  protected List<ReferenceValue> relatedFeature = new ArrayList<>();

  protected List<ReferenceValue> association = new ArrayList<>();

  protected List<ReferenceValue> connectorEnd = new ArrayList<>();

  protected ReferenceValue sourceFeature = null;

  protected List<ReferenceValue> targetFeature = new ArrayList<>();

  protected ReferenceValue owningType = null;

  protected Boolean isUnique;

  protected Boolean isOrdered;

  protected List<ReferenceValue> type = new ArrayList<>();

  protected List<ReferenceValue> ownedRedefinition = new ArrayList<>();

  protected List<ReferenceValue> ownedSubsetting = new ArrayList<>();

  protected ReferenceValue owningFeatureMembership = null;

  protected Boolean isComposite;

  protected Boolean isEnd;

  protected ReferenceValue endOwningType = null;

  protected List<ReferenceValue> ownedTyping = new ArrayList<>();

  protected List<ReferenceValue> featuringType = new ArrayList<>();

  protected List<ReferenceValue> ownedTypeFeaturing = new ArrayList<>();

  protected Boolean isDerived;

  protected List<ReferenceValue> chainingFeature = new ArrayList<>();

  protected List<ReferenceValue> ownedFeatureInverting = new ArrayList<>();

  protected List<ReferenceValue> ownedFeatureChaining = new ArrayList<>();

  protected Boolean isReadOnly;

  protected Boolean isPortion;

  protected FeatureDirectionKind direction;

  protected ReferenceValue ownedReferenceSubsetting = null;

  protected ReferenceValue crossFeature = null;

  protected ReferenceValue ownedCrossSubsetting = null;

  protected ReferenceValue featureTarget = null;

  protected Boolean isNonunique;

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

  protected List<IElement> ownedRelatedElement = new ArrayList<>();

  protected ReferenceValue owningRelatedElement = null;

  protected List<ReferenceValue> relatedElement = new ArrayList<>();

  protected List<ReferenceValue> target = new ArrayList<>();

  protected List<ReferenceValue> source = new ArrayList<>();

  protected Boolean isImplied;

  protected List<ReferenceValue> itemType = new ArrayList<>();

  protected ReferenceValue targetInputFeature = null;

  protected ReferenceValue sourceOutputFeature = null;

  protected List<ReferenceValue> itemFlowEnd = new ArrayList<>();

  protected ReferenceValue itemFeature = null;

  protected List<ReferenceValue> interaction = new ArrayList<>();

  protected List<ReferenceValue> behavior = new ArrayList<>();

  protected List<ReferenceValue> parameter = new ArrayList<>();

  public SuccessionFlowConnectionUsage(@NotNull String id) {
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
    return SysmlLanguage.getInstance().getSuccessionFlowConnectionUsage();
  }

  public void setTransitionStep(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("transitionStep"), 0, transitionStep);
      }
      transitionStep = null;
    } else {
      if (partitionObserverCache != null) {
        if (transitionStep != null) {
          ReferenceValue oldValue = transitionStep;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("transitionStep"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("transitionStep"), 0, value);
        }
      }
      this.transitionStep = value;
    }
  }

  public ReferenceValue getTransitionStep() {
    return transitionStep;
  }

  public int addToTriggerStep(ReferenceValue referenceValue, int index) {
    if (index > triggerStep.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("triggerStep"), index, referenceValue);
    }
    triggerStep.add(index, referenceValue);
    return triggerStep.size() - 1;
  }

  public List<ReferenceValue> getTriggerStep() {
    return triggerStep;
  }

  public int addToTriggerStep(IStep referred) {
    return addToTriggerStep(new ReferenceValue(referred, null), triggerStep.size());
  }

  public int addToTriggerStep(IStep referred, int index) {
    return addToTriggerStep(new ReferenceValue(referred, null), index);
  }

  public void clearTriggerStep() {
    while (!triggerStep.isEmpty()) {
            removeFromTriggerStep(0);
        };
  }

  public void removeFromTriggerStep(@NotNull ReferenceValue child) {
    int index = triggerStep.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromTriggerStep(index);;
  }

  public void removeFromTriggerStep(int index) {
    if (triggerStep.size() > index) {

            ReferenceValue removed = triggerStep.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("triggerStep"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + triggerStep.size());
          }
  }

  public void setTriggerStep(@NotNull List<? extends ReferenceValue> newValue) {
    clearTriggerStep();
          for (ReferenceValue referenceValue : newValue) {
              addToTriggerStep(referenceValue, triggerStep.size());
          }
  }

  public int addToEffectStep(ReferenceValue referenceValue, int index) {
    if (index > effectStep.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("effectStep"), index, referenceValue);
    }
    effectStep.add(index, referenceValue);
    return effectStep.size() - 1;
  }

  public List<ReferenceValue> getEffectStep() {
    return effectStep;
  }

  public int addToEffectStep(IStep referred) {
    return addToEffectStep(new ReferenceValue(referred, null), effectStep.size());
  }

  public int addToEffectStep(IStep referred, int index) {
    return addToEffectStep(new ReferenceValue(referred, null), index);
  }

  public void clearEffectStep() {
    while (!effectStep.isEmpty()) {
            removeFromEffectStep(0);
        };
  }

  public void removeFromEffectStep(@NotNull ReferenceValue child) {
    int index = effectStep.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromEffectStep(index);;
  }

  public void removeFromEffectStep(int index) {
    if (effectStep.size() > index) {

            ReferenceValue removed = effectStep.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("effectStep"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + effectStep.size());
          }
  }

  public void setEffectStep(@NotNull List<? extends ReferenceValue> newValue) {
    clearEffectStep();
          for (ReferenceValue referenceValue : newValue) {
              addToEffectStep(referenceValue, effectStep.size());
          }
  }

  public int addToGuardExpression(ReferenceValue referenceValue, int index) {
    if (index > guardExpression.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("guardExpression"), index, referenceValue);
    }
    guardExpression.add(index, referenceValue);
    return guardExpression.size() - 1;
  }

  public List<ReferenceValue> getGuardExpression() {
    return guardExpression;
  }

  public int addToGuardExpression(IExpression referred) {
    return addToGuardExpression(new ReferenceValue(referred, null), guardExpression.size());
  }

  public int addToGuardExpression(IExpression referred, int index) {
    return addToGuardExpression(new ReferenceValue(referred, null), index);
  }

  public void clearGuardExpression() {
    while (!guardExpression.isEmpty()) {
            removeFromGuardExpression(0);
        };
  }

  public void removeFromGuardExpression(@NotNull ReferenceValue child) {
    int index = guardExpression.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromGuardExpression(index);;
  }

  public void removeFromGuardExpression(int index) {
    if (guardExpression.size() > index) {

            ReferenceValue removed = guardExpression.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("guardExpression"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + guardExpression.size());
          }
  }

  public void setGuardExpression(@NotNull List<? extends ReferenceValue> newValue) {
    clearGuardExpression();
          for (ReferenceValue referenceValue : newValue) {
              addToGuardExpression(referenceValue, guardExpression.size());
          }
  }

  public int addToRelatedFeature(ReferenceValue referenceValue, int index) {
    if (index > relatedFeature.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("relatedFeature"), index, referenceValue);
    }
    relatedFeature.add(index, referenceValue);
    return relatedFeature.size() - 1;
  }

  public List<ReferenceValue> getRelatedFeature() {
    return relatedFeature;
  }

  public int addToRelatedFeature(IFeature referred) {
    return addToRelatedFeature(new ReferenceValue(referred, null), relatedFeature.size());
  }

  public int addToRelatedFeature(IFeature referred, int index) {
    return addToRelatedFeature(new ReferenceValue(referred, null), index);
  }

  public void clearRelatedFeature() {
    while (!relatedFeature.isEmpty()) {
            removeFromRelatedFeature(0);
        };
  }

  public void removeFromRelatedFeature(@NotNull ReferenceValue child) {
    int index = relatedFeature.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromRelatedFeature(index);;
  }

  public void removeFromRelatedFeature(int index) {
    if (relatedFeature.size() > index) {

            ReferenceValue removed = relatedFeature.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("relatedFeature"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + relatedFeature.size());
          }
  }

  public void setRelatedFeature(@NotNull List<? extends ReferenceValue> newValue) {
    clearRelatedFeature();
          for (ReferenceValue referenceValue : newValue) {
              addToRelatedFeature(referenceValue, relatedFeature.size());
          }
  }

  public int addToAssociation(ReferenceValue referenceValue, int index) {
    if (index > association.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("association"), index, referenceValue);
    }
    association.add(index, referenceValue);
    return association.size() - 1;
  }

  public List<ReferenceValue> getAssociation() {
    return association;
  }

  public int addToAssociation(IAssociation referred) {
    return addToAssociation(new ReferenceValue(referred, null), association.size());
  }

  public int addToAssociation(IAssociation referred, int index) {
    return addToAssociation(new ReferenceValue(referred, null), index);
  }

  public void clearAssociation() {
    while (!association.isEmpty()) {
            removeFromAssociation(0);
        };
  }

  public void removeFromAssociation(@NotNull ReferenceValue child) {
    int index = association.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromAssociation(index);;
  }

  public void removeFromAssociation(int index) {
    if (association.size() > index) {

            ReferenceValue removed = association.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("association"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + association.size());
          }
  }

  public void setAssociation(@NotNull List<? extends ReferenceValue> newValue) {
    clearAssociation();
          for (ReferenceValue referenceValue : newValue) {
              addToAssociation(referenceValue, association.size());
          }
  }

  public int addToConnectorEnd(ReferenceValue referenceValue, int index) {
    if (index > connectorEnd.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("connectorEnd"), index, referenceValue);
    }
    connectorEnd.add(index, referenceValue);
    return connectorEnd.size() - 1;
  }

  public List<ReferenceValue> getConnectorEnd() {
    return connectorEnd;
  }

  public int addToConnectorEnd(IFeature referred) {
    return addToConnectorEnd(new ReferenceValue(referred, null), connectorEnd.size());
  }

  public int addToConnectorEnd(IFeature referred, int index) {
    return addToConnectorEnd(new ReferenceValue(referred, null), index);
  }

  public void clearConnectorEnd() {
    while (!connectorEnd.isEmpty()) {
            removeFromConnectorEnd(0);
        };
  }

  public void removeFromConnectorEnd(@NotNull ReferenceValue child) {
    int index = connectorEnd.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromConnectorEnd(index);;
  }

  public void removeFromConnectorEnd(int index) {
    if (connectorEnd.size() > index) {

            ReferenceValue removed = connectorEnd.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("connectorEnd"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + connectorEnd.size());
          }
  }

  public void setConnectorEnd(@NotNull List<? extends ReferenceValue> newValue) {
    clearConnectorEnd();
          for (ReferenceValue referenceValue : newValue) {
              addToConnectorEnd(referenceValue, connectorEnd.size());
          }
  }

  public void setSourceFeature(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("sourceFeature"), 0, sourceFeature);
      }
      sourceFeature = null;
    } else {
      if (partitionObserverCache != null) {
        if (sourceFeature != null) {
          ReferenceValue oldValue = sourceFeature;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("sourceFeature"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("sourceFeature"), 0, value);
        }
      }
      this.sourceFeature = value;
    }
  }

  public ReferenceValue getSourceFeature() {
    return sourceFeature;
  }

  public int addToTargetFeature(ReferenceValue referenceValue, int index) {
    if (index > targetFeature.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("targetFeature"), index, referenceValue);
    }
    targetFeature.add(index, referenceValue);
    return targetFeature.size() - 1;
  }

  public List<ReferenceValue> getTargetFeature() {
    return targetFeature;
  }

  public int addToTargetFeature(IFeature referred) {
    return addToTargetFeature(new ReferenceValue(referred, null), targetFeature.size());
  }

  public int addToTargetFeature(IFeature referred, int index) {
    return addToTargetFeature(new ReferenceValue(referred, null), index);
  }

  public void clearTargetFeature() {
    while (!targetFeature.isEmpty()) {
            removeFromTargetFeature(0);
        };
  }

  public void removeFromTargetFeature(@NotNull ReferenceValue child) {
    int index = targetFeature.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromTargetFeature(index);;
  }

  public void removeFromTargetFeature(int index) {
    if (targetFeature.size() > index) {

            ReferenceValue removed = targetFeature.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("targetFeature"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + targetFeature.size());
          }
  }

  public void setTargetFeature(@NotNull List<? extends ReferenceValue> newValue) {
    clearTargetFeature();
          for (ReferenceValue referenceValue : newValue) {
              addToTargetFeature(referenceValue, targetFeature.size());
          }
  }

  public void setOwningType(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("owningType"), 0, owningType);
      }
      owningType = null;
    } else {
      if (partitionObserverCache != null) {
        if (owningType != null) {
          ReferenceValue oldValue = owningType;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("owningType"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("owningType"), 0, value);
        }
      }
      this.owningType = value;
    }
  }

  public ReferenceValue getOwningType() {
    return owningType;
  }

  public Boolean getIsUnique() {
    return isUnique;
  }

  public void setIsUnique(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isUnique"), getIsUnique(), value);
        }
    this.isUnique = value;
  }

  public Boolean getIsOrdered() {
    return isOrdered;
  }

  public void setIsOrdered(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isOrdered"), getIsOrdered(), value);
        }
    this.isOrdered = value;
  }

  public int addToType(ReferenceValue referenceValue, int index) {
    if (index > type.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("type"), index, referenceValue);
    }
    type.add(index, referenceValue);
    return type.size() - 1;
  }

  public List<ReferenceValue> getType() {
    return type;
  }

  public int addToType(IType referred) {
    return addToType(new ReferenceValue(referred, null), type.size());
  }

  public int addToType(IType referred, int index) {
    return addToType(new ReferenceValue(referred, null), index);
  }

  public void clearType() {
    while (!type.isEmpty()) {
            removeFromType(0);
        };
  }

  public void removeFromType(@NotNull ReferenceValue child) {
    int index = type.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromType(index);;
  }

  public void removeFromType(int index) {
    if (type.size() > index) {

            ReferenceValue removed = type.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("type"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + type.size());
          }
  }

  public void setType(@NotNull List<? extends ReferenceValue> newValue) {
    clearType();
          for (ReferenceValue referenceValue : newValue) {
              addToType(referenceValue, type.size());
          }
  }

  public int addToOwnedRedefinition(ReferenceValue referenceValue, int index) {
    if (index > ownedRedefinition.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedRedefinition"), index, referenceValue);
    }
    ownedRedefinition.add(index, referenceValue);
    return ownedRedefinition.size() - 1;
  }

  public List<ReferenceValue> getOwnedRedefinition() {
    return ownedRedefinition;
  }

  public int addToOwnedRedefinition(Redefinition referred) {
    return addToOwnedRedefinition(new ReferenceValue(referred, null), ownedRedefinition.size());
  }

  public int addToOwnedRedefinition(Redefinition referred, int index) {
    return addToOwnedRedefinition(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedRedefinition() {
    while (!ownedRedefinition.isEmpty()) {
            removeFromOwnedRedefinition(0);
        };
  }

  public void removeFromOwnedRedefinition(@NotNull ReferenceValue child) {
    int index = ownedRedefinition.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedRedefinition(index);;
  }

  public void removeFromOwnedRedefinition(int index) {
    if (ownedRedefinition.size() > index) {

            ReferenceValue removed = ownedRedefinition.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedRedefinition"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedRedefinition.size());
          }
  }

  public void setOwnedRedefinition(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedRedefinition();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedRedefinition(referenceValue, ownedRedefinition.size());
          }
  }

  public int addToOwnedSubsetting(ReferenceValue referenceValue, int index) {
    if (index > ownedSubsetting.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedSubsetting"), index, referenceValue);
    }
    ownedSubsetting.add(index, referenceValue);
    return ownedSubsetting.size() - 1;
  }

  public List<ReferenceValue> getOwnedSubsetting() {
    return ownedSubsetting;
  }

  public int addToOwnedSubsetting(Subsetting referred) {
    return addToOwnedSubsetting(new ReferenceValue(referred, null), ownedSubsetting.size());
  }

  public int addToOwnedSubsetting(Subsetting referred, int index) {
    return addToOwnedSubsetting(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedSubsetting() {
    while (!ownedSubsetting.isEmpty()) {
            removeFromOwnedSubsetting(0);
        };
  }

  public void removeFromOwnedSubsetting(@NotNull ReferenceValue child) {
    int index = ownedSubsetting.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedSubsetting(index);;
  }

  public void removeFromOwnedSubsetting(int index) {
    if (ownedSubsetting.size() > index) {

            ReferenceValue removed = ownedSubsetting.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedSubsetting"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedSubsetting.size());
          }
  }

  public void setOwnedSubsetting(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedSubsetting();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedSubsetting(referenceValue, ownedSubsetting.size());
          }
  }

  public void setOwningFeatureMembership(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("owningFeatureMembership"), 0, owningFeatureMembership);
      }
      owningFeatureMembership = null;
    } else {
      if (partitionObserverCache != null) {
        if (owningFeatureMembership != null) {
          ReferenceValue oldValue = owningFeatureMembership;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("owningFeatureMembership"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("owningFeatureMembership"), 0, value);
        }
      }
      this.owningFeatureMembership = value;
    }
  }

  public ReferenceValue getOwningFeatureMembership() {
    return owningFeatureMembership;
  }

  public Boolean getIsComposite() {
    return isComposite;
  }

  public void setIsComposite(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isComposite"), getIsComposite(), value);
        }
    this.isComposite = value;
  }

  public Boolean getIsEnd() {
    return isEnd;
  }

  public void setIsEnd(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isEnd"), getIsEnd(), value);
        }
    this.isEnd = value;
  }

  public void setEndOwningType(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("endOwningType"), 0, endOwningType);
      }
      endOwningType = null;
    } else {
      if (partitionObserverCache != null) {
        if (endOwningType != null) {
          ReferenceValue oldValue = endOwningType;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("endOwningType"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("endOwningType"), 0, value);
        }
      }
      this.endOwningType = value;
    }
  }

  public ReferenceValue getEndOwningType() {
    return endOwningType;
  }

  public int addToOwnedTyping(ReferenceValue referenceValue, int index) {
    if (index > ownedTyping.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedTyping"), index, referenceValue);
    }
    ownedTyping.add(index, referenceValue);
    return ownedTyping.size() - 1;
  }

  public List<ReferenceValue> getOwnedTyping() {
    return ownedTyping;
  }

  public int addToOwnedTyping(FeatureTyping referred) {
    return addToOwnedTyping(new ReferenceValue(referred, null), ownedTyping.size());
  }

  public int addToOwnedTyping(FeatureTyping referred, int index) {
    return addToOwnedTyping(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedTyping() {
    while (!ownedTyping.isEmpty()) {
            removeFromOwnedTyping(0);
        };
  }

  public void removeFromOwnedTyping(@NotNull ReferenceValue child) {
    int index = ownedTyping.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedTyping(index);;
  }

  public void removeFromOwnedTyping(int index) {
    if (ownedTyping.size() > index) {

            ReferenceValue removed = ownedTyping.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedTyping"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedTyping.size());
          }
  }

  public void setOwnedTyping(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedTyping();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedTyping(referenceValue, ownedTyping.size());
          }
  }

  public int addToFeaturingType(ReferenceValue referenceValue, int index) {
    if (index > featuringType.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("featuringType"), index, referenceValue);
    }
    featuringType.add(index, referenceValue);
    return featuringType.size() - 1;
  }

  public List<ReferenceValue> getFeaturingType() {
    return featuringType;
  }

  public int addToFeaturingType(IType referred) {
    return addToFeaturingType(new ReferenceValue(referred, null), featuringType.size());
  }

  public int addToFeaturingType(IType referred, int index) {
    return addToFeaturingType(new ReferenceValue(referred, null), index);
  }

  public void clearFeaturingType() {
    while (!featuringType.isEmpty()) {
            removeFromFeaturingType(0);
        };
  }

  public void removeFromFeaturingType(@NotNull ReferenceValue child) {
    int index = featuringType.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromFeaturingType(index);;
  }

  public void removeFromFeaturingType(int index) {
    if (featuringType.size() > index) {

            ReferenceValue removed = featuringType.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("featuringType"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + featuringType.size());
          }
  }

  public void setFeaturingType(@NotNull List<? extends ReferenceValue> newValue) {
    clearFeaturingType();
          for (ReferenceValue referenceValue : newValue) {
              addToFeaturingType(referenceValue, featuringType.size());
          }
  }

  public int addToOwnedTypeFeaturing(ReferenceValue referenceValue, int index) {
    if (index > ownedTypeFeaturing.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedTypeFeaturing"), index, referenceValue);
    }
    ownedTypeFeaturing.add(index, referenceValue);
    return ownedTypeFeaturing.size() - 1;
  }

  public List<ReferenceValue> getOwnedTypeFeaturing() {
    return ownedTypeFeaturing;
  }

  public int addToOwnedTypeFeaturing(TypeFeaturing referred) {
    return addToOwnedTypeFeaturing(new ReferenceValue(referred, null), ownedTypeFeaturing.size());
  }

  public int addToOwnedTypeFeaturing(TypeFeaturing referred, int index) {
    return addToOwnedTypeFeaturing(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedTypeFeaturing() {
    while (!ownedTypeFeaturing.isEmpty()) {
            removeFromOwnedTypeFeaturing(0);
        };
  }

  public void removeFromOwnedTypeFeaturing(@NotNull ReferenceValue child) {
    int index = ownedTypeFeaturing.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedTypeFeaturing(index);;
  }

  public void removeFromOwnedTypeFeaturing(int index) {
    if (ownedTypeFeaturing.size() > index) {

            ReferenceValue removed = ownedTypeFeaturing.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedTypeFeaturing"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedTypeFeaturing.size());
          }
  }

  public void setOwnedTypeFeaturing(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedTypeFeaturing();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedTypeFeaturing(referenceValue, ownedTypeFeaturing.size());
          }
  }

  public Boolean getIsDerived() {
    return isDerived;
  }

  public void setIsDerived(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isDerived"), getIsDerived(), value);
        }
    this.isDerived = value;
  }

  public int addToChainingFeature(ReferenceValue referenceValue, int index) {
    if (index > chainingFeature.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("chainingFeature"), index, referenceValue);
    }
    chainingFeature.add(index, referenceValue);
    return chainingFeature.size() - 1;
  }

  public List<ReferenceValue> getChainingFeature() {
    return chainingFeature;
  }

  public int addToChainingFeature(IFeature referred) {
    return addToChainingFeature(new ReferenceValue(referred, null), chainingFeature.size());
  }

  public int addToChainingFeature(IFeature referred, int index) {
    return addToChainingFeature(new ReferenceValue(referred, null), index);
  }

  public void clearChainingFeature() {
    while (!chainingFeature.isEmpty()) {
            removeFromChainingFeature(0);
        };
  }

  public void removeFromChainingFeature(@NotNull ReferenceValue child) {
    int index = chainingFeature.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromChainingFeature(index);;
  }

  public void removeFromChainingFeature(int index) {
    if (chainingFeature.size() > index) {

            ReferenceValue removed = chainingFeature.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("chainingFeature"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + chainingFeature.size());
          }
  }

  public void setChainingFeature(@NotNull List<? extends ReferenceValue> newValue) {
    clearChainingFeature();
          for (ReferenceValue referenceValue : newValue) {
              addToChainingFeature(referenceValue, chainingFeature.size());
          }
  }

  public int addToOwnedFeatureInverting(ReferenceValue referenceValue, int index) {
    if (index > ownedFeatureInverting.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedFeatureInverting"), index, referenceValue);
    }
    ownedFeatureInverting.add(index, referenceValue);
    return ownedFeatureInverting.size() - 1;
  }

  public List<ReferenceValue> getOwnedFeatureInverting() {
    return ownedFeatureInverting;
  }

  public int addToOwnedFeatureInverting(FeatureInverting referred) {
    return addToOwnedFeatureInverting(new ReferenceValue(referred, null), ownedFeatureInverting.size());
  }

  public int addToOwnedFeatureInverting(FeatureInverting referred, int index) {
    return addToOwnedFeatureInverting(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedFeatureInverting() {
    while (!ownedFeatureInverting.isEmpty()) {
            removeFromOwnedFeatureInverting(0);
        };
  }

  public void removeFromOwnedFeatureInverting(@NotNull ReferenceValue child) {
    int index = ownedFeatureInverting.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedFeatureInverting(index);;
  }

  public void removeFromOwnedFeatureInverting(int index) {
    if (ownedFeatureInverting.size() > index) {

            ReferenceValue removed = ownedFeatureInverting.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedFeatureInverting"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedFeatureInverting.size());
          }
  }

  public void setOwnedFeatureInverting(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedFeatureInverting();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedFeatureInverting(referenceValue, ownedFeatureInverting.size());
          }
  }

  public int addToOwnedFeatureChaining(ReferenceValue referenceValue, int index) {
    if (index > ownedFeatureChaining.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedFeatureChaining"), index, referenceValue);
    }
    ownedFeatureChaining.add(index, referenceValue);
    return ownedFeatureChaining.size() - 1;
  }

  public List<ReferenceValue> getOwnedFeatureChaining() {
    return ownedFeatureChaining;
  }

  public int addToOwnedFeatureChaining(FeatureChaining referred) {
    return addToOwnedFeatureChaining(new ReferenceValue(referred, null), ownedFeatureChaining.size());
  }

  public int addToOwnedFeatureChaining(FeatureChaining referred, int index) {
    return addToOwnedFeatureChaining(new ReferenceValue(referred, null), index);
  }

  public void clearOwnedFeatureChaining() {
    while (!ownedFeatureChaining.isEmpty()) {
            removeFromOwnedFeatureChaining(0);
        };
  }

  public void removeFromOwnedFeatureChaining(@NotNull ReferenceValue child) {
    int index = ownedFeatureChaining.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromOwnedFeatureChaining(index);;
  }

  public void removeFromOwnedFeatureChaining(int index) {
    if (ownedFeatureChaining.size() > index) {

            ReferenceValue removed = ownedFeatureChaining.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("ownedFeatureChaining"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + ownedFeatureChaining.size());
          }
  }

  public void setOwnedFeatureChaining(@NotNull List<? extends ReferenceValue> newValue) {
    clearOwnedFeatureChaining();
          for (ReferenceValue referenceValue : newValue) {
              addToOwnedFeatureChaining(referenceValue, ownedFeatureChaining.size());
          }
  }

  public Boolean getIsReadOnly() {
    return isReadOnly;
  }

  public void setIsReadOnly(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isReadOnly"), getIsReadOnly(), value);
        }
    this.isReadOnly = value;
  }

  public Boolean getIsPortion() {
    return isPortion;
  }

  public void setIsPortion(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isPortion"), getIsPortion(), value);
        }
    this.isPortion = value;
  }

  public FeatureDirectionKind getDirection() {
    return direction;
  }

  public void setDirection(FeatureDirectionKind value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("direction"), getDirection(), value);
        }
    this.direction = value;
  }

  public void setOwnedReferenceSubsetting(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("ownedReferenceSubsetting"), 0, ownedReferenceSubsetting);
      }
      ownedReferenceSubsetting = null;
    } else {
      if (partitionObserverCache != null) {
        if (ownedReferenceSubsetting != null) {
          ReferenceValue oldValue = ownedReferenceSubsetting;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("ownedReferenceSubsetting"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedReferenceSubsetting"), 0, value);
        }
      }
      this.ownedReferenceSubsetting = value;
    }
  }

  public ReferenceValue getOwnedReferenceSubsetting() {
    return ownedReferenceSubsetting;
  }

  public void setCrossFeature(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("crossFeature"), 0, crossFeature);
      }
      crossFeature = null;
    } else {
      if (partitionObserverCache != null) {
        if (crossFeature != null) {
          ReferenceValue oldValue = crossFeature;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("crossFeature"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("crossFeature"), 0, value);
        }
      }
      this.crossFeature = value;
    }
  }

  public ReferenceValue getCrossFeature() {
    return crossFeature;
  }

  public void setOwnedCrossSubsetting(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("ownedCrossSubsetting"), 0, ownedCrossSubsetting);
      }
      ownedCrossSubsetting = null;
    } else {
      if (partitionObserverCache != null) {
        if (ownedCrossSubsetting != null) {
          ReferenceValue oldValue = ownedCrossSubsetting;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("ownedCrossSubsetting"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("ownedCrossSubsetting"), 0, value);
        }
      }
      this.ownedCrossSubsetting = value;
    }
  }

  public ReferenceValue getOwnedCrossSubsetting() {
    return ownedCrossSubsetting;
  }

  public void setFeatureTarget(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("featureTarget"), 0, featureTarget);
      }
      featureTarget = null;
    } else {
      if (partitionObserverCache != null) {
        if (featureTarget != null) {
          ReferenceValue oldValue = featureTarget;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("featureTarget"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("featureTarget"), 0, value);
        }
      }
      this.featureTarget = value;
    }
  }

  public ReferenceValue getFeatureTarget() {
    return featureTarget;
  }

  public Boolean getIsNonunique() {
    return isNonunique;
  }

  public void setIsNonunique(Boolean value) {
    if (partitionObserverCache != null) {
          partitionObserverCache.propertyChanged(
              this, this.getClassifier().requirePropertyByName("isNonunique"), getIsNonunique(), value);
        }
    this.isNonunique = value;
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

  public int addToItemType(ReferenceValue referenceValue, int index) {
    if (index > itemType.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("itemType"), index, referenceValue);
    }
    itemType.add(index, referenceValue);
    return itemType.size() - 1;
  }

  public List<ReferenceValue> getItemType() {
    return itemType;
  }

  public int addToItemType(IClassifier referred) {
    return addToItemType(new ReferenceValue(referred, null), itemType.size());
  }

  public int addToItemType(IClassifier referred, int index) {
    return addToItemType(new ReferenceValue(referred, null), index);
  }

  public void clearItemType() {
    while (!itemType.isEmpty()) {
            removeFromItemType(0);
        };
  }

  public void removeFromItemType(@NotNull ReferenceValue child) {
    int index = itemType.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromItemType(index);;
  }

  public void removeFromItemType(int index) {
    if (itemType.size() > index) {

            ReferenceValue removed = itemType.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("itemType"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + itemType.size());
          }
  }

  public void setItemType(@NotNull List<? extends ReferenceValue> newValue) {
    clearItemType();
          for (ReferenceValue referenceValue : newValue) {
              addToItemType(referenceValue, itemType.size());
          }
  }

  public void setTargetInputFeature(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("targetInputFeature"), 0, targetInputFeature);
      }
      targetInputFeature = null;
    } else {
      if (partitionObserverCache != null) {
        if (targetInputFeature != null) {
          ReferenceValue oldValue = targetInputFeature;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("targetInputFeature"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("targetInputFeature"), 0, value);
        }
      }
      this.targetInputFeature = value;
    }
  }

  public ReferenceValue getTargetInputFeature() {
    return targetInputFeature;
  }

  public void setSourceOutputFeature(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("sourceOutputFeature"), 0, sourceOutputFeature);
      }
      sourceOutputFeature = null;
    } else {
      if (partitionObserverCache != null) {
        if (sourceOutputFeature != null) {
          ReferenceValue oldValue = sourceOutputFeature;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("sourceOutputFeature"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("sourceOutputFeature"), 0, value);
        }
      }
      this.sourceOutputFeature = value;
    }
  }

  public ReferenceValue getSourceOutputFeature() {
    return sourceOutputFeature;
  }

  public int addToItemFlowEnd(ReferenceValue referenceValue, int index) {
    if (index > itemFlowEnd.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("itemFlowEnd"), index, referenceValue);
    }
    itemFlowEnd.add(index, referenceValue);
    return itemFlowEnd.size() - 1;
  }

  public List<ReferenceValue> getItemFlowEnd() {
    return itemFlowEnd;
  }

  public int addToItemFlowEnd(ItemFlowEnd referred) {
    return addToItemFlowEnd(new ReferenceValue(referred, null), itemFlowEnd.size());
  }

  public int addToItemFlowEnd(ItemFlowEnd referred, int index) {
    return addToItemFlowEnd(new ReferenceValue(referred, null), index);
  }

  public void clearItemFlowEnd() {
    while (!itemFlowEnd.isEmpty()) {
            removeFromItemFlowEnd(0);
        };
  }

  public void removeFromItemFlowEnd(@NotNull ReferenceValue child) {
    int index = itemFlowEnd.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromItemFlowEnd(index);;
  }

  public void removeFromItemFlowEnd(int index) {
    if (itemFlowEnd.size() > index) {

            ReferenceValue removed = itemFlowEnd.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("itemFlowEnd"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + itemFlowEnd.size());
          }
  }

  public void setItemFlowEnd(@NotNull List<? extends ReferenceValue> newValue) {
    clearItemFlowEnd();
          for (ReferenceValue referenceValue : newValue) {
              addToItemFlowEnd(referenceValue, itemFlowEnd.size());
          }
  }

  public void setItemFeature(ReferenceValue value) {
    if (value == null) {
      if (partitionObserverCache != null) {
        partitionObserverCache.referenceValueRemoved(this, this.getClassifier().requireReferenceByName("itemFeature"), 0, itemFeature);
      }
      itemFeature = null;
    } else {
      if (partitionObserverCache != null) {
        if (itemFeature != null) {
          ReferenceValue oldValue = itemFeature;
          partitionObserverCache.referenceValueChanged(this, this.getClassifier().requireReferenceByName("itemFeature"), 0, oldValue.getReferredID(), oldValue.getResolveInfo(), value.getReferredID(), value.getResolveInfo());
        } else {
          partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("itemFeature"), 0, value);
        }
      }
      this.itemFeature = value;
    }
  }

  public ReferenceValue getItemFeature() {
    return itemFeature;
  }

  public int addToInteraction(ReferenceValue referenceValue, int index) {
    if (index > interaction.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("interaction"), index, referenceValue);
    }
    interaction.add(index, referenceValue);
    return interaction.size() - 1;
  }

  public List<ReferenceValue> getInteraction() {
    return interaction;
  }

  public int addToInteraction(IInteraction referred) {
    return addToInteraction(new ReferenceValue(referred, null), interaction.size());
  }

  public int addToInteraction(IInteraction referred, int index) {
    return addToInteraction(new ReferenceValue(referred, null), index);
  }

  public void clearInteraction() {
    while (!interaction.isEmpty()) {
            removeFromInteraction(0);
        };
  }

  public void removeFromInteraction(@NotNull ReferenceValue child) {
    int index = interaction.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromInteraction(index);;
  }

  public void removeFromInteraction(int index) {
    if (interaction.size() > index) {

            ReferenceValue removed = interaction.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("interaction"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + interaction.size());
          }
  }

  public void setInteraction(@NotNull List<? extends ReferenceValue> newValue) {
    clearInteraction();
          for (ReferenceValue referenceValue : newValue) {
              addToInteraction(referenceValue, interaction.size());
          }
  }

  public int addToBehavior(ReferenceValue referenceValue, int index) {
    if (index > behavior.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("behavior"), index, referenceValue);
    }
    behavior.add(index, referenceValue);
    return behavior.size() - 1;
  }

  public List<ReferenceValue> getBehavior() {
    return behavior;
  }

  public int addToBehavior(IBehavior referred) {
    return addToBehavior(new ReferenceValue(referred, null), behavior.size());
  }

  public int addToBehavior(IBehavior referred, int index) {
    return addToBehavior(new ReferenceValue(referred, null), index);
  }

  public void clearBehavior() {
    while (!behavior.isEmpty()) {
            removeFromBehavior(0);
        };
  }

  public void removeFromBehavior(@NotNull ReferenceValue child) {
    int index = behavior.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromBehavior(index);;
  }

  public void removeFromBehavior(int index) {
    if (behavior.size() > index) {

            ReferenceValue removed = behavior.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("behavior"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + behavior.size());
          }
  }

  public void setBehavior(@NotNull List<? extends ReferenceValue> newValue) {
    clearBehavior();
          for (ReferenceValue referenceValue : newValue) {
              addToBehavior(referenceValue, behavior.size());
          }
  }

  public int addToParameter(ReferenceValue referenceValue, int index) {
    if (index > parameter.size()) {
      throw new IllegalArgumentException("Index must be less than or equal to size");
    }
    if (partitionObserverCache != null) {
      partitionObserverCache.referenceValueAdded(this, this.getClassifier().requireReferenceByName("parameter"), index, referenceValue);
    }
    parameter.add(index, referenceValue);
    return parameter.size() - 1;
  }

  public List<ReferenceValue> getParameter() {
    return parameter;
  }

  public int addToParameter(IFeature referred) {
    return addToParameter(new ReferenceValue(referred, null), parameter.size());
  }

  public int addToParameter(IFeature referred, int index) {
    return addToParameter(new ReferenceValue(referred, null), index);
  }

  public void clearParameter() {
    while (!parameter.isEmpty()) {
            removeFromParameter(0);
        };
  }

  public void removeFromParameter(@NotNull ReferenceValue child) {
    int index = parameter.indexOf(child);
             if (index == -1) {
                 throw new IllegalArgumentException("Child not found: " + child);
             }
             removeFromParameter(index);;
  }

  public void removeFromParameter(int index) {
    if (parameter.size() > index) {

            ReferenceValue removed = parameter.remove(index);
            if (partitionObserverCache != null) {
              partitionObserverCache.referenceValueRemoved(this, getClassifier().requireReferenceByName("parameter"), index, removed);
            }
          } else {
            throw new IllegalArgumentException(
                "Invalid index "
                    + index
                    + " when reference values are "
                    + parameter.size());
          }
  }

  public void setParameter(@NotNull List<? extends ReferenceValue> newValue) {
    clearParameter();
          for (ReferenceValue referenceValue : newValue) {
              addToParameter(referenceValue, parameter.size());
          }
  }

  @Override
  public Object getPropertyValue(Property property) {
    if (Objects.equals(property.getKey(), "sysml-IFeature-isUnique")) {
      return isUnique;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-isOrdered")) {
      return isOrdered;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-isComposite")) {
      return isComposite;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-isEnd")) {
      return isEnd;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-isDerived")) {
      return isDerived;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-isReadOnly")) {
      return isReadOnly;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-isPortion")) {
      return isPortion;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-direction")) {
      return direction;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-isNonunique")) {
      return isNonunique;
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
    if (Objects.equals(property.getKey(), "sysml-IRelationship-isImplied")) {
      return isImplied;
    }
    throw new IllegalStateException("Property " + property + " not found.");
  }

  @Override
  public void setPropertyValue(Property property, Object value) {
    Objects.requireNonNull(property, "Property should not be null");;
    Objects.requireNonNull(property.getKey(), "Cannot assign a property with no Key specified");;
    if (Objects.equals(property.getKey(), "sysml-IFeature-isUnique")) {
      setIsUnique((Boolean) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-isOrdered")) {
      setIsOrdered((Boolean) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-isComposite")) {
      setIsComposite((Boolean) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-isEnd")) {
      setIsEnd((Boolean) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-isDerived")) {
      setIsDerived((Boolean) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-isReadOnly")) {
      setIsReadOnly((Boolean) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-isPortion")) {
      setIsPortion((Boolean) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-direction")) {
      setDirection((FeatureDirectionKind) value);
      return;
    }
    if (Objects.equals(property.getKey(), "sysml-IFeature-isNonunique")) {
      setIsNonunique((Boolean) value);
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
    if (Objects.equals(property.getKey(), "sysml-IRelationship-isImplied")) {
      setIsImplied((Boolean) value);
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
    if (Objects.equals(containment.getKey(), "sysml-IRelationship-ownedRelatedElement")) {
      return ownedRelatedElement;
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
    if (containment.getKey().equals("sysml-IRelationship-ownedRelatedElement")) {
      addToOwnedRelatedElement((IElement) child);
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
    if (containment.getKey().equals("sysml-IRelationship-ownedRelatedElement")) {
      addToOwnedRelatedElement((IElement) child, index);
      return;
    }
    throw new IllegalStateException("Containment " + containment + " not found.");
  }

  @Override
  public List<ReferenceValue> getReferenceValues(@NotNull Reference reference) {
    Objects.requireNonNull(reference, "reference should not be null");;
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-transitionStep")) {
      return Collections.singletonList(transitionStep);
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-triggerStep")) {
      return triggerStep;
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-effectStep")) {
      return effectStep;
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-guardExpression")) {
      return guardExpression;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-relatedFeature")) {
      return relatedFeature;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-association")) {
      return association;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-connectorEnd")) {
      return connectorEnd;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-sourceFeature")) {
      return Collections.singletonList(sourceFeature);
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-targetFeature")) {
      return targetFeature;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-owningType")) {
      return Collections.singletonList(owningType);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-type")) {
      return type;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedRedefinition")) {
      return ownedRedefinition;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedSubsetting")) {
      return ownedSubsetting;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-owningFeatureMembership")) {
      return Collections.singletonList(owningFeatureMembership);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-endOwningType")) {
      return Collections.singletonList(endOwningType);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedTyping")) {
      return ownedTyping;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-featuringType")) {
      return featuringType;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedTypeFeaturing")) {
      return ownedTypeFeaturing;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-chainingFeature")) {
      return chainingFeature;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedFeatureInverting")) {
      return ownedFeatureInverting;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedFeatureChaining")) {
      return ownedFeatureChaining;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedReferenceSubsetting")) {
      return Collections.singletonList(ownedReferenceSubsetting);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-crossFeature")) {
      return Collections.singletonList(crossFeature);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedCrossSubsetting")) {
      return Collections.singletonList(ownedCrossSubsetting);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-featureTarget")) {
      return Collections.singletonList(featureTarget);
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
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemType")) {
      return itemType;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-targetInputFeature")) {
      return Collections.singletonList(targetInputFeature);
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-sourceOutputFeature")) {
      return Collections.singletonList(sourceOutputFeature);
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemFlowEnd")) {
      return itemFlowEnd;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemFeature")) {
      return Collections.singletonList(itemFeature);
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-interaction")) {
      return interaction;
    }
    if (Objects.equals(reference.getKey(), "sysml-IStep-behavior")) {
      return behavior;
    }
    if (Objects.equals(reference.getKey(), "sysml-IStep-parameter")) {
      return parameter;
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public int addReferenceValue(Reference reference, ReferenceValue referredNode) {
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-triggerStep")) {
      return addToTriggerStep(referredNode, triggerStep.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-effectStep")) {
      return addToEffectStep(referredNode, effectStep.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-guardExpression")) {
      return addToGuardExpression(referredNode, guardExpression.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-relatedFeature")) {
      return addToRelatedFeature(referredNode, relatedFeature.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-association")) {
      return addToAssociation(referredNode, association.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-connectorEnd")) {
      return addToConnectorEnd(referredNode, connectorEnd.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-targetFeature")) {
      return addToTargetFeature(referredNode, targetFeature.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-type")) {
      return addToType(referredNode, type.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedRedefinition")) {
      return addToOwnedRedefinition(referredNode, ownedRedefinition.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedSubsetting")) {
      return addToOwnedSubsetting(referredNode, ownedSubsetting.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedTyping")) {
      return addToOwnedTyping(referredNode, ownedTyping.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-featuringType")) {
      return addToFeaturingType(referredNode, featuringType.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedTypeFeaturing")) {
      return addToOwnedTypeFeaturing(referredNode, ownedTypeFeaturing.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-chainingFeature")) {
      return addToChainingFeature(referredNode, chainingFeature.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedFeatureInverting")) {
      return addToOwnedFeatureInverting(referredNode, ownedFeatureInverting.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedFeatureChaining")) {
      return addToOwnedFeatureChaining(referredNode, ownedFeatureChaining.size());
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
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-relatedElement")) {
      return addToRelatedElement(referredNode, relatedElement.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-target")) {
      return addToTarget(referredNode, target.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-source")) {
      return addToSource(referredNode, source.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemType")) {
      return addToItemType(referredNode, itemType.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemFlowEnd")) {
      return addToItemFlowEnd(referredNode, itemFlowEnd.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-interaction")) {
      return addToInteraction(referredNode, interaction.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IStep-behavior")) {
      return addToBehavior(referredNode, behavior.size());
    }
    if (Objects.equals(reference.getKey(), "sysml-IStep-parameter")) {
      return addToParameter(referredNode, parameter.size());
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public int addReferenceValue(Reference reference, int index, ReferenceValue referredNode) {
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-triggerStep")) {
      return addToTriggerStep(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-effectStep")) {
      return addToEffectStep(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-guardExpression")) {
      return addToGuardExpression(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-relatedFeature")) {
      return addToRelatedFeature(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-association")) {
      return addToAssociation(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-connectorEnd")) {
      return addToConnectorEnd(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-targetFeature")) {
      return addToTargetFeature(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-type")) {
      return addToType(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedRedefinition")) {
      return addToOwnedRedefinition(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedSubsetting")) {
      return addToOwnedSubsetting(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedTyping")) {
      return addToOwnedTyping(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-featuringType")) {
      return addToFeaturingType(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedTypeFeaturing")) {
      return addToOwnedTypeFeaturing(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-chainingFeature")) {
      return addToChainingFeature(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedFeatureInverting")) {
      return addToOwnedFeatureInverting(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedFeatureChaining")) {
      return addToOwnedFeatureChaining(referredNode, index);
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
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-relatedElement")) {
      return addToRelatedElement(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-target")) {
      return addToTarget(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IRelationship-source")) {
      return addToSource(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemType")) {
      return addToItemType(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemFlowEnd")) {
      return addToItemFlowEnd(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-interaction")) {
      return addToInteraction(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IStep-behavior")) {
      return addToBehavior(referredNode, index);
    }
    if (Objects.equals(reference.getKey(), "sysml-IStep-parameter")) {
      return addToParameter(referredNode, index);
    }
    throw new IllegalStateException("Reference " + reference + " not found.");
  }

  @Override
  public void setReferenceValues(@NotNull Reference reference,
      @NotNull List<? extends ReferenceValue> values) {
    Objects.requireNonNull(reference, "reference cannot be null");
    Objects.requireNonNull(values, "values cannot be null");
    if (Objects.equals(reference.getKey(), "sysml-FlowConnectionUsage-flowConnectionDefinition")) {
      setFlowConnectionDefinition(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-transitionStep")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setTransitionStep(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-triggerStep")) {
      setTriggerStep(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-effectStep")) {
      setEffectStep(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-guardExpression")) {
      setGuardExpression(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemType")) {
      setItemType(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-targetInputFeature")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setTargetInputFeature(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-sourceOutputFeature")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setSourceOutputFeature(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemFlowEnd")) {
      setItemFlowEnd(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemFeature")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setItemFeature(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-interaction")) {
      setInteraction(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IActionUsage-actionDefinition")) {
      setActionDefinition(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IOccurrenceUsage-occurrenceDefinition")) {
      setOccurrenceDefinition(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IOccurrenceUsage-individualDefinition")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setIndividualDefinition(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IStep-behavior")) {
      setBehavior(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IStep-parameter")) {
      setParameter(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-variant")) {
      setVariant(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-variantMembership")) {
      setVariantMembership(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-owningDefinition")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwningDefinition(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-owningUsage")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwningUsage(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedUsage")) {
      setNestedUsage(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-definition")) {
      setDefinition(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-usage")) {
      setUsage(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-directedUsage")) {
      setDirectedUsage(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedReference")) {
      setNestedReference(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedAttribute")) {
      setNestedAttribute(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedEnumeration")) {
      setNestedEnumeration(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedOccurrence")) {
      setNestedOccurrence(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedItem")) {
      setNestedItem(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedPart")) {
      setNestedPart(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedPort")) {
      setNestedPort(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedConnection")) {
      setNestedConnection(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedFlow")) {
      setNestedFlow(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedInterface")) {
      setNestedInterface(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedAllocation")) {
      setNestedAllocation(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedAction")) {
      setNestedAction(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedState")) {
      setNestedState(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedTransition")) {
      setNestedTransition(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedCalculation")) {
      setNestedCalculation(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedConstraint")) {
      setNestedConstraint(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedRequirement")) {
      setNestedRequirement(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedConcern")) {
      setNestedConcern(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedCase")) {
      setNestedCase(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedAnalysisCase")) {
      setNestedAnalysisCase(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedVerificationCase")) {
      setNestedVerificationCase(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedUseCase")) {
      setNestedUseCase(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedView")) {
      setNestedView(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedViewpoint")) {
      setNestedViewpoint(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedRendering")) {
      setNestedRendering(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedMetadata")) {
      setNestedMetadata(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-relatedFeature")) {
      setRelatedFeature(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-association")) {
      setAssociation(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-connectorEnd")) {
      setConnectorEnd(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-sourceFeature")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setSourceFeature(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-targetFeature")) {
      setTargetFeature(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-owningType")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwningType(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-type")) {
      setType(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedRedefinition")) {
      setOwnedRedefinition(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedSubsetting")) {
      setOwnedSubsetting(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-owningFeatureMembership")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwningFeatureMembership(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-endOwningType")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setEndOwningType(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedTyping")) {
      setOwnedTyping(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-featuringType")) {
      setFeaturingType(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedTypeFeaturing")) {
      setOwnedTypeFeaturing(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-chainingFeature")) {
      setChainingFeature(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedFeatureInverting")) {
      setOwnedFeatureInverting(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedFeatureChaining")) {
      setOwnedFeatureChaining(values);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedReferenceSubsetting")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwnedReferenceSubsetting(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-crossFeature")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setCrossFeature(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedCrossSubsetting")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setOwnedCrossSubsetting(values.isEmpty() ? null : values.get(0));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-featureTarget")) {
      if (values.size() > 0) throw new IllegalArgumentException("Cannot specifiy more than one value for a single-valued reference");
      setFeatureTarget(values.isEmpty() ? null : values.get(0));
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
    if (Objects.equals(reference.getKey(), "sysml-FlowConnectionUsage-flowConnectionDefinition")) {
      if (index >= flowConnectionDefinition.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = flowConnectionDefinition.get(index);
      flowConnectionDefinition.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-transitionStep")) {
      if (index >= 1 || transitionStep == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      transitionStep = transitionStep.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-triggerStep")) {
      if (index >= triggerStep.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = triggerStep.get(index);
      triggerStep.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-effectStep")) {
      if (index >= effectStep.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = effectStep.get(index);
      effectStep.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-guardExpression")) {
      if (index >= guardExpression.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = guardExpression.get(index);
      guardExpression.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemType")) {
      if (index >= itemType.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = itemType.get(index);
      itemType.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-targetInputFeature")) {
      if (index >= 1 || targetInputFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      targetInputFeature = targetInputFeature.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-sourceOutputFeature")) {
      if (index >= 1 || sourceOutputFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      sourceOutputFeature = sourceOutputFeature.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemFlowEnd")) {
      if (index >= itemFlowEnd.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = itemFlowEnd.get(index);
      itemFlowEnd.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemFeature")) {
      if (index >= 1 || itemFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      itemFeature = itemFeature.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-interaction")) {
      if (index >= interaction.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = interaction.get(index);
      interaction.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IActionUsage-actionDefinition")) {
      if (index >= actionDefinition.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = actionDefinition.get(index);
      actionDefinition.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IOccurrenceUsage-occurrenceDefinition")) {
      if (index >= occurrenceDefinition.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = occurrenceDefinition.get(index);
      occurrenceDefinition.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IOccurrenceUsage-individualDefinition")) {
      if (index >= 1 || individualDefinition == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      individualDefinition = individualDefinition.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IStep-behavior")) {
      if (index >= behavior.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = behavior.get(index);
      behavior.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IStep-parameter")) {
      if (index >= parameter.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = parameter.get(index);
      parameter.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-variant")) {
      if (index >= variant.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = variant.get(index);
      variant.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-variantMembership")) {
      if (index >= variantMembership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = variantMembership.get(index);
      variantMembership.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-owningDefinition")) {
      if (index >= 1 || owningDefinition == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningDefinition = owningDefinition.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-owningUsage")) {
      if (index >= 1 || owningUsage == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningUsage = owningUsage.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedUsage")) {
      if (index >= nestedUsage.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedUsage.get(index);
      nestedUsage.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-definition")) {
      if (index >= definition.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = definition.get(index);
      definition.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-usage")) {
      if (index >= usage.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = usage.get(index);
      usage.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-directedUsage")) {
      if (index >= directedUsage.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = directedUsage.get(index);
      directedUsage.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedReference")) {
      if (index >= nestedReference.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedReference.get(index);
      nestedReference.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedAttribute")) {
      if (index >= nestedAttribute.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedAttribute.get(index);
      nestedAttribute.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedEnumeration")) {
      if (index >= nestedEnumeration.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedEnumeration.get(index);
      nestedEnumeration.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedOccurrence")) {
      if (index >= nestedOccurrence.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedOccurrence.get(index);
      nestedOccurrence.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedItem")) {
      if (index >= nestedItem.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedItem.get(index);
      nestedItem.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedPart")) {
      if (index >= nestedPart.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedPart.get(index);
      nestedPart.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedPort")) {
      if (index >= nestedPort.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedPort.get(index);
      nestedPort.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedConnection")) {
      if (index >= nestedConnection.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedConnection.get(index);
      nestedConnection.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedFlow")) {
      if (index >= nestedFlow.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedFlow.get(index);
      nestedFlow.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedInterface")) {
      if (index >= nestedInterface.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedInterface.get(index);
      nestedInterface.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedAllocation")) {
      if (index >= nestedAllocation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedAllocation.get(index);
      nestedAllocation.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedAction")) {
      if (index >= nestedAction.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedAction.get(index);
      nestedAction.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedState")) {
      if (index >= nestedState.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedState.get(index);
      nestedState.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedTransition")) {
      if (index >= nestedTransition.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedTransition.get(index);
      nestedTransition.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedCalculation")) {
      if (index >= nestedCalculation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedCalculation.get(index);
      nestedCalculation.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedConstraint")) {
      if (index >= nestedConstraint.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedConstraint.get(index);
      nestedConstraint.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedRequirement")) {
      if (index >= nestedRequirement.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedRequirement.get(index);
      nestedRequirement.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedConcern")) {
      if (index >= nestedConcern.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedConcern.get(index);
      nestedConcern.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedCase")) {
      if (index >= nestedCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedCase.get(index);
      nestedCase.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedAnalysisCase")) {
      if (index >= nestedAnalysisCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedAnalysisCase.get(index);
      nestedAnalysisCase.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedVerificationCase")) {
      if (index >= nestedVerificationCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedVerificationCase.get(index);
      nestedVerificationCase.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedUseCase")) {
      if (index >= nestedUseCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedUseCase.get(index);
      nestedUseCase.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedView")) {
      if (index >= nestedView.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedView.get(index);
      nestedView.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedViewpoint")) {
      if (index >= nestedViewpoint.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedViewpoint.get(index);
      nestedViewpoint.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedRendering")) {
      if (index >= nestedRendering.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedRendering.get(index);
      nestedRendering.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedMetadata")) {
      if (index >= nestedMetadata.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedMetadata.get(index);
      nestedMetadata.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-relatedFeature")) {
      if (index >= relatedFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = relatedFeature.get(index);
      relatedFeature.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-association")) {
      if (index >= association.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = association.get(index);
      association.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-connectorEnd")) {
      if (index >= connectorEnd.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = connectorEnd.get(index);
      connectorEnd.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-sourceFeature")) {
      if (index >= 1 || sourceFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      sourceFeature = sourceFeature.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-targetFeature")) {
      if (index >= targetFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = targetFeature.get(index);
      targetFeature.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-owningType")) {
      if (index >= 1 || owningType == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningType = owningType.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-type")) {
      if (index >= type.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = type.get(index);
      type.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedRedefinition")) {
      if (index >= ownedRedefinition.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedRedefinition.get(index);
      ownedRedefinition.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedSubsetting")) {
      if (index >= ownedSubsetting.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedSubsetting.get(index);
      ownedSubsetting.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-owningFeatureMembership")) {
      if (index >= 1 || owningFeatureMembership == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningFeatureMembership = owningFeatureMembership.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-endOwningType")) {
      if (index >= 1 || endOwningType == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      endOwningType = endOwningType.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedTyping")) {
      if (index >= ownedTyping.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedTyping.get(index);
      ownedTyping.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-featuringType")) {
      if (index >= featuringType.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = featuringType.get(index);
      featuringType.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedTypeFeaturing")) {
      if (index >= ownedTypeFeaturing.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedTypeFeaturing.get(index);
      ownedTypeFeaturing.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-chainingFeature")) {
      if (index >= chainingFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = chainingFeature.get(index);
      chainingFeature.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedFeatureInverting")) {
      if (index >= ownedFeatureInverting.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedFeatureInverting.get(index);
      ownedFeatureInverting.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedFeatureChaining")) {
      if (index >= ownedFeatureChaining.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedFeatureChaining.get(index);
      ownedFeatureChaining.set(index, original.withReferred(referredNode));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedReferenceSubsetting")) {
      if (index >= 1 || ownedReferenceSubsetting == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      ownedReferenceSubsetting = ownedReferenceSubsetting.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-crossFeature")) {
      if (index >= 1 || crossFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      crossFeature = crossFeature.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedCrossSubsetting")) {
      if (index >= 1 || ownedCrossSubsetting == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      ownedCrossSubsetting = ownedCrossSubsetting.withReferred(referredNode);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-featureTarget")) {
      if (index >= 1 || featureTarget == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      featureTarget = featureTarget.withReferred(referredNode);
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
    if (Objects.equals(reference.getKey(), "sysml-FlowConnectionUsage-flowConnectionDefinition")) {
      if (index >= flowConnectionDefinition.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = flowConnectionDefinition.get(index);
      flowConnectionDefinition.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-transitionStep")) {
      if (index >= 1 || transitionStep == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      transitionStep = transitionStep.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-triggerStep")) {
      if (index >= triggerStep.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = triggerStep.get(index);
      triggerStep.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-effectStep")) {
      if (index >= effectStep.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = effectStep.get(index);
      effectStep.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-ISuccession-guardExpression")) {
      if (index >= guardExpression.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = guardExpression.get(index);
      guardExpression.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemType")) {
      if (index >= itemType.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = itemType.get(index);
      itemType.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-targetInputFeature")) {
      if (index >= 1 || targetInputFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      targetInputFeature = targetInputFeature.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-sourceOutputFeature")) {
      if (index >= 1 || sourceOutputFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      sourceOutputFeature = sourceOutputFeature.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemFlowEnd")) {
      if (index >= itemFlowEnd.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = itemFlowEnd.get(index);
      itemFlowEnd.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-itemFeature")) {
      if (index >= 1 || itemFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      itemFeature = itemFeature.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IItemFlow-interaction")) {
      if (index >= interaction.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = interaction.get(index);
      interaction.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IActionUsage-actionDefinition")) {
      if (index >= actionDefinition.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = actionDefinition.get(index);
      actionDefinition.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IOccurrenceUsage-occurrenceDefinition")) {
      if (index >= occurrenceDefinition.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = occurrenceDefinition.get(index);
      occurrenceDefinition.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IOccurrenceUsage-individualDefinition")) {
      if (index >= 1 || individualDefinition == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      individualDefinition = individualDefinition.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IStep-behavior")) {
      if (index >= behavior.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = behavior.get(index);
      behavior.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IStep-parameter")) {
      if (index >= parameter.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = parameter.get(index);
      parameter.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-variant")) {
      if (index >= variant.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = variant.get(index);
      variant.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-variantMembership")) {
      if (index >= variantMembership.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = variantMembership.get(index);
      variantMembership.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-owningDefinition")) {
      if (index >= 1 || owningDefinition == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningDefinition = owningDefinition.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-owningUsage")) {
      if (index >= 1 || owningUsage == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningUsage = owningUsage.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedUsage")) {
      if (index >= nestedUsage.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedUsage.get(index);
      nestedUsage.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-definition")) {
      if (index >= definition.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = definition.get(index);
      definition.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-usage")) {
      if (index >= usage.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = usage.get(index);
      usage.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-directedUsage")) {
      if (index >= directedUsage.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = directedUsage.get(index);
      directedUsage.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedReference")) {
      if (index >= nestedReference.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedReference.get(index);
      nestedReference.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedAttribute")) {
      if (index >= nestedAttribute.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedAttribute.get(index);
      nestedAttribute.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedEnumeration")) {
      if (index >= nestedEnumeration.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedEnumeration.get(index);
      nestedEnumeration.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedOccurrence")) {
      if (index >= nestedOccurrence.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedOccurrence.get(index);
      nestedOccurrence.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedItem")) {
      if (index >= nestedItem.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedItem.get(index);
      nestedItem.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedPart")) {
      if (index >= nestedPart.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedPart.get(index);
      nestedPart.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedPort")) {
      if (index >= nestedPort.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedPort.get(index);
      nestedPort.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedConnection")) {
      if (index >= nestedConnection.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedConnection.get(index);
      nestedConnection.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedFlow")) {
      if (index >= nestedFlow.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedFlow.get(index);
      nestedFlow.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedInterface")) {
      if (index >= nestedInterface.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedInterface.get(index);
      nestedInterface.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedAllocation")) {
      if (index >= nestedAllocation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedAllocation.get(index);
      nestedAllocation.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedAction")) {
      if (index >= nestedAction.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedAction.get(index);
      nestedAction.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedState")) {
      if (index >= nestedState.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedState.get(index);
      nestedState.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedTransition")) {
      if (index >= nestedTransition.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedTransition.get(index);
      nestedTransition.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedCalculation")) {
      if (index >= nestedCalculation.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedCalculation.get(index);
      nestedCalculation.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedConstraint")) {
      if (index >= nestedConstraint.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedConstraint.get(index);
      nestedConstraint.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedRequirement")) {
      if (index >= nestedRequirement.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedRequirement.get(index);
      nestedRequirement.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedConcern")) {
      if (index >= nestedConcern.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedConcern.get(index);
      nestedConcern.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedCase")) {
      if (index >= nestedCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedCase.get(index);
      nestedCase.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedAnalysisCase")) {
      if (index >= nestedAnalysisCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedAnalysisCase.get(index);
      nestedAnalysisCase.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedVerificationCase")) {
      if (index >= nestedVerificationCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedVerificationCase.get(index);
      nestedVerificationCase.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedUseCase")) {
      if (index >= nestedUseCase.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedUseCase.get(index);
      nestedUseCase.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedView")) {
      if (index >= nestedView.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedView.get(index);
      nestedView.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedViewpoint")) {
      if (index >= nestedViewpoint.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedViewpoint.get(index);
      nestedViewpoint.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedRendering")) {
      if (index >= nestedRendering.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedRendering.get(index);
      nestedRendering.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IUsage-nestedMetadata")) {
      if (index >= nestedMetadata.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = nestedMetadata.get(index);
      nestedMetadata.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-relatedFeature")) {
      if (index >= relatedFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = relatedFeature.get(index);
      relatedFeature.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-association")) {
      if (index >= association.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = association.get(index);
      association.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-connectorEnd")) {
      if (index >= connectorEnd.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = connectorEnd.get(index);
      connectorEnd.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-sourceFeature")) {
      if (index >= 1 || sourceFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      sourceFeature = sourceFeature.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IConnector-targetFeature")) {
      if (index >= targetFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = targetFeature.get(index);
      targetFeature.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-owningType")) {
      if (index >= 1 || owningType == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningType = owningType.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-type")) {
      if (index >= type.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = type.get(index);
      type.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedRedefinition")) {
      if (index >= ownedRedefinition.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedRedefinition.get(index);
      ownedRedefinition.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedSubsetting")) {
      if (index >= ownedSubsetting.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedSubsetting.get(index);
      ownedSubsetting.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-owningFeatureMembership")) {
      if (index >= 1 || owningFeatureMembership == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      owningFeatureMembership = owningFeatureMembership.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-endOwningType")) {
      if (index >= 1 || endOwningType == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      endOwningType = endOwningType.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedTyping")) {
      if (index >= ownedTyping.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedTyping.get(index);
      ownedTyping.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-featuringType")) {
      if (index >= featuringType.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = featuringType.get(index);
      featuringType.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedTypeFeaturing")) {
      if (index >= ownedTypeFeaturing.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedTypeFeaturing.get(index);
      ownedTypeFeaturing.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-chainingFeature")) {
      if (index >= chainingFeature.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = chainingFeature.get(index);
      chainingFeature.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedFeatureInverting")) {
      if (index >= ownedFeatureInverting.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedFeatureInverting.get(index);
      ownedFeatureInverting.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedFeatureChaining")) {
      if (index >= ownedFeatureChaining.size()) throw new IllegalArgumentException("index should be less than the size of the list");;
      ReferenceValue original = ownedFeatureChaining.get(index);
      ownedFeatureChaining.set(index, original.withResolveInfo(resolveInfo));
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedReferenceSubsetting")) {
      if (index >= 1 || ownedReferenceSubsetting == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      ownedReferenceSubsetting = ownedReferenceSubsetting.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-crossFeature")) {
      if (index >= 1 || crossFeature == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      crossFeature = crossFeature.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-ownedCrossSubsetting")) {
      if (index >= 1 || ownedCrossSubsetting == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      ownedCrossSubsetting = ownedCrossSubsetting.withResolveInfo(resolveInfo);
      return;
    }
    if (Objects.equals(reference.getKey(), "sysml-IFeature-featureTarget")) {
      if (index >= 1 || featureTarget == null) throw new IllegalArgumentException("index should be less than the size of the list");;
      featureTarget = featureTarget.withResolveInfo(resolveInfo);
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
