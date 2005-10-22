Summary:	XF86BigFont protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u XF86BigFont i pomocnicze
Name:		xorg-proto-xf86bigfontproto
Version:	1.1.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/xf86bigfontproto-%{version}.tar.bz2
# Source0-md5:	e93b1b833a0531e546bf6f4cfbde4786
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XF86BigFont protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u XF86BigFont i pomocnicze.

%package devel
Summary:	XF86BigFont protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u XF86BigFont i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-fontsproto-devel

%description devel
XF86BigFont protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u XF86BigFont i pomocnicze

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xf86bigfontproto.pc
