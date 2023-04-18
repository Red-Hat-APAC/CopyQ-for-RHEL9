#!/bin/bash
# Tue 18 Apr 2023 06:21:04 UTC
COPYQ_VER=7.0.0
ARCH=x86_64
RELEASEVER=9
# Run the build
podman build -t copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH} -f Containerfile .
podman run --name copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH} copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}
# Copy the artifacts from inside the container
podman cp copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}:/root/rpmbuild/RPMS/${ARCH}/CopyQ-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}.rpm .
podman cp copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}:/root/rpmbuild/RPMS/${ARCH}/CopyQ-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}.md5 .
podman cp copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}:/root/rpmbuild/SRPMS/CopyQ-${COPYQ_VER}-1.el${RELEASEVER}.src.rpm .
podman cp copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}:/root/rpmbuild/SRPMS/CopyQ-${COPYQ_VER}-1.el${RELEASEVER}.src.md5 .
# Cleanup container & image
podman rm copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}
podman rmi copyq-${COPYQ_VER}-1.el${RELEASEVER}.${ARCH}
# Cleanup UBI9
# podman images --format "{{.ID}} {{.Repository}}" | grep registry.access.redhat.com/ubi9 | cut -d ' ' -f 1 | xargs podman rmi
