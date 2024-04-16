FROM spack/ubuntu-jammy:v0.20.1 AS builder

# What we want to install and how we want to install it
# is specified in a manifest file (spack.yaml)
RUN mkdir /opt/spack-environment \
&&  (echo spack: \
&&   echo '  # add package specs to the `specs` list' \
&&   echo '  specs: [paraview+mpi+osmesa+python~qt ^mesa+osmesa+llvm ^llvm~clang~lld~gold ^openmpi+legacylaunchers+pmi+thread_multiple fabrics=ucx schedulers=slurm]' \
&&   echo '  view: /opt/views/view' \
&&   echo '  concretizer:' \
&&   echo '    unify: true' \
&&   echo '  config:' \
&&   echo '    install_tree: /opt/software') > /opt/spack-environment/spack.yaml

WORKDIR /opt/spack-environment

RUN spack env activate . && spack concretize && spack install

# Modifications to the environment that are necessary to run
RUN spack env activate --sh -d . > activate.sh

FROM spack/ubuntu-jammy:v0.20.1 AS build

COPY --from=builder /opt/spack-environment /opt/spack-environment
COPY --from=builder /opt/software /opt/software
COPY --from=builder /opt/views /opt/views

RUN { \
      echo '#!/bin/sh' \
      && echo '.' /opt/spack-environment/activate.sh \
      && echo 'exec "$@"'; \
    } > /entrypoint.sh \
&& chmod a+x /entrypoint.sh \
&& ln -s /opt/views/view /opt/view

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "/bin/bash" ]

EXPOSE 11112