Name:           libuninameslist
Version:        20080409
Release:        3.1%{?dist}

Summary:        A library providing Unicode character names and annotations

Group:          System Environment/Libraries
License:        BSD
URL:            http://libuninameslist.sourceforge.net
Source0:        http://dl.sf.net/libuninameslist/libuninameslist-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
libuninameslist provides applications with access to Unicode name and
annotation data from the official Unicode Character Database.

%package        devel
Summary:        Header files and static libraries for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains header files and static libraries for %{name}.


%prep
%setup -q -n libuninameslist


%build
%configure --enable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall incdir=$RPM_BUILD_ROOT%{_includedir}
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc LICENSE
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 20080409-3.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080409-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080409-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Roozbeh Pournader <roozbeh@gmail.com> - 20080409-1
- Update to upstream 20080409: Unicode 5.1 support
- Change package versioning scheme
- Update summary and description
- Add DistTag
- Remove copy of GPL from RPM: the only file it applies to is not shipped

* Sun Feb 10 2008 Kevin Fenzi <kevin@tummy.com> - 0.0-8.20060907
- Rebuild for gcc43

* Sun Aug 26 2007 Kevin Fenzi <kevin@tummy.com> - 0.0-7.20060907
- Rebuild for BuildID

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.0-6.20060907
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 Kevin Fenzi <kevin@tummy.com> - 0.0-5.20060907
- Take over maintainership. 
- Update to 20060907

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.0-4.040707
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Jul 17 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.0-0.fdr.2.040707
- Updated to 040707.

* Fri Jul  2 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.0-0.fdr.2.040701
- Updated to 040701.

* Mon Oct 13 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0-0.fdr.2.030713
- Enable static libs, add -devel subpackage.

* Mon Oct 13 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.0-0.fdr.1.030713
- Initial RPM release.
