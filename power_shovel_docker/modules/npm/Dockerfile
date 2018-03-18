FROM ubuntu:artful-20180123

###### Builder Boilerplate ####################################################
RUN touch /root/.bash_history
ADD build /usr/bin/
RUN chmod +x /usr/bin/build
CMD 'build'
###############################################################################

# install NodeJS
ARG NODE_VERSION=8.x
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_$NODE_VERSION | bash -
RUN apt-get install -y nodejs
RUN npm config set ca="" --global

# install NPM Check Update
RUN npm install -g npm-check-updates
# TODO might need to do this to get NCU to working
#RUN ln -s /usr/bin/nodejs /usr/bin/node
