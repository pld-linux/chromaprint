Summary:	Library implementing the AcoustID fingerprinting
Summary(pl.UTF-8):	Biblioteka implementująca odciski AcoustID
Name:		chromaprint
Version:	1.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://bitbucket.org/acoustid/chromaprint/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	748da044a8f0ee5f31edec8b67045b3e
URL:		https://acoustid.org/chromaprint
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.6
BuildRequires:	ffmpeg-devel >= 0.6
BuildRequires:	libstdc++-devel
BuildRequires:	taglib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chromaprint library is the core component of the AcoustID project.
It's a client-side library that implements a custom algorithm for
extracting fingerprints from raw audio sources.

The library exposes a simple C API and the Python language binding is
also available. The documentation for the C API can be found in the
main header file.

%description -l pl.UTF-8
Biblioteka Chromaprint to główny element projektu AcoustID. Jest to
biblioteka kliencka implementująca własny algorytm wydobywania
odcisków identyfikacyjnych z surowych strumieni dźwiękowych.

Biblioteka udostępnia proste API C. Dostępne są także wiązania dla
Pythona. Dokumentację dla API C można znaleźć w głównym pliku
nagłówkowym.

%package -n libchromaprint
Summary:	Library implementing the AcoustID fingerprinting
Summary(pl.UTF-8):	Biblioteka implementująca odciski AcoustID
Group:		Libraries

%description -n libchromaprint
Chromaprint library is the core component of the AcoustID project.
It's a client-side library that implements a custom algorithm for
extracting fingerprints from raw audio sources.

The library exposes a simple C API and the Python language binding
is also available. The documentation for the C API can be found in the
main header file.

%description -n libchromaprint -l pl.UTF-8
Biblioteka Chromaprint to główny element projektu AcoustID. Jest to
biblioteka kliencka implementująca własny algorytm wydobywania
odcisków identyfikacyjnych z surowych strumieni dźwiękowych.

Biblioteka udostępnia proste API C. Dostępne są także wiązania dla
Pythona. Dokumentację dla API C można znaleźć w głównym pliku
nagłówkowym.

%package -n libchromaprint-devel
Summary:	Headers for developing programs that will use libchromaprint
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia programów wykorzystujących libchromaprint
Group:		Development/Libraries
Requires:	libchromaprint = %{version}-%{release}

%description -n libchromaprint-devel
This package contains the headers that programmers will need to
develop applications which will use libchromaprint.

%description -n libchromaprint-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne programistom do
tworzenia aplikacji wykorzystujących bibliotekę libchromaprint.

%prep
%setup -q

%build
%cmake . \
	-DBUILD_EXAMPLES=ON \
	-DWITH_AVFFT=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm  -rf $RPM_BUILD_ROOT

%post	-n libchromaprint -p /sbin/ldconfig
%postun	-n libchromaprint -p /sbin/ldconfig

%files -n libchromaprint
%defattr(644,root,root,755)
%doc NEWS.txt README.md
%attr(755,root,root) %{_bindir}/fpcalc
%attr(755,root,root) %{_libdir}/libchromaprint.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchromaprint.so.0

%files -n libchromaprint-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libchromaprint.so
%{_includedir}/chromaprint.h
%{_pkgconfigdir}/libchromaprint.pc
