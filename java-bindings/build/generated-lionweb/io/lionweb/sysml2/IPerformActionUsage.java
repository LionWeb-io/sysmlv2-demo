package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IPerformActionUsage extends Node, IActionUsage, IEventOccurrenceUsage {
  void setPerformedAction(ReferenceValue value);

  ReferenceValue getPerformedAction();
}
