Summary: A free library for decoding ATSC A/52 (aka AC-3) streams.
Name: a52dec
Version: 0.7.4
Release: 7.0.2%{?dist}
License: GPL
Group: Applications/Multimedia
Source0: http://liba52.sourceforge.net/files/%{name}-%{version}.tar.gz
Patch0: a52dec-0.7.4-fPIC.patch
URL: http://liba52.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: autoconf
Requires: a52dec-libs_%{version}

%description
liba52 is a free library for decoding ATSC A/52 streams. It is released
under the terms of the GPL license. The A/52 standard is used in a
variety of applications, including digital television and DVD. It is
also known as AC-3.

%package libs_%{version}
Summary: A free library for decoding ATSC A/52 (aka AC-3) streams.
Group: Applications/Multimedia
Obsoletes: liba52dec*

%description libs_%{version}
liba52 is a free library for decoding ATSC A/52 streams. It is released
under the terms of the GPL license. The A/52 standard is used in a
variety of applications, including digital television and DVD. It is
also known as AC-3.

%package devel
Summary: Header files and static libraries for liba52.
Group: Development/Libraries
Requires: a52dec-libs_%{version}

%description devel
liba52 is a free library for decoding ATSC A/52 streams. It is released
under the terms of the GPL license. The A/52 standard is used in a
variety of applications, including digital television and DVD. It is
also known as AC-3.

These are the header files and static libraries from liba52 that are needed
to build programs that use it.


%prep
%setup -q
%patch0 -p1 -b .fPIC

%build
autoconf
%configure --enable-shared
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%post libs_%{version} -p /sbin/ldconfig

%postun libs_%{version} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO doc/liba52.txt
%{_bindir}/*
%{_mandir}/man1/*

%files libs_%{version}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la

%changelog
* Sat Jun 13 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> 0.7.4-7.0.2
- Changed lib naming convention to comply with ClearOS policy

* Sat Jun 14 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.7.4-7.0.1
- Fix not utf-8	specfile entries.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Thu Sep 26 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 8.0.
- Added SMP build macro.

* Mon Jul 29 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.7.4.

* Sun Mar 24 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Fixed the devel file ownership error.

* Tue Mar 19 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.7.3.

* Mon Dec 17 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.7.2.

* Mon Oct 29 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Spec file cleanup and fixes.

* Thu Sep 20 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Added missing .la files
- Building statically

* Thu Sep 20 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Initial version

