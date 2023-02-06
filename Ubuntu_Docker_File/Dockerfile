# I followed this tutorial here: https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-your-first-docker-application-cc03de9b639f/
# And made modifications to best suit my own purposes

# Setup using ubuntu image.
FROM ubuntu:latest

# Create a user working directory.
WORKDIR /tmp

# Setup apt packages.
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    rm -rf /var/lib/apt/lists/*

# Add repo to docker image so we can install other packages.
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4 && \
    add-apt-repository 'deb [arch=amd64] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse' 

# Install tools.
RUN apt-get install -y neofetch
RUN apt-get install -y nano
RUN apt-get install -y vim

