# Fri Jul 8 00:11:39 UTC 2022
FROM registry.access.redhat.com/ubi9@sha256:a8ea009de0c2bc5a33f6c7b83133ce6f83f927bf0ac770ee1cbea48bc47c6879
MAINTAINER lmaly@redhat.com
RUN dnf install -y --disableplugin=subscription-manager https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
RUN dnf install -y --enablerepo=rhel-9-for-x86_64-appstream-rpms \
  cmake \
  extra-cmake-modules \
  gcc-c++ \
  git \
  kf5-knotifications-devel \
  libSM-devel \
  libXfixes-devel \
  libXtst-devel \
  qt5-qtbase-devel \
  qt5-qtbase-private-devel \
  qt5-qtdeclarative-devel \
  qt5-qtsvg-devel \
  qt5-qttools-devel \
  qt5-qtwayland-devel \
  qt5-qtx11extras-devel \
  rpmdevtools \
  wayland-devel \
  wget
RUN rpmdev-setuptree
COPY copyq.spec /root/rpmbuild/SPECS/
RUN cd /root/rpmbuild/SOURCES/ && wget https://github.com/hluk/CopyQ/archive/refs/tags/v6.2.0.tar.gz
RUN rpmbuild -ba /root/rpmbuild/SPECS/copyq.spec
RUN md5sum /root/rpmbuild/RPMS/x86_64/CopyQ-6.2.0-1.el9.x86_64.rpm > /root/rpmbuild/RPMS/x86_64/CopyQ-6.2.0-1.el9.x86_64.md5
RUN md5sum /root/rpmbuild/SRPMS/CopyQ-6.2.0-1.el9.src.rpm > /root/rpmbuild/SRPMS/CopyQ-6.2.0-1.el9.src.md5
