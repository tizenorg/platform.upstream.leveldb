Name:   	leveldb
Summary:    A fast key-value storage library
Version: 	1.1
Release:    1
Group:      System/Libraries
License:    BSD-2.0
Source0:    %{name}-%{version}.tar.gz
Source1001: 	leveldb.manifest

%description
LevelDB is a fast key-value storage library written at Google
that provides an ordered mapping from string keys to string values.


%package -n libleveldb
Summary:   A fast key-value storage library
Group:     System/Libraries
	
%description -n libleveldb
LevelDB is a fast key-value storage library written at Google
that provides an ordered mapping from string keys to string values.


%package devel
Summary:   A fast key-value storage library - Development
Group:     Development/Libraries
Requires:   libleveldb
	
%description devel
LevelDB is a fast key-value storage library written at Google
that provides an ordered mapping from string keys to string values.

Development Files.


%prep
%setup -q
cp %{SOURCE1001} .

%build
make libdir=%{_libdir} %{?jobs:-j%jobs}

%install
make install DESTDIR=%{buildroot} libdir=%{_libdir}


%post -p /sbin/ldconfig -n libleveldb

%postun -p /sbin/ldconfig -n libleveldb


%files -n libleveldb
%manifest %{name}.manifest
%license LICENSE
%defattr(-,root,root,-)
%{_libdir}/libleveldb.so.0
%{_libdir}/libleveldb.so.1.1.0
%{_libdir}/libmemenv.so.0
%{_libdir}/libmemenv.so.1.1.0


%files devel
%manifest %{name}.manifest

%{_libdir}/libmemenv.so
%{_libdir}/pkgconfig/leveldb.pc
%{_libdir}/pkgconfig/memenv.pc
%{_includedir}/leveldb/*.h
%{_includedir}/helpers/memenv/*.h
%{_libdir}/libleveldb.so
