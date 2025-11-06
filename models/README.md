# README

## Diagrams

The `diagrams/` directory contains PlantUML diagrams (including exports to PNG and SVG) of the SysMLv2 language – as exported to LionWeb format –, and code to generate those diagrams.

Execute the following to print a URL for a required JAR file:

```shell
$ ./print-PlantUML-jar-url.sh
```

Download the JAR from that URL, and place/copy it into the `diagrams/` directory.

Execute the following to download all required NPM dependencies:

```shell
npm install
```

Execute the following to generate the diagrams:

```shell
$ ./generate.sh
```


## TypeScript

The `typescript/` directory contains TypeScript types for the SysMLv2 language – in the `src/` subdirectory –, and code to generate that.

Execute the following in the `typescript/` directory to download all required NPM dependencies:

```shell
npm install
```

Execute the following to generate the TypeScript code into the `src/` subdirectory:

```shell
$ node generate.js
```

This “JavaScript-let” relies on the following features from various LionWeb TypeScript libraries:

* `generateApiFromLanguages(<array of languages>)` from `@lionweb/class-core-generator`: generate a complete API for a collection of LionWeb languages
* `deserializeLanguages(<serialization chunk>)` from `@lionweb/core`: deserialize a LionWeb serialization chunk containing one or more languages, as instances of `Language`
* `readFileAsJson(<path>)` from `@lionweb/utilities`: read and parse a JSON file from the filesystem
* (`setEOLStyleFromOS()` from `littoral-templates-node`: ensure that line endings are OS-compliant)

