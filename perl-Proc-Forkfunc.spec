%include	/usr/lib/rpm/macros.perl
%define	pdir	Proc
%define	pnam	Forkfunc
Summary:	Proc::Forkfunk -- fork off a function
Summary(pl):	Modu³ Proc::Forkfunk - uruchamiaj±cy funkcjê w procesie potomnym
Name:		perl-Proc-Forkfunc
Version:	96.042201
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0b34666fa7fd32602f75d22a4da9adf6
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fork off a process.  Call a function on the child process the function
should be passed in as a reference.  The child function should not
return.

%description -l pl
Ten modu³ tworzy proces potomny i wywo³uje w tym procesie funkcjê
przekazan± przez referencjê. Funkcja potomna nie powinna wracaæ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Proc/Forkfunc.pm
%{_mandir}/man3/*
