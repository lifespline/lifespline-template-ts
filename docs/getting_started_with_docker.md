- [About](#about)
- [Docker: A Minimalistic Introduction](#docker-a-minimalistic-introduction)
- [Getting Started](#getting-started)
  - [`run`](#run)
  - [`ENTRYPOINT`](#entrypoint)
  - [`cmd`](#cmd)
# About

The guide gets you started with docker and the AWS ECR.

# Docker: A Minimalistic Introduction

Read the [circleci][docker-intro] introduction for a minimalistic introduction.

# Getting Started

`asset/lambda/example3/Dockerfile` is the blueprint for a docker image. The image needs to be built and run:

```shell
docker build 
```

*TODO*

`default.sh`
```shell
#!/bin/bash
echo default
```
`optional.sh`
```shell
#!/bin/bash
echo optional
```

`Dockerfile`
```dockerfile
from ubuntu:20.04
run echo "image build step 1"
run echo "image build step 2"
cmd ["./default.sh"]
```

```shell
$ docker build . -t delete
Sending build context to Docker daemon  3.584kB
Step 1/4 : from ubuntu:20.04
 ---> 20fffa419e3a
Step 2/4 : run echo "image build step 1"
 ---> Running in eae125bc86fb
image build step 1
Removing intermediate container eae125bc86fb
 ---> 65577edb29ff
Step 3/4 : run echo "image build step 2"
 ---> Running in d36873ac9b9d
image build step 2
Removing intermediate container d36873ac9b9d
 ---> 8dc99f532dc5
Step 4/4 : cmd ["echo", "default command with default parameter"]
 ---> Running in c7b25ef74337
Removing intermediate container c7b25ef74337
 ---> 3a7ce19975b3
Successfully built 3a7ce19975b3
Successfully tagged delete:latest

$ docker run delete
default

$ docker run delete ./optional.sh
optional
```

`Dockerfile`
```dockerfile
from ubuntu:20.04
run echo "image build step 1"
run echo "image build step 2"
entrypoint ["./default.sh"]
# $ docker run delete
# default

# $ docker run delete ./optional.sh
# default
```


*TODO*

```dockerfile
from ubuntu:20.04
cmd ["whoami"]
# root
```

```dockerfile
from ubuntu:20.04
cmd ["echo", "hi from docker"]
# hi from docker
```

`asset/lambda/example3/default.sh`
```shell
#!/bin/bash
echo hi from docker script
```

```dockerfile
from ubuntu:20.04
copy asset/lambda/example3/default.sh ./
cmd ["./default.sh"]
# hi from docker script
```

```javascript
module.exports.test = function() {
  console.log('hi from js function')
};
// $ node -e 'require("./test").test()'
// hi from js function
```

`asset/lambda/example3/handler.js`
```javascript
async function request(respTime) {

  const callback = (resolve, reject) => {
    if (respTime < 500) {
      setTimeout(() => resolve('waiting time: acceptable'), respTime);
    } else {
      reject('waiting time: non-acceptable');
    }
  }

  // simulate a request with a response time
  const promise = new Promise(callback);

  await promise.then(console.log).catch(console.log);
}


const time = 401;
request(time)
setTimeout(() => console.log('impatiently awaiting...'), time - 1);
```

```dockerfile
FROM ubuntu:22.04
COPY asset/lambda/example3/handler.js ./
RUN apt update
RUN yes | apt install nodejs npm
RUN npm i -g typescript
CMD ["node", "handler.js"]
# impatiently awaiting...
# waiting time: acceptable
```

```dockerfile
FROM ubuntu:22.04
RUN apt update
RUN yes | apt install nodejs npm
RUN npm i -g typescript
COPY asset/lambda/example3/handler.ts ./
CMD ["tsc", "handler.ts"]
CMD ["node", "handler.js"]
# impatiently awaiting...
# waiting time: acceptable
```

*TODO*

```dockerfile
FROM ubuntu:22.04
RUN apt update
RUN yes | apt install nodejs npm
RUN npm i -g typescript
COPY package.json asset/lambda/example3/handler.ts ./
RUN npm i
RUN tsc handler.ts
ENTRYPOINT [ "node" ]
CMD ["handler.js"]
```

```typescript
import {
  STSClient, STSClientConfig, GetCallerIdentityCommand, GetCallerIdentityCommandInput,
} from '@aws-sdk/client-sts';
import { fromIni } from '@aws-sdk/credential-providers';

async function request(profile: string = process.argv[2], region = process.argv[3]) {
  const credentials = fromIni({ profile });

  const configuration: STSClientConfig = {
    credentials,
    region,
  };
  const sts: STSClient = new STSClient(configuration);
  const input: GetCallerIdentityCommandInput = {};
  const command = new GetCallerIdentityCommand(input);
  const res = await sts.send(command);
  return res;
}

function handle(profile, region) {
  request(profile, region).then((res) => {
    console.log('Success');
    console.log(res.Account);
    console.log(res.UserId);
    console.log(res.Arn);
  }).catch((err) => {
    console.log('Error');
    console.log(err);
  });
}

handle('dev', 'eu-central-1');
// Error
// CredentialsProviderError: Profile dev could not be found or parsed in shared credentials file.
```

## `run`

Image build step. The step creates a temporary image which replaces the first, runs the script/command and commits the temporary image as the new image.

## `ENTRYPOINT`

A new container is created to execute the script/command. The command cannot be overwritten by CLI arguments. There can only be one `entrypoint` (all but the last will be ignored). Compare the example with `CMD`:

`default.sh`
```shell
#!/bin/bash
echo default
```

`optional.sh`
```shell
#!/bin/bash
echo optional
```

```dockerfile
from ubuntu:20.04
run echo "image build step 1"
run echo "image build step 2"
entrypoint ["./default.sh"]
# $ docker run delete
# default

# $ docker run delete ./optional.sh
# default
```

`ENTRYPOINT` and `RUN` are typically used in combination with one another: `ENTRYPOINT` defines the entrypoint command and `CMD` defines the default parameter to the entrypoint command. If the CLI provides an argument, it will overwrite the parameter provided by `CMD`. Example:

```dockerfile
from ubuntu:20.04
copy . ./
run apt update && yes | apt install iputils-ping
entrypoint ["/bin/ping"]
CMD ["localhost"]
# $ docker run delete
# PING localhost (127.0.0.1) 56(84) bytes of data.
# 64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.039 ms

# $ docker run delete "google.com"
# PING google.com (142.251.36.46) 56(84) bytes of data.
# 64 bytes from ams17s12-in-f14.1e100.net (142.251.36.46): icmp_seq=1 ttl=115 time=79.0 ms
```


## `cmd`

Command executed by **default** when the built image is run. If you run a Docker container without specifying any additional CLI arguments, the `cmd` instruction will be executed with the provided arguments, otherwise it overwrites them with the ones passed by the CLI. Th default command is typically a script.

`default.sh`
```shell
#!/bin/bash
echo default
```

`optional.sh`
```shell
#!/bin/bash
echo optional
```

```dockerfile
from ubuntu:20.04
run echo "image build step 1"
run echo "image build step 2"
cmd ["./default.sh"]
# $ docker run delete
# default

# $ docker run delete ./optional.sh
# optional
```

[docker-intro]: https://circleci.com/blog/docker-image-vs-container/?utm_source=google&utm_medium=sem&utm_campaign=sem-google-dg--emea-en-dsa-maxConv-auth-nb&utm_term=g_-_c__dsa_&utm_content=&gclid=Cj0KCQjw54iXBhCXARIsADWpsG_oFdxiEDNioEoWP1aYvBgZ4CUtqrw9J5Z8Bi402J4t0W8cjvt7-mkaAr6MEALw_wcB