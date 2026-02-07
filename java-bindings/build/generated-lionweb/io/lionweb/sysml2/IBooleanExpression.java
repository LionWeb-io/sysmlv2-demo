package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IBooleanExpression extends Node, IExpression {
  void setPredicate(ReferenceValue value);

  ReferenceValue getPredicate();
}
