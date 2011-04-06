Summary:	GtkGLArea OpenGL widget for GTK+
Summary(pl.UTF-8):	GtkGLArea - kontrolka GTK+ do prezentacji obiektów OpenGL
Summary(pt_BR.UTF-8):	Um widget OpenGL para a biblioteca GUI GTK+
Summary(ru.UTF-8):	GtkGLArea - это OpenGL виджет для GTK+
Summary(uk.UTF-8):	GtkGLArea - це OpenGL віджет для GTK+
Summary(wa.UTF-8):	GtkGLArea est on ahesse pol toolkit grafike GTK+
Name:		gtkglarea
Version:	2.0.1
Release:	3
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkglarea/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	19af1b2185555b3bb28eef8bbaa36067
# libGLU for examples only
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.1.3-3
BuildRequires:	libtool
BuildRequires:	pkgconfig
Obsoletes:	libgtkglarea5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of
gdkgl which is basically wrapper around GLX functions. The widget
itself is derived from GtkDrawinigArea widget and adds only few extra
functions.

%description -l pl.UTF-8
Podobnie jak GTK+ jest zbudowane na GDK, tak i GtkGLArea powstało na
bazie gdkgl, który jest wrapperem funkcji GLX. Sam widget pochodzi od
GtkDrawingArea i posiada jedynie kilka dodatkowych funkcji.

%description -l pt_BR.UTF-8
GtkGLArea é um OpenGL widget para GTK+ (the Gimp ToolKit), uma
biblioteca GUI. GtkGLArea é construída em cima do gdkgl. Gdkgl é
basicamente um wrapper de funções GLX. GtkGLArea widget é derivado do
widget GtkDrawingArea e adiciona somente algumas funções.

%description -l ru.UTF-8
Так же как GTK+ строится поверх GDK, GtkGLArea построена поверх gdkgl,
которая по сути есть оберткой вокруг функций GLX. Сам виджет очень
похож на виджет GtkDrawinigArea и добавляет только три новые функции.

%description -l uk.UTF-8
Так само, як GTK+ будується поверх GDK, GtkGLArea побудована поверх
gdkgl, яка по суті є обгорткою навкруг функцій GLX. Сам віджет дуже
схожий на віджет GtkDrawinigArea та додає лише три нові функції.

%package devel
Summary:	GtkGLArea OpenGL widget for GTK+ - development libs and headers
Summary(pl.UTF-8):	Pliki nagłówkowe GtkGLArea
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações que usem a biblioteca GtkGLArea
Summary(ru.UTF-8):	GtkGLArea - файлы для разработки программ
Summary(uk.UTF-8):	GtkGLArea - файли для розробки програм
Summary(wa.UTF-8):	GtkGLArea est on ahesse po GTK+ - fitchîs *.h èt statikès lîvreyes
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-devel
Requires:	gtk+2-devel >= 1:2.1.2
Obsoletes:	libgtkglarea5-devel

%description devel
Header files for development using the GtkGLArea widget.

%description devel -l pl.UTF-8
Pliki nagłówkowe do budowania programów używających widgetu GtkGLArea.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações
que usem a biblioteca GtkGLArea.

%description devel -l ru.UTF-8
Файлы для разработки программ с использованием GtkGLArea.

%description devel -l uk.UTF-8
Файли для розробки програм з використанням GtkGLArea.

%description devel -l wa.UTF-8
Ci paket chal a dvins les fitchîs *.h eyèt les statikès lîvreyes k' i
gn a mezåjhe po fé des porogrames avou les foncsions di GtkGLArea.

%package static
Summary:	GtkGLArea static libraries
Summary(pl.UTF-8):	Statyczne biblioteki GtkGLArea
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento de aplicações que usem a biblioteca GtkGLArea
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GtkGLArea (OpenGL for GTK+) static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki GtkGLArea (OpenGL dla GTK+).

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento de aplicações que usem a
biblioteca GtkGLArea.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

# lib doesn't use libGLU
%{__make} -C gtkgl \
	GL_LIBS="-lGL"

# but examples do
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgtkgl-2.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkgl-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkgl-2.0.so.1

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README docs/*.txt
%attr(755,root,root) %{_libdir}/libgtkgl-2.0.so
%{_includedir}/gtkgl-2.0
%{_pkgconfigdir}/gtkgl-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkgl-2.0.a
