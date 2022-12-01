Getting Started
===============

About
-----

Introduction to Typescript.

Typescript
----------

The key value proposition of JS:

   The ability to run your code anywhere and on every platform, browser, or host.

JS wasn't designed however for very complex applications and it lacks features from more mature languages. TS is a superset of JS (`ES6 <https://www.ecma-international.org/ecma-262/6.0/>`_ to be precise), meaning it **extends** JS, that is:

* Any JS file is a TS file: It suffices to change the extension from `.js` to `.ts`. Indeed, any TS file compiles into JS before being executed.
* Any TS file `builds/transpiles <https://babeljs.io/>`_ or `compiles <https://www.typescriptlang.org/download>`_ to an equivalent JS file: Most runtimes can't process TS natively, only JS.
* The superset adds to JS some of the features of more mature languages:
   * static type checking
   * interfaces
   * generics
   * abstract classes
   * data modifiers
   * optionals
   * function overloading
   * decorators
   * type utils
   * readonly keyword


Install
-------

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

The TS compiler is configured in ``tsconfig.json``, which looks like:

.. code-block:: json

   {
       "include": ["app/*.ts"],
       "exclude": [],
       "compilerOptions": {
           // compile TS into the ES6 JS standard (OPT)
           "target": "es6",
           // Use the CommonJS API to (OPT)
           "module": "CommonJS",
           // VS Code has built-in support for TypeScript debugging. To support 
           // debugging TypeScript in combination with the executing     JavaScriptcode, 
           // VS Code relies on source maps for the debugger to map between the 
           // original TypeScript source code and the running JavaScript.
           "sourceMap": true
       }
   }

Running ``tsc`` compiles all TS files and executes them. 


Running a TS file
-----------------

Having compiled the TS files into JS files:

.. code:: shell

   $ node <file>.js
