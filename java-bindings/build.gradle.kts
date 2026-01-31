plugins {
    id("io.lionweb") version "1.3.1-SNAPSHOT"
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

repositories {
    mavenLocal()
    mavenCentral()
}

tasks.findByName("compileJava")?.dependsOn("generateLWLanguages", "generateLWNodeClasses")