#!/usr/bin/env python3

# General informational properties of the project, including version.
name = "Goost: Godot Engine Extension"
short_name = "goost"
version = {
    "major": 2,
    "minor": 0,
    "patch": 0,
    "branch": "gd3",
    "status": "dev",
    "year": 2022,
}
url = "https://github.com/goostengine/goost"
doc_url = "https://goost.readthedocs.io/en/%s/" % version["branch"]
website = "https://goostengine.github.io/"

modules = [
    {
        "visible_name": "Steamworks",
        "internal_name": "steamworks",
    },
    {
        "visible_name": "Input Glyphs",
        "internal_name": "input_glyphs",
    }
]

import importlib.util
import sys


if __name__ == "__main__":
    import os
    import sys
    import argparse
    import subprocess

    parser = argparse.ArgumentParser(prog="eirteam_docs")
    parser.add_argument("--generate-docs", metavar="<path>", required=True,
            help="Generates a list of classes per component in `.rst` format.")
    parser.add_argument("--godot-path", metavar="<path>", required=True)

    args = parser.parse_args()

    if args.generate_docs:
        output_path = args.generate_docs
        godot_path = args.godot_path
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        def write_comment_warning(f):
            f.write(".. THIS FILE IS GENERATED, DO NOT EDIT!\n")
            f.write(".. Use `python docs.py --generate-docs` at this source tree instead.\n\n")

        # Generate Goost class reference.
        if not os.path.exists(args.godot_path):
            print("Error: Cannot find the provided `godot` directory.")
            print("Please make sure it exists first.")
            sys.exit(255)

        modules_filter = "|".join(f"^(?=.*modules\\/{module['internal_name']})" for module in modules)

        subprocess.run([sys.executable,
            os.path.join(godot_path, "doc/tools/make_rst.py"),
            os.path.join(godot_path, "doc/classes"),
            os.path.join(godot_path, "modules"),
            "doc",
            "modules",
            "--output", output_path,
            "--filter", modules_filter,
        ])

        print("Generating Goost API per component... ")
        with open(os.path.join(output_path, "index.rst"), "w") as f:
            f.write(":github_url: hide\n")
            f.write("\n")
            write_comment_warning(f)
            f.write(".. _eirteam_api:\n")
            f.write("\n")
            f.write("EIRTeam Godot Modules API\n")
            f.write("=========================\n")
            f.write("\n")
            f.write("This is a list of all classes provided by EIRTeam modules.\n")
            f.write("\n")
            for module in modules:
                classes = []
                module_config_path = os.path.join(godot_path, f"modules/{module['internal_name']}/config.py")
                if not os.path.exists(module_config_path):
                    continue

                config_spec = importlib.util.spec_from_file_location(module["internal_name"], module_config_path)
                module_config = importlib.util.module_from_spec(config_spec)
                config_spec.loader.exec_module(module_config)
                classes = module_config.get_doc_classes()

                if not classes:
                    continue
                f.write(module["visible_name"])
                f.write("\n")
                f.write("=" * len(module["visible_name"]))
                f.write("\n\n")
                f.write(".. toctree::\n")
                f.write("    :maxdepth: 1\n")
                module_visible_name = module["visible_name"]
                module_internal_name = module["internal_name"]
                #f.write("    :caption: %s\n" % module_visible_name)
                f.write("    :name: toc-module-%s\n" % module_internal_name)
                f.write("\n")
                for class_name in classes:
                    f.write("    class_%s.rst\n" % class_name.lower())
                f.write("\n")

        print("Done. You can find generated files at `%s`" % os.path.abspath(output_path))
