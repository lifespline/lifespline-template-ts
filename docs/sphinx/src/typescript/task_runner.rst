Task Runner
===========

About
-----

A typescript project will typically use the npm scripts as the task runner for simple enough tasks. The npm scripts are defined in ``package.json``, typically at the project root. Below, an example of two scripts, for running unit tests and linting respectfully:

.. code-block:: json

   {
      "scripts": {
          "test": "jest --verbose",
          "lint": "eslint lib/*.ts",
      }
   }


Example with linting the TS code through a task:

.. code:: shell

   $ npm run lint
   
   > hawk-typescript-template@1.0.0-dev lint
   > eslint lib/*.ts
