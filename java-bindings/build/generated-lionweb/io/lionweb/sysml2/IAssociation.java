package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IAssociation extends Node, IClassifier, IRelationship {
  int addToRelatedType(ReferenceValue referenceValue, int index);

  void setSourceType(ReferenceValue value);

  ReferenceValue getSourceType();

  int addToTargetType(ReferenceValue referenceValue, int index);

  int addToAssociationEnd(ReferenceValue referenceValue, int index);
}
