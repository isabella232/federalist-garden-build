[![CircleCI](https://circleci.com/gh/18F/federalist-garden-build-py.svg?style=svg)](https://circleci.com/gh/18F/federalist-garden-build-py)
[![Dependency Status](https://gemnasium.com/badges/github.com/18F/federalist-garden-build-py.svg)](https://gemnasium.com/github.com/18F/federalist-garden-build-py)

### Notes

- http://docs.pyinvoke.org/en/latest/

- TODO: pytest
- TODO: send logs after each step
- TODO: capture errors and post logs:
  http://alanwsmith.com/capturing-python-log-output-in-a-variable
- TODO: use mypy?
- TODO: gemnasium, circle, etc.
- TODO: dockerize for both dev and deploy
- TODO: write README. can use lots of old one.
    - update development section

## Environment Variables

### Variables available to build bngines

The following environment variables may be accessed during a site's build. They may be useful for customizing the display of certain information in the published site, for example, to display the current published branch name.

1. `OWNER`: the GitHub account that owns the repository.
1. `REPOSITORY`: the repository name.
1. `BRANCH`: the branch being built.
1. `SITE_PREFIX`: the S3 bucket "path" that the site files will be published to.
  - for the live site: `site/<OWNER>/<REPOSITORY>`.
  - for the demo site: `demo/<OWNER>/<REPOSITORY>`.
  - for branch previews: `preview/<OWNER>/<REPOSITORY>/<BRANCH>`.
1. `BASEURL`: the base URL that will be used by the build engine to determine the path for site assets.
  - for a live site with a custom URL, this will be empty.
  - for anything else, it will be the same as `SITE_PREFIX` but
    with a `/` at the beginning. ex: `/site/<OWNER>/<REPOSITORY>`.
1. `LANG`: `en_US.UTF-8` (necessary to avoid encoding issues).

### Private variables

TODO: fill out

## Development

Use Docker Compose for local development and testing.

To make setting environment variables easier for local development,
create a new `.env` file based on the `.env.sample`:

```sh
cp .env.sample .env
```

For the AWS S3 values needed, you might find it helpful to
spin up an S3 service in your cloud.gov sandbox space.

For the `GITHUB_TOKEN`, create a new OAuth token for your GitHub account
and use that.

Then fill out the values in it. Be careful not to commit this file because
it might have sensitive information in it. It is ignored by the `.gitignore` file.

```
docker-compose build
docker-compose run app
```

Run `docker-compose run app bash` to start up `bash` in a transient `app` container. Then you can run `inv main` (or any other `inv <TASK>`) directly from that terminal.

For testing:

```sh
docker-compose run app pytest
```
