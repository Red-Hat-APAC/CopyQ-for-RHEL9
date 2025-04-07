Name:           CopyQ
Version:        10.0.0
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
* Apr 04, 2025, 06:25 AM UTC Hulk
  Added
  * Emacs navigation key-bindings support.
  * Adds support for setting urgency and persistency to notifications. Script
    function `notification()` takes new arguments: '.urgency' (low, normal, high,
    critical), '.persistent' (toggle persistent notification)

  Changed
  * Updates icon font from Font-Awesome 6.7.2.
  * On Windows, the main window is shown when starting the application using
    the program icon (#2965).
  * Calling `exit()` script function prints "Terminating server" on stderr
    instead of stdout.

  Fixed
  * Fixes item selection with Ctrl+Space (#2850).
  * Fixes confirming exit if any commands are running.
  * Fixes selecting specific row on search (#2770).
  * Clipboard data cloning will be now aborted if the data changes during the
    process. This avoids using incomplete data in rare cases.
  * Fixes contrast of the selected row number color (#2887). The row number text
    color of selected item is set to the same color as item text by default. This
    can be overridden via "Edit Theme" button using option `num_sel_fg`.
  * Fixes internal editor syntax highlighting for numbers containing separators
    (for example `100_000`, `0x1234_abcd`) and avoids incorrectly highlighting
    multiple lines as regular expression in some cases.
  * On GNOME (Wayland session), the clipboard monitor and provider processes run
    in XWayland mode because GNOME does not support Wayland data control
    protocol. This behavior can be skipped by settings `QT_QPA_PLATFORM`
    environment variable to "wayland" (or other value).
  * On Wayland compositors, fixes unnecessary application start delay if
    clipboard access (the data control protocol) is not supported.
  * On Linux, the "Ignore items with no or single character" predefined command
    properly avoids synchronizing empty text or single character.
  * On Linux, fixes waiting on keyboard modifiers release when synchronizing
    selection.
  * Avoids recursive item preview updates when using display commands.
  * Avoids removing items if drag'n'drop action fails.
  * Wayland: Fixes crash if getting owned clipboard data.
  * Wayland: Fixes setting UTF-8 text on broken GNOME's XWayland.
