package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;
import java.lang.Boolean;

public interface IRelationship extends Node, IElement {
  int addToOwnedRelatedElement(IElement child, int index);

  void setOwningRelatedElement(ReferenceValue value);

  ReferenceValue getOwningRelatedElement();

  int addToRelatedElement(ReferenceValue referenceValue, int index);

  int addToTarget(ReferenceValue referenceValue, int index);

  int addToSource(ReferenceValue referenceValue, int index);

  Boolean getIsImplied();

  void setIsImplied(Boolean value);
}
