Summary:	GtkGLArea OpenGL widget for GTK+
Summary(pl):	GtkGLArea - kontrolka Gtk+ do prezentacji obiektСw OpenGL
Summary(pt_BR):	Um widget OpenGL para a biblioteca GUI GTK+
Summary(ru):	GtkGLArea - это OpenGL виджет для GTK+
Summary(uk):	GtkGLArea - це OpenGL в╕джет для GTK+
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
Requires:	gtk+2-devel => 2.1.2
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
