# About

Guide for the template's task-runner.

# Getting started

npm scripts as the [task-runner](task_runner.md). Check the available tasks at `package.json`:

```json
"scripts": {
    "test": "jest --verbose",
    "lint": "eslint lib/*.ts",
    "synth": "cdk synth",
    "deploy": "cdk deploy",
    "cpsso": "ssocreds"
}
```

## Examples

Linting `.js` and `.ts` files:

```sh
npm run lint

> hawk-typescript-template@1.0.0-dev lint
> eslint lib/*.ts
```
