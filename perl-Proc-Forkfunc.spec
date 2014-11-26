#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Proc
%define		pnam	Forkfunc
%include	/usr/lib/rpm/macros.perl
Summary:	Proc::Forkfunk Perl module - fork off a function
Summary(pl.UTF-8):	Moduł Perla Proc::Forkfunk - uruchamianie funkcji w procesie potomnym
Name:		perl-Proc-Forkfunc
Version:	96.042201
Release:	13
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0b34666fa7fd32602f75d22a4da9adf6
URL:		http://search.cpan.org/dist/Proc-Forkfunc/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fork off a process. Call a function on the child process the function
should be passed in as a reference. The child function should not
return.

%description -l pl.UTF-8
Ten moduł tworzy proces potomny i wywołuje w tym procesie funkcję
przekazaną przez referencję. Funkcja potomna nie powinna wracać.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Proc/Forkfunc.pm
%{_mandir}/man3/*
