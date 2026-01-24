package io.lionweb.sysml2;

public class Example {




    static void main(String[] args) {
        Instantiator instantiator = new Instantiator();
        Package pkg = instantiator.create(Package.class);
        pkg.setName("BrakeSystem");

    }
}
