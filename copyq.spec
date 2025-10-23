Name:           CopyQ
Version:        13.0.0
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
* Wed Oct 22 2025 Hluk <hluk@email.cz> - 13.0.0
  - Windows: Preferences now include auto-start option, previously available only in the installer.
  - Tabs synchronized with a directory on the disk will now include files from sub-directories (#2638).
  - Filtering/searching items in large tabs no longer blocks UI (#3111, #3261).
  - Fixes saving edited HTML and setting style in internal editor (#3227).
  - Fixes updating selected item colors (#3219).
  - Wayland: Fixes clipboard access in KDE Plasma 6.5 (#3228). This requires KGuiAddons library installed on the system.
