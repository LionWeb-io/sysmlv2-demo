package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface ISuccession extends Node, IConnector {
  void setTransitionStep(ReferenceValue value);

  ReferenceValue getTransitionStep();

  int addToTriggerStep(ReferenceValue referenceValue, int index);

  int addToEffectStep(ReferenceValue referenceValue, int index);

  int addToGuardExpression(ReferenceValue referenceValue, int index);
}
