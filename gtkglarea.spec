Summary:	GtkGLArea OpenGL widget for GTK+
Summary(wa):	GtkGLArea est on ahesse pol toolkit grafike GTK+
Name:		gtkglarea
Version:	1.2.3
Release:	3
License:	LGPL
Group:		X11/Libraries
Source0:	http://www.student.oulu.fi/~jlof/gtkglarea/download/%{name}-%{version}.tar.gz
Requires:	OpenGL
BuildRequires:	OpenGL-devel
BuildRequires:	gtk+-devel => 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgtkglarea5

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_datadir	/usr/share

%description
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of
gdkgl which is basically wrapper around GLX functions. The widget
itself is derived from GtkDrawinigArea widget and adds only few extra
functions.

%description -l pl
Podobnie jak GTK+ jest zbudowane na GDK, tak i GtkGLArea powsta³o na
bazie gdkgl, który jest wrapperem funkcji GLX. Sam widget pochodzi od
GtkDrawingArea i posiada jedynie kilka dodatkowych funkcji.

%package devel
Summary:	GtkGLArea OpenGL widget for GTK+.  Development libs and headers
Summary(wa):	GtkGLArea est on ahesse po GTK+ - fitchîs *.h èt statikès lîvreyes
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL-devel
Requires:	gtk+-devel => 1.2.0
Obsoletes:	libgtkglarea5-devel

%description devel
Header files for development using the GtkGLArea widget.

%description devel -l pl
Pliki nag³ówkowe do budowania programów u¿ywaj±cych widgetu GtkGLArea.

%description devel -l wa
Ci paket chal a dvins les fitchîs *.h eyèt les statikès lîvreyes k' i
gn a mezåjhe po fé des porogrames avou les foncsions di GtkGLArea.

%package static
Summary:	GtkGLArea static libraries
Summary(pl):	Statyczne biblioteki GtkGLArea
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}

%description static
GtkGLArea (OpenGL for GTK+) static libraries.

%description static -l pl
Statyczne biblioteki GtkGLArea (OpenGL dla GTK+).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf AUTHORS ChangeLog NEWS README docs/HOWTO.txt docs/gdkgl.txt \
	docs/gtkglarea.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *gz docs/*.gz
%{_includedir}/gtkgl
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.*a
