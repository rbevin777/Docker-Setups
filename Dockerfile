# I followed this tutorial here: https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-your-first-docker-application-cc03de9b639f/
# And made modifications to best suit my own purposes

# A dockerfile must always start by importing the base image.
# We use the keyword 'FROM' to do that.
# In our example, we want import the gcc image.
# So we write 'gcc' for the image name and 'latest' for the version.
FROM gcc:latest

# In order to launch our C code, we must import it into our image.
# We use the keyword 'COPY' to do that.
# The first parameter 'main.c' is the name of the file on the host.
# The second parameter '/' is the path where to put the file on the image.
# Here we put the file at the image root folder.
COPY . /usr/src/main.c
#WORKDIR /usr/src/

# We need to define the command to launch when we are going to run the image.
# We use the keyword 'CMD' to do that.
# The following commands will compile our code and run it to print hello world.
#RUN "gcc main.c -o main"
#CMD ["./main"]