FROM nginx

ARG PROJECT

WORKDIR /opt/${PROJECT}

RUN ln -sf /opt/${PROJECT}/nginx/default.conf /etc/nginx/conf.d/default.conf

COPY ./ ${WORKDIR}

COPY ./docker-config/entrypoint.sh /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint"]
