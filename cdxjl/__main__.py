from builder import build
from parse import parser
from flags import *

fullpath = "/home/richard/code/NewJuliaProject"
output_name = "sbom.json"
# path, output = get_arguments()

parse_julia_project = parser(fullpath)
project, manifest = parse_julia_project.get_julia_data()
# print(type(project))
# print(type(manifest))
julia_sbom_builder = build(project_data=project, manifest_data=manifest, output_file=output_name)
julia_sbom_builder.create_sbom()
