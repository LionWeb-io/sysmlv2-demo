package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;

public interface IActionUsage extends Node, IOccurrenceUsage, IStep {
  int addToActionDefinition(ReferenceValue referenceValue, int index);
}
