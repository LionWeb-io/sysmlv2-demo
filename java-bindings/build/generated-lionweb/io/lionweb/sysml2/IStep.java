package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IStep extends Node, IFeature {
  int addToBehavior(ReferenceValue referenceValue, int index);

  int addToParameter(ReferenceValue referenceValue, int index);
}
