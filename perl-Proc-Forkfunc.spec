%define	pdir	Proc
%define	pnam	Forkfunc
%include	/usr/lib/rpm/macros.perl
Summary:	Proc-Forkfunc perl module
Summary(pl):	Modu³ perla Proc-Forkfunc
Name:		perl-Proc-Forkfunc
Version:	96.042201
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc-Forkfunc perl module.

%description -l pl
Modu³ perla Proc-Forkfunc.

%prep
%setup -q -n Proc-Forkfunc-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Proc/Forkfunc.pm
%{_mandir}/man3/*
