package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IAnnotatingElement extends Node, IElement {
  int addToAnnotatedElement(ReferenceValue referenceValue, int index);

  int addToOwnedAnnotatingRelationship(ReferenceValue referenceValue, int index);

  int addToAnnotation(ReferenceValue referenceValue, int index);

  void setOwningAnnotatingRelationship(ReferenceValue value);

  ReferenceValue getOwningAnnotatingRelationship();
}
