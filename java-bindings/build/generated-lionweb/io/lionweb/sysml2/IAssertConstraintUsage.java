package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IAssertConstraintUsage extends Node, IConstraintUsage, IInvariant {
  void setAssertedConstraint(ReferenceValue value);

  ReferenceValue getAssertedConstraint();
}
