import argparse


def get_arguments(args=None):
    parser = argparse.ArgumentParser(description="cdxjl: A Command Line Application to Create CycloneDX SBOMs from Julia Projects.")
    parser.add_argument("-p", type=str, required=True, help="Julia project file path.")
    parser.add_argument("-o", type=str, required=True, help="SBOM output file")
    args=parser.parse_args(args)
    file_path = args.p
    output_file = args.o
    return file_path, output_file




