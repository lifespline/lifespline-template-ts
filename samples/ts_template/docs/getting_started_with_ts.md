# About 

The guide provides an introduction to typescript.

# Extending Javascript

The key value proposition of JavaScript: the ability to run your code anywhere and on every platform, browser, or host. JS wasn't designed however for very complex applications and it lacks features from more mature languages. Typescript is a superset of JS ([ES6](https://www.ecma-international.org/ecma-262/6.0/) to be precise):
+ Any JS file is a TS file (it suffices to change the extension from `.js` to `.ts`)
+ Any TS file [builds/transpiles](https://babeljs.io/) or [compiles](https://www.typescriptlang.org/download) to an equivalent JS file (most runtimes can't process TS natively, only JS)
+ The superset adds to JS some of the features of more mature languages:
  + static type checking
  + interfaces
  + generics
  + abstract classes
  + data modifiers
  + optionals
  + function overloading
  + decorators
  + type utils
  + readonly keyword

TS compiles into JS before being executed.

# Install

Run `sudo init.sh` to install typescript in your host.

# Running a TS file

Running `tsc` compiles all TS files and executes them. The compiler is configured with `tsconfig.json`. Read about the configuration in [layout](layout.md). Execute a specific file by running `node <file>.js`.

# Resources

+ [Getting started with Typescript](https://docs.microsoft.com/en-us/learn/modules/typescript-get-started/1-introduction)