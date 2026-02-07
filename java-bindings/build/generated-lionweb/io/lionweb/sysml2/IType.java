package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;
import java.lang.Boolean;

public interface IType extends Node, INamespace {
  int addToOwnedFeatureMembership(ReferenceValue referenceValue, int index);

  int addToOwnedFeature(ReferenceValue referenceValue, int index);

  int addToOwnedEndFeature(ReferenceValue referenceValue, int index);

  int addToFeature(ReferenceValue referenceValue, int index);

  int addToInput(ReferenceValue referenceValue, int index);

  int addToOutput(ReferenceValue referenceValue, int index);

  Boolean getIsAbstract();

  void setIsAbstract(Boolean value);

  int addToInheritedMembership(ReferenceValue referenceValue, int index);

  int addToEndFeature(ReferenceValue referenceValue, int index);

  Boolean getIsSufficient();

  void setIsSufficient(Boolean value);

  void setOwnedConjugator(ReferenceValue value);

  ReferenceValue getOwnedConjugator();

  Boolean getIsConjugated();

  void setIsConjugated(Boolean value);

  int addToInheritedFeature(ReferenceValue referenceValue, int index);

  void setMultiplicity(ReferenceValue value);

  ReferenceValue getMultiplicity();

  int addToUnioningType(ReferenceValue referenceValue, int index);

  int addToOwnedIntersecting(ReferenceValue referenceValue, int index);

  int addToIntersectingType(ReferenceValue referenceValue, int index);

  int addToOwnedUnioning(ReferenceValue referenceValue, int index);

  int addToOwnedDisjoining(ReferenceValue referenceValue, int index);

  int addToFeatureMembership(ReferenceValue referenceValue, int index);

  int addToDifferencingType(ReferenceValue referenceValue, int index);

  int addToOwnedDifferencing(ReferenceValue referenceValue, int index);

  int addToDirectedFeature(ReferenceValue referenceValue, int index);

  int addToOwnedSpecialization(ReferenceValue referenceValue, int index);
}
