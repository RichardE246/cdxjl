from cdxjl import flags



def test_args():
    testargs = ["-p", "juliaproject", "-o", "sbomfile.json"]
    project, out = flags.get_arguments(testargs)
    assert project == "juliaproject" and out == "sbomfile.json"