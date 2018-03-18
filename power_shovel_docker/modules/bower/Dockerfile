FROM builder.npm

RUN apt-get install -y git
RUN npm install bower

###### Builder Boilerplate ####################################################
ADD build /usr/bin/
RUN chmod +x /usr/bin/build
CMD 'build'

RUN touch /root/.bash_history
###############################################################################
