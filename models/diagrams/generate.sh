#!/bin/sh

npm run generate

java -DPLANTUML_LIMIT_SIZE=131072 -Xmx1024m -jar plantuml-1.2024.8.jar -tpng artifacts/*.puml
java -DPLANTUML_LIMIT_SIZE=131072 -Xmx1024m -jar plantuml-1.2024.8.jar -tsvg artifacts/*.puml

open -a Opera artifacts/*.svg

