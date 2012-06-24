Summary:	GtkGLArea OpenGL widget for GTK+
Summary(wa):	GtkGLArea est on ahesse pol toolkit grafike GTK+
Name:		gtkglarea
Version:	1.2.2
Release:	1
License:	LGPL
Group:		X11/Libraries
Source:		http://www.student.oulu.fi/~jlof/gtkglarea/download/%{name}-%{version}.tar.gz
BuildRequires:	gtk+-devel => 1.2.0
BuildRequires:	Mesa-devel => 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_datadir	/usr/share

%description
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl
which is basically wrapper around GLX functions. The widget itself is
derived from GtkDrawinigArea widget and adds only few extra functions.

%package devel
Summary:	GtkGLArea OpenGL widget for GTK+.  Development libs and headers.
Summary(wa):	GtkGLArea est on ahesse po GTK+ - fitch�s *.h �t statik�s l�vreyes
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	Mesa-devel => 3.0
Requires:	gtk+-devel => 1.2.0

%description devel
Static libraries and header files for development using the GtkGLArea
widget.

%description -l wa devel
Ci paket chal a dvins les fitch�s *.h ey�t les statik�s l�vreyes k' i gn a
mez�jhe po f� des porogrames avou les foncsions di GtkGLArea.

%package static
Summary:	GtkGLArea OpenGL OpenGL for GTK+ static libraries
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}

%description static
GtkGLArea OpenGL OpenGL for GTK+ static libraries.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README docs/HOWTO.txt docs/gdkgl.txt \
	docs/gtkglarea.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *gz docs/*.gz

%{_includedir}/gtkgl
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_datadir}/aclocal/*

%files static
%attr(644,root,root) %{_libdir}/lib*.*a
