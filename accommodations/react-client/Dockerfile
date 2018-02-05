# base image
FROM node:8.6
EXPOSE 8080

# set working directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# add node_modules .bin directory to the path
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependancies
COPY . /usr/src/app/
RUN npm install ---silent

# Build for production.
RUN npm run build

# Install `serve` to run the application.
RUN npm install -g serve --silent

# start the app
# Set the command to start the node server.
CMD ["serve", "-s", "/usr/src/app/", "--port", "8080"]
