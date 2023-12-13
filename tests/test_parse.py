from cdxjl.parse import parser


parse = parser("example_data")


def test_read_project():
    test_dict = {
                    "name": "Example_Julia_Project",
                    "uuid": "d9c4a96b-6299-43f5-9d34-05b6b65b3224",
                    "authors": ["author <author@email.com>"],
                    "version": "0.1.0",
                    "deps":{
                                "Flux": "587475ba-b771-5e3f-ad9e-33799f191a9c",
                                "Plots": "91a5bcdd-55d7-5caf-9e0b-520d859cae80"
                    }
                }
    
    ret = parse.read_project()
    assert ret == test_dict



def test_read_manifest():
    test_dict = {
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
    
    ret = parse.read_manifest()
    assert ret == test_dict



def test_get_data():
    test_dict_1 = {
                "name": "Example_Julia_Project",
                "uuid": "d9c4a96b-6299-43f5-9d34-05b6b65b3224",
                "authors": ["author <author@email.com>"],
                "version": "0.1.0",
                "deps":{
                            "Flux": "587475ba-b771-5e3f-ad9e-33799f191a9c",
                            "Plots": "91a5bcdd-55d7-5caf-9e0b-520d859cae80"
                }
            }
    
    test_dict_2 = {
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

    ret_1, ret_2 = parse.get_julia_data()
    assert ret_1 == test_dict_1 and ret_2 == test_dict_2


