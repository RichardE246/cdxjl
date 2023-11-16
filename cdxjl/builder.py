import json
import os
from cyclonedx.model.bom import Bom, BomMetaData
from cyclonedx.model.component import ComponentType, Component
from cyclonedx.model import OrganizationalEntity, OrganizationalContact, XsUri
from cyclonedx.model import HashAlgorithm, HashType, License, LicenseChoice, ExternalReference, ExternalReferenceType
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
    



    def get_julia_project_metadata(self, project_data:dict):
        project_name = project_data.get("name")
        project_version = project_data.get("version")
        project_type=ComponentType("application") #hardcoded for now
        project_authors = self.get_authors(project_data.get("authors"))

        print(type(project_authors))


        metadata_component = Component(
            name=project_name,
            version=project_version,
            component_type=project_type
        )

        metadata = BomMetaData(
            component=metadata_component
            # authors=project_authors
        )

        return metadata
    
    def get_julia_hash(self, julia_hash_str: str):
        #julia hashes are of the format git-tree-sha1, which streamlines things
        julia_hash = HashType(
            algorithm=HashAlgorithm.SHA_1,
            hash_value=julia_hash_str
        )
        julia_hash_array = [julia_hash]
        return julia_hash_array




    def get_component(self, component_name:str, component_data):

        name=component_name
        delisted_component_data = component_data[0]
        version=delisted_component_data.get("version")
        hash=self.get_julia_hash(delisted_component_data.get("git-tree-sha1"))

        component = Component(
            name=name,
            version=version
            #hashes=hash
            
        )

        return component


    def get_julia_project_components(self, manifest_data:dict):
        components = [self.get_component(component_name=key, component_data=value) for key, value in manifest_data.items()]
        return components



    def create_sbom(self):
        bom_components = self.get_julia_project_components(self.mani_data)
        bom_metadata = self.get_julia_project_metadata(self.proj_data)
        bom_uuid_string = self.proj_data.get("uuid")
        if bom_uuid_string is not None:
            bom_uuid = UUID(self.proj_data.get("uuid"))
        else:
            bom_uuid = uuid4()
        sbom = Bom()
        sbom.components = bom_components
        sbom.metadata = bom_metadata
        sbom.uuid = bom_uuid
        outputter: BaseOutput = get_instance(bom=sbom, output_format=OutputFormat.JSON)
        outputter.output_to_file(self.out)
    

    




