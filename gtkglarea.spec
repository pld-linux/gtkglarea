Summary:	GtkGLArea OpenGL widget for GTK+
Summary(pl):	GtkGLArea - kontrolka Gtk+ do prezentacji obiekt�w OpenGL
Summary(pt_BR):	Um widget OpenGL para a biblioteca GUI GTK+
Summary(ru):	GtkGLArea - ��� OpenGL ������ ��� GTK+
Summary(uk):	GtkGLArea - �� OpenGL צ���� ��� GTK+
Summary(wa):	GtkGLArea est on ahesse pol toolkit grafike GTK+
Name:		gtkglarea
Version:	1.99.0
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gtkglarea/1.99/%{name}-%{version}.tar.bz2
# Source0-md5: cd69f77240ae8038f95a2e5e0b7e5f25
Requires:	OpenGL
BuildRequires:	automake
BuildRequires:	OpenGL-devel
BuildRequires:	gtk+2-devel => 2.1.3-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgtkglarea5

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of
gdkgl which is basically wrapper around GLX functions. The widget
itself is derived from GtkDrawinigArea widget and adds only few extra
functions.

%description -l pl
Podobnie jak GTK+ jest zbudowane na GDK, tak i GtkGLArea powsta�o na
bazie gdkgl, kt�ry jest wrapperem funkcji GLX. Sam widget pochodzi od
GtkDrawingArea i posiada jedynie kilka dodatkowych funkcji.

%description -l pt_BR
GtkGLArea � um OpenGL widget para GTK+ (the Gimp ToolKit), uma
biblioteca GUI. GtkGLArea � constru�da em cima do gdkgl. Gdkgl �
basicamente um wrapper de fun��es GLX. GtkGLArea widget � derivado do
widget GtkDrawingArea e adiciona somente algumas fun��es.

%description -l ru
��� �� ��� GTK+ �������� ������ GDK, GtkGLArea ��������� ������ gdkgl,
������� �� ���� ���� �������� ������ ������� GLX. ��� ������ �����
����� �� ������ GtkDrawinigArea � ��������� ������ ��� ����� �������.

%description -l uk
��� ����, �� GTK+ ���դ���� ������ GDK, GtkGLArea ���������� ������
gdkgl, ��� �� ��Ԧ � ��������� ������� ����æ� GLX. ��� צ���� ����
������ �� צ���� GtkDrawinigArea �� ����� ���� ��� ��צ ����æ�.

%package devel
Summary:	GtkGLArea OpenGL widget for GTK+ - development libs and headers
Summary(pl):	Pliki nag��wkowe GtkGLArea
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para desenvolvimento de aplica��es que usem a biblioteca GtkGLArea
Summary(ru):	GtkGLArea - ����� ��� ���������� ��������
Summary(uk):	GtkGLArea - ����� ��� �������� �������
Summary(wa):	GtkGLArea est on ahesse po GTK+ - fitch�s *.h �t statik�s l�vreyes
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL-devel
Requires:	gtk+2-devel => 2.1.2
Obsoletes:	libgtkglarea5-devel

%description devel
Header files for development using the GtkGLArea widget.

%description devel -l pl
Pliki nag��wkowe do budowania program�w u�ywaj�cych widgetu GtkGLArea.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o para desenvolvimento de aplica��es
que usem a biblioteca GtkGLArea.

%description devel -l ru
����� ��� ���������� �������� � �������������� GtkGLArea.

%description devel -l uk
����� ��� �������� ������� � ������������� GtkGLArea.

%description devel -l wa
Ci paket chal a dvins les fitch�s *.h ey�t les statik�s l�vreyes k' i
gn a mez�jhe po f� des porogrames avou les foncsions di GtkGLArea.

%package static
Summary:	GtkGLArea static libraries
Summary(pl):	Statyczne biblioteki GtkGLArea
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento de aplica��es que usem a biblioteca GtkGLArea
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}

%description static
GtkGLArea (OpenGL for GTK+) static libraries.

%description static -l pl
Statyczne biblioteki GtkGLArea (OpenGL dla GTK+).

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento de aplica��es que usem a
biblioteca GtkGLArea.

%prep
%setup -q

%build
cp /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README docs/*.txt
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
