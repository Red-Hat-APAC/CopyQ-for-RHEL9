Name:           CopyQ
Version:        9.1.0
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
* Oct 20, 2024, 5:27 PM GMT+11 Hulk
  Added
    * Allows processing all clipboard changes (#2787, #2746).
      If clipboard contains secret (for example, copied from a password manager),
      onSecretClipboardChanged() script function is called with data containing
      mimeSecret format set to 1. Also ensures that callbacks are called
      consistently for all clipboard changes with properly set formats
      mimeClipboardMode, mimeOutputTab and mimeCurrentTab.

  Fixed
    * Fixes editing multiple items (#2810).
    * Fixes synchronization plugin causing redundant UI updates and menu misbehavior (#2649).
    * Fixes showing sub-menus for custom commands in tray menu (#2730).
    * Fixes switching tab if onItemsLoaded() is overridden (#2788).
    * Fixes theme option hover_item_css (#2687).
    * Avoids modifying data from display commands and causing redundant UI updates (#2837).
    * Avoids sharing execute() state in case it is launched recursively.
