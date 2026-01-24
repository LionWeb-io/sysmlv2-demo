plugins {
    id("io.lionweb") version "1.2.6-SNAPSHOT"
    id("java")
}

lionweb {
    languagesDirectory = file("../models")
    defaultPackageName = "io.lionweb.sysml2"
    primitiveTypes = mapOf(
        "types-String" to "java.lang.String",
        "types-Boolean" to "java.lang.Boolean",
        "types-Integer" to "java.lang.Integer",
        "types-Real" to "java.lang.Double")
}

sourceSets {
    main {
        java.srcDirs("src/main/java")
        java.srcDirs("build/generated-lionweb")
    }
}