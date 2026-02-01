package io.lionweb.sysml2;

import io.lionweb.model.Node;
import io.lionweb.model.ReferenceValue;
import java.lang.Boolean;

public interface IUsage extends Node, IFeature {
  Boolean getIsReference();

  void setIsReference(Boolean value);

  Boolean getIsVariation();

  void setIsVariation(Boolean value);

  int addToVariant(ReferenceValue referenceValue, int index);

  int addToVariantMembership(ReferenceValue referenceValue, int index);

  void setOwningDefinition(ReferenceValue value);

  ReferenceValue getOwningDefinition();

  void setOwningUsage(ReferenceValue value);

  ReferenceValue getOwningUsage();

  int addToNestedUsage(ReferenceValue referenceValue, int index);

  int addToDefinition(ReferenceValue referenceValue, int index);

  int addToUsage(ReferenceValue referenceValue, int index);

  int addToDirectedUsage(ReferenceValue referenceValue, int index);

  int addToNestedReference(ReferenceValue referenceValue, int index);

  int addToNestedAttribute(ReferenceValue referenceValue, int index);

  int addToNestedEnumeration(ReferenceValue referenceValue, int index);

  int addToNestedOccurrence(ReferenceValue referenceValue, int index);

  int addToNestedItem(ReferenceValue referenceValue, int index);

  int addToNestedPart(ReferenceValue referenceValue, int index);

  int addToNestedPort(ReferenceValue referenceValue, int index);

  int addToNestedConnection(ReferenceValue referenceValue, int index);

  int addToNestedFlow(ReferenceValue referenceValue, int index);

  int addToNestedInterface(ReferenceValue referenceValue, int index);

  int addToNestedAllocation(ReferenceValue referenceValue, int index);

  int addToNestedAction(ReferenceValue referenceValue, int index);

  int addToNestedState(ReferenceValue referenceValue, int index);

  int addToNestedTransition(ReferenceValue referenceValue, int index);

  int addToNestedCalculation(ReferenceValue referenceValue, int index);

  int addToNestedConstraint(ReferenceValue referenceValue, int index);

  int addToNestedRequirement(ReferenceValue referenceValue, int index);

  int addToNestedConcern(ReferenceValue referenceValue, int index);

  int addToNestedCase(ReferenceValue referenceValue, int index);

  int addToNestedAnalysisCase(ReferenceValue referenceValue, int index);

  int addToNestedVerificationCase(ReferenceValue referenceValue, int index);

  int addToNestedUseCase(ReferenceValue referenceValue, int index);

  int addToNestedView(ReferenceValue referenceValue, int index);

  int addToNestedViewpoint(ReferenceValue referenceValue, int index);

  int addToNestedRendering(ReferenceValue referenceValue, int index);

  int addToNestedMetadata(ReferenceValue referenceValue, int index);
}
