%define major 0
%define libname %mklibname squish %{major}
%define develname %mklibname squish -d

Summary:	Open source DXT compression library
Name:		libsquish
Version:	1.15
Release:	1
License:	MIT
Group:		System/Libraries
URL:		https://sourceforge.net/projects/libsquish/
Source0:	https://download.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tgz
Patch0:		https://src.fedoraproject.org/rpms/libsquish/raw/rawhide/f/libsquish-cmake_install.patch
BuildRequires:	cmake

%description
The libSquish library compresses images with the DXT standard
(also known as S3TC). This standard is mainly used by OpenGL and
DirectX for the lossy compression of RGBA textures.

#------------------------------------------------

%package -n %{libname}
Summary:	Open source DXT compression library
Group:		System/Libraries

%description -n %{libname}
The libSquish library compresses images with the DXT standard
(also known as S3TC). This standard is mainly used by OpenGL and
DirectX for the lossy compression of RGBA textures.

#------------------------------------------------

%package -n %{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	squish-devel = %{version}-%{release}

%description -n %{develname}
Header files for development with %{name}.

#------------------------------------------------

%prep
%autosetup -c libsquish-%{version}

%build
%cmake \
%ifnarch %{x86_64}
	-DBUILD_SQUISH_WITH_SSE2=OFF \
%endif
	-DBUILD_SHARED_LIBS=ON

%make_build

%install
%make_install -C build

%files -n %{libname}
%license LICENSE.txt
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc README.txt
%{_libdir}/*.so
%{_includedir}/*
