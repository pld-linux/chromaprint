#
# Conditional build:
%bcond_without	ffmpeg	# fpcalc build + libchromaprint using avfft
%bcond_with	fftw3	# libchromaprint using fftw3 instead of avfft
#
%if %{without ffmpeg}
%define	with_fftw3	1
%endif
Summary:	Library implementing the AcoustID fingerprinting
Summary(pl.UTF-8):	Biblioteka implementująca odciski AcoustID
Name:		chromaprint
Version:	1.5.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/acoustid/chromaprint/releases
Source0:	https://github.com/acoustid/chromaprint/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	54e71f86bcf1d34989db639044ba9628
URL:		https://acoustid.org/chromaprint
BuildRequires:	cmake >= 3.3
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel >= 0.6}
%{?with_fftw3:BuildRequires:	fftw3-devel >= 3}
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	taglib-devel
Requires:	libchromaprint = %{version}-%{release}
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
install -d build
cd build
%cmake .. \
	%{?with_ffmpeg:-DBUILD_TOOLS=ON} \
	%{!?with_fftw3:-DWITH_AVFFT=ON} \
	%{?with_fftw3:-DWITH_FFTW3=ON}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm  -rf $RPM_BUILD_ROOT

%post	-n libchromaprint -p /sbin/ldconfig
%postun	-n libchromaprint -p /sbin/ldconfig

%if %{with ffmpeg}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fpcalc
%endif

%files -n libchromaprint
%defattr(644,root,root,755)
%doc NEWS.txt README.md
%attr(755,root,root) %{_libdir}/libchromaprint.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchromaprint.so.1

%files -n libchromaprint-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libchromaprint.so
%{_includedir}/chromaprint.h
%{_pkgconfigdir}/libchromaprint.pc
