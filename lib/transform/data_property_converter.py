import json
import os

from tqdm import tqdm

from lib.config.data_transformation_loader import Property
from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def convert_data_properties(
    data_transformation, source_path, results_path, clean=False, quiet=False
):
    already_exists, converted, exception = 0, 0, 0

    if data_transformation.input_ports:
        for input_port in data_transformation.input_ports:
            for file in input_port.files:
                source_file_path = os.path.join(
                    source_path, input_port.id, file.target_file_name
                )
                target_file_path = os.path.join(
                    results_path, input_port.id, file.target_file_name
                )

                try:
                    with open(source_file_path, "r", encoding="utf-8") as geojson_file:
                        geojson = json.load(geojson_file, strict=False)

                        geojson, changed = convert_properties(geojson, file.properties)

                        if not changed:
                            already_exists += 1
                            if not quiet:
                                print(f"✓ Already converted {file.target_file_name}")
                            continue

                        with open(
                            target_file_path, "w", encoding="utf-8"
                        ) as geojson_file:
                            json.dump(geojson, geojson_file, ensure_ascii=False)

                            converted += 1
                            if not quiet:
                                print(f"✓ Convert {file.target_file_name}")
                except Exception as e:
                    exception += 1
                    print(f"✗️ Exception: {str(e)}")

    print(
        f"convert_data_properties finished with already_exists: {already_exists}, converted: {converted}, exception: {exception}"
    )


def convert_properties(geojson, properties: list[Property]):
    changed = False

    for feature in tqdm(
        iterable=geojson["features"], desc="Convert features", unit="feature"
    ):
        for property in properties:
            if property.concat is not None:
                feature["properties"][property.name] = "".join(
                    [feature["properties"][prop] for prop in property.concat]
                )
                changed = True

            if property.rename is not None and property.name in feature["properties"]:
                feature["properties"][property.rename] = feature["properties"].pop(
                    property.name
                )
                changed = True

            if property.remove is not None and property.name in feature["properties"]:
                feature["properties"].pop(property.name)
                changed = True
    return geojson, changed
