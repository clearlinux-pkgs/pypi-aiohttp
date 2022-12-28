#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-aiohttp
Version  : 3.8.3
Release  : 20
URL      : https://files.pythonhosted.org/packages/ff/4f/62d9859b7d4e6dc32feda67815c5f5ab4421e6909e48cbc970b6a40d60b7/aiohttp-3.8.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/ff/4f/62d9859b7d4e6dc32feda67815c5f5ab4421e6909e48cbc970b6a40d60b7/aiohttp-3.8.3.tar.gz
Summary  : Async http client/server framework (asyncio)
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: pypi-aiohttp-filemap = %{version}-%{release}
Requires: pypi-aiohttp-lib = %{version}-%{release}
Requires: pypi-aiohttp-license = %{version}-%{release}
Requires: pypi-aiohttp-python = %{version}-%{release}
Requires: pypi-aiohttp-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : pypi(aiosignal)
BuildRequires : pypi(async_timeout)
BuildRequires : pypi(attrs)
BuildRequires : pypi(charset_normalizer)
BuildRequires : pypi(frozenlist)
BuildRequires : pypi(multidict)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(yarl)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
==================================
Async http client/server framework
==================================

%package filemap
Summary: filemap components for the pypi-aiohttp package.
Group: Default

%description filemap
filemap components for the pypi-aiohttp package.


%package lib
Summary: lib components for the pypi-aiohttp package.
Group: Libraries
Requires: pypi-aiohttp-license = %{version}-%{release}
Requires: pypi-aiohttp-filemap = %{version}-%{release}

%description lib
lib components for the pypi-aiohttp package.


%package license
Summary: license components for the pypi-aiohttp package.
Group: Default

%description license
license components for the pypi-aiohttp package.


%package python
Summary: python components for the pypi-aiohttp package.
Group: Default
Requires: pypi-aiohttp-python3 = %{version}-%{release}

%description python
python components for the pypi-aiohttp package.


%package python3
Summary: python3 components for the pypi-aiohttp package.
Group: Default
Requires: pypi-aiohttp-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(aiohttp)
Requires: pypi(aiodns)
Requires: pypi(aiosignal)
Requires: pypi(async_timeout)
Requires: pypi(attrs)
Requires: pypi(brotli)
Requires: pypi(charset_normalizer)
Requires: pypi(frozenlist)
Requires: pypi(multidict)
Requires: pypi(yarl)

%description python3
python3 components for the pypi-aiohttp package.


%prep
%setup -q -n aiohttp-3.8.3
cd %{_builddir}/aiohttp-3.8.3
pushd ..
cp -a aiohttp-3.8.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672249051
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . charset-normalizer
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . charset-normalizer
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-aiohttp
cp %{_builddir}/aiohttp-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-aiohttp/d4c7ca48f2d26cd60006bc2ace82041594ebfe63
cp %{_builddir}/aiohttp-%{version}/vendor/llhttp/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-aiohttp/f7eb77642fea2d18bc5b53d361802ca0fb698b3e
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} charset-normalizer
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-aiohttp

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-aiohttp/d4c7ca48f2d26cd60006bc2ace82041594ebfe63
/usr/share/package-licenses/pypi-aiohttp/f7eb77642fea2d18bc5b53d361802ca0fb698b3e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
