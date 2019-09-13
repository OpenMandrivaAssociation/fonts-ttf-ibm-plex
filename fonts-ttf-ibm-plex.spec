%define fontname 	ibm-plex
%define fontdir		%{_datadir}/fonts/TTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	The package of IBM’s typeface, IBM Plex.
Name:		fonts-ttf-ibm-plex
Version:	2.0.0
Release:	1
License:	OFL
Group:		System/Fonts/True type
URL:		https://github.com/IBM/plex
Source0:	https://github.com/IBM/plex/releases/download/%{version}/TrueType.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	mkfontscale
BuildRequires:	mkfontdir

%description
The package of IBM’s typeface, IBM Plex.

%prep
%setup -qn TrueType

%build

%install
install -dm 0755 %{buildroot}/%{fontdir}/
install -m 644 */*.ttf %{buildroot}%{_xfontdir}/TTF/ibm-plex
mkfontscale %{buildroot}%{fontdir}/
mkfontdir %{buildroot}%{fontdir}/
mkdir -p %{buildroot}%{fontconfdir}/
ln -s ../../..%{buildroot}%{fontdir} %{buildroot}%{fontconfdir}/ttf-%{fontname}:pri=50

%files
%dir %{fontdir}
%{fontconfdir}/ttf-%{fontname}:pri=50
%{fontdir}/*.ttf
%verify(not mtime)%{fontdir}/fonts.dir
%{fontdir}/fonts.scale
# All other licenses are the same
%license IBM-Plex-Mono/license.txt
