Summary:	Python client for DICT protocol
Name:		python-dictclient
Version:	1.0.1
Release:	3
License:	GPL v2+
Group:		Development/Languages
URL:		http://gopher.quux.org:70/devel/dictclient
Source0:	http://gopher.quux.org:70/devel/dictclient/dictclient_%{version}.tar.gz
# Source0-md5:	0a677022c2ae311d8cbff8f67ce1ba21
BuildRequires:	python-distribute
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A client library for the DICT protocol.

%prep
%setup -q -n dictclient

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog dictclient.html dictclient.txt README
%{py_sitescriptdir}/dictclient.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/dictclient-*.egg-info
%endif
