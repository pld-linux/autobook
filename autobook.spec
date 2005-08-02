Summary:	GNU Autoconf, Automake and Libtool
Summary(pl):	Podrêcznik Autoconf, Automake i Libtoola
Name:		autobook
Version:	1.4
Release:	1
License:	Open Publication License
Group:		Documentation
Source0:	http://sources.redhat.com/autobook/%{name}-%{version}.tar.gz
# Source0-md5:	623957f2ebe498457f4527c1477690f2
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *
