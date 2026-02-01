package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IItemUsage extends Node, IOccurrenceUsage {
  int addToItemDefinition(ReferenceValue referenceValue, int index);
}
