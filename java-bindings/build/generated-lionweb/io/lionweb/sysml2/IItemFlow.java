package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IItemFlow extends Node, IConnector, IStep {
  int addToItemType(ReferenceValue referenceValue, int index);

  void setTargetInputFeature(ReferenceValue value);

  ReferenceValue getTargetInputFeature();

  void setSourceOutputFeature(ReferenceValue value);

  ReferenceValue getSourceOutputFeature();

  int addToItemFlowEnd(ReferenceValue referenceValue, int index);

  void setItemFeature(ReferenceValue value);

  ReferenceValue getItemFeature();

  int addToInteraction(ReferenceValue referenceValue, int index);
}
