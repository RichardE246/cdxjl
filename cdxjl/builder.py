import json
import os
from cyclonedx.model.bom import Bom, BomMetaData
from cyclonedx.model.component import ComponentType, Component
from cyclonedx.model import OrganizationalEntity, OrganizationalContact, XsUri
from cyclonedx.model import HashAlgorithm, HashType, ExternalReference, ExternalReferenceType
from cyclonedx.output import get_instance, BaseOutput, OutputFormat
from packageurl import PackageURL
from pathlib import Path
from uuid import UUID, uuid4

class build:
    def __init__(self, project_data:dict, manifest_data:dict, output_file:str) -> None:
    #first check to see if a file with the output name exists already
        self.proj_data = project_data
        self.mani_data = manifest_data
        self.out = output_file

    def get_authors(self, authors: list):
        #Julia has a [name <email>] format for authors. We need to parse it.
        author_array = []
        for author in authors:
            split_author = author.split("<")
            split_email = split_author[1].split(">")
            name = split_author[0].strip()
            email = split_email[0].strip()
            author_dict = {
                "name":name,
                "email":email
            }
            author_array.append(author_dict)
        return author_array
    
    
    def get_julia_hash(self, julia_hash_str: str):
        #julia hashes are of the format git-tree-sha1, which streamlines things
        julia_hash = HashType(
            alg=HashAlgorithm.SHA_1,
            content=julia_hash_str
        )
        julia_hash_array = [julia_hash]
        return julia_hash_array




    def get_component(self, component_name:str, component_data):

        name=component_name
        delisted_component_data = component_data[0]
        version=delisted_component_data.get("version")
        hashes = self.get_julia_hash(delisted_component_data.get("git-tree-sha1"))
        component = Component(
            name=name,
            version=version,
            hashes=hashes   
        )

        return component


    def get_components(self, manifest_data:dict):
        components = [self.get_component(component_name=key, component_data=value) for key, value in manifest_data.items()]
        return components


    def create_sbom(self):
        bom = Bom()
        bom.components = self.get_components(self.mani_data)
        comp_dict = {comp.name: comp for comp in bom.components}
        dep_dict = {key: value[0].get("deps") for key, value in self.mani_data.items()}

        for key, value in dep_dict.items():
            if value is not None:
                dependencies = [comp_dict.get(val) for val in value]
                bom.register_dependency(comp_dict.get(key), dependencies)

        project_name = self.proj_data.get("name")
        project_version = self.proj_data.get("version")
        project_type=ComponentType("application")

        bom.metadata.component = root_component = Component(
                            name=project_name,
                            version=project_version,
                            type=project_type
                        )

        deplist = [dep for dep in self.proj_data.get("deps")]
        dependencies = [comp_dict.get(depname) for depname in deplist]
        bom.register_dependency(root_component, dependencies)

        outputter: BaseOutput = get_instance(bom=bom, output_format=OutputFormat.JSON)
        outputter.output_to_file(filename=self.out, allow_overwrite=True)

        
    

    




