# $Rev: 3247 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	XF86BigFont protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u XF86BigFont i pomocnicze
Name:		xorg-proto-xf86bigfontproto
Version:	1.1
Release:	0.03
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/xf86bigfontproto-%{version}.tar.bz2
# Source0-md5:	64e07e66df4df483f221492bac2edef6
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/xf86bigfontproto-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XF86BigFont protocol and ancillary headers.

%description -l pl
Nag��wki protoko�u XF86BigFont i pomocnicze


%package devel
Summary:	XF86BigFont protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u XF86BigFont i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-fontsproto-devel

%description devel
XF86BigFont protocol and ancillary headers.

%description devel -l pl
Nag��wki protoko�u XF86BigFont i pomocnicze


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
