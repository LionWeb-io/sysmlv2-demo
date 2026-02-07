package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;
import java.lang.Boolean;

public interface IExpression extends Node, IStep {
  void setFunction(ReferenceValue value);

  ReferenceValue getFunction();

  void setResult(ReferenceValue value);

  ReferenceValue getResult();

  Boolean getIsModelLevelEvaluable();

  void setIsModelLevelEvaluable(Boolean value);
}
