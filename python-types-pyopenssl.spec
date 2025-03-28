%define module types-pyOpenSSL
%define typename types_pyOpenSSL

Name:		python-types-pyopenssl
Version:	24.1.0.20240722
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/t/%{module}/%{module}-%{version}.tar.gz
Summary:	Typing stubs for pyOpenSSL
URL:		https://pypi.org/project/types-pyopenssl/
License:	Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
Requires:	python%{pyver}dist(types_cffi)
Requires:	python%{pyver}dist(cryptography)
Provides:	python%{pyver}dist(%{module})

%description
Typing stubs for pyOpenSSL

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py3_install


%files
%{py_sitedir}/OpenSSL-stubs/*.pyi
%{py_sitedir}/OpenSSL-stubs/*.typed
%{py_sitedir}/OpenSSL-stubs/*.toml
%{py_sitedir}/%{typename}-%{version}-*.*-info/*
