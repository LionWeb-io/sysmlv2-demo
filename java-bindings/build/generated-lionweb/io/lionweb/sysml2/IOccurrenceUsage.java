package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;
import java.lang.Boolean;

public interface IOccurrenceUsage extends Node, IUsage {
  int addToOccurrenceDefinition(ReferenceValue referenceValue, int index);

  void setIndividualDefinition(ReferenceValue value);

  ReferenceValue getIndividualDefinition();

  Boolean getIsIndividual();

  void setIsIndividual(Boolean value);

  PortionKind getPortionKind();

  void setPortionKind(PortionKind value);
}
