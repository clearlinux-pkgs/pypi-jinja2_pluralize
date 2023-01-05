#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jinja2_pluralize
Version  : 0.3.0
Release  : 14
URL      : https://files.pythonhosted.org/packages/bb/1e/9d5a177fd1e4f74091743777518c432ad290c4630aac557b61087dffd6df/jinja2_pluralize-0.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/bb/1e/9d5a177fd1e4f74091743777518c432ad290c4630aac557b61087dffd6df/jinja2_pluralize-0.3.0.tar.gz
Summary  : Jinja2 pluralize filters.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jinja2_pluralize-license = %{version}-%{release}
Requires: pypi-jinja2_pluralize-python = %{version}-%{release}
Requires: pypi-jinja2_pluralize-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(inflect)
BuildRequires : pypi(jinja2)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Jinja2 Pluralize
        ===============================

%package license
Summary: license components for the pypi-jinja2_pluralize package.
Group: Default

%description license
license components for the pypi-jinja2_pluralize package.


%package python
Summary: python components for the pypi-jinja2_pluralize package.
Group: Default
Requires: pypi-jinja2_pluralize-python3 = %{version}-%{release}

%description python
python components for the pypi-jinja2_pluralize package.


%package python3
Summary: python3 components for the pypi-jinja2_pluralize package.
Group: Default
Requires: python3-core
Provides: pypi(jinja2_pluralize)
Requires: pypi(inflect)
Requires: pypi(jinja2)

%description python3
python3 components for the pypi-jinja2_pluralize package.


%prep
%setup -q -n jinja2_pluralize-0.3.0
cd %{_builddir}/jinja2_pluralize-0.3.0
pushd ..
cp -a jinja2_pluralize-0.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672284137
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jinja2_pluralize
cp %{_builddir}/jinja2_pluralize-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jinja2_pluralize/118be01e666f044d00718e2d1845210cba2f2fff || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jinja2_pluralize/118be01e666f044d00718e2d1845210cba2f2fff

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
