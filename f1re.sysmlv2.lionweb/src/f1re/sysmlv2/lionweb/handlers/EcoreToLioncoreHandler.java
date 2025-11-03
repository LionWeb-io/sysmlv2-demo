package f1re.sysmlv2.lionweb.handlers;

import java.io.File;
import java.util.Iterator;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.runtime.Adapters;
import org.eclipse.emf.common.util.Diagnostic;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.resource.URIConverter;
import org.eclipse.ui.IWorkbenchWindow;
import org.eclipse.ui.handlers.HandlerUtil;

import f1re.sysmlv2.lionweb.transform.LionwebTransformer;
import f1re.sysmlv2.lionweb.transform.MMTransformer;
import org.eclipse.jface.viewers.IStructuredSelection;

public class EcoreToLioncoreHandler extends AbstractHandler {	
	
	@Override
	public Object execute(ExecutionEvent event) throws ExecutionException {
		
		IStructuredSelection selection = HandlerUtil.getCurrentStructuredSelection(event);

		if (!selection.isEmpty()) {
			IResource resource = Adapters.adapt(selection.getFirstElement(), IResource.class);

			if (resource != null && resource instanceof IFile) {
				IFile file = (IFile)resource;
				System.out.println(resource.getName());
				
				LionwebTransformer transformer = new LionwebTransformer();
                transformer.transformEcore2Lionweb(resource.getLocation().toString());
			}
		}
		
		return null;
	}
	
}
