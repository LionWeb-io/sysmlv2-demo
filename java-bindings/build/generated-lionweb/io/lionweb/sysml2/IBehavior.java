package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IBehavior extends Node, IClass {
  int addToStep(ReferenceValue referenceValue, int index);

  int addToParameter(ReferenceValue referenceValue, int index);
}
