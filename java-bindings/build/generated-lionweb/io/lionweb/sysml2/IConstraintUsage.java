package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IConstraintUsage extends Node, IOccurrenceUsage, IBooleanExpression {
  void setConstraintDefinition(ReferenceValue value);

  ReferenceValue getConstraintDefinition();
}
