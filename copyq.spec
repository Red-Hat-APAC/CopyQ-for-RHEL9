Name:           CopyQ
Version:        8.0.0
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
* Mar 14, 2024, 11:57 PM GMT+11 2024 Hulk
  Added
    * Tab item limit has been increased to 100,000 (#1144).
    * New macOS builds for M1/arm64 architectures are available (#1884).
    * New Debian/Raspbian builds for arm/arm64 architectures are available.
    * Allows overriding item activation using paste().
    * Allows overriding script functions to handle some events: items
      added/removed/changed (onItemsAdded(), onItemsRemoved(),
      onItemsChanged()), tab items loaded (onItemsLoaded()), tab selected
      (onTabSelected()) (#59).
    * Allows to cancel removing items by overriding onItemsRemoved() script
      function. If the exit code is non-zero (for example fail() is called),
      items will not be removed. But this can also cause a new items not to be
      added if the tab is full.
    * Allows overriding current clipboard owner (currentClipboardOwner()) used by
      the clipboard monitor process. By default it uses currentWindowTitle().
    * Allows using Ctrl+C to copy items even if search entry box is focused unless
      it has a selection (#2440).
    * Linux: Adds build option to disable X11 support (cmake -DWITH_X11=OFF ...)
      (#2532).
    * Linux: Adds build option to disable autostart which is useful mainly for
      Flatpak builds (#2517, #2518).

  Changed
    * Windows binaries (which are 64 bit) are now by default installed to "Program
      Files" instead of incorrect "Program Files (X86)". After installing the new
      version, the old path must be manually removed.
    * Windows and macOS builds are now based on newer Qt 6.
    * Avoids accessing clipboard from password managers (#2282, #2495, #2500). This
      disallows storing and processing such data. Specifically, the clipboard is
      ignored if it contains following data: Clipboard Viewer Ignore on Windows,
      application/x-nspasteboard-concealed-type on macOS,
      x-kde-passwordManagerHint with secret value on Linux.
    * Large data items in tabs are now stored in separate location unless
      Synchronize or Encryption plugins are active for the tab. This allows storing
      more items in tabs while using less memory. The data path can be printed via
      copyq info data command and overridden using COPYQ_ITEM_DATA_PATH
      environment variable. To disable this functionality use copyq config item_data_threshold -1 - the default value is 1024 and items larger than
      this amount of bytes are stored in the separate location.
    * Command dialog now shows advanced properties for built-in commands allowing
      to copy the command line to set global shortcut in system.
    * Global shortcuts are now also visible in menus (#2382).
    * Avoids pasting all image formats as new item.
    * Display commands are now applied to tray menu items too.
    * Linux: Last stored text item is updated from any new mouse selection only if
      the item content matches the start or the end of the selection (but not the
      middle like previously). This may avoid some unexpected item updates.
    * Updates icon font from Font-Awesome 6.5.1.

  Fixed
    * Fixes drag'n'drop ordering for plugins and commands. This could have caused a
      missing icon, app crash or various inconsistencies.
    * Fixes managing keys with gpg 2.1 and above (#2463, #1208).
    * Fixes creating duplicate item with Synchronize plugin when adding a tag for
      example (#2355).
    * Fixes conflicting notes and text with Synchronize plugin (#2355)
    * Fixes deleted global object after running scripts (#2542).
    * Wayland: Fixes copying images to another app instance.
