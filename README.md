[![Issues](https://img.shields.io/github/issues/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata)](https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/issues)

<br />
<p align="center">
  <a href="https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata">
    <img src="logo_with_text.png" alt="Logo" height="80">
  </a>

  <h1 align="center">Open Lifeworlds Data Product - Berlin Electoral Districts geodata</h1>

  <p align="center">
    Data product providing geodata of Berlin electoral districts</a>
  </p>
</p>

## About The Project

See [data product canvas](docs/data-product-canvas.md).

### Built With

* [Python](https://www.python.org/)
* [uv](https://docs.astral.sh/uv/)
* [ruff](https://docs.astral.sh/ruff/)

## Installation

Install uv, see https://github.com/astral-sh/uv?tab=readme-ov-file#installation.

```shell
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Usage

Run this command to generate and activate a virtual environment.

```shell
uv venv
```

Run this command to start the main script.

```shell
python3 main.py [OPTION]...

  -h, --help                           show this help
  -c, --clean                          clean intermediate results before start
  -q, --quiet                          do not log outputs

Examples:
  python3 main.py -c
```

## Roadmap

See the [open issues](https://github.com/open-lifeworlds/berlin-electoral-districts-geodata/issues) for a list of proposed features (and known issues).

## License

Data product distributed under the [CC-BY 4.0 License](https://creativecommons.org/licenses/by/4.0/). See [LICENSE.md](./LICENSE.md) for more information.

## Contact

openlifeworlds@gmail.com
