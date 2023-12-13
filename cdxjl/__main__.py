from builder import build
from parse import parser
from flags import *

def main():
    project_file, output_filename = get_arguments()
    parse_julia_project = parser(project_file)
    project, manifest = parse_julia_project.get_julia_data()
    julia_sbom_builder = build(project_data=project, manifest_data=manifest, output_file=output_filename)
    julia_sbom_builder.create_sbom()



if __name__ == "__main__":
    main()
