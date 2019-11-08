FROM python:3.7.3
ENV WORKING_DIR /app
WORKDIR ${WORKING_DIR}
COPY ./requirements.txt ${WORKING_DIR}/requirements.txt
RUN pip install -U pip && pip install -r ${WORKING_DIR}/requirements.txt
ADD . ${WORKING_DIR}
RUN rm -fr ${WORKING_DIR}/initiator/Logs/*
RUN rm -fr ${WORKING_DIR}/initiator/Sessions/*
RUN rm -fr ${WORKING_DIR}/acceptor/Logs/*
RUN rm -fr ${WORKING_DIR}/acceptor/Sessions/*
