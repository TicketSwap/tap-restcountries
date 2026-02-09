# tap-restcountries

`tap-restcountries` is a Singer tap for the [REST Countries](https://restcountries.com/) API (v3.1).

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

Install from GitHub:

```bash
uv tool install git+https://github.com/ORG_NAME/tap-restcountries.git@main
```

## Streams

| Stream | Endpoint | Primary Key | Replication |
|-----------|----------|-------------|-------------|
| countries | `/all` | `cca3` | Full table |

## Configuration

### Accepted Config Options

| Setting | Type | Required | Default | Description |
|---------|------|----------|---------|-------------|
| `api_url` | string | No | `https://restcountries.com/v3.1` | Base URL for the REST Countries API |
| `fields` | array | No | (all) | List of fields to request — see [Fields](#fields) below |

### Fields

> **⚠️ Important:** The REST Countries API enforces a **maximum of 10 fields** when
> calling the `/all` endpoint. If you need more fields, omit the `fields` setting
> entirely to retrieve the full response, or make multiple requests with different
> field selections.

Available fields: `cca2`, `cca3`, `ccn3`, `cioc`, `fifa`, `independent`, `status`,
`unMember`, `name`, `altSpellings`, `translations`, `area`, `borders`, `capital`,
`capitalInfo`, `continents`, `landlocked`, `latlng`, `maps`, `region`, `subregion`,
`timezones`, `population`, `languages`, `demonyms`, `currencies`, `idd`, `tld`,
`postalCode`, `startOfWeek`, `car`, `gini`, `flag`, `flags`, `coatOfArms`.

Example configuration selecting specific fields:

```json
{
  "fields": ["name", "cca2", "cca3", "capital", "region", "population"]
}
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

```bash
export TAP_RESTCOUNTRIES_API_URL=https://restcountries.com/v3.1
export TAP_RESTCOUNTRIES_FIELDS='["name","cca2","capital"]'
```

### Source Authentication and Authorization

No authentication is required. The REST Countries API is free and open.

## Usage

You can easily run `tap-restcountries` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-restcountries --version
tap-restcountries --help
tap-restcountries --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

Prerequisites:

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)

```bash
uv sync
```

### Create and Run Tests

Create tests within the `tests` subfolder and
then run:

```bash
uv run pytest
```

You can also test the `tap-restcountries` CLI interface directly using `uv run`:

```bash
uv run tap-restcountries --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Use Meltano to run an EL pipeline:

```bash
# Install meltano
uv tool install meltano

# Test invocation
meltano invoke tap-restcountries --version

# Run a test EL pipeline
meltano run tap-restcountries target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
# tap-restcountries
