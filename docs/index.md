# Sample SourceDocs (Sphinx)

Welcome to our awesome SourceDocs for Sphinx!

**Core subproject**

<https://danielmartin-rtd-tutorial-mkdocs.readthedocs.io/projects/core/en/main/>

**iOS subproject**

<https://danielmartin-rtd-tutorial-mkdocs.readthedocs.io/projects/ios/en/main/>

## Sample File Structure for Sphinx and Readthedocs in a Monorepo

```console
.
├── .gitignore
├── .readthedocs.yaml (**Configuration file for ReadTheDocs**)
├── README.md
├── core (Documentation subproject)
│   ├── .readthedocs.yaml
│   ├── docs
│   │   ├── Makefile (If you want to build the documentation manually)
│   │   ├── add-new-api.md
│   │   ├── conf.py (Configuration file for Sphinx)
│   │   ├── getting-started.md
│   │   ├── make.bat (If you want to build the documentation manually on Windows)
│   │   └── requirements.txt (Declare Python dependencies)
│   ├── index.md (Landing page for subproject)
│   └── subfolder
│       ├── docs (Documentation next to source code)
│       │   └── index.md
│       └── subsubfolder
│           └── docs (**Documentation next to source code**)
│               └── index.md
├── docs
│   ├── Makefile
│   ├── conf.py
│   ├── index.md
│   ├── make.bat
│   └── requirements.txt
└── ios (Documentation subproject)
    ├── .readthedocs.yaml
    └── docs
        ├── Makefile
        ├── conf.py
        ├── configure-page-view.md
        ├── getting-started.md
        ├── index.md
        ├── make.bat
        └── requirements.txt

```

tl;dr; On each subproject that you want to add to the org, follow these steps:

1. Add a `readthedocs.yaml` file.
2. Add a `docs/` folder.
3. Inside the `docs/` folder, add the following files: `conf.py` (to configure Sphinx), `requirements.txt` (to configure Python dependencies), `Makefile/make.bat` (optionally, to build the docs locally). **These files could be generated automatically from a template.**
4. Configure the ReadTheDocs website and add a new subproject.
