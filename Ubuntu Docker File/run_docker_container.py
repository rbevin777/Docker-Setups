import os
import click


class DockerInfo:
    
    def __init__(self, image_name, volume_name):
        self.image_name = image_name
        self.volume_name = volume_name
    
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

    
    
@click.command()
@click.option("--volume_name", default="ubuntu-vol-1", help="Enter a Docker Volume Name")
@click.option("--image_name", default="ubuntu-img-1", help="Enter a Docker Image Name")
def run_docker_container(image_name, volume_name):
    """ Simple program that will run a docker container with a given volume and image. """
    docker_run = DockerInfo(image_name, volume_name)
    docker_run.check_docker_volume_exists()


if __name__ == '__main__':
    run_docker_container()
