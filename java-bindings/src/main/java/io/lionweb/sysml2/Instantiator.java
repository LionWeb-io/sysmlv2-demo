package io.lionweb.sysml2;

import io.lionweb.model.Node;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Instantiator {

    private long id = 0;
    private final Map<java.lang.Class<?>, Constructor<?>> constructorCache = new HashMap<>();

    public String nextID() {
        return "id" + (++id);
    }

    public <T extends Node> T create(java.lang.Class<T> clazz) {
        Constructor<T> constructor = (Constructor<T>) constructorCache.computeIfAbsent(clazz, c ->
            Arrays.stream(c.getConstructors())
                .filter(cons -> cons.getParameterCount() == 1 && cons.getParameterTypes()[0] == String.class)
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("No constructor with single String parameter found for " + c.getName()))
        );
        try {
            return constructor.newInstance(nextID());
        } catch (InstantiationException | InvocationTargetException | IllegalAccessException e) {
            throw new RuntimeException(e);
        }
    }
}
