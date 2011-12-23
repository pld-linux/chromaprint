Summary:	Library implementing the AcoustID fingerprinting
Name:		chromaprint
Version:	0.5
Release:	1
License:	LGPL v2+
Group:		Libraries
URL:		http://www.acoustid.org/chromaprint/
Source0:	https://github.com/downloads/lalinsky/chromaprint/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	fftw3-devel >= 3
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chromaprint library is the core component of the AcoustID project.
It's a client-side library that implements a custom algorithm for
extracting fingerprints from raw audio sources.

The library exposes a simple C API and the package also includes
bindings for the Python language. The documentation for the C API can
be found in the main header file.

%package -n libchromaprint
Summary:	Library implementing the AcoustID fingerprinting
Group:		Development/Libraries

%description -n libchromaprint
Chromaprint library is the core component of the AcoustID project.
It's a client-side library that implements a custom algorithm for
extracting fingerprints from raw audio sources.

The library exposes a simple C API and the package also includes
bindings for the Python language. The documentation for the C API can
be found in the main header file.

%package -n libchromaprint-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Libraries
Requires:	libchromaprint = %{version}-%{release}
Requires:	pkgconfig

%description -n libchromaprint-devel
This package contains the headers that programmers will need to
develop applications which will use %{name}.

%package -n python-chromaprint
Summary:	Python module for %{name}
License:	MIT
Group:		Development/Libraries
Requires:	libchromaprint = %{version}-%{release}

%description -n python-chromaprint
This package contains the python module to use %{name}.

%prep
%setup -q

%build
# examples require ffmpeg, so turn off examples
%cmake \
	-DBUILD_EXAMPLES=off \
	-DBUILD_TESTS=off

%{__make}

cd python
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd python
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm  -rf $RPM_BUILD_ROOT

%post	-n libchromaprint -p /sbin/ldconfig
%postun	-n libchromaprint -p /sbin/ldconfig

%files -n libchromaprint
%defattr(644,root,root,755)
%doc CHANGES.txt COPYING.txt NEWS.txt README.txt
%attr(755,root,root) %{_libdir}/libchromaprint.so.*.*.*
%ghost %{_libdir}/libchromaprint.so.0

%files -n libchromaprint-devel
%defattr(644,root,root,755)
%{_includedir}/chromaprint.h
%{_libdir}/libchromaprint.so
%{_pkgconfigdir}/libchromaprint.pc

# MIT licensed
%files -n python-chromaprint
%defattr(644,root,root,755)
%doc python/examples python/LICENSE
%{py_sitescriptdir}/chromaprint
%{py_sitescriptdir}/*.egg-info
