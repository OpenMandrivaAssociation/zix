	
%global         maj 0
 
Name:           zix
Version:        0.4.0
Release:        1
Summary:        A lightweight C library of portability wrappers and data structures
 
License:        ISC
URL:            https://gitlab.com/drobilla/%{name}
Source0:        https://download.drobilla.net/%{name}-%{version}.tar.xz
 
BuildRequires:  meson
BuildRequires:  doxygen
BuildRequires:  python-sphinx
#BuildRequires:  python-sphinxygen
 
%description
%{name} is a lightweight C library of portability wrappers and data structures.
 
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
 
%package        doc
Summary:        Documentation files for %{name}
Provides:       bundled(js-jquery) = 3.6.0
Buildarch:      noarch
 
%description    doc
The %{name}-doc package contains documentation files for
developing applications that use %{name}.
 
%prep
%autosetup -p1

%build
# Do not build benchmarks
%meson 	\
	-Dbenchmarks=disabled \
 	-Ddocs=disabled \
  	-Dhtml=disabled \
   	-Dsinglehtml=disabled
%meson_build

%install
%meson_install
# Delete duplicated sphinx docs
rm -rf %{buildroot}%{_docdir}/%{name}-%{maj}/singlehtml
# Delete sphinx buildinfo
rm -f %{buildroot}%{_docdir}/%{name}-%{maj}/html/.buildinfo
# Move devel docs to the right directory
install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_docdir}/%{name}-%{maj} %{buildroot}%{_docdir}/%{name}
 
%check
%meson_test
%files
%license COPYING
%doc README.md
%{_libdir}/lib%{name}-%{maj}.so.%{maj}*
 
%files devel
%{_includedir}/%{name}-%{maj}
%{_libdir}/lib%{name}-%{maj}.so
%{_libdir}/pkgconfig/%{name}-%{maj}.pc
 
%files doc
%license COPYING
%doc %{_docdir}/%{name}/%{name}-%{maj}
