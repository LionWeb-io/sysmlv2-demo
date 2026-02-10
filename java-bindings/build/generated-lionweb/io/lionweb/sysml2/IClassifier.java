package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IClassifier extends Node, IType {
  int addToOwnedSubclassification(ReferenceValue referenceValue, int index);
}
