import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description="cdxjl")
    parser.add_argument("-p", type=str, required=True, help="Julia project file path.")
    parser.add_argument("-o", type=str, required=True, help="SBOM output file")
    args=parser.parse_args()
    file_path = args.p
    output_file = args.o
    return file_path, output_file




