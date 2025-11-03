package f1re.sysmlv2.lionweb.transform

import java.io.File
import java.io.FileOutputStream
import java.io.IOException
import java.util.Collections
import java.util.Iterator
import org.eclipse.emf.common.util.EList
import org.eclipse.emf.common.util.URI
import org.eclipse.emf.ecore.EAttribute
import org.eclipse.emf.ecore.EClass
import org.eclipse.emf.ecore.EPackage
import org.eclipse.emf.ecore.EStructuralFeature
import org.eclipse.emf.ecore.EcoreFactory
import org.eclipse.emf.ecore.impl.EcoreFactoryImpl
import org.eclipse.emf.ecore.resource.Resource
import org.eclipse.emf.ecore.resource.ResourceSet
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl
import org.eclipse.emf.ecore.util.EcoreUtil
import org.eclipse.ui.SelectionListenerFactory.ISelectionModel
import java.util.Map
import java.util.HashMap
import org.eclipse.emf.ecore.util.EcoreUtil.Copier
import org.eclipse.emf.ecore.EObject

class MMTransformer {
	
	EcoreFactory factory = new EcoreFactoryImpl()
	
	def void transform(String inputFilePath) {		
		
		// Get the URI of the input model file.
		var URI fileURI = URI.createFileURI(inputFilePath);
		
		if (fileURI.fileExtension != "ecore") {
			System.out.println("Not an ecore meta-model selected")
			return
		}

		// Create a resource set.
	   	var ResourceSet resourceSet = new ResourceSetImpl()		
	
		// Demand load the resource for this file.
		var Resource resource = resourceSet.getResource(fileURI, true);
	
		// Process the content of the file
		for(obj: resource.allContents.toIterable.filter(typeof(EClass))) {
			var newobj = attributesWithHighMultiplicity(obj)
			EcoreUtil.replace(obj, newobj)
		}

		// Save the contents of the resource to a new file
		try {
			val outputFile = new File(fileURI.trimFileExtension.toFileString + "_lionweb.ecore")
			resource.save(new FileOutputStream(outputFile), Collections.EMPTY_MAP);
			System.out.println("Saved new model to: " + outputFile.path);
		}
		catch (IOException e) {
			System.out.println(e.stackTrace)
		}
	}
	
// !!! Create methods in Xtend allow to do graph transformation in one pass where it usually needs two passes. 
// That means you don’t need to separate a translation from one graph to another in the typical two phases: 
// tree construction and interlinking the tree nodes. You basically just need to write the whole transformation 
// using create methods and the built-in identity preservation will take care of the rest.
	
	
	// LionCore supports properties (features with DataType as a type) only with 0..1 multiplicity
	// For the Ecore attributes with high multiplicity we introduce an intermediate link and a concept to hold this attribute
	def EClass attributesWithHighMultiplicity(EClass original) {		
		var Iterator<EStructuralFeature> structuralFeatures = original.EStructuralFeatures.iterator
		// Map to keep track of the changes to the structural features of the ecore class
		var Map<EStructuralFeature, EStructuralFeature> replaceFeatures = new HashMap
		
		for (eattr: original.EStructuralFeatures) {
			if (eattr instanceof EAttribute && eattr.many) {				
				// Check whether such an intermediate class already exists in the package: by name and by type of the attribute
				val intermClassName = eattr.name.substring(0, 1).toUpperCase() + eattr.name.substring(1, eattr.name.length) + "Container"				
				var EClass intermClass = (original.eContainer as EPackage).EClassifiers.findFirst[ec | 
					ec.name == intermClassName && (ec as EClass).EAllStructuralFeatures.findFirst [ ea |
						ea.name == eattr.name && ea.EType == eattr.EType
					] !== null
				] as EClass
				
				// If the intermediate class is not there yet, create it
				if(intermClass === null) {					
					intermClass = factory.createEClass
					intermClass.name = intermClassName
					intermClass.abstract = false
					(original.eContainer as EPackage).EClassifiers.add(intermClass)
					
					val intermAttribute = EcoreUtil.copy(eattr)
					intermAttribute.upperBound = 1
					intermClass.EStructuralFeatures.add(intermAttribute)
				}				
				
				// Create a reference to replace the attribute
				val intermContainment = factory.createEReference
				intermContainment.containment = true
				intermContainment.EType = intermClass
				intermContainment.upperBound = -1
				intermContainment.name = eattr.name + "Container"
				
				// Save the change for later
				replaceFeatures.put(eattr, intermContainment)
				System.out.println("Processed an attribute with high multiplicity: " + eattr.name + " in " + original.name);
			}
		}
		
		// Apply changes to the structural features of the original class
		for(replacePair: replaceFeatures.entrySet()) {
			EcoreUtil.replace(replacePair.key, replacePair.value)
		}
		
		return original;
	}
	
//	def EObject copy(EObject eObject)
//	{
//		var copier = new Copier()
//		var result = copier.copy(eObject);
//		copier.copyReferences();
//		return result;
//	}
	
}