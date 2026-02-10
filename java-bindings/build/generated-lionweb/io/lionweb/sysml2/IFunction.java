package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;
import java.lang.Boolean;

public interface IFunction extends Node, IBehavior {
  int addToExpression(ReferenceValue referenceValue, int index);

  void setResult(ReferenceValue value);

  ReferenceValue getResult();

  Boolean getIsModelLevelEvaluable();

  void setIsModelLevelEvaluable(Boolean value);
}
