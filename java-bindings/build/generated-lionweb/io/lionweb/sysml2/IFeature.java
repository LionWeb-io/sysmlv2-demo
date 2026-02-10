package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;
import java.lang.Boolean;

public interface IFeature extends Node, IType {
  void setOwningType(ReferenceValue value);

  ReferenceValue getOwningType();

  Boolean getIsUnique();

  void setIsUnique(Boolean value);

  Boolean getIsOrdered();

  void setIsOrdered(Boolean value);

  int addToType(ReferenceValue referenceValue, int index);

  int addToOwnedRedefinition(ReferenceValue referenceValue, int index);

  int addToOwnedSubsetting(ReferenceValue referenceValue, int index);

  void setOwningFeatureMembership(ReferenceValue value);

  ReferenceValue getOwningFeatureMembership();

  Boolean getIsComposite();

  void setIsComposite(Boolean value);

  Boolean getIsEnd();

  void setIsEnd(Boolean value);

  void setEndOwningType(ReferenceValue value);

  ReferenceValue getEndOwningType();

  int addToOwnedTyping(ReferenceValue referenceValue, int index);

  int addToFeaturingType(ReferenceValue referenceValue, int index);

  int addToOwnedTypeFeaturing(ReferenceValue referenceValue, int index);

  Boolean getIsDerived();

  void setIsDerived(Boolean value);

  int addToChainingFeature(ReferenceValue referenceValue, int index);

  int addToOwnedFeatureInverting(ReferenceValue referenceValue, int index);

  int addToOwnedFeatureChaining(ReferenceValue referenceValue, int index);

  Boolean getIsReadOnly();

  void setIsReadOnly(Boolean value);

  Boolean getIsPortion();

  void setIsPortion(Boolean value);

  FeatureDirectionKind getDirection();

  void setDirection(FeatureDirectionKind value);

  void setOwnedReferenceSubsetting(ReferenceValue value);

  ReferenceValue getOwnedReferenceSubsetting();

  void setCrossFeature(ReferenceValue value);

  ReferenceValue getCrossFeature();

  void setOwnedCrossSubsetting(ReferenceValue value);

  ReferenceValue getOwnedCrossSubsetting();

  void setFeatureTarget(ReferenceValue value);

  ReferenceValue getFeatureTarget();

  Boolean getIsNonunique();

  void setIsNonunique(Boolean value);
}
