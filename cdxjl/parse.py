import toml
import os




'''
Parser class.
Validates that a particular Julia Project exists, and it contains the appropriate manifest files "Project.toml" & "Manifest.toml".
It then returns the requisite data found in these files as dictionaries, with the method "get_julia_data", with a return format of: 

<project data>, <manifest data> = parse("path-to-julia-project).get_julia_data()
'''
class parser:
    def __init__(self, path: str) -> None:
        self.manifest_path = os.path.join(path, "Manifest.toml")
        self.project_path =  os.path.join(path, "Project.toml")
        if os.path.isdir(path) is False:
            print(f"Could not find project {path}. No file or directory found.")
            exit(-1)
        
        elif os.path.isfile(self.manifest_path) is False:
            print("Error, no Manifest.toml found")
            exit(-1)
        
        elif os.path.isfile(self.project_path) is False:
            print("Error, no Project.toml found")
            exit(-1)

        else:
            print("Analyzing project...")

    def read_manifest(self):
        with open(self.manifest_path, "r") as f:
            data = toml.load(f)
        return data


    def read_project(self):
        with open(self.project_path, "r") as f:
            data = toml.load(f)
        return data
    
    def get_julia_data(self):
        project_data = self.read_project()
        manifest_data = self.read_manifest()
        return project_data, manifest_data


