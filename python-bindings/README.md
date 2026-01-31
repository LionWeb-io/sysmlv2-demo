# Python Bindings for SysML2

You typically create a Python virtual environment and install the package there:

```
python3 -m venv venv
source venv/bin/activate
pip install lionweb
```

Launch generation:
```
lionweb-gen ../models/types_lionweb.json sysml2py/types
lionweb-gen ../models/kerml_lionweb_lionweb.json -d../models/types_lionweb.json sysml2py/kerml --lp types=sysml2py.types \
--pt String=str --pt Boolean=bool --pt Integer=int --pt Real=float
lionweb-gen ../models/SysML_lionweb_lionweb.json -d../models/types_lionweb.json sysml2py/sysml --lp types=sysml2py.types \
--pt String=str --pt Boolean=bool --pt Integer=int --pt Real=float 
```