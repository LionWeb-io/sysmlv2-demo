package f1re.sysmlv2.lionweb.transform;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.util.List;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.emf.common.util.BasicDiagnostic;
import org.eclipse.emf.common.util.Diagnostic;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.m2m.qvt.oml.BasicModelExtent;
import org.eclipse.m2m.qvt.oml.ExecutionContextImpl;
import org.eclipse.m2m.qvt.oml.ExecutionDiagnostic;
import org.eclipse.m2m.qvt.oml.ModelExtent;
import org.eclipse.m2m.qvt.oml.TransformationExecutor;
import org.eclipse.m2m.qvt.oml.util.WriterLog;

public class LionwebTransformer {
	
	private final URI ecoreToLionWeb = URI.createPlatformPluginURI("/f1re.sysmlv2.lionweb/transforms/TransformMetaModel2LW.qvto", false);
	
	
	public void transformEcore2Lionweb(String inputFilePath) {
		
		// Get the URI of the input model file.
		URI fileURI = URI.createFileURI(inputFilePath);
		
		if (!fileURI.fileExtension().equals("ecore")) {
			System.out.println("Not an ecore meta-model selected: " + inputFilePath);
			System.out.println("File extension: " + fileURI.fileExtension());
			return;
		}

		runTransformation(ecoreToLionWeb, fileURI, URI.createFileURI(fileURI.trimFileExtension().toFileString() + "_lionweb.ecore"));
	}
	
	private void runTransformation(URI transformationURI, URI inputFile, URI outputFile) {
		// load the input model
		ModelExtent input = loadModel(inputFile);
		// create an empty extent to catch the output
		ModelExtent output = new BasicModelExtent();		
		
		// create executor for the given transformation
		TransformationExecutor qvtExecutor = new TransformationExecutor(transformationURI);
		
		// setup the execution environment details -> 
		// configuration properties, logger, monitor object etc.
		ExecutionContextImpl context = new ExecutionContextImpl();
		context.setConfigProperty("keepModeling", true);
		context.setLog(new WriterLog(new OutputStreamWriter(System.out)));
		
		// run the transformation assigned to the executor with the given 
		// input and output and execution context -> ChangeTheWorld(in, out)
		// Remark: variable arguments count is supported
		System.out.println("Executing QVTo transformation from: " + transformationURI.path());
		ExecutionDiagnostic result = qvtExecutor.execute(context, input, output);		
		
		// check the result for success
		if(result.getSeverity() == Diagnostic.OK) {
			saveModel(output, outputFile);
		} else {
			// turn the result diagnostic into status and send it to error log			
			IStatus status = BasicDiagnostic.toIStatus(result);
			System.out.println(status);
		}
	}
	
	private ModelExtent loadModel(URI fileURI) {
		// Create a resource set.
	   	ResourceSet resourceSet = new ResourceSetImpl();	
	
		// Demand load the resource for this file.
		Resource resource = resourceSet.getResource(fileURI, true);
		EList<EObject> inObjects = resource.getContents();
		
		// create the input extent with its initial contents
		return new BasicModelExtent(inObjects);
	}
	
	private void saveModel(ModelExtent model, URI fileURI) {
		try {
			// the output objects got captured in the output extent
			List<EObject> outObjects = model.getContents();
			// persist those into a new resource			
		    ResourceSet resourceSet2 = new ResourceSetImpl();
		    Resource outResource = resourceSet2.createResource(fileURI);
			outResource.getContents().addAll(outObjects);			
			outResource.save(Collections.emptyMap());
			
			System.out.println("Saved new model to: " + fileURI.path());
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
