package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IEventOccurrenceUsage extends Node, IOccurrenceUsage {
  void setEventOccurrence(ReferenceValue value);

  ReferenceValue getEventOccurrence();
}
