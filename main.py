import getopt
import os
import sys

from lib.config.data_product_manifest_loader import load_data_product_manifest
from lib.config.data_transformation_loader import load_data_transformation
from lib.documentation.data_product_canvas_generator import generate_data_product_canvas
from lib.documentation.data_product_manifest_updater import update_data_product_manifest
from lib.extract.data_extractor import extract_data
from lib.tracking_decorator import TrackingDecorator
from lib.transform.data_copier import copy_data

file_path = os.path.realpath(__file__)
script_path = os.path.dirname(file_path)


@TrackingDecorator.track_time
def main(argv):
    # Set default values
    clean = False
    quiet = False

    # Read command line arguments
    try:
        opts, args = getopt.getopt(argv, "hcq", ["help", "clean", "quiet"])
    except getopt.GetoptError:
        print("main.py --help --clean --quiet")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("main.py")
            print("--help                           show this help")
            print(
                "--clean                          clean intermediate results before start"
            )
            print("--quiet                          do not log outputs")
            sys.exit()
        elif opt in ("-c", "--clean"):
            clean = True
        elif opt in ("-q", "--quiet"):
            quiet = True

    data_path = os.path.join(script_path, "data")
    bronze_path = os.path.join(data_path, "01-bronze")
    silver_path = os.path.join(data_path, "02-silver")
    gold_path = os.path.join(data_path, "03-gold")
    docs_path = os.path.join(script_path, "docs")

    data_product_manifest = load_data_product_manifest(config_path=script_path)
    data_transformation = load_data_transformation(config_path=script_path)

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

    copy_data(
        data_transformation=data_transformation,
        source_path=bronze_path,
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
        file_endings=(".csv"),
    )

    generate_data_product_canvas(
        data_product_manifest=data_product_manifest,
        data_transformation=data_transformation,
        docs_path=docs_path,
    )


if __name__ == "__main__":
    main(sys.argv[1:])
