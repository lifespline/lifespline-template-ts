Getting Started
===============

About
-----

Introduction to Typescript using the vscode IDE.

Typescript
----------

The key value proposition of JS:

   The ability to run your code anywhere and on every platform, browser, or host.

JS wasn't designed however for very complex applications and it lacks features from more mature languages. TS is a superset of JS (`ES6 <https://www.ecma-international.org/ecma-262/6.0/>`_ to be precise), meaning it **extends** JS, that is:

* Any JS file is a TS file: It suffices to change the extension from `.js` to `.ts`. Indeed, any TS file compiles into JS before being executed.
* Any TS file `builds/transpiles <https://babeljs.io/>`_ or `compiles <https://www.typescriptlang.org/download>`_ to an equivalent JS file: Most runtimes can't process TS natively, only JS. No browser can interpret TS.
* The superset adds to JS some of the features of more mature languages (although you need to configure the compiler appropriately in some cases):
   * static typing
   * interfaces
   * generics
   * abstract classes
   * data modifiers
   * optionals
   * function overloading
   * decorators
   * type utils
   * readonly keyword


Installing Typescript
---------------------

TS dependencies

.. code:: shell

   $ sudo apt update
   $ sudo apt install nodejs npm
   $ yes | sudo apt autoremove

TS

.. code:: shell

   $ sudo npm install -g typescript

Compiling a TS file into JS
---------------------------

The TS compiler is configured in ``tsconfig.json`` (which can be created by running ``tsc --init``) and it enables the configuration of the compilation process. Some of the the possible configuration options:

``include``: all the files necessary to compile this project
* ``types``: ["jest"] See this `vid::5.37 <https://www.youtube.com/watch?v=6oHy58OOQkA>`_ for an explanation.
* ``noEmit``: ``true`` if using Babel.
* ``target``: the version of JS to transpile the TS files into (all browsers implement at least ``ES2016``)
* ``module``: 
* ``rootDir``: directory with TS source files
* ``outDir``: transpiled JS source files
* ``removeComments``: remove comments on transpilation
* ``strict``: ``true``, to enable all default JS compiling specifications
* ``strictNullChecks``: ``true``, evaluate null values
* ``noEmit``: 
* ``noEmitOnError``: Don't transpile into JS if there are errors in TS
* ``sourceMap``: maps how each TS line maps to the transpiled JS source code. This is necessary to debug TS code
* ``noImplicitAny``: don't compile is a varaible is implicitly declared as of type any
* ``noUnusedParameters``: Don't allow for unused parameters
* ``noImplicitReturns``: Don't allow the compiler to infer the return type from the return statements, which can cause problems.
* ``noUnusedLocals``: Don't allow unused variables.
* ``strictPropertyInitialization``: ``false``, enable declaring class properties without initializing them in the constructor.

.. code-block:: json

   {
      "include": [
          "samples/**/*.ts",
          "samples/**/test/*.ts"
      ],
      "exclude": [],
      "compilerOptions": {
          "types": [
            "jest"
          ],
          "target": "es6",
          "module": "CommonJS",
          "sourceMap": true,
          "strict": true,
          "strictNullChecks": true,
          "noEmitOnError": true,
          "noImplicitAny": true,
          "noImplicitReturns": true,
          "noUnusedParameters": true,
          "noUnusedLocals": true,
          "removeComments": true,
          "strictPropertyInitialization": false,
          "outDir": "dist"
      }
   }


.. note::

   Running ``tsc`` compiles all TS files found in ``compilerOptions.rootDir``, or in the intersection of ``include`` and ``exclude``


Project Dependencies
--------------------

Each typescript project defines its dependencies in ``package.json``. These dependencies can be installed in your system either locally ``<project>/node_modules/.bin`` or globally ``/usr/local/bin``. Running ``npm install`` will install those dependencies in the project folder (hence ignoring them in ``.gitignore`` by adding the line ``node_modules``, i.e., the dependencies).

* project information
    * author
    * name
    * version
    * scripts
* Production Dependencies
    * ``none``
* Development dependencies
    * typescript: ``typescript``
    * Linting:
        * linter: ``eslint``
        * parser: ``babel-eslint``


.. code-block:: json

    {
    "author": "https://github.com/lifespline",
    "dependencies": {},
    "devDependencies": {
        "babel-eslint": "^10.1.0",
        "eslint": "^8.29.0",
        "typescript": "^4.9.3"
    },
    "jest": {
        "preset": "ts-jest",
        "testMatch": [
        "**/**/test/*.ts?(x)"
        ]
    },
    "name": "arteklabs-samples-ts",
    "scripts": {
        "lint": "eslint ./**/*.ts ./test/*.ts --no-error-on-unmatched-pattern",
        "test": "jest --verbose --passWithNoTests"
    },
    "version": "1.0.0-beta"
    }

.. note::

   UT configuration with ``jest`` can be specified either at ``package.json::jest`` or at ``jest.config.js``.

Running a TS file
-----------------

Having compiled the TS files into JS files:

.. code:: shell

   $ node <file>.js

Debugging a TS file
-------------------

vscode requires the debug configuration at ``.vscode/launch.json``. The configuration includes properties like the ones listed below:

* ``program``: the TS file to debug
* ``outFiles``: the corresponding compiled JS file 
* ``preLaunchTask``: the operation to perform before debugging, in this case, compiling from TS to JS (hence the value below)
* ``name``: Debugging scenario label

.. code-block:: json

   {
       "version": "0.2.0",
       "configurations": [
          {
              "type": "node",
              "request": "launch",
              "name": "samples: inheritance",
              "skipFiles": [
                  "<node_internals>/**"
              ],
              "preLaunchTask": "tsc: build - tsconfig.json",
              "program": "${workspaceFolder}/samples/inheritance/solution.ts",
              "outFiles": [
                  "${workspaceFolder}/dist/inheritance/*.js"
              ]
          }
       ]
   }

Place breakpoints in the code editor and launch the debugging scenario. The kernell will run in debug mode and listen to the interrupt.

ESLinting
---------

Required (sufficient and necessary) linting specification are described below. The project has a redundant linting specification however in the files ``package.json``, ``.eslintrc.json`` and ``.vscode/settings.json``. This is due to lack of knowledge on how to properly specify the babel typescript parser and the linter.

At ``package.json``, the following configurations are required:

* ``"devDependencies.@babel/eslint-parser"``: install the typescript parser ``babel`` specified in ``.eslintrc.json`` as ``parser = @babel/eslint-parser``
* ``devDependencies.@typescript-eslint/eslint-plugin``
* ``babel.plugins = @babel/plugin-transform-typescript``: the ``babel`` plugin (the babel config can also be specified at ``.babelrc.json``)


.. code-block:: json

   {
      "devDependencies": {
          "@babel/eslint-parser": "^7.19.1",
          "@babel/plugin-transform-typescript": "^7.20.2",
          "@typescript-eslint/eslint-plugin": "^5.45.1"
      },
      "babel": {
         "plugins": [
            "@babel/plugin-transform-typescript"
         ]
      }
   }

At ``.eslintrc.json``, it is required to specify the typescript parser ``parser = @babel/eslint-parser``.

.. code-block:: json

   {
      "parser": "@babel/eslint-parser"
   }

JSdocs
------

Use ``jsdocs`` to document the TS code by typing ``/**`` the line just before the TS component.

Docs
----

Generate static webpage docs from your ``jsdocs`` with ``typedoc``. Configure ``typedoc`` either in ``typedoc.json`` or in ``package.json`` as:

.. code-block:: json
   
   {
      "typedocOptions": {
            "entryPoints": [
            "samples/function/solution.ts"
         ],
         "out": "docs/sphinx/src/typedocs"
      }
   }

.. node::

   ``entryPoints`` should be understood as the users of the project can import

The task in the ``npm`` task runner (``packge.json``):

.. code-block:: json
   
   {
      "scripts": {
         "docs": "typedoc samples/index.ts"
      }
   }

.. note::
   
   See `github issue <https://github.com/TypeStrong/typedoc/issues/1515>`_ on specifying the typedoc entrypoint explicitly in the npm script.



Data Types
----------

* ``number``
* ``string``
* ``boolean``
* ``null``
* ``undefined``
* ``object``
* ``any``: declared variable without a type, which allows the variable to hold any type.
* ``unknown``
* ``never``
* ``enum``
* ``tuple``: multi-type array
* ``array``
* ``function``