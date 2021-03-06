# NOTE: now maintained in xorg-proto-xorgproto.spec
Summary:	XF86BigFont extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia XF86BigFont
Name:		xorg-proto-xf86bigfontproto
Version:	1.2.0
Release:	2.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/proto/xf86bigfontproto-%{version}.tar.bz2
# Source0-md5:	120e226ede5a4687b25dd357cc9b8efe
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XF86BigFont extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia XF86BigFont.

%package devel
Summary:	XF86BigFont extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia XF86BigFont
Group:		X11/Development/Libraries
Requires:	xorg-proto-fontsproto-devel

%description devel
XF86BigFont extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia XF86BigFont.

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
%{_includedir}/X11/extensions/xf86bigf*.h
%{_pkgconfigdir}/xf86bigfontproto.pc
