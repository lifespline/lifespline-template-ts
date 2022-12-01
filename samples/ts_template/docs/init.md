# About

The guide shows how to bootstrap your AWS TS project with `lifespline-ts-template`.

# Getting started

1. Change these values to you project's corresponding values:
    1. `package.json::name`
    1. `package.json::author`
    1. `package.json::version`
1. Run `sudo bash init.sh` to install the default system and application dependencies of your AWS TS project.
1. Configure your AWS SSO profile(s) with:
    ```shell
    aws configure sso --profile <profile>
    ```

    Read more about AWS profiles and AWS profile authentication in the [guide](https://dev.azure.com/novonordiskit/CMC%20Data%20Foundation/_git/hawk-typescript-template?path=/doc/aws_profile_authenticate.md).
1. Login to your AWS SSO profile(s) with:
    ```shell
    aws sso login --profile <profile>
    ```

    You are now ready to make requests to your AWS profile with the `aws-cli`. Read more about AWS profiles and AWS profile authentication in the [guide](aws_profile_authenticate.md). Read more about the `aws-cli` in the [guide](getting_started_with_the_cli.md).
1. So that the SDK and the CDK can access the temporary authentication credentials of your AWS SSO profile(s), having authenticated, copy them to `~/.aws/credentials` with:
    ```shell
    npm run cpsso -- --profile <profile>
    ```

    You are now ready to run your SDK files. Read more about the [AWS SDK](getting_started_with_sdk.md).
1. Bootstrap your AWS profile(s) with:
    ```shell
    cdk bootstrap aws://<profile-account-id>/<profile-region> --profile <profile>
    ```
