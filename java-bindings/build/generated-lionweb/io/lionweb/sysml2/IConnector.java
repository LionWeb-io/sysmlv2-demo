package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IConnector extends Node, IFeature, IRelationship {
  int addToRelatedFeature(ReferenceValue referenceValue, int index);

  int addToAssociation(ReferenceValue referenceValue, int index);

  int addToConnectorEnd(ReferenceValue referenceValue, int index);

  void setSourceFeature(ReferenceValue value);

  ReferenceValue getSourceFeature();

  int addToTargetFeature(ReferenceValue referenceValue, int index);
}
