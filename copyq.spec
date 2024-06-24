Name:           CopyQ
Version:        9.0.0
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
* Jun 22, 2024, 06:51 PM GMT+10 2024 Hulk
  Added
    * Adds editItem() script function for editing any item format (#2672).
    * Item color is now shown in tray menu as the default icon (#2700).

  Changed
    * Removes large margins in the tab tree.
    * Single action "Toggle Tag …" replaces the two separate actions "Tag as …" and
      "Remove tag …" for each custom tag (this can make the item context menu a lot
      more compact).
    * Selected items can now be accessed even from commands started from outside
      the app using global commands or from command line.
    * The dialog() script function can now be used for asking Yes/No questions
      without providing any fields. In such case, the function will return true
      instead of undefined after accepting the dialog.
    * The execute() script function now throws an exception when command cannot
      be executed instead of returning undefine.

  Fixed
    * Includes many performance improvements for working with large amount of items.
    * Fixes triggering menu items by number (#2569).
    * Fixes text color in the internal item editor (#2643).
    * Fixes showing global shortcuts in tray menu (#2382).
    * Fixes passing captured texts to automated commands (#2707).
    * Fixes duplicate synchronized items after tagging or modifying data.
    * Fixes situation when display commands stop updating items.
    * The pre-defined "Move to tab" action will be shown only if the current tab is
      not the same as target tab (#2669). Previously, in such case the item was
      removed unexpectedly.
    * Windows: Detect and ignore secrets from more apps (#2679).
    * Linux: Fixes storing previously synchronized clipboard (#2630).
    * Linux: Fixes storing selection when "Store text selected using mouse" option
      is enabled but "Run automatic commands on selection" is disabled (#2651).
    * Linux: Fixes clipboard synchronization with Qt 6 GUI framework.
    * Linux: Fixes showing tab tree labels with Qt 6 GUI framework.
