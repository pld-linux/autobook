Summary:	GNU Autoconf, Automake and Libtool
Summary(pl):	Podrêcznik Autoconf, Automake i Libtoola
Name:		autobook
Version:	1.3
Release:	1
License:	Open Publication License
Group:		Documentation
Source0:	http://sources.redhat.com/autobook/%{name}-%{version}.tar.gz
URL:		http://sources.redhat.com/autobook/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This document is a tutorial on GNU autoconf, automake and libtool.

%description -l pl
Ten dokument jest podrêcznikiem narzêdzi GNU autoconfa, automake
i libtoola.

%prep
%setup -q -n %{name}

%files
%defattr(644,root,root,755)
%doc *
