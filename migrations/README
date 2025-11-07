# Getting Started

This project uses LinkML and [just](https://github.com/casey/just). To get started you can run the following:


```bash
# install the project
poetry install

# Linux / Mac
source .venv/bin/activate

# Windows
.venv/Scripts/activate
```

# Generating SQLAlchemy from LinkML

SQL Alchemy projects require the Schema and Enums to be generated seperately in most cases.
This project will generate both files using just:



```bash
just gen
```

This will produce two files in `migrations/`

- `migrations/schema.py`
- `migrations/enums.py`

# Producing SVG Renders

```bash
npm install -g dbdocs
npm install -g @softwaretechnik/dbml-renderer

just render
```