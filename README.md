# tap-restcountries

`tap-restcountries` is a Singer tap for the [REST Countries](https://restcountries.com/) API. It reads the v5
countries list and emits records in the v3.1 shape, so existing loads keep their columns.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

Install from GitHub:

```bash
uv tool install git+https://github.com/TicketSwap/tap-restcountries.git@main
```

## Streams

| Stream | Endpoint | Primary Key | Replication |
|-----------|----------|-------------|-------------|
| countries | `/countries/v5` (100 per page) | `cca3` | Full table |

## Configuration

### Accepted Config Options

| Setting | Type | Required | Default | Description |
|---------|------|----------|---------|-------------|
| `api_key` | string | Yes | | REST Countries API key |
| `fields` | array | No | (all) | v3.1 field names to emit, see [Fields](#fields) |

### Fields

`cca2`, `cca3`, `ccn3`, `cioc`, `fifa`, `independent`, `status`, `unMember`, `name`, `altSpellings`,
`translations`, `area`, `borders`, `capital`, `capitalInfo`, `continents`, `landlocked`, `latlng`, `maps`,
`region`, `subregion`, `timezones`, `population`, `languages`, `demonyms`, `currencies`, `tld`, `postalCode`,
`startOfWeek`, `car`, `gini`, `flag`, `flags`.

v5 has no equivalent for the v3.1 `idd` and `coatOfArms` fields, and `status` carries the v5 values
(`official`, `user_assigned`).

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

```bash
export TAP_RESTCOUNTRIES_API_KEY=your_api_key
export TAP_RESTCOUNTRIES_FIELDS='["name","cca2","capital"]'
```

### Source Authentication and Authorization

Every request needs an API key from [restcountries.com](https://restcountries.com/sign-up), sent as a bearer
token. The free plan allows 1,000 requests a month; a full sync takes 3. The demo key `rc_live_demo` returns
one sample country and no quota.

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

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)

```bash
uv sync
```

### Create and Run Tests

Create tests within the `tests` subfolder and
then run:

```bash
TAP_RESTCOUNTRIES_API_KEY=your_api_key uv run pytest
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
