Summary:	XF86BigFont protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu XF86BigFont i pomocnicze
Name:		xorg-proto-xf86bigfontproto
Version:	1.1.2
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/proto/xf86bigfontproto-%{version}.tar.bz2
# Source0-md5:	a318c1e86123832d7b0c95fc7d47ef35
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XF86BigFont protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu XF86BigFont i pomocnicze.

%package devel
Summary:	XF86BigFont protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu XF86BigFont i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-fontsproto-devel

%description devel
XF86BigFont protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu XF86BigFont i pomocnicze

%prep
%setup -q -n xf86bigfontproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xf86bigfontproto.pc
