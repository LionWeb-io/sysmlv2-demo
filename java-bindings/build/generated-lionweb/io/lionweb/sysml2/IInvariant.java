package io.lionweb.sysml2;

import io.lionweb.model.Node;
import java.lang.Boolean;

public interface IInvariant extends Node, IBooleanExpression {
  Boolean getIsNegated();

  void setIsNegated(Boolean value);
}
