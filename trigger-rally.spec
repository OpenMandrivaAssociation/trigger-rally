%define oname trigger
%define Summary Rally racing game
%define name %{oname}-rally
%define version 0.5.2.1
%define release %mkrel 1

%define distname %{oname}-%{version}-src

Summary: %{Summary}
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/trigger-rally/%{distname}.tar.bz2
Source1: %{name}.png
Patch0: trigger-0.5.2.1-nodoc.patch
License: GPL
Group: Games/Arcade
Url: http://sourceforge.net/projects/trigger-rally/
BuildRequires: automake1.8
BuildRequires: jam
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel
BuildRequires: freealut-devel
BuildRequires: glew-devel
BuildRequires: openal-devel
BuildRequires: physfs-devel
Requires: %{name}-data

%description
Trigger is a fast-paced open source rally racing game.

%prep
%setup -q -n %{distname}
%patch0 -p1 -b .nodoc

%build
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}/%{oname}
jam

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} jam install
# only contains .a files
rm -rf %{buildroot}%{_libdir}

install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/%{name}.png

install -d %{buildroot}%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Trigger Rally
Comment=%{Summary}
Exec=soundwrapper %{_gamesbindir}/%{oname}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesbindir}/%{oname}
%{_datadir}/icons/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop


