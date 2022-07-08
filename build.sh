#!/bin/zsh

# Run the build
podman build -t copyq-6.2.0 -f Containerfile .
podman run --name copyq-6.2.0 copyq-6.2.0
# Copy the artifacts from inside the container
podman cp copyq-6.2.0:/root/rpmbuild/RPMS/x86_64/CopyQ-6.2.0-1.el9.x86_64.rpm .
podman cp copyq-6.2.0:/root/rpmbuild/RPMS/x86_64/CopyQ-6.2.0-1.el9.x86_64.md5 .
podman cp copyq-6.2.0:/root/rpmbuild/SRPMS/CopyQ-6.2.0-1.el9.src.rpm .
podman cp copyq-6.2.0:/root/rpmbuild/SRPMS/CopyQ-6.2.0-1.el9.src.md5 .
# Cleanup container & image
# podman rm copyq-6.2.0
# podman rmi copyq-6.2.0
