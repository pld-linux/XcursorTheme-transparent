Summary:	A fully transparent (invisible) X cursor theme
Summary(pl.UTF-8):   Całkowicie przezroczysty (niewidzialny) motyw kursora X
Name:		XcursorTheme-transparent
Version:	0.1.1
Release:	1
License:	GPL(?)
Group:		Themes
Source0:	http://projects.o-hand.com/matchbox/sources/utils/xcursor-transparent-theme-%{version}.tar.gz
# Source0-md5:	7b0c623049d4aab20600d6473f8aab23
Patch0:		xcursor-transparent-theme-make.patch
URL:		http://projects.o-hand.com/matchbox/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a totally transparent X cursor theme. Using
the theme provides an effective and flexible way to hide the X11
Cursor. This kind of behaviour maybe required on Handheld or embedded
computers running the X Window System.

%description -l pl.UTF-8
Ten pakiet zawiera całkowicie przezroczysty motyw kursora X. Użycie
tego motywu daje efektywny i elastyczny sposób ukrycia kursora X11.
Takie zachowanie może być wymagane na komputerach kieszonkowych czy
wbudowanych z działającym systemem X Window.

%prep
%setup -q -n xcursor-transparent-theme-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_iconsdir}/xcursor-transparent
