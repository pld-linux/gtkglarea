Summary:	GtkGLArea OpenGL widget for GTK+
Summary(pl):	GtkGLArea - kontrolka Gtk+ do prezentacji obiektСw OpenGL
Summary(pt_BR):	Um widget OpenGL para a biblioteca GUI GTK+
Summary(ru):	GtkGLArea - это OpenGL виджет для GTK+
Summary(uk):	GtkGLArea - це OpenGL в╕джет для GTK+
Summary(wa):	GtkGLArea est on ahesse pol toolkit grafike GTK+
Name:		gtkglarea
Version:	1.2.3
Release:	7
License:	LGPL
Group:		X11/Libraries
Source0:	http://www.student.oulu.fi/~jlof/gtkglarea/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-m4_fix.patch
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
Podobnie jak GTK+ jest zbudowane na GDK, tak i GtkGLArea powstaЁo na
bazie gdkgl, ktСry jest wrapperem funkcji GLX. Sam widget pochodzi od
GtkDrawingArea i posiada jedynie kilka dodatkowych funkcji.

%description -l pt_BR
GtkGLArea И um OpenGL widget para GTK+ (the Gimp ToolKit), uma
biblioteca GUI. GtkGLArea И construМda em cima do gdkgl. Gdkgl И
basicamente um wrapper de funГУes GLX. GtkGLArea widget И derivado do
widget GtkDrawingArea e adiciona somente algumas funГУes.

%description -l ru
Так же как GTK+ строится поверх GDK, GtkGLArea построена поверх gdkgl,
которая по сути есть оберткой вокруг функций GLX. Сам виджет очень
похож на виджет GtkDrawinigArea и добавляет только три новые функции.

%description -l uk
Так само, як GTK+ буду╓ться поверх GDK, GtkGLArea побудована поверх
gdkgl, яка по сут╕ ╓ обгорткою навкруг функц╕й GLX. Сам в╕джет дуже
схожий на в╕джет GtkDrawinigArea та дода╓ лише три нов╕ функц╕╖.

%package devel
Summary:	GtkGLArea OpenGL widget for GTK+ - development libs and headers
Summary(pl):	Pliki nagЁСwkowe GtkGLArea
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo para desenvolvimento de aplicaГУes que usem a biblioteca GtkGLArea
Summary(ru):	GtkGLArea - файлы для разработки программ
Summary(uk):	GtkGLArea - файли для розробки програм
Summary(wa):	GtkGLArea est on ahesse po GTK+ - fitchНs *.h Хt statikХs lНvreyes
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL-devel
Requires:	gtk+-devel => 1.2.0
Obsoletes:	libgtkglarea5-devel

%description devel
Header files for development using the GtkGLArea widget.

%description devel -l pl
Pliki nagЁСwkowe do budowania programСw u©ywaj╠cych widgetu GtkGLArea.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusЦo para desenvolvimento de aplicaГУes
que usem a biblioteca GtkGLArea.

%description devel -l ru
Файлы для разработки программ с использованием GtkGLArea.

%description devel -l uk
Файли для розробки програм з використанням GtkGLArea.

%description devel -l wa
Ci paket chal a dvins les fitchНs *.h eyХt les statikХs lНvreyes k' i
gn a mezЕjhe po fИ des porogrames avou les foncsions di GtkGLArea.

%package static
Summary:	GtkGLArea static libraries
Summary(pl):	Statyczne biblioteki GtkGLArea
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento de aplicaГУes que usem a biblioteca GtkGLArea
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}

%description static
GtkGLArea (OpenGL for GTK+) static libraries.

%description static -l pl
Statyczne biblioteki GtkGLArea (OpenGL dla GTK+).

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento de aplicaГУes que usem a
biblioteca GtkGLArea.

%prep
%setup -q
%patch0

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
%{_libdir}/lib*.a
