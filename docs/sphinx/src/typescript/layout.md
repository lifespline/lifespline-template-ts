# About #

The guide shows the layout of the project and the purpose of each file.

# Doc #

The `README.md` and the `doc` directory contain all the documentation for the project that could not be included in the project's source files.

```txt
/
│
├╴ doc
│  │
│  ├╴ CONTRIBUTING.md
│  ├╴ layout.md
│  ├╴ getting_started_with_ts.md
│  ├╴ getting_started.md
│  ├╴ format.md
│  ├╴ lint.md
│  └╴ test.md
│
└╴ README.md
```

# Project Requirements #

```txt
/
│
├╴ package-lock.json
└╴ package.json
```

## `package.json` ##

Package configuration file. Being a `json` file, it contains the following keys:
+ `name` The project name: `lifespline-ts-template`
+ `description` The project´s description
+ `version` The project's version
+ `scripts` Command aliases to run with `npm run <alias>`
+ `devDependencies` The package development dependencies listed with versions. Running `npm install <package> --save-dev | -D` will add the package to `devDependencies`. Development dependencies are dependencies not required in production, like linting, testing or task-running tools. Essentially, a development build is different than a production build. List of development dependencies:
  + `typescript` The typescript compiler from TS to JS
  + Linting dependencies:
    + `eslint`
    + `@typescript-eslint/eslint-plugin`
    + `@typescript-eslint/parser`
    + `eslint-config-airbnb-base`
    + `eslint-plugin-import`
  + Testing dependencies:
    + `@types/jest`
    + `jest`
    + `ts-jest`
  + AWS SDK
    + `@types/node`
    + `aws-sdk`
  + AWS CDK
    + `aws-cdk`
    + `ts-node`
+ `dependencies` The package production dependencies. Running `npm install <package> --save` will add the package to `dependencies`.
  + AWS SDK clients:
    + `@aws-sdk/client-sts`
    + `@aws-sdk/client-s3`
    + `@aws-sdk/credential-providers`
  + AWS CDK:
    + `aws-cdk-lib`
    + `constructs`
    + `source-map-support`

# Configuration #

The list of files below configure:

+ linting
+ testing
+ ide (vscode)

```txt
/
│
├╴ .vscode
│   │
│   ├╴ launch.json
│   └╴ settings.json
│
├╴ .eslintignore
├╴ .eslintrc.js
├╴ .gitignore
├╴ babel.config.js
├╴ init.sh
├╴ jest.config.js
├╴ package-lock.json
├╴ package.json
├╴ tsconfig.eslint.json
└╴ tsconfig.json
```

### `tsconfig.json` ###

The file configures the TS compiler `tsc`.

Specify which files to compile (ignores any other paths) (**required**)

```json
{
  "include": ["app/*.ts", "test/*.ts"]
}
```

Specify which is the JS standard the TS files should be compiled to

```json
{
  "compilerOptions": { "target": "es5" }
}
```

Specify the CommonJS standard JS API: API to declare modules that work in hosts different than a browser.

```json
{
  "compilerOptions": { "module": "CommonJS" }
}
```

### `.eslintrc.json` ###

*TODO* Linting specifications (generate automatically)

### `tsconfig.eslint.json` ###

Linting specifications. This file is specified in `.eslintrc.js::parser.project`.

* `extends`
* `include` The directories containing files to be lint or the full paths of files to be lint. The types of files in these directories that will be lint are specified as an argument on the npm script `package.json::scripts.lint`, i.e., `eslint . --ext .js,.jsx,.ts,.tsx`.

### `jest.config.js` ###

Unit test specifications. See the inline comments on `jest.config.js` for more details.


### `package-lock.json` ##

Locks the versions of the application dependencies. Ignore the file if you intend to always install the latest versions.

## Git-ignored files ##

See the respective ignored files for the corresponding explanation.

```txt
/
│
├╴ src
│   │
│   └╴ .gitignore
│
└╴.gitignore
```


# Resources

+ [tsconfig.json]](https://www.typescriptlang.org/tsconfig)