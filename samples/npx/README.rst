npx
===

Whereas running a node dependency requires the dependency to be installed in ``node_modules`` (which is accessed when you run the npm scripts), ``npx`` allows you to run that module directly. The script is configured and executed as:

.. code-block:: json

   {
       "scripts": {
           "test": "jest --verbose --passWithNoTests"
       }
   }

.. code:: shell

   $ npm run test
   ...
   Test Suites: 1 passed, 1 total
   Tests:       1 passed, 1 total
   Snapshots:   0 total
   Time:        0.59 s, estimated 1 s

However:

.. code:: shell

   $ jest --verbose --passWithNoTests
   Command 'jest' not found, did you mean
   ...

   $ npx jest --verbose --passWithNoTests
   ...
   Test Suites: 1 passed, 1 total
   Tests:       1 passed, 1 total
   Snapshots:   0 total
   Time:        0.59 s, estimated 1 s


Literature
----------

* `npm vs npx <https://www.freecodecamp.org/news/npm-vs-npx-whats-the-difference/>`_
