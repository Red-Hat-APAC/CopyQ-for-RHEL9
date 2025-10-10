Name:           CopyQ
Version:        12.0.1
Release:        1%{?dist}
Summary:        CopyQ monitors system clipboard and saves its content in customized tabs.
Group:          Applications/Multimedia
License:        GPL
URL:            https://hluk.github.io/CopyQ/
Vendor:         Hluk
Source:         https://github.com/hluk/%{name}/archive/v%{version}.tar.gz
Prefix:         %{_prefix}
Packager:       lmaly@redhat.com
BuildRoot:      %{_tmppath}/%{name}-root

%description
CopyQ monitors system clipboard and saves its content in customized tabs. Saved clipboard can be later copied and pasted directly into any application.

%global debug_package %{nil}

%prep

%setup -q -n %{name}-%{version}

%build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local .
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
/*

%changelog
* Tue Sep 30 2025 Hluk <hluk@email.cz> - 12.0.1
  - X11: Fix registering global shortcuts with modifiers (#3212)
  - macOS: Fix providing builds for Intel architecture
  - Fix maximum length for session name (16 characters, not 15)
