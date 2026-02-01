package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IFeaturing extends Node, IRelationship {
  void setType(ReferenceValue value);

  ReferenceValue getType();

  void setFeature(ReferenceValue value);

  ReferenceValue getFeature();
}
