from cdxjl.builder import build
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

project = {
            "name": "Example_Julia_Project",
            "uuid": "d9c4a96b-6299-43f5-9d34-05b6b65b3224",
            "authors": ["author <author@email.com>"],
            "version": "0.1.0",
            "deps":{
                        "Flux": "587475ba-b771-5e3f-ad9e-33799f191a9c",
                        "Plots": "91a5bcdd-55d7-5caf-9e0b-520d859cae80"
            }
        }

manifest = {
            'AbstractFFTs': [
                            {'deps': ['LinearAlgebra'], 
                                'git-tree-sha1': '051c95d6836228d120f5f4b984dd5aba1624f716', 
                                'uuid': '621f4979-c628-5d54-868e-fcf4e3e8185c', 
                                'version': '0.5.0'}
                        ], 
            'AbstractTrees': [
                            {
                                'git-tree-sha1': '03e0550477d86222521d254b741d470ba17ea0b5', 
                                'uuid': '1520ce14-60c1-5f80-bbc7-55ef81b5835c', 
                                'version': '0.3.4'
                                }
                        ], 
            'Adapt': [
                        {
                            'deps': ['LinearAlgebra'], 
                            'git-tree-sha1': '345a14764e43fe927d6f5c250fe4c8e4664e6ee8', 
                            'uuid': '79e6a3ab-5dfb-504d-930d-738a2a938a0e', 
                            'version': '2.4.0'
                        }
                    ], 
            'ArrayLayouts': [
                                {
                                    'deps': [
                                                'Compat', 
                                                'FillArrays', 
                                                'LinearAlgebra', 
                                                'SparseArrays'
                                            ], 
                                    'git-tree-sha1': 'a577e27915fdcb3f6b96118b56655b38e3b466f2', 
                                    'uuid': '4c555306-a7a7-4459-81d9-ec55ddd5c99a', 
                                    'version': '0.4.12'
                                }
                            ], 
            'Artifacts': [
                            {
                                'deps': ['Pkg'], 
                                'git-tree-sha1': 'c30985d8821e0cd73870b17b0ed0ce6dc44cb744', 
                                'uuid': '56f22d72-fd6d-98f1-02f0-08ddc0907c33', 
                                'version': '1.3.0'
                            }
                        ]
        }


output = "out.json"

bld = build(project_data=project, manifest_data=manifest, output_file=output)

def test_authors():
    authors = ["author <author@email.com>"]
    test_author_dict = [
                            {
                                "name": "author",
                                "email": "author@email.com"
                            }
                        ]
    ret = bld.get_authors(authors=authors)
    assert ret == test_author_dict

def test_get_hashes():
    hash = '051c95d6836228d120f5f4b984dd5aba1624f716'
    test_julia_hash = [
                    HashType(
                                        alg=HashAlgorithm.SHA_1,
                                        content='051c95d6836228d120f5f4b984dd5aba1624f716'
                                    )
                ]
    
    ret = bld.get_julia_hash(hash)
    assert ret == test_julia_hash



def test_get_component():

    test_data = {
                    'AbstractFFTs': [
                                        {'deps': ['LinearAlgebra'], 
                                            'git-tree-sha1': '051c95d6836228d120f5f4b984dd5aba1624f716', 
                                            'uuid': '621f4979-c628-5d54-868e-fcf4e3e8185c', 
                                            'version': '0.5.0'}
                                    ]
                }
    (name, data), = test_data.items()

    test_component = Component(
                                name=name,
                                version=data[0].get("version"),
                                hashes=bld.get_julia_hash(data[0].get('git-tree-sha1'))
                            )
    
    ret = bld.get_component(component_name=name, component_data=data)

    assert ret == test_component


def test_get_components():
    test_components = {
                            'AbstractFFTs': [
                                            {'deps': ['LinearAlgebra'], 
                                                'git-tree-sha1': '051c95d6836228d120f5f4b984dd5aba1624f716', 
                                                'uuid': '621f4979-c628-5d54-868e-fcf4e3e8185c', 
                                                'version': '0.5.0'}
                                        ], 
                            'AbstractTrees': [
                                            {
                                                'git-tree-sha1': '03e0550477d86222521d254b741d470ba17ea0b5', 
                                                'uuid': '1520ce14-60c1-5f80-bbc7-55ef81b5835c', 
                                                'version': '0.3.4'
                                                }
                                        ]
                    }
    
    name1, data1 = list(test_components.items())[0]
    name2, data2 = list(test_components.items())[1]

    test_component_list = [
                            Component(
                                                    name=name1,
                                                    version=data1[0].get("version"),
                                                    hashes=bld.get_julia_hash(data1[0].get('git-tree-sha1'))
                                    ),
                            
                            Component(
                                                    name=name2,
                                                    version=data2[0].get("version"),
                                                    hashes=bld.get_julia_hash(data2[0].get('git-tree-sha1'))
                                    )
                        ]
    
    ret = bld.get_components(test_components)


    assert ret == test_component_list







