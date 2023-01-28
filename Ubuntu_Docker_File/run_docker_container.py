import os
import click


class DockerInfo:
    
    def __init__(self, image_name, volume_name, image_directory):
        self.image_name = image_name
        self.volume_name = volume_name
        self.image_directory = image_directory
    
    def create_docker_image(self):
        """ If one doesn't already exist, we want to create a docker image. """
        try:
            response = os.system(f"docker build -t {self.image_name} .")
        except:
            print(f"Unable build docker image {self.image_name}")
            
    def check_docker_volume_exists(self):
        """ Check if a volume exists, if it doesn't then create it, if it does then move on."""
        exists = False
        try:
            response = os.system(f"docker volume inspect {self.volume_name}")
            # If the reponse is not 256 then the volume exists.
            if not response == 256: # 256 is the standard response on a linux OS for this command. It may vary based on the OS and based on the command.
                exists = True
        except:
            print(f"Unable to check if volume {self.volume_name} exists")
        
        if exists:
            print(f"Docker Volume {self.volume_name} exists, skipping creation")
        else:
            os.system(f"docker volume create {self.volume_name}")

    def share_volume_into_container(self):
        """ Shares our created volume within the same container as the image. """
        try:
            os.system(f"docker run --rm -it -v `$(pwd)`:{self.image_directory} {self.image_name}")
        except:
            print(f"Unable to share volume {self.volume_name} to container {self.image_name}")

    
@click.command()
@click.option("--volume_name", default="ubuntu-vol-1", help="Enter a Docker Volume Name")
@click.option("--image_name", default="ubuntu-img-1", help="Enter a Docker Image Name")
@click.option("--image_directory", default="/tmp", help="Enter the directory path where we want to share the volume in the container.")
def run_docker_container(image_name, volume_name, image_directory):
    """ Simple program that will run a docker container with a given volume and image. """
    docker_run = DockerInfo(image_name, volume_name, image_directory)
    docker_run.create_docker_image()
    docker_run.check_docker_volume_exists()
    docker_run.share_volume_into_container()


if __name__ == '__main__':
    run_docker_container()
