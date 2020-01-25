#
# Conditional build:
%bcond_with	tests	# perform "make test" (needs DISPLAY)
#
%define		pdir	Gtk2
%define		pnam	Ex-Carp
Summary:	GTK+ friendly die() and warn() functions
Summary(pl.UTF-8):	Funkcje die() i warn() przyjazne dla GTK+
Name:		perl-%{pdir}-%{pnam}
Version:	0.01
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9e6de1c2e54c504d19b6b0f5faa3f5b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Gtk2 >= 1.101-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ friendly die() and warn() functions.

%description -l pl.UTF-8
Funkcje die() i warn() przyjazne dla GTK+.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Gtk2/Ex/Carp.pm
%{_mandir}/man3/*
