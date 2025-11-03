package f1re.sysmlv2.lionweb.handlers;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.runtime.Adapters;
import org.eclipse.emf.codegen.ecore.genmodel.GenModel;
import org.eclipse.emf.codegen.ecore.genmodel.GenPackage;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EcorePackage;
import org.eclipse.emf.ecore.plugin.EcorePlugin;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.ui.handlers.HandlerUtil;

import io.lionweb.lioncore.java.language.Language;
import io.lionweb.lioncore.java.serialization.JsonSerialization;
import io.lionweb.lioncore.java.serialization.SerializationProvider;
import io.lionweb.lioncore.java.LionWebVersion;
import io.lionweb.lioncore.java.emf.*;

public class EcoreToJsonHandler extends AbstractHandler {
	
	List<Language> metamodels = new ArrayList<Language>();

	@Override
	public Object execute(ExecutionEvent event) throws ExecutionException {
		
		IStructuredSelection selection = HandlerUtil.getCurrentStructuredSelection(event);

		if (!selection.isEmpty()) {
			IResource resource = Adapters.adapt(selection.getFirstElement(), IResource.class);

			if (resource != null && resource instanceof IFile) {
				System.out.println(resource.getName());
				importLanguagesFromEcore(resource.getLocation().toString());
				
				System.out.println("Imported " + metamodels.size() + " languages into lionweb:");
	            for (Language lang: metamodels) {
	            	System.out.println("	" + lang.getName());
	            	try {
	            		File outputFile = new File(resource.getLocation().removeFileExtension().toString() + "_lionweb.json");
//	            		JsonSerialization jsonSerialization = SerializationProvider.getStandardJsonSerialization(LionWebVersion.v2023_1);
	            		JsonSerialization.saveLanguageToFile(lang, outputFile);
						System.out.println("	exported into: " + outputFile.getPath());
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
	            }
			}
		}
		
		return null;
	}
	
	private void importLanguagesFromEcore(String inputFilePath) {
		// Get the URI of the input model file.
		URI fileURI = URI.createFileURI(inputFilePath);
		
		if (!fileURI.fileExtension().equals("ecore")) {
			System.out.println("Not an ecore meta-model selected: " + inputFilePath);
			System.out.println("File extension: " + fileURI.fileExtension());
			return;
		}
		
		// Create a resource set.
	   	ResourceSet resourceSet = new ResourceSetImpl();	
	
		// Demand load the resource for this file.
		Resource resource = resourceSet.getResource(fileURI, true);
		
		// LionWeb EMF importer
		EMFMetamodelImporter lionwebEcoreImporter = new EMFMetamodelImporter(LionWebVersion.v2023_1);
		
		for (EObject content : resource.getContents()) {
			if (content.eClass().getName().equals(EcorePackage.Literals.EPACKAGE.getName())) {
				EPackage currentPackage = (EPackage)content;
				metamodels.add(lionwebEcoreImporter.importEPackage(currentPackage));
			}
		}
	}

	
	
}
