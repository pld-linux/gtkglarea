# Note that this is NOT a relocatable package
%define ver      1.2.1
%define rel      SNAP
%define prefix   /usr

Summary: GtkGLArea OpenGL widget for GTK+
Name: gtkglarea
Version: %ver
Release: %rel
Copyright: LGPL
Packager: Ray Glendenning <ray.glendenning@hackery.demon.co.uk>
Group: X11/Libraries
Source:  http://www.student.oulu.fi/~jlof/gtkglarea/download/gtkglarea-%{version}.tar.gz
BuildRoot: /var/tmp/gtkglarea-%{version}-root
Docdir: %{prefix}/doc
Requires: Mesa => 3.0, gtk+ => 1.1.5

%description
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl which
is basically wrapper around GLX functions. The widget itself is derived from
GtkDrawinigArea widget and adds only few extra functions.

%package devel
Summary: GtkGLArea OpenGL widget for GTK+.  Development libs and headers.
Group: X11/Libraries
Requires: %{name} = %{version} , Mesa-devel => 3.0 , gtk+-devel => 1.1.5

%description devel
Static libraries and header files for development using the GtkGLArea widget.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog INSTALL NEWS README docs/HOWTO.txt docs/gdkgl.txt docs/gtkglarea.txt
%{prefix}/lib/lib*.so.*

%files devel
%defattr(-, root, root)

%{prefix}/include/gtkgl/*
%{prefix}/lib/lib*.*a
%{prefix}/lib/lib*.so
%{prefix}/share/aclocal/*
