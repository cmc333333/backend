FROM node:6.6.0

EXPOSE 8000
EXPOSE 5858
EXPOSE 8080

RUN apt-get update

# for network testing 
RUN apt-get install -y netcat

# for editing 
RUN apt-get install -y vim-tiny

RUN apt-get install -y git

#
# It would be excellent to have this file run the
# following commands, where the contents
# of the nodeAppPostPg folder are files on the host as in:
# docker run -v $(pwd):/usr/src/app ...
#

ARG CACHEBUST=1
ARG BRANCH_NAME=docker-1
ARG REPO=https://github.com/jkbits1/backend

WORKDIR /usr/src/app/

RUN git clone --single-branch --branch $BRANCH_NAME $REPO \
&& cd /usr/src/app/backend/db \
&& git checkout $BRANCH_NAME

WORKDIR /usr/src/app/backend/nodeAppPostPg

RUN git fetch origin
RUN git merge origin/$BRANCH_NAME

RUN cd /usr/src/app/backend/nodeAppPostPg

RUN npm install

# can't get these two lines going yet
# RUN . ./scripts/expo.sh

ENV PORT=8000 PGUSER=carpool_web PGDATABASE=carpoolvote
# ENV PGHOST=$CP_PG_SVR_PORT_5432_TCP_ADDR PGPASSWORD=$CP_PG_SVR_ENV_POSTGRES_PASSWORD 

COPY ./expo-start.sh /
COPY ./expo-bash.sh /

# these steps may be needed
# https://github.com/moby/moby/issues/27182
RUN chmod +x /expo-start.sh
RUN chmod +x /expo-bash.sh

# RUN npm install -g nightwatch

# ENTRYPOINT ["/expo-start.sh"]
CMD ["/expo-start.sh"]


# CMD ["npm start"]

