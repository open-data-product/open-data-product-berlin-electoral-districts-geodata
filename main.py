# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "click>=8.2.1",
#     "open-data-product-python-lib",
# ]
#
# [tool.uv.sources]
# open-data-product-python-lib = { git = "https://github.com/open-data-product/open-data-product-python-lib.git" }
# ///

import os
import sys

from opendataproduct.config.data_product_manifest_loader import (
    load_data_product_manifest,
)
from opendataproduct.config.dpds_loader import load_dpds
from opendataproduct.config.geodata_transformation_loader import (
    load_data_transformation,
)
from opendataproduct.config.odps_loader import load_odps
from opendataproduct.document.data_product_canvas_generator import (
    generate_data_product_canvas,
)
from opendataproduct.document.data_product_manifest_updater import (
    update_data_product_manifest,
)
from opendataproduct.document.dpds_canvas_generator import generate_dpds_canvas
from opendataproduct.document.dpds_updater import update_dpds
from opendataproduct.document.jupyter_notebook_creator import (
    create_jupyter_notebook_for_geojson,
)
from opendataproduct.document.odps_canvas_generator import generate_odps_canvas
from opendataproduct.document.odps_updater import update_odps
from opendataproduct.extract.data_extractor import extract_data
from opendataproduct.transform.geodata_bounding_box_converter import (
    convert_bounding_box,
)
from opendataproduct.transform.geodata_geojson_converter import convert_to_geojson
from opendataproduct.transform.geodata_geometry_converter import convert_data_geometry
from opendataproduct.transform.geodata_projection_converter import convert_projection
from opendataproduct.transform.geodata_property_converter import convert_data_properties

file_path = os.path.realpath(__file__)
script_path = os.path.dirname(file_path)
lib_path = os.path.join(script_path, "lib")

sys.path.append(lib_path)

import click


@click.command()
@click.option("--clean", "-c", default=False, is_flag=True, help="Regenerate results.")
@click.option("--quiet", "-q", default=False, is_flag=True, help="Do not log outputs.")
def main(clean, quiet):
    data_path = os.path.join(script_path, "data")
    bronze_path = os.path.join(data_path, "01-bronze")
    silver_path = os.path.join(data_path, "02-silver")
    gold_path = os.path.join(data_path, "03-gold")
    docs_path = os.path.join(script_path, "docs")

    data_product_manifest = load_data_product_manifest(config_path=script_path)
    data_transformation = load_data_transformation(config_path=script_path)
    odps = load_odps(config_path=script_path)
    dpds = load_dpds(config_path=script_path)

    #
    # Extract
    #

    extract_data(
        data_product_manifest=data_product_manifest,
        results_path=bronze_path,
        clean=clean,
        quiet=quiet,
    )

    #
    # Transform
    #

    convert_to_geojson(
        data_transformation=data_transformation,
        source_path=bronze_path,
        results_path=silver_path,
        clean=clean,
        quiet=quiet,
    )

    convert_data_properties(
        data_transformation=data_transformation,
        source_path=silver_path,
        results_path=silver_path,
        clean=clean,
        quiet=quiet,
    )

    convert_data_geometry(
        data_transformation=data_transformation,
        source_path=silver_path,
        results_path=silver_path,
        clean=clean,
        quiet=quiet,
    )

    convert_projection(
        data_transformation=data_transformation,
        source_path=silver_path,
        results_path=silver_path,
        clean=clean,
        quiet=quiet,
    )

    convert_bounding_box(
        data_transformation=data_transformation,
        source_path=silver_path,
        results_path=silver_path,
        clean=clean,
        quiet=quiet,
    )

    #
    # Documentation
    #

    create_jupyter_notebook_for_geojson(
        data_product_manifest=data_product_manifest,
        results_path=script_path,
        data_path=silver_path,
        clean=True,
        quiet=quiet,
    )

    update_data_product_manifest(
        data_product_manifest=data_product_manifest,
        config_path=script_path,
        data_paths=[silver_path, gold_path],
        file_endings=(".geojson", ".json"),
    )

    update_odps(
        data_product_manifest=data_product_manifest,
        odps=odps,
        config_path=script_path,
        output_file_formats=["geojson", "json"],
    )

    update_dpds(
        data_product_manifest=data_product_manifest,
        dpds=dpds,
        config_path=script_path,
    )

    generate_data_product_canvas(
        data_product_manifest=data_product_manifest,
        docs_path=docs_path,
    )

    generate_odps_canvas(
        odps=odps,
        docs_path=docs_path,
    )

    generate_dpds_canvas(
        dpds=dpds,
        docs_path=docs_path,
    )


if __name__ == "__main__":
    main()
