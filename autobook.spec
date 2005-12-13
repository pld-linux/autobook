Summary:	GNU Autoconf, Automake and Libtool
Summary(pl):	Podrêcznik Autoconf, Automake i Libtoola
Name:		autobook
Version:	1.3
Release:	2
License:	Open Publication License
Group:		Documentation
Source0:	http://sources.redhat.com/autobook/%{name}-%{version}.tar.gz
# Source0-md5:	3e7c4928ca30747a1589f61e6acf934d
URL:		http://sources.redhat.com/autobook/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This document is a tutorial on GNU autoconf, automake and libtool.

%description -l pl
Ten dokument jest podrêcznikiem narzêdzi GNU autoconfa, automake
i libtoola.

%prep
%setup -q
%{__sed} -i 's/bgcolor=#6688aa/bgcolor=#f2f7e8/gi' *.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *
