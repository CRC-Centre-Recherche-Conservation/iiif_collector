import click
import tqdm
import os
import requests

from scr.iiif import ManifestIIIF
from scr.utils import make_out_dirs

# test https://bvmm.irht.cnrs.fr/iiif/17495/manifest
# ref 1 https://github.com/PonteIneptique/iiif-random-downloader/blob/main/cli.py
# ref 2 https://github.com/YaleDHLab/iiif-downloader/blob/master/iiif_downloader/__init__.py#L16


@click.command()
@click.argument("url", type=click.STRING)
@click.option("-d", "--directory", "directory", type=click.Path(exists=True, dir_okay=True, file_okay=False), default="./",
              help="Directory where to save the images")
@click.option("-n", "--number", "number", type=int, help="Number of images to save", default=10)
@click.option("-v", "--verbose", "verbose", type=bool, default=False)
def run_collect(url, directory, **kwargs):
    """
    Running script to get and download iiif images, metadata and manifests

    :param url: url
    :param directory: str, path to directory files as you want !
    :return:
    """

    current_path = os.path.dirname(os.path.abspath(__file__))
    if directory != "./":
        current_path = os.path.join(current_path, directory)

    manifest = ManifestIIIF(str(url), path=current_path, n=kwargs['number'], verbose=kwargs['verbose'])
    if kwargs['verbose']:
        print("Creating directory to IIIF files")
    #make_out_dirs(manifest.out_dir)

    manifest.get_images_from_manifest()

if __name__ == "__main__":
    run_collect()
