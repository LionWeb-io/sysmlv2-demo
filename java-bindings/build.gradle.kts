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

repositories {
    mavenLocal()
    mavenCentral()
}

dependencies {
    implementation("io.lionweb.lionweb-java:lionweb-java-2024.1-core:1.2.6-SNAPSHOT")
}