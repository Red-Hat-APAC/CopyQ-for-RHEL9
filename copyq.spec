Name:           CopyQ
Version:        11.0.0
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
* Aug 22, 2025, 06:35 PM UTC Hulk
  Added
  * Adds support for dark/light window title scheme.
  * New frameless_window option (#2570) toggles the main window frame and title
    bar (if supported by the window manager)
  * Adds support for localizing command names in the command INI files (#3032)
  * Adds support for showing preview for more image formats
    (namely ico and webp).
  * Adds support for more complex network requests in scripts. New
    NetworkRequest class can be used to set custom headers, HTTP method, number
    of allowed redirects and timeout.

  Changed
  * Avoids hiding the main window on backspace (#3107).
  * Enables Vi/Emacs navigation (#3012) in menus, and Ctrl+[ in Vi and Ctrl+G
    in Emacs to work in many other places as Esc key (for example, to hide menus,
    dialogs). Users can override shortcuts, but not some reserved ones in
    specific cases (mainly, if the item list or a menu has focus).
  * Selections and current items/rows/data in scripts now only relate to the
    tab selected with tab(...) in scripts (this is still by default the
    selected tab when the command started).
  * Drops unnecessary timeouts when executing commands and actions from scripts.
  * Avoids fetching and passing clipboard to action()/execute() if the
    commands do not contains %1 placeholder. This can improve performance.
