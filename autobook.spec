Summary:	GNU Autoconf, Automake and Libtool
Summary(pl.UTF-8):	Podręcznik Autoconf, Automake i Libtoola
Name:		autobook
Version:	1.5
Release:	1
License:	Open Publication License
Group:		Documentation
Source0:	http://sources.redhat.com/autobook/%{name}-%{version}.tar.gz
# Source0-md5:	ce2be49c716a917e7c9342e7dedfeaf0
URL:		http://sources.redhat.com/autobook/
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This document is a tutorial on GNU autoconf, automake and libtool.

%description -l pl.UTF-8
Ten dokument jest podręcznikiem narzędzi GNU autoconfa, automake
i libtoola.

%prep
%setup -q
%{__sed} -i 's/bgcolor=#6688aa/bgcolor=#f2f7e8/gi' *.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *
