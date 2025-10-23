# Thu 23 Oct 2025 01:59:54 UTC
FROM registry.access.redhat.com/ubi10:10.0-1760519443
MAINTAINER lmaly@redhat.com
ENV COPYQ_VER=13.0.0
ENV RELEASEVER=10
RUN dnf install -y --disableplugin=subscription-manager https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
RUN dnf install -y --enablerepo=rhel-10-for-x86_64-appstream-rpms --enablerepo=codeready-builder-for-rhel-10-x86_64-rpms \
  cmake \
  extra-cmake-modules \
  gcc-c++ \
  git \
  kf6-kguiaddons-devel \
  kf6-knotifications-devel \
  kf6-kstatusnotifieritem-devel \
  libSM-devel \
  libXfixes-devel \
  libXtst-devel \
  qt6-qtbase-devel \
  qt6-qtbase-private-devel \
  qt6-qtdeclarative-devel \
  qt6-qtsvg-devel \
  qt6-qttools-devel \
  qt6-qtwayland-devel \
  rpmdevtools \
  wayland-devel \
  wget
RUN rpmdev-setuptree
COPY copyq.spec /root/rpmbuild/SPECS/
RUN cd /root/rpmbuild/SOURCES/ && wget https://github.com/hluk/CopyQ/archive/refs/tags/v${COPYQ_VER}.tar.gz
RUN rpmbuild -ba /root/rpmbuild/SPECS/copyq.spec
RUN md5sum /root/rpmbuild/RPMS/x86_64/CopyQ-${COPYQ_VER}-1.el${RELEASEVER}.x86_64.rpm > /root/rpmbuild/RPMS/x86_64/CopyQ-${COPYQ_VER}-1.el${RELEASEVER}.x86_64.md5
RUN md5sum /root/rpmbuild/SRPMS/CopyQ-${COPYQ_VER}-1.el${RELEASEVER}.src.rpm > /root/rpmbuild/SRPMS/CopyQ-${COPYQ_VER}-1.el${RELEASEVER}.src.md5
