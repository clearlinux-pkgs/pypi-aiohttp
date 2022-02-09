#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-aiohttp
Version  : 3.8.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/5a/86/5f63de7a202550269a617a5d57859a2961f3396ecd1739a70b92224766bc/aiohttp-3.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/5a/86/5f63de7a202550269a617a5d57859a2961f3396ecd1739a70b92224766bc/aiohttp-3.8.1.tar.gz
Summary  : Async http client/server framework (asyncio)
Group    : Development/Tools
License  : Apache-2.0 MIT
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

%description
==================================
Async http client/server framework
==================================

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
Requires: python3-core
Provides: pypi(aiohttp)
Requires: pypi(aiosignal)
Requires: pypi(async_timeout)
Requires: pypi(attrs)
Requires: pypi(charset_normalizer)
Requires: pypi(frozenlist)
Requires: pypi(multidict)
Requires: pypi(yarl)

%description python3
python3 components for the pypi-aiohttp package.


%prep
%setup -q -n aiohttp-3.8.1
cd %{_builddir}/aiohttp-3.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644431902
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-aiohttp
cp %{_builddir}/aiohttp-3.8.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-aiohttp/feafff86ed3f0b6b54d85426a1c8e33caa365e8a
cp %{_builddir}/aiohttp-3.8.1/vendor/llhttp/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-aiohttp/f7eb77642fea2d18bc5b53d361802ca0fb698b3e
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-aiohttp/f7eb77642fea2d18bc5b53d361802ca0fb698b3e
/usr/share/package-licenses/pypi-aiohttp/feafff86ed3f0b6b54d85426a1c8e33caa365e8a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
