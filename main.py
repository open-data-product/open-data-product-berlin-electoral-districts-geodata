import os
import sys

from documentation.odps_canvas_generator import generate_odps_canvas

file_path = os.path.realpath(__file__)
script_path = os.path.dirname(file_path)
lib_path = os.path.join(script_path, "lib")

sys.path.append(lib_path)

import click

from lib.config.odps_loader import load_odps
from lib.config.data_product_manifest_loader import load_data_product_manifest
from lib.config.data_transformation_loader import load_data_transformation
from lib.documentation.data_product_canvas_generator import generate_data_product_canvas
from lib.documentation.data_product_manifest_updater import update_data_product_manifest
from lib.extract.data_extractor import extract_data
from lib.transform.data_bounding_box_converter import convert_bounding_box
from lib.transform.data_geojson_converter import convert_to_geojson
from lib.transform.data_geometry_converter import convert_data_geometry
from lib.transform.data_projection_converter import convert_projection
from lib.transform.data_property_converter import convert_data_properties


@click.command()
@click.option("--clean", default=False, help="Regenerate results.")
@click.option("--quiet", default=False, help="Do not log outputs.")
def main(clean, quiet):
    data_path = os.path.join(script_path, "data")
    bronze_path = os.path.join(data_path, "01-bronze")
    silver_path = os.path.join(data_path, "02-silver")
    gold_path = os.path.join(data_path, "03-gold")
    docs_path = os.path.join(script_path, "docs")

    data_product_manifest = load_data_product_manifest(config_path=script_path)
    data_transformation = load_data_transformation(config_path=script_path)
    odps = load_odps(config_path=script_path)

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

    update_data_product_manifest(
        data_product_manifest=data_product_manifest,
        config_path=script_path,
        data_paths=[silver_path, gold_path],
        file_endings=(".geojson", ".json"),
    )

    generate_data_product_canvas(
        data_product_manifest=data_product_manifest,
        docs_path=docs_path,
    )

    generate_odps_canvas(
        odps=odps,
        docs_path=docs_path,
    )


if __name__ == "__main__":
    main()
