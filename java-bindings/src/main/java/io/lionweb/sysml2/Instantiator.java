package io.lionweb.sysml2;

import io.lionweb.model.Node;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.util.Arrays;

public class Instantiator {

    private long id = 0;

    public String nextID() {
        return "id" + (++id);
    }

    public <T extends Node> T create(java.lang.Class<T> clazz) {
        Constructor<T> constructor = (Constructor<T>) Arrays.stream(clazz.getConstructors()).filter(c -> c.getParameterCount() == 1).findFirst().get();
        try {
            return constructor.newInstance(nextID());
        } catch (InstantiationException | InvocationTargetException | IllegalAccessException e) {
            throw new RuntimeException(e);
        }
    }
}
