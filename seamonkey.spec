%define major_nspr 4
%define epoch_nspr 1
%define lib_nspr_name %mklibname nspr %{major_nspr}
%define devel_nspr_name %mklibname -d nspr %{major_nspr}
%define major_nss 3
%define epoch_nss 1
%define epoch_mozilla 0
%define lib_nss_name %mklibname nss %{major_nss}
%define devel_nss_name %mklibname nss
#warning : always end release date with 00 
# (it should be the hour of build but it is not significant for rpm)
%define releasedate 2009040800
%define french_policy 0
%define dirversion  %{version}
%define mozillalibdir %{_libdir}/seamonkey-%{dirversion}
%define mozillaplugindir %{_libdir}/mozilla/plugins
%define mozillaincludedir %{_includedir}/seamonkey-%{dirversion}
%define mozillaidldir %{_datadir}/idl/seamonkey-%{dirversion}
%define build_enigmail   1
%define build_xmlterm	 0
%define enable_svg       1
%define build_is_final   1
%define enable_l10n      1
%define build_debug      0
%define build_corefonts	 0
%define build_ggdefaults 0
%define build_gtk	 0
%define build_pie	 0
%define build_pango	 1
%define build_nspr_nss   0
%define build_gre	 0

%define toolkit		 gtk2

# used for enigmail and protozilla sources:
%define enigmail_version 0.95.7

%{?_with_enigmail: %global build_enigmail 1}

# Build a mozilla with debug enabled
%{?_with_mydebug: %global build_debug 1}
%{?_without_mydebug: %global build_debug 0}

# Use corefonts as default (Patch105)
%{?_with_corefonts: %global build_corefonts 1}
%{?_without_corefonts: %global build_corefonts 0}

# Enable/Disable some annoying parameters as defaults, e.g.
# - disable remote images in mail/news to avoid self bannering
# - enable pipelining
# - enable a4 paper
%{?_with_ggdefaults: %global build_ggdefaults 1}
%{?_without_ggdefaults: %global build_ggdefaults 0}

# Build with gtk (gtk1) toolkit instead of gtk2
%{?_with_gtk: %global build_gtk 1}
%{?_without_gtk: %global build_gtk 0}

# Enable pie (Position Independent Executable)
%{?_with_pie: %global build_pie 1}
%{?_without_pie: %global build_pie 0}

# Enable Pango 
%{?_with_pango: %global build_pango 1}
%{?_without_pango: %global build_pango 0}

# Build nspr/nss packages
%{?_with_nspr: %global build_nspr_nss 1}
%{?_without_nspr: %global build_nspr_nss 0}

# Install gre.conf
%{?_with_gre: %global build_gre 1}
%{?_without_gre: %global build_gre 0}

%if %{build_gtk}
%define build_xmlterm	1
%define toolkit		gtk
%endif

# For distro < 10.2
%if %mdkversion < 1020
%define build_pango		0
%define build_nspr_nss		1
%define build_ggdefaults	1
%endif

%define _provides_exceptions libaccessibility.so\\|libappcomps.so\\|libauth.so\\|libautoconfig.so\\|libcaps.so\\|libchrome.so\\|libcomposer.so\\|libcookie.so\\|libdocshell.so\\|libeditor.so\\|libembedcomponents.so\\|libfileview.so\\|libgfx_gtk.so\\|libgfxps.so\\|libgfxpsshar.so\\|libgkgfx.so\\|libgklayout.so\\|libgkplugin.so\\|libgtkembedmoz.so\\|libgtkxtbin.so\\|libhtmlpars.so\\|libi18n.so\\|libimgicon.so\\|libimglib2.so\\|libjar50.so\\|libjsd.so\\|libjsj.so\\|libldap50.so\\|libmork.so\\|libmozfind.so\\|libmozjs.so\\|libmozldap.so\\|libmsgbaseutil.so\\|libnecko.so\\|libnecko2.so\\|libnkgnomevfs.so\\|libnsappshell.so\\|libnsprefm.so\\|libnullplugin.so\\|liboji.so\\|libp3p.so\\|libpermissions.so\\|libpipboot.so\\|libpipnss.so\\|libpippki.so\\|libpref.so\\|libprldap50.so\\|libprofile.so\\|librdf.so\\|libremoteservice.so\\|libschemavalidation.so\\|libsearchservice.so\\|libsql.so\\|libsroaming.so\\|libstoragecomps.so\\|libsystem-pref.so\\|libtransformiix.so\\|libtxmgr.so\\|libtypeaheadfind.so\\|libuconv.so\\|libucvmath.so\\|libuniversalchardet.so\\|libunixprintplugin.so\\|libwallet.so\\|libwalletviewers.so\\|libwebbrwsr.so\\|libwebsrvcs.so\\|libwidget_gtk2.so\\|libxforms.so\\|libxmlextras.so\\|libxpcom.so\\|libxpcom_compat.so\\|libxpcom_compat_c.so\\|libxpcom_core.so\\|libxpconnect.so\\|libxpinstall.so\\|libxpistub.so\\|libxremoteservice\\|libaddrbook.so\\|libbayesflt.so\\|libimpComm4xMail.so\\|libimport.so\\|libimpText.so\\|liblocalmail.so\\|libmailnews.so\\|libmailview.so\\|libmimeemitter.so\\|libmime.so\\|libmsgbaseutil.so\\|libmsgcompose.so\\|libmsgdb.so\\|libmsgimap.so\\|libmsgmdn.so\\|libmsgnews.so\\|libmsgsmime.so\\|libvcard.so\\|libmyspell.so\\|libspellchecker.so\\|libenigmime.so
%define _requires_exceptions libaccessibility.so\\|libappcomps.so\\|libauth.so\\|libautoconfig.so\\|libcaps.so\\|libchrome.so\\|libcomposer.so\\|libcookie.so\\|libdocshell.so\\|libeditor.so\\|libembedcomponents.so\\|libfileview.so\\|libgfx_gtk.so\\|libgfxps.so\\|libgfxpsshar.so\\|libgkgfx.so\\|libgklayout.so\\|libgkplugin.so\\|libgtkembedmoz.so\\|libgtkxtbin.so\\|libhtmlpars.so\\|libi18n.so\\|libimgicon.so\\|libimglib2.so\\|libjar50.so\\|libjsd.so\\|libjsj.so\\|libldap50.so\\|libmork.so\\|libmozfind.so\\|libmozjs.so\\|libmozldap.so\\|libmsgbaseutil.so\\|libnecko.so\\|libnecko2.so\\|libnkgnomevfs.so\\|libnsappshell.so\\|libnsprefm.so\\|libnullplugin.so\\|liboji.so\\|libp3p.so\\|libpermissions.so\\|libpipboot.so\\|libpipnss.so\\|libpippki.so\\|libpref.so\\|libprldap50.so\\|libprofile.so\\|librdf.so\\|libremoteservice.so\\|libschemavalidation.so\\|libsearchservice.so\\|libsql.so\\|libsroaming.so\\|libstoragecomps.so\\|libsystem-pref.so\\|libtransformiix.so\\|libtxmgr.so\\|libtypeaheadfind.so\\|libuconv.so\\|libucvmath.so\\|libuniversalchardet.so\\|libunixprintplugin.so\\|libwallet.so\\|libwalletviewers.so\\|libwebbrwsr.so\\|libwebsrvcs.so\\|libwidget_gtk2.so\\|libxforms.so\\|libxmlextras.so\\|libxpcom.so\\|libxpcom_compat.so\\|libxpcom_compat_c.so\\|libxpcom_core.so\\|libxpconnect.so\\|libxpinstall.so\\|libxpistub.so\\|libxremoteservice\\|libaddrbook.so\\|libbayesflt.so\\|libimpComm4xMail.so\\|libimport.so\\|libimpText.so\\|liblocalmail.so\\|libmailnews.so\\|libmailview.so\\|libmimeemitter.so\\|libmime.so\\|libmsgbaseutil.so\\|libmsgcompose.so\\|libmsgdb.so\\|libmsgimap.so\\|libmsgmdn.so\\|libmsgnews.so\\|libmsgsmime.so\\|libvcard.so\\|libmyspell.so\\|libspellchecker.so\\|libenigmime.so

Name:      seamonkey
Summary:   SeaMonkey, all-in-one internet application suite
Version:   1.1.16
Release:   %mkrel 1
License:   MPL
Source0:   ftp://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/seamonkey-%{version}.source.tar.bz2
Source2:   seamonkey16.png
Source3:   seamonkey32.png
Source4:   seamonkey64.png
Source5:   mozilla-firefox-bookmarks-mdk2006.tar.bz2
Source6:   mozilla-1.7-libart_lgpl.tar.bz2
%if %{enable_l10n}
Source99:  locale.alias
%define l10ns be-BY ca-AD cs-CZ de-AT el-GR en-GB es-ES fr-FR he-IL hi-IN hu-HU it-IT ja-JP lt-LT nl-NL pl-PL ru-RU sv-SE pt-BR ur-PK
# not up-to-date: eu-ES ka-GE nb-NO ne-NP tr-TR

Source100: %{name}-1.1.9.be-BY.langpack.xpi
Source101: %{name}-1.1.15.ca-AD.langpack.xpi
Source102: %{name}-1.1.16.cs-CZ.langpack.xpi
Source103: %{name}-1.1.16.de-AT.langpack.xpi
Source104: %{name}-1.1.2.el-GR.langpack.xpi
Source105: %{name}-1.1.en-GB.langpack.xpi
Source106: %{name}-1.1.14.es-ES.langpack.xpi
Source108: %{name}-1.1.15.fr-FR.langpack.xpi
Source109: %{name}-1.1.2.he-IL.langpack.xpi
Source110: %{name}-1.1.15.it-IT.langpack.xpi
Source114: %{name}-1.1.16.pl-PL.langpack.xpi
Source115: %{name}-1.1.16.ru-RU.langpack.xpi
Source116: %{name}-1.1.12.sv-SE.langpack.xpi
Source118: %{name}-1.1.16.pt-BR.langpack.xpi
Source119: %{name}-1.1.16.ja-JP.langpack.xpi
Source120: %{name}-1.1.15.nl-NL.langpack.xpi
Source121: %{name}-1.1.9.ur-PK.langpack.xpi
Source122: %{name}-1.1.7.hi-IN.langpack.xpi
Source123: %{name}-1.1.11.hu-HU.langpack.xpi
Source124: %{name}-1.1.12.lt-LT.langpack.xpi

#Source107: %{name}-1.0.eu-ES.langpack.xpi
#Source111: %{name}-1.0.ka-GE.langpack.xpi
#Source112: %{name}-1.0.nb-NO.langpack.xpi
#Source113: %{name}-1.0.2.ne-NP.langpack.xpi
#Source117: %{name}-1.0.tr-TR.langpack.xpi
%endif
# (fc) 0.9.8-1mdk fix loading of file through command line (contributed by Chmouel) ,
# set MOZ_PLUGIN_PATH to $HOME/.mozilla/plugins, autodetect locale, add -splash parameter
Source10:  seamonkey-1.0.0-sh.in.bz2
Source22:  http://www.mozilla-enigmail.org/downloads/src/enigmail-%{enigmail_version}.tar.bz2
Source23:  mdkbugzilla.gif
Source24:  mozilla-1.6-startmail.tar.bz2
Source25:  mozilla-make-package.pl
Source26:  seamonkey-rebuild-databases.pl.in
Source27:  mozilla-xpcom-exclude-list
Source28:  mozilla-psm-exclude-list
# Enigmail 0.95.7 is broken in x86_64 (#44426)
Source29:  http://www.mozilla-enigmail.org/download/source/enigmail-0.95.6.tar.gz
#Source31:  enigmail-%{enigmail_version}-l10n.tar.bz2

# (fc) 1.1-0.beta.1mdk remove Debug menu
Patch0:    mozilla-1.7-no-debug-overlay-menu.patch
Patch7:    mozilla-browser-home-page.patch
Patch12:   mozilla-1.7-psfonts.patch
Patch13:   mozilla-nspr-packages.patch
# (fc) 0.9.6-3mdk remove buildid from titlebar (Ximian)
Patch23:   mozilla-1.1-remove-buildid-from-title.patch
# (fc) 0.9.6-3mdk fix french policy
Patch24:   mozilla-0.9.6-frenchpolicy.patch
# (fc) 1.0.rc2.1mdk make default plugin less annoying (Mozilla official RPM)
Patch27:   mozilla-default-plugin-less-annoying.patch
# (gg) 1.4-14mdk use Standard Symbols L too for MathML
Patch42:   mozilla-1.6-mathml-standardsymbolsl.patch
# (gg) 1.4-14mdk fix problem with time font in MathML
Patch43:   mozilla-mathml-times.patch

# (fc) 1.1-0.branch.1mdk use standard mozilla packaging tool for enigmail/enigmime
Patch46:   mozilla-1.7-enigmail-package.patch
# (fc) 1.1-0.branch.1mdk fix spellchecker includes
Patch47:   mozilla-1.1.14-spellcheckerinclude.patch
# (gb) 1.1-4mdk myspell dictionaries are in /usr/share/dict/ooo/
# (fc) 1.3-0.alpha.2mdk google is now search engine by default, add mdk bugzilla in search engines list
Patch59:   mozilla-1.7-search.patch
# (fc) 1.4-0.alpha.1mdk allow to change UI font (rawhide + ghibo)
Patch62:   mozilla-1.3-uifont.patch
#
# (gg) 1.3-2mdk enabled default pipelining
Patch100:  mozilla-1.7-pipelining.patch
# (gg) Disable remote image "selfbannering" on mailnews
Patch101:  mozilla-1.7-disable-mailnews-remoteimage.patch
# (gg) Add some dir to the freetype2 font path
Patch102:  mozilla-1.7-freetype2-antialias-path.patch
# (gg) Enable "A4" paper by default instead of "letter"
Patch104:  mozilla-1.7-a4paper.patch
# (gg) Patch for default font names for x-western
Patch105:  mozilla-1.7-corefonts-fontnames.patch
# (gg) 1.4-4mdk patches for MathML (bug #176290)
Patch113:  mozilla-176290_127030.patch
# (fc) 1.4-10mdk use xvt instead of xterm
Patch132:  mozilla-1.7-xvt.patch
# (gg) 1.4-15mdk workaround problems with prdtoa (merged from RH)
Patch174:  mozilla-1.4-prdtoa.patch
# (gg) 1.4-15mdk patch for using -pie for linking mozilla-bin (merged from RH)
Patch178:  mozilla-1.4.1-pie.patch
# (fc) 1.7.2-10mdk initial startup as maximized 
Patch251:  mozilla-1.7.5-defaultsize.patch
# (fc) 1.7.3-1mdk try to load castella PKCS#11 module if available
Patch257:  mozilla-1.6-castella.patch
# (fc) 1.7.3-2mdk fix compilation with latest freetype2 (Moz bug #234035)
Patch258:  mozilla-1.7.7-freetype-compile.patch
# (fc) 1.7.3-2mdk prevent inlining of stack direction detection (RH bug #135255)
Patch267:  mozilla-1.7.3-stack-direction.patch
# (fc) 1.7.3-2mdk Fix problem where default apps aren't showing up in the download dialog (RH bug #136261) (Fedora)
Patch268:  mozilla-1.7.3-gnome-vfs-default-app.patch
# (fc) 1.7.3-2mdk fix dynamic library loading on 64bit system (gb)
Patch270:  mozilla-1.6-lib64.patch
# (gb) 1.7.5-5mdk fix loading of libXext.so.6 and libXt.so.6 
Patch274:  mozilla-load-full-dso.patch
# (fc) 1.7.5-5mdk enable automatic language detection at startup (Debian)
Patch276:  mozilla-1.7.5-lang.patch
# (fc) 1.7.5-5mdk don't call netstat to set entropy (Debian) (Mdk bug #9427)
# (cjw) doesn't apply to seamonkey 1.1
#Patch277:  mozilla-1.7.5-fixrandom.patch.bz2
# (fc) 1.7.5-5mdk ignore unknown mouse button event (Debian)
Patch278:  mozilla-1.7.5-unknownmousebutton.patch
# (fc) 1.7.6-3mdk add env variable to disable GNOME uri handler (Fedora)
Patch281:  mozilla-1.6-gnome-uriloader.patch
#
Patch295:  mozilla-1.7.12-pango-direction.patch
Patch298:  mozilla-1.7.12-g-application-name.patch
Patch299:  seamonkey-1.0.3-gcc41.patch
# (gg) fix for rounding error in style values https://bugzilla.mozilla.org/show_bug.cgi?id=182670
Patch300:  mozilla-182670.patch
# (cjw) some X11 libs missing for libgklayout link command
Patch301:  seamonkey-1.1-layout-link-fix.patch
# (cjw) from mozilla-firefox package: fix buffer overflow crash with glibc 2.8
Patch302:  firefox-3.0rc1-glibc28-max_path-fix.patch
# (cjw) fix build error from enigmail due to a visibility problem
Patch303:  enigmail-0.95.6-visibility.patch
# fix build with -Werror=format-security in compile flags
Patch304:  seamonkey-1.1.14-fix-string-format.patch
Epoch:     %{epoch_mozilla}
Conflicts: j2re = 1.4.0-beta3
Conflicts: j2sdk = 1.4.0-beta3

BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	autoconf2.1
BuildRequires:	libjpeg-devel libpng-devel libIDL-devel
BuildRequires:  zip tcsh
%if %{mdkversion} >= 200610
BuildRequires:  libxft-devel
BuildRequires:	libxt-devel
%endif
BuildRequires:  gtk+2-devel >= 2.4.0
BuildRequires:  gnome-vfs2-devel
BuildRequires:	libgnomeui2-devel
BuildRequires:  krb-devel
%if %{mdkversion} >= 200900
BuildRequires:	gcc4.2-c++
%endif

%if %{mdkversion} >= 200610
BuildRequires:	rootcerts >= 20060621
%endif
%if !%{build_nspr_nss}
# -static for libcrmf.a
BuildRequires:  nss-static-devel
%endif

%if %{build_nspr_nss}
Requires(post):		%{lib_nspr_name} >= %{epoch_nspr}:%{version}-%{release} 
Requires(postun):	%{lib_nspr_name} >= %{epoch_nspr}:%{version}-%{release} 
%else
Requires(post):		%{lib_nspr_name} 
Requires(postun):	%{lib_nspr_name} 
%endif
Requires(post):		perl psmisc
Requires(postun):	perl psmisc
%if %{build_nspr_nss}
Requires:	%{lib_nss_name} = %{epoch_nss}:%{version}-%{release} 
%else
Requires:	%{lib_nss_name}
%endif
Requires:	indexhtml 
Requires:	gtk+2 >= 2.4.0

%if %{build_pango}
BuildRequires:	pango >= 1.5.0
%endif

Group:		Networking/WWW
Url:		http://www.seamonkey-project.org/
Obsoletes:	mozilla-xpcom mozilla-browser mozilla-psm mozilla-ctl mozilla
Provides:	mozilla-xpcom = 0:1.8-1mdk
Provides:	mozilla-browser = 0:1.8-1mdk
Provides:	mozilla-psm = 0:1.8-1mdk
Provides:	mozilla-ctl = 0:1.8-1mdk
Provides:	webclient
Provides:	mozilla = 0:1.8-1mdk
Obsoletes:	mozilla

%description
The SeaMonkey project is a community effort to develop the SeaMonkey
all-in-one internet application suite. Such a software suite was
previously made popular by Netscape and Mozilla, and the SeaMonkey
project continues to develop and deliver high-quality updates as well
as new features and improvements to this concept. Containing an
Internet browser, email & newsgroup client, HTML editor, IRC chat
and web development tools, SeaMonkey is sure to appeal to advanced
users, web developers and corporate users.

%if %{build_nspr_nss}
%package -n %{lib_nspr_name}
Epoch:		%{epoch_nspr}
License:	MPL/GPL
URL:		http://www.mozilla.org/projects/nspr/index.html
Summary:	Netscape Portable Runtime Library
Group:		System/Libraries
Obsoletes:	nspr
Provides:	nspr = %{version}-%{release}
Provides:	mozilla-nspr = %{version}-%{release}
Conflicts:	mozilla < 0.9.9

%description -n %{lib_nspr_name}
NSPR provides platform independence for non-GUI operating system
facilities. These facilities include threads, thread synchronization,
normal file and network I/O, interval timing and calendar time, basic
memory management (malloc and free) and shared library linking.

%package -n %{devel_nspr_name}
Epoch:		%{epoch_nspr}
Summary:	Netscape Portable Runtime library - development files
Group:		Development/C++
Requires:	%{lib_nspr_name} = %{epoch_nss}:%{version}-%{release}
Obsoletes:	nspr-devel
Provides:	nspr-devel = %{version}-%{release}
Provides:	libnspr-devel = %{version}-%{release}

%description -n %{devel_nspr_name}
Header files for doing development with the Netscape Portable Runtime.

%package -n %{lib_nss_name}
Epoch:		%{epoch_nss}
License:	MPL/GPL
URL:		http://mozilla.org/projects/security/pki/nss/
Summary:	Network Security Services (NSS)
Group:		System/Libraries
Provides:	mozilla-nss = %{version}-%{release}

%description -n %{lib_nss_name}
Network Security Services (NSS) is a set of libraries designed 
to support cross-platform development of security-enabled server 
applications. Applications built with NSS can support SSL v2 and v3, 
TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509 v3 certificates,
and other security standards. 

%package -n %{devel_nss_name}
Epoch:		%{epoch_nss}
Summary:	Network Security Services (NSS) - development files
Group:		Development/C++
Requires:	%{lib_nss_name} = %{epoch_nss}:%{version}-%{release}
Requires:	%{lib_nspr_name}-devel = %{epoch_nspr}:%{version}-%{release}
Provides:	libnss-devel = %{version}-%{release}
Provides:	nss-devel = %{version}-%{release}

%description -n %{devel_nss_name}
Header files to doing development with Network Security Services.
%endif 

%package devel
Summary:	SeaMonkey development files
Group:		Development/Other
Requires:	%{name} = %{epoch_mozilla}:%{version}-%{release}
Requires:	libnspr-devel
Provides:	mozilla-devel = 0:1.8-1mdk
Obsoletes:	mozilla-devel
%description devel
Mozilla development files

%package mail
Summary:		SeaMonkey-based mail system
Group:			Networking/Mail
Requires(post):		%{name} = %{epoch_mozilla}:%{version}-%{release}
Requires(postun):	%{name} = %{epoch_mozilla}:%{version}-%{release}
Provides:		mozilla-mail = 0:1.8-1mdk
Obsoletes:		mozilla-mail

%description mail
Mail/news client based on the Mozilla web browser.  The mail/news
client supports IMAP, POP, and NNTP and has an easy to use interface.

%package irc
Summary:		IRC support for SeaMonkey
Group:			Networking/IRC
Requires(post):		%{name} = %{epoch_mozilla}:%{version}-%{release}
Requires(postun):	%{name} = %{epoch_mozilla}:%{version}-%{release}
Provides:		mozilla-chatzilla mozilla-chat mozilla-irc = 0:1.8-1mdk
Obsoletes:		mozilla-chatzilla mozilla-chat mozilla-irc

%description irc
IRC support for SeaMonkey.

%if %{build_xmlterm}
%package xmlterm
Summary:		XML enabled Terminal Client for SeaMonkey
Group:			Networking/Other
Requires(post):		%{name} = %{epoch_mozilla}:%{version}-%{release}
Requires(postun):	%{name} = %{epoch_mozilla}:%{version}-%{release}
Provides:		mozilla-xmlterm = 0:1.8-1mdk
Obsoletes:		mozilla-xmlterm

%description xmlterm
This is a terminal client written for SeaMonkey that has special capabilities.
When combined with the xls, and xcat programs, you can get directory listings 
with thumbnails for images, and you can cat known file types 
and view them inline.
%endif

%package js-debugger
Summary:		JavaScript debugger for use with SeaMonkey
Group:			Networking/WWW
Requires(post):		%{name} = %{epoch_mozilla}:%{version}-%{release}
Requires(postun):	%{name} = %{epoch_mozilla}:%{version}-%{release}
Provides:		mozilla-js-debugger = 0:1.8-1mdk
Obsoletes:		mozilla-js-debugger

%description js-debugger
JavaScript debugger for use with SeaMonkey.

%package dom-inspector
Summary:		A tool for inspecting the DOM of pages in SeaMonkey
Group:			Networking/WWW
Requires(post):		%{name} = %{epoch_mozilla}:%{version}-%{release}
Requires(postun):	%{name} = %{epoch_mozilla}:%{version}-%{release}
Provides:		mozilla-dom-inspector = 0:1.8-1mdk
Obsoletes:		mozilla-dom-inspector

%description dom-inspector
This is a tool that allows you to inspect the DOM for web pages in
SeaMonkey.  This is of great use to people who are doing Mozilla chrome
development or web page development.


%package spellchecker
Summary:		Spellchecker for SeaMonkey
Group:			Networking/Mail
Requires(post):		%{name} = %{epoch_mozilla}:%{version}-%{release}
Requires(postun):	%{name} = %{epoch_mozilla}:%{version}-%{release}
Requires:		myspell-dictionary
Provides:		mozilla-spellchecker = 0:1.8-1mdk
Obsoletes:		mozilla-spellchecker

%description spellchecker
Spellchecker package for SeaMonkey.

%if %build_enigmail
%package enigmail
Summary:		GPG encryption support for SeaMonkey
Group:			Networking/Mail
Requires(post):		%{name} = %{epoch_mozilla}:%{version}-%{release}
Requires(postun):	%{name} = %{epoch_mozilla}:%{version}-%{release}
Requires:		%{name}-enigmime = %{epoch_mozilla}:%{version}-%{release}
Requires:		gnupg
Provides:		mozilla-enigmail = 0:1.8-1mdk
Obsoletes:		mozilla-enigmail

%description enigmail
GPG encryption support for SeaMonkey

%package enigmime
Summary:		Inter-process communication required for enigmail
Group:			Networking/Mail
Requires(post):		%{name} = %{epoch_mozilla}:%{version}-%{release}
Requires(postun):	%{name} = %{epoch_mozilla}:%{version}-%{release}
Requires:		%{name}-mail = %{epoch_mozilla}:%{version}-%{release}
Provides:		mozilla-enigmime = 0:1.8-1mdk
Obsoletes:		mozilla-enigmime

%description enigmime
Inter-process communication required for enigmail
%endif

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -c %{name}-%{version} -a 6
%setup -q -T -D -n %{name}-%{version}/mozilla

%patch47 -p1 -b .spellcheckinclude

%if %build_enigmail
#setup -T -D -n %{name}-%{version}/mozilla/extensions -q -a21
%ifarch x86_64
%setup -T -D -n %{name}-%{version}/mozilla/mailnews/extensions -q -a29
%else
%setup -T -D -n %{name}-%{version}/mozilla/mailnews/extensions -q -a22
%endif
%setup -T -D -n %{name}-%{version}/mozilla -q
%endif

#those patches are commented for "final" version of mozilla
%if !%build_is_final
%patch0 -p1 -b .nodebug
%patch23 -p1 -b .nobuildid
%endif

%patch7 -p1 -b .browser-home-page

%patch12 -p1 -b .psfont
%patch13 -p1 -b .nspr
%if %french_policy
%patch24 -p1 -b .frenchpolicy
%endif
%patch27 -p1 -b .defaultplugin
%patch42 -p1 -b .standardsym
%patch43 -p1 -b .mathmltimes

%patch46 -p1 -b .enigmailpackage
#patch53 -p1 -b .spellcheck-system-dicts
#patch54 -p1 -b .spellcheck-full-langname
%patch59 -p1 -b .search
%patch62 -p1 -b .uifont

%if %build_ggdefaults
%patch100 -p1 -b .pipelining
%patch101 -p1 -b .mailnews
%patch102 -p1 -b .antialias
%patch104 -p1 -b .a4
%endif

%if %build_corefonts
%patch105 -p1 -b .corefonts
%endif

# MathML patches
%patch113 -p1 -b .mathml

# Other patches
%patch132 -p1 -b .xvt
%patch174 -p1 -b .prdtoa
%if %build_pie
%patch178 -p1 -b .pie
%endif

%patch251 -p1 -b .defaultsize
%patch257 -p1 -b .castella
%if %build_ggdefaults
%patch258 -p0 -b .freetype-compile
%endif
%patch267 -p1 -b .stackdirection
%patch268 -p1 -b .gnomevfsdefaultapp
%patch270 -p1 -b .lib64
%patch274 -p1 -b .load-full-dso
%patch276 -p1 -b .lang
#patch277 -p1 -b .fixrandom
%patch278 -p1 -b .unknownmousebutton
%patch281 -p1 -b .gnome-uriloader

%if %build_pango
%patch295 -p1 -b .pango-direction
%endif
#
%patch298 -p1 -b .g-application-name
%patch299 -p2 -b .gcc41
%patch300 -p1 -b .182670
%patch301 -p1 -b .x11_xrender
%patch302 -p1 -b .glibc28
%patch303 -p1 -b .enigmail-visibility
%patch304 -p1 -b .strfmt

rm -f profile/defaults/bookmarks.html
touch profile/defaults/bookmarks.html
cp %{SOURCE23} xpfe/components/search/datasets

tar xjf %{SOURCE24} -C mailnews/base/resources/locale/en-US

# let jars get compressed
%__perl -p -i -e 's|\-0|\-9|g' config/make-jars.pl

%build
#needed by patch 178, 182 & 205 & 262
autoconf-2.13

# needed by patch291
pushd directory/c-sdk
rm -f configure
aclocal -I config/autoconf
autoconf
popd

# needed to regenerate certdata.c
%if %{mdkversion} >= 200610
cd security/nss/lib/ckfw/builtins
perl ./certdata.perl < /etc/pki/tls/mozilla/certdata.txt
cd -
%endif
export MOZ_BUILD_DATE="%{releasedate}"

# Build with -fabi-version=1 when compiling with gcc3.4+ so that a
# certain level of compatibility is kept to run Sun's Java plugin
GCC_VERSION=`gcc -dumpversion | perl -pe '/(\d+)\.(\d)\.?(\d)?/; $_="$1$2".($3||0)'`
[[ $GCC_VERSION -ge 340 ]] && export CXXFLAGS="-fabi-version=1"

OPT_FLAGS="$RPM_OPT_FLAGS"

BUILD_OFFICIAL=1 MOZILLA_OFFICIAL=1 MOZ_INTERNAL_LIBART_LGPL=1 \
%if %{mdkversion} >= 200900
	CC=gcc4.2 CXX=g++4.2 CPP=cpp4.2 \
%endif
	./configure --build=%{_target_platform} \
	--enable-application=suite \
	--prefix=%{_prefix} --libdir=%{_libdir} \
	--enable-optimize="$OPT_FLAGS" \
	--disable-strip \
%if %build_debug
	--enable-debug \
%else
	--disable-debug \
%endif
	--disable-pedantic \
%if %build_pie
	--enable-pie \
%endif
	--disable-tests \
	--enable-crypto \
%if %{build_nspr_nss}
	--enable-nspr-autoconf \
	--without-system-nspr \
	--without-system-nss \
%else
	--with-system-nspr \
	--with-system-nss \
%endif
	--with-default-mozilla-five-home=%{mozillalibdir} \
	--enable-extensions --disable-short-wchar \
	--enable-xinerama \
	--enable-mathml \
	--with-system-zlib --with-system-png \
	--enable-system-cairo \
	--with-system-jpeg --enable-ipv6 \
	--enable-old-abi-compat-wrappers --mandir=%{_mandir} \
%if %enable_svg
	--enable-svg \
	--enable-svg-renderer-libart \
%endif
	--enable-xft \
%if %build_ggdefaults
	--enable-freetype2 \
%else
	--disable-freetype2 \
%endif
%if %build_pango
	--enable-pango \
%endif
	--enable-default-toolkit=%{toolkit}

BUILD_OFFICIAL=1 MOZILLA_OFFICIAL=1 make -s export
#only this part should be parallel (ie use make macro)
BUILD_OFFICIAL=1 MOZILLA_OFFICIAL=1 make -s libs

%if %build_enigmail
#cd extensions/ipc
#./makemake
#BUILD_OFFICIAL=1 MOZILLA_OFFICIAL=1 %make -s
cd mailnews/extensions/enigmail
./makemake -r
BUILD_OFFICIAL=1 MOZILLA_OFFICIAL=1 make -s
(cd lang
 BUILD_OFFICIAL=1 MOZILLA_OFFICIAL=1 make -s
)
cd ../../..
%endif

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{mozillalibdir}/plugins

BUILD_OFFICIAL=1 MOZILLA_OFFICIAL=1 %makeinstall_std

%if %{build_nspr_nss}
#move nspr/nss to %{_libdir}
mv $RPM_BUILD_ROOT%{mozillalibdir}/{libnspr4.so,libplc4.so,libplds4.so,libnss3.so,libnssckbi.so,libsmime3.so,libsoftokn3.so,libssl3.so,libsoftokn3.chk} $RPM_BUILD_ROOT%{_libdir}

# create a list of all of the different package and the files that
# will hold them
rm -f %{_tmppath}/mozilla-nspr.list

%{SOURCE25} --package nspr \
    --output-file %{_tmppath}/mozilla-nspr.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{_libdir} \
    --install-root %{_libdir}

rm -f %{_tmppath}/mozilla-nss.list
%{SOURCE25} --package nss \
    --output-file %{_tmppath}/mozilla-nss.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{_libdir} \
    --install-root %{_libdir}
%endif

rm -f %{_tmppath}/mozilla.list
%{SOURCE25} --package langenus \
    --output-file %{_tmppath}/mozilla.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{mozillalibdir} \
    --install-root %{mozillalibdir}

%{SOURCE25} --package regus \
    --output-file %{_tmppath}/mozilla.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{mozillalibdir} \
    --install-root %{mozillalibdir}

%{SOURCE25} --package deflenus \
    --output-file %{_tmppath}/mozilla.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{mozillalibdir} \
    --install-root %{mozillalibdir}

%{SOURCE25} --package xpcom \
    --output-file %{_tmppath}/mozilla.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{mozillalibdir} \
    --install-root %{mozillalibdir} \
    --exclude-file=%{SOURCE27}

%{SOURCE25} --package browser \
    --output-file %{_tmppath}/mozilla.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{mozillalibdir} \
    --install-root %{mozillalibdir}

# workaround for bug 81429
(cd $RPM_BUILD_ROOT%{mozillalibdir} 
ln -s ../libnssckbi.so libnssckbi.so
)


rm -f %{_tmppath}/mozilla-mail.list
%{SOURCE25} --package mail --output-file %{_tmppath}/mozilla-mail.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{mozillalibdir} \
    --install-root %{mozillalibdir}

%{SOURCE25} --package psm \
    --output-file %{_tmppath}/mozilla.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{mozillalibdir} \
    --install-root %{mozillalibdir} \
    --exclude-file=%{SOURCE28}

rm -f %{_tmppath}/mozilla-chat.list
%{SOURCE25} --package chatzilla --output-file %{_tmppath}/mozilla-chat.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{mozillalibdir} \
    --install-root %{mozillalibdir}

rm -f %{_tmppath}/mozilla-js-debugger.list
%{SOURCE25} --package venkman \
    --output-file %{_tmppath}/mozilla-js-debugger.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{mozillalibdir} \
    --install-root %{mozillalibdir}

rm -f %{_tmppath}/mozilla-dom-inspector.list
%{SOURCE25} --package inspector \
    --output-file %{_tmppath}/mozilla-dom-inspector.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{mozillalibdir} \
    --install-root %{mozillalibdir}

cat >%{_tmppath}/mozilla-spellchecker-exclude.list <<EOF
dictionaries/en-US.aff
dictionaries/en-US.dic
EOF

rm -f %{_tmppath}/mozilla-spellchecker.list
%{SOURCE25} --package spellcheck \
    --output-file %{_tmppath}/mozilla-spellchecker.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{mozillalibdir} \
    --install-root %{mozillalibdir} \
    --exclude-file=%{_tmppath}/mozilla-spellchecker-exclude.list

%if %build_enigmail
#hack to get the enigmail stuff to install:
for i in components/enigmime.xpt components/ipc.xpt components/libenigmime.so \
	components/enigmail.js components/enigmail.xpt chrome/enigmail.jar \
	components/enigprefs-service.js chrome/enigmail-skin.jar \
	chrome/enigmime.jar defaults/pref/enigmail.js chrome/enigmail-en-US.jar ; do 
		install dist/bin/$i $RPM_BUILD_ROOT/%{mozillalibdir}/$i;
done

chmod 644 $RPM_BUILD_ROOT/%{mozillalibdir}/defaults/pref/enigmail.js
perl -pi -e 's|agentPath",""|agentPath","/usr/bin/gpg"|' $RPM_BUILD_ROOT/%{mozillalibdir}/defaults/pref/enigmail.js 

rm -f %{_tmppath}/mozilla-enigmail.list
%{SOURCE25} --package enigmail \
    --output-file %{_tmppath}/mozilla-enigmail.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{mozillalibdir} \
    --install-root %{mozillalibdir}

cd $RPM_BUILD_ROOT%{mozillalibdir}/chrome
#tar -xjf %{SOURCE31} 
for i in enigmail-*-*.jar ; do 
 RPMLANG=`echo $i | cut -d '-' -f 2`
 if [ "$RPMLANG" = "en" ]; then 
  echo "%{mozillalibdir}/chrome/$i" >> %{_tmppath}/mozilla-enigmail.list
 else
  echo "%lang($RPMLANG) %{mozillalibdir}/chrome/$i" >> %{_tmppath}/mozilla-enigmail.list
 fi
done
cd -

rm -f %{_tmppath}/mozilla-enigmime.list
%{SOURCE25} --package enigmime \
    --output-file %{_tmppath}/mozilla-enigmime.list \
    --package-file xpinstall/packager/packages-unix \
    --install-dir $RPM_BUILD_ROOT%{mozillalibdir} \
    --install-root %{mozillalibdir}
%endif

# copy xmlterm files
%if %{build_xmlterm}
/bin/cp -rL dist/bin/{xmlterm,xcat,xenv,xls}  $RPM_BUILD_ROOT%{_bindir} || \
	/bin/cp -r dist/bin/{xmlterm,xcat,xenv,xls}  $RPM_BUILD_ROOT%{_bindir}
/bin/cp -rL dist/bin/chrome/xmlterm.jar  $RPM_BUILD_ROOT%{mozillalibdir}/chrome || \
	/bin/cp -r dist/bin/chrome/xmlterm.jar  $RPM_BUILD_ROOT%{mozillalibdir}/chrome
/bin/cp -rL dist/bin/components/*xmlterm*  $RPM_BUILD_ROOT%{mozillalibdir}/components || \
	/bin/cp -r dist/bin/components/*xmlterm*  $RPM_BUILD_ROOT%{mozillalibdir}/components
%endif

# install l10n files
%if %{enable_l10n}
cat %{SOURCE99} >$RPM_BUILD_ROOT%{mozillalibdir}/chrome/locale.alias
mkdir -p ../l10n
pushd ../l10n
# should be done in prep....
unzip -o %{SOURCE100}
unzip -o %{SOURCE101}
unzip -o %{SOURCE102}
unzip -o %{SOURCE103}
unzip -o %{SOURCE104}
unzip -o %{SOURCE105}
unzip -o %{SOURCE106}
unzip -o %{SOURCE108}
unzip -o %{SOURCE109}
unzip -o %{SOURCE110}
unzip -o %{SOURCE114}
unzip -o %{SOURCE115}
unzip -o %{SOURCE116}
unzip -o %{SOURCE118}
unzip -o %{SOURCE119}
unzip -o %{SOURCE120}
unzip -o %{SOURCE121}
unzip -o %{SOURCE122}
unzip -o %{SOURCE123}
unzip -o %{SOURCE124}

#unzip -o %{SOURCE107}
#unzip -o %{SOURCE111}
#unzip -o %{SOURCE112}
#unzip -o %{SOURCE113}
#unzip -o %{SOURCE117}

for lang in %{l10ns}; do
  RPMLANG=$(echo $lang|cut -d '-' -f 1)
  JARFILE=${lang}.jar
  UNIXFILE=${RPMLANG}-unix.jar
  if ! ( [ -f ./chrome/$UNIXFILE ] || [ -f bin/chrome/$UNIXFILE ] ); then
    UNIXFILE=${lang}-unix.jar
  fi
  if [ -f bin/chrome/$JARFILE ]; then
    cp bin/chrome/$JARFILE bin/chrome/$UNIXFILE $RPM_BUILD_ROOT%{mozillalibdir}/chrome/
  else
    cp ./chrome/$JARFILE ./chrome/$UNIXFILE $RPM_BUILD_ROOT%{mozillalibdir}/chrome/
  fi
  chmod 644 $RPM_BUILD_ROOT%{mozillalibdir}/chrome/$JARFILE $RPM_BUILD_ROOT%{mozillalibdir}/chrome/$UNIXFILE
  echo "%lang($RPMLANG) %{mozillalibdir}/chrome/$JARFILE" >> %{_tmppath}/mozilla.list
  echo "%lang($RPMLANG) %{mozillalibdir}/chrome/$UNIXFILE" >> %{_tmppath}/mozilla.list
  cat << EOF | sed -e "s/@LOCALE@/$lang/g" -e "s/@LANG@/$RPMLANG/g" >> $RPM_BUILD_ROOT%{mozillalibdir}/chrome/installed-chrome.txt
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/autoconfig/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/chatzilla/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/communicator/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/content-packs/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/cookie/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/editor/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/embed/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/forms/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/inspector/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/global/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/help/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/messenger/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/messenger-smime/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/messenger-mapi/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/mozldap/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/navigator/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/necko/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/pipnss/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/pippki/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/venkman/
locale,install,url,jar:resource:/chrome/@LOCALE@.jar!/locale/@LOCALE@/wallet/
locale,install,url,jar:resource:/chrome/@LANG@-unix.jar!/locale/@LOCALE@/global-platform/
locale,install,url,jar:resource:/chrome/@LANG@-unix.jar!/locale/@LOCALE@/communicator-platform/
locale,install,url,jar:resource:/chrome/@LANG@-unix.jar!/locale/@LOCALE@/navigator-platform/
EOF
done
echo "%{mozillalibdir}/chrome/locale.alias" >> %{_tmppath}/mozilla.list
popd
%endif

# remove duplicated entries
cat %{_tmppath}/mozilla.list | sort -k 2 | \
	grep -v "%lang(en) %{mozillalibdir}/chrome/en-unix.jar" | \
	uniq > %{_tmppath}/mozilla.list.uniq
mv -f %{_tmppath}/mozilla.list.uniq %{_tmppath}/mozilla.list

# build our initial component and chrome registry
# we don't need to do this anymore
pushd `pwd`
  cd $RPM_BUILD_ROOT%{mozillalibdir}
  # register our components
  LD_LIBRARY_PATH=`pwd`/..:`pwd` MOZILLA_FIVE_HOME=`pwd` ./regxpcom
  # set up the default skin and locale to trigger the generation of
  # the user-locales and users-skins.rdf
  echo "skin,install,select,classic/1.0" >> chrome/installed-chrome.txt
  echo "locale,install,select,en-US" >> chrome/installed-chrome.txt
  # set up the chrome rdf files
  LD_LIBRARY_PATH=`pwd`/..:`pwd` MOZILLA_FIVE_HOME=`pwd` ./regchrome
  # fix permissions of the chrome directories
  find . -type d -perm 0700 -exec chmod 755 {} \; || :
popd

# cp -L (dereference all symlinks) is required for fileutils >= 2.0.27
# (POSIX compliance); prior versions don't understand -L, so fall back...

%if %{build_nspr_nss}
# copy the nss files to the right place
mkdir -p $RPM_BUILD_ROOT%{mozillaincludedir}/nss/
find security/nss/lib/ -name '*.h' -type f -exec /bin/cp {} \
 $RPM_BUILD_ROOT%{mozillaincludedir}/nss/ \;
%endif

# build the list of include files
rm -f %{_tmppath}/mozilla-devel.list
rm -f %{_tmppath}/mozilla-nss-devel.list
rm -f %{_tmppath}/mozilla-nspr-devel.list

find $RPM_BUILD_ROOT%{mozillaincludedir}/ -type f | \
  sed -e "s,$RPM_BUILD_ROOT,," | \
  grep -v "%{mozillaincludedir}/nss" | \
  grep -v "%{mozillaincludedir}/nspr" > \
  %{_tmppath}/mozilla-devel.list

%if %{build_nspr_nss}
find $RPM_BUILD_ROOT%{mozillaincludedir}/ -type f | \
  sed -e "s,$RPM_BUILD_ROOT,," | \
  grep "%{mozillaincludedir}/nspr" > \
  %{_tmppath}/mozilla-nspr-devel.list

find $RPM_BUILD_ROOT%{mozillaincludedir}/ -type f | \
  sed -e "s,$RPM_BUILD_ROOT,," | \
  grep "%{mozillaincludedir}/nss" > \
  %{_tmppath}/mozilla-nss-devel.list
%endif


# copy our devel tools
install -c -m 755 dist/bin/xpcshell \
  dist/bin/xpidl \
  dist/bin/xpt_dump \
  dist/bin/xpt_link \
  $RPM_BUILD_ROOT%{mozillalibdir}

mkdir -p $RPM_BUILD_ROOT%{_miconsdir} $RPM_BUILD_ROOT%{_liconsdir}

cp -f %SOURCE2 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
cp -f %SOURCE3 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
cp -f %SOURCE4 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

# move manpage in the correct directory
#mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
#mv $RPM_BUILD_ROOT/usr/man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1/

# install our mozilla.sh file
bzcat %{SOURCE10} | sed -e "s|SEAMONKEY_VERSION|%{dirversion}|g;s|LIBDIR|%{_libdir}|g" > $RPM_BUILD_ROOT%{_bindir}/seamonkey
chmod 755 $RPM_BUILD_ROOT%{_bindir}/seamonkey

# install our rebuild file
cat %{SOURCE26} | sed -e "s|SEAMONKEY_VERSION|%{dirversion}|g;s|LIBDIR|%{_libdir}|g" > \
  $RPM_BUILD_ROOT%{mozillalibdir}/seamonkey-rebuild-databases.pl

chmod 755 \
  $RPM_BUILD_ROOT%{mozillalibdir}/seamonkey-rebuild-databases.pl

# we own /usr/lib/mozilla/plugins which is the version-independent
# place that our plugins can be installed
mkdir -p $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins

%if %build_gre
# install the gre.conf file
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
echo [%{version}] >  $RPM_BUILD_ROOT%{_sysconfdir}/gre.conf
echo GRE_PATH=%{mozillalibdir} >> $RPM_BUILD_ROOT%{_sysconfdir}/gre.conf
%endif

# installs menu file
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/applications

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=SeaMonkey Navigator
Comment=Seamonkey Navigator web browser
Exec=%{_bindir}/seamonkey %u
Icon=seamonkey
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Network;WebBrowser;X-MandrivaLinux-Internet-WebBrowsers;
StartupWMClass=Seamonkey-bin
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-composer.desktop << EOF
[Desktop Entry]
Name=SeaMonkey Composer
Comment=Seamonkey Composer HTML editor
Exec=%{_bindir}/seamonkey -edit %u
Icon=seamonkey
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Network;WebDevelopment;X-MandrivaLinux-Internet-WebEditors;
StartupWMClass=Seamonkey-bin
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-mail.desktop << EOF
[Desktop Entry]
Name=SeaMonkey Mail
Comment=Seamonkey Mail & Newsgroups e-mail client
Exec=%{_bindir}/seamonkey -mail
Icon=seamonkey
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;X-MandrivaLinux-Internet-Mail;Office;Network;Email;
StartupWMClass=Seamonkey-bin
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-addressbook.desktop << EOF
[Desktop Entry]
Name=SeaMonkey Address Book
Comment=Seamonkey Address Book
Exec=%{_bindir}/seamonkey -addressbook
Icon=seamonkey
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;X-MandrivaLinux-Internet-Mail;Office;Network;Email;
StartupWMClass=Seamonkey-bin
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-news.desktop << EOF
[Desktop Entry]
Name=SeaMonkey News
Comment=Seamonkey Mail & Newsgroups news reader
Exec=%{_bindir}/seamonkey -news
Icon=seamonkey
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;X-MandrivaLinux-Internet-News;Network;News;
StartupWMClass=Seamonkey-bin
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-chat.desktop << EOF
[Desktop Entry]
Name=ChatZilla
Comment=Seamonkey IRC client
Exec=%{_bindir}/seamonkey -chat
Icon=seamonkey
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;X-MandrivaLinux-Internet-Chat;Network;IRCClient;
StartupWMClass=Seamonkey-bin
EOF

%if %{build_xmlterm}
# installs menu file
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-xmlterm.desktop << EOF
[Desktop Entry]
Name=SeaMonkey XMLTerm
Comment=Seamonkey XMLTerm terminal emulator implemented with Mozilla toolkit
Exec=%{_bindir}/seamonkey -terminal
Icon=seamonkey
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;X-MandrivaLinux-System-Terminals;TerminalEmulator;
StartupWMClass=Seamonkey-bin
EOF
%endif

bzcat %{SOURCE5} | tar -C $RPM_BUILD_ROOT%{mozillalibdir}/defaults/profile/US -xf - 

# .js files should not be executable
chmod a-x $RPM_BUILD_ROOT%{mozillalibdir}/components/*.js

# disable check for new versions
sed -i -re 's/("update_notifications.enabled", )true/\1false/' $RPM_BUILD_ROOT%{mozillalibdir}/defaults/pref/browser-prefs.js

# remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{mozillalibdir}/chrome/{cview,embed-sample,layoutdebug,tasks}.jar \
 $RPM_BUILD_ROOT%{mozillalibdir}/chrome/icons/default/{calendar-*,default}.xpm \
 $RPM_BUILD_ROOT%{mozillalibdir}/components/{accessproxy,content,iiextras,xmlsecurity,ipcd,profilesharingsetup,transmngr,ucnative,layout_debug}.xpt \
 $RPM_BUILD_ROOT%{mozillalibdir}/components/{libaccessproxy,libiiextras,libnkdatetime,libnkfinger,libembed_lite,libipcdc,libtransmngr_client,libgkdebug}.so \
 $RPM_BUILD_ROOT%{mozillalibdir}/defaults/profile/US/chrome/*example.css \
 $RPM_BUILD_ROOT%{mozillalibdir}/defaults/profile/chrome/*example.css \
 $RPM_BUILD_ROOT%{mozillalibdir}/res/{gfx/icon_0.gif,gfx/icon_1.gif}  \
 $RPM_BUILD_ROOT%{mozillalibdir}/res/rdf/*test* \
 $RPM_BUILD_ROOT%{mozillalibdir}/res/sample.unixpsfonts.properties  \
 $RPM_BUILD_ROOT%{mozillalibdir}/res/throbber  \
 $RPM_BUILD_ROOT%{mozillalibdir}/res/viewer.properties  \
 $RPM_BUILD_ROOT%{mozillalibdir}/{timebombgen,TestGtkEmbed*,libnullplugin.so,mozilla-ipcd,tmModuleTest,TestIPC} \
 $RPM_BUILD_ROOT%{mozillalibdir}/ipc/modules/{liblockmodule,libtestmodule,libtransmgr}.so \
 $RPM_BUILD_ROOT%{mozillalibdir}/{liblockmodule,libtestmodule,libtr\ansmngr}.so \
 $RPM_BUILD_ROOT%{mozillalibdir}/mozilla-installer-bin \
 $RPM_BUILD_ROOT%{mozillalibdir}/extensions \
 $RPM_BUILD_ROOT%{mozillalibdir}/res/samples \
 $RPM_BUILD_ROOT%{mozillalibdir}/dictionaries

# $RPM_BUILD_ROOT%{mozillalibdir}/res/samples/sampleimages

%if %{build_xmlterm}
rm -f $RPM_BUILD_ROOT%{mozillalibdir}/{xcat,xenv,xls,xmlterm} \
 $RPM_BUILD_ROOT%{mozillalibdir}/escape \
 $RPM_BUILD_ROOT%{mozillalibdir}/teststream \
 $RPM_BUILD_ROOT%{mozillalibdir}/DocStream \
 $RPM_BUILD_ROOT%{mozillalibdir}/HelloWorld \
 $RPM_BUILD_ROOT%{mozillalibdir}/INSTALL.xmlterm
%endif

%if !%{build_nspr_nss}
rm -rf $RPM_BUILD_ROOT%{mozillaincludedir}/nspr \
 $RPM_BUILD_ROOT%{mozillaincludedir}/nss \
 $RPM_BUILD_ROOT%{mozillalibdir}/{libplc4.so,libplds4.so,libsmime3.so,libsoftokn3.so,libssl3.so,libnspr4.so,libnss3.so,libnssckbi.so} \
 $RPM_BUILD_ROOT%{_libdir}/pkgconfig/seamonkey-{nspr,nss}.pc \
 $RPM_BUILD_ROOT%{_datadir}/aclocal/nspr.m4
sed -i -e 's/mozilla-nspr = %{version}/mozilla-nspr/'   $RPM_BUILD_ROOT%{_libdir}/pkgconfig/seamonkey-xpcom.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/seamonkey-js.pc
ln -s nspr.pc %{buildroot}%{_libdir}/pkgconfig/seamonkey-nspr.pc
ln -s nss.pc %{buildroot}%{_libdir}/pkgconfig/seamonkey-nss.pc
%endif

# multiarch
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/seamonkey-config
%multiarch_includes $RPM_BUILD_ROOT%{_includedir}/seamonkey-%{version}/{mozilla-config.h,js/jsautocfg.h}

# myspell dictionaries
ln -s ../../share/dict/mozilla $RPM_BUILD_ROOT%{mozillalibdir}/dictionaries

%if %build_debug
export DONT_STRIP=1
%endif

%clean
rm -rf $RPM_BUILD_ROOT
rm -f %{_tmppath}/mozilla*.list


%post
%if %mdkversion < 200900
%{update_menus}
%endif
ulimit -c 0
# run ldconfig before regxpcom
/sbin/ldconfig >/dev/null 2>/dev/null

# we should only rebuild database for first install
# rebuild for update is done in postun
# but it seems we need we might need to do it twince
if [ -x %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi

if [ "$1" = "2" ]; then
		update-alternatives --remove webclient-gnome /usr/bin/mozilla
		update-alternatives --remove webclient-kde /usr/bin/mozilla
fi

# Default to paper size from locale setting
case `LC_ALL=$LC_MESSAGES /usr/bin/locale -k LC_PAPER | grep width` in
*216) paper="letter";;
*) paper="a4";;
esac
perl -pi -e "s/^(pref\(\"print.postscript.paper_size\",[^\"]+)\"[a-z0-9]+\"/\1\"$paper\"/" \
  %{mozillalibdir}/greprefs/all.js

if [ ! -r /etc/sysconfig/oem ]; then
  case `grep META_CLASS /etc/sysconfig/system` in
  *server) bookmark="mozilla-powerpackplus.html" ;;
  *PowerPack)  bookmark="mozilla-powerpack.html" ;;
  *) bookmark="mozilla-discovery-download.html";;
  esac
  ln -s -f $bookmark  %{mozillalibdir}/defaults/profile/US/bookmarks.html
fi

%preun
if [ "$1" = "0" ]; then 
    /bin/rm -rf %{mozillalibdir}/chrome/overlayinfo
	/bin/rm -f %{mozillalibdir}/chrome/*.rdf
fi

%postun
%if %mdkversion < 200900
%{clean_menus}
%endif
# was this an upgrade?
if [ "$1" == "2" -a -x %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi

%if %{build_nspr_nss}
%if %mdkversion < 200900
%post -n %{lib_nspr_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_nspr_name} -p /sbin/ldconfig
%endif
%endif

%post mail
%if %mdkversion < 200900
%{update_menus}
%endif
# run ldconfig before regxpcom
/sbin/ldconfig >/dev/null 2>/dev/null

if [ -x %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi

%postun mail
%if %mdkversion < 200900
%{clean_menus}
%endif
# run ldconfig before regxpcom
/sbin/ldconfig >/dev/null 2>/dev/null

if [ -x %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi


%post irc
if [ -x %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi

%postun irc
if [ -x %{mozillalibdir}seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi

%if %{build_xmlterm}
%post xmlterm
%if %mdkversion < 200900
%{update_menus}
%endif
if [ -x %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi


%postun xmlterm
%if %mdkversion < 200900
%{clean_menus}
%endif
if [ -x %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi
%endif

%post js-debugger
if [ -f %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi

%postun js-debugger
if [ -f %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi

%post dom-inspector
if [ -f %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi

%postun dom-inspector
if [ -f %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi

%post spellchecker
if [ -f %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi

%postun spellchecker
if [ -f %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi

%if %build_enigmail
%post enigmail
if [ -f %{mozillalibdir}/chrome/installed-chrome.txt ]; then
# make sure we don't have old registration info around
   perl -pi -e 's/.*enigmail.*\n//' %{mozillalibdir}/chrome/installed-chrome.txt
  cat << EOF >> %{mozillalibdir}/chrome/installed-chrome.txt
content,install,url,jar:resource:/chrome/enigmail.jar!/content/enigmail/
skin,install,url,jar:resource:/chrome/enigmail-skin.jar!/skin/modern/enigmail/
skin,install,url,jar:resource:/chrome/enigmail-skin.jar!/skin/classic/enigmail/
EOF
  cd %{mozillalibdir}/chrome/
  for i in enigmail-*-*.jar ; do
  LOC=`echo $i | sed -e "s/.jar//" -e "s/enigmail-//"`
  cat << EOF >>  %{mozillalibdir}/chrome/installed-chrome.txt
locale,install,url,jar:resource:/chrome/$i!/locale/$LOC/enigmail/
EOF
  done
  cd -
fi
if [ -f %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi

%postun enigmail
# only remove on uninstall
if [ "$1" = "0" ]; then 
 if [ -f %{mozillalibdir}/chrome/installed-chrome.txt ]; then
   perl -pi -e 's/.*enigmail.*\n//' %{mozillalibdir}/chrome/installed-chrome.txt
 fi
fi
if [ -f %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi

%post enigmime
if [ -f %{mozillalibdir}/chrome/installed-chrome.txt ]; then
# make sure we don't have old registration info around
   perl -pi -e 's/.*enigmime.*\n//' %{mozillalibdir}/chrome/installed-chrome.txt
  cat << EOF >> %{mozillalibdir}/chrome/installed-chrome.txt
content,install,url,jar:resource:/chrome/enigmime.jar!/content/enigmime/
EOF
fi
if [ -f %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi

%postun enigmime
# only remove on uninstall
if [ "$1" = "0" ]; then 
 if [ -f %{mozillalibdir}/chrome/installed-chrome.txt ]; then
   perl -pi -e 's/.*enigmime.*\n//' %{mozillalibdir}/chrome/installed-chrome.txt
 fi
fi

if [ -f %{mozillalibdir}/seamonkey-rebuild-databases.pl ]; then
    %{mozillalibdir}/seamonkey-rebuild-databases.pl
fi
%endif


%files -f %{_tmppath}/mozilla.list
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/seamonkey
%attr(755,root,root) %{mozillalibdir}/seamonkey-rebuild-databases.pl
%if %build_gre
%config(noreplace) %{_sysconfdir}/gre.conf
%endif
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/applications/mandriva-%{name}-composer.desktop
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%dir %{_libdir}/mozilla
%dir %{mozillaplugindir}

%ghost %{mozillalibdir}/defaults/profile/US/bookmarks.html
%{mozillalibdir}/defaults/profile/US/mozilla-*.html

%dir %{mozillalibdir}/defaults/autoconfig
%dir %{mozillalibdir}/defaults/pref
%dir %{mozillalibdir}/defaults/messenger/US
%dir %{mozillalibdir}/defaults/messenger
%dir %{mozillalibdir}/defaults/profile/US
%dir %{mozillalibdir}/defaults/profile
%dir %{mozillalibdir}/defaults/wallet
%dir %{mozillalibdir}/defaults
%dir %{mozillalibdir}/chrome
%dir %{mozillalibdir}/chrome/icons
%dir %{mozillalibdir}/chrome/icons/default
%dir %{mozillalibdir}/components
%dir %{mozillalibdir}/greprefs
%dir %{mozillalibdir}/init.d
%dir %{mozillalibdir}/res/dtd
%dir %{mozillalibdir}/res/html
#dir %{mozillalibdir}/res/samples
%dir %{mozillalibdir}/res/entityTables
#dir %{mozillalibdir}/res/rdf
%dir %{mozillalibdir}/res/fonts
%dir %{mozillalibdir}/res
%dir %{mozillalibdir}/searchplugins
%dir %{mozillalibdir}/plugins
%dir %{mozillalibdir}
%verify (not md5 mtime size) %{mozillalibdir}/components/compreg.dat
%verify (not md5 mtime size) %{mozillalibdir}/components/xpti.dat
%verify (not md5 mtime size) %{mozillalibdir}/chrome/*.rdf
#ghost %{mozillalibdir}/chrome/overlayinfo
%verify (not md5 mtime size) %{mozillalibdir}/greprefs/all.js
%if %{enable_svg}
#{mozillalibdir}/chrome/svg.jar
#{mozillalibdir}/components/gksvgrenderer.xpt
#{mozillalibdir}/res/svg.css
%endif
%{mozillalibdir}/plugins/libunixprintplugin.so
%{mozillalibdir}/chrome/reporter.jar
%{mozillalibdir}/chrome/xforms.jar
%{mozillalibdir}/components/xforms.xpt
%{mozillalibdir}/components/libxforms.so
%{mozillalibdir}/components/schemavalidation.xpt
%{mozillalibdir}/components/libschemavalidation.so
%{mozillalibdir}/components/nsSchemaValidatorRegexp.js
%{mozillalibdir}/components/nsURLFormatter.js
%{mozillalibdir}/components/saxparser.xpt
%{mozillalibdir}/components/urlformatter.xpt
%{mozillalibdir}/chrome/sql.jar
%{mozillalibdir}/components/sql.xpt
%{mozillalibdir}/components/libsql.so
%{mozillalibdir}/chrome/xforms.manifest
%{mozillalibdir}/chrome/inspector.manifest
%{mozillalibdir}/chrome/reporter.manifest

%files mail -f %{_tmppath}/mozilla-mail.list
%defattr(-,root,root)
%{_datadir}/applications/mandriva-%{name}-mail.desktop
%{_datadir}/applications/mandriva-%{name}-news.desktop
%{_datadir}/applications/mandriva-%{name}-addressbook.desktop
%dir %{mozillalibdir}
%{mozillalibdir}/isp

%files irc -f %{_tmppath}/mozilla-chat.list
%defattr(-,root,root)
%{_datadir}/applications/mandriva-%{name}-chat.desktop


%files devel -f %{_tmppath}/mozilla-devel.list
%defattr (-,root,root)
%{_bindir}/seamonkey-config
%if %{mdkversion} >= 1020
%multiarch %{multiarch_bindir}/seamonkey-config
%multiarch %{multiarch_includedir}/seamonkey-%{version}/js/jsautocfg.h
%multiarch %{multiarch_includedir}/seamonkey-%{version}/mozilla-config.h
%endif
%dir  %{mozillaincludedir}/accessibility
%dir  %{mozillaincludedir}/addrbook
%dir  %{mozillaincludedir}/appcomps
%dir  %{mozillaincludedir}/appshell
%dir  %{mozillaincludedir}/autoconfig
%dir  %{mozillaincludedir}/bayesflt
%dir  %{mozillaincludedir}/browser
%dir  %{mozillaincludedir}/caps
%dir  %{mozillaincludedir}/chardet
%dir  %{mozillaincludedir}/commandhandler
%dir  %{mozillaincludedir}/composer
%dir  %{mozillaincludedir}/content
%dir  %{mozillaincludedir}/cookie
%dir  %{mozillaincludedir}/dbm
%dir  %{mozillaincludedir}/docshell
%dir  %{mozillaincludedir}/dom
%dir  %{mozillaincludedir}/downloadmanager
%dir  %{mozillaincludedir}/editor
%dir  %{mozillaincludedir}/embed_base
%dir  %{mozillaincludedir}/embedcomponents
%dir  %{mozillaincludedir}/expat
%dir  %{mozillaincludedir}/exthandler
%dir  %{mozillaincludedir}/filepicker
%dir  %{mozillaincludedir}/find
%dir  %{mozillaincludedir}/gfx
%dir  %{mozillaincludedir}/gtkxtbin
%dir  %{mozillaincludedir}/gtkembedmoz
#dir  %{mozillaincludedir}/helperAppDlg
%dir  %{mozillaincludedir}/history
%dir  %{mozillaincludedir}/htmlparser
%dir  %{mozillaincludedir}/imglib2
%dir  %{mozillaincludedir}/impComm4xMail
%dir  %{mozillaincludedir}/import
%dir  %{mozillaincludedir}/inspector
%dir  %{mozillaincludedir}/intl
#dir  %{mozillaincludedir}/ipcd
%dir  %{mozillaincludedir}/jar
%dir  %{mozillaincludedir}/java
%dir  %{mozillaincludedir}/js
%dir  %{mozillaincludedir}/jsconsole
%dir  %{mozillaincludedir}/jsdebug
%dir  %{mozillaincludedir}/jsurl
%dir  %{mozillaincludedir}/layout
%dir  %{mozillaincludedir}/layout_debug
%dir  %{mozillaincludedir}/ldap
#dir  %{mozillaincludedir}/libart_lgpl
%dir  %{mozillaincludedir}/libreg
%dir  %{mozillaincludedir}/liveconnect
%dir  %{mozillaincludedir}/locale
%dir  %{mozillaincludedir}/lwbrk
%dir  %{mozillaincludedir}/mailnews
%dir  %{mozillaincludedir}/mailview
%dir  %{mozillaincludedir}/mime
%dir  %{mozillaincludedir}/mimeemitter
%dir  %{mozillaincludedir}/mimetype
%dir  %{mozillaincludedir}/mork
%dir  %{mozillaincludedir}/mozldap
%dir  %{mozillaincludedir}/msgbase
%dir  %{mozillaincludedir}/msgbaseutil
%dir  %{mozillaincludedir}/msgcompose
%dir  %{mozillaincludedir}/msgdb
%dir  %{mozillaincludedir}/msgimap
%dir  %{mozillaincludedir}/msglocal
%dir  %{mozillaincludedir}/msgmdn
%dir  %{mozillaincludedir}/msgsmime
%dir  %{mozillaincludedir}/msgnews
%dir  %{mozillaincludedir}/necko
%dir  %{mozillaincludedir}/necko2
%dir  %{mozillaincludedir}/nkcache
%dir  %{mozillaincludedir}/oji
%dir  %{mozillaincludedir}/p3p
%dir  %{mozillaincludedir}/pipboot
%dir  %{mozillaincludedir}/pipnss
%dir  %{mozillaincludedir}/pippki
%dir  %{mozillaincludedir}/plugin
%dir  %{mozillaincludedir}/pref
%dir  %{mozillaincludedir}/prefetch
%dir  %{mozillaincludedir}/prefmigr
%dir  %{mozillaincludedir}/profdirserviceprovider
%dir  %{mozillaincludedir}/profile
#dir  %{mozillaincludedir}/profilesharingsetup
%dir  %{mozillaincludedir}/progressDlg
%dir  %{mozillaincludedir}/rdf
%dir  %{mozillaincludedir}/rdfutil
%dir  %{mozillaincludedir}/shistory
#dir  %{mozillaincludedir}/sidebar
%dir  %{mozillaincludedir}/spellchecker
%dir  %{mozillaincludedir}/string
%dir  %{mozillaincludedir}/system-pref
%dir  %{mozillaincludedir}/typeaheadfind
%dir  %{mozillaincludedir}/txmgr
%dir  %{mozillaincludedir}/txtsvc
%dir  %{mozillaincludedir}/uconv
%dir  %{mozillaincludedir}/ucvcn
%dir  %{mozillaincludedir}/ucvibm
%dir  %{mozillaincludedir}/ucvja
%dir  %{mozillaincludedir}/ucvko
%dir  %{mozillaincludedir}/ucvlatin
%dir  %{mozillaincludedir}/ucvmath
%dir  %{mozillaincludedir}/ucvtw
%dir  %{mozillaincludedir}/ucvtw2
%dir  %{mozillaincludedir}/unicharutil
%dir  %{mozillaincludedir}/uriloader
%dir  %{mozillaincludedir}/util
%dir  %{mozillaincludedir}/view
%dir  %{mozillaincludedir}/wallet
%dir  %{mozillaincludedir}/walletviewers
%dir  %{mozillaincludedir}/webbrowserpersist
%dir  %{mozillaincludedir}/webbrwsr
%dir  %{mozillaincludedir}/websrvcs
%dir  %{mozillaincludedir}/webshell
%dir  %{mozillaincludedir}/widget
%dir  %{mozillaincludedir}/windowwatcher
#dir  %{mozillaincludedir}/xlibrgb
%dir  %{mozillaincludedir}/xml-rpc
#dir  %{mozillaincludedir}/xmlextras
%if %{build_xmlterm}
%dir  %{mozillaincludedir}/xmlterm
%endif
%dir  %{mozillaincludedir}/xpcom
%dir  %{mozillaincludedir}/xpcom_obsolete
%dir  %{mozillaincludedir}/xpconnect
%dir  %{mozillaincludedir}/xpinstall
%dir  %{mozillaincludedir}/xpnet
#dir  %{mozillaincludedir}/xprintutil
#dir  %{mozillaincludedir}/xremoteservice
%dir  %{mozillaincludedir}/xul
%dir  %{mozillaincludedir}/xuldoc
%dir  %{mozillaincludedir}/xultmpl
%dir  %{mozillaincludedir}/zlib
%{mozillalibdir}/xpcshell
%{mozillalibdir}/xpidl
%{mozillalibdir}/xpt_dump
%{mozillalibdir}/xpt_link
%{_libdir}/pkgconfig/seamonkey-js.pc
%{_libdir}/pkgconfig/seamonkey-xpcom.pc
%{_libdir}/pkgconfig/seamonkey-gtkmozembed.pc
%{_libdir}/pkgconfig/seamonkey-plugin.pc
%if !%{build_nspr_nss}
%{_libdir}/pkgconfig/seamonkey-nspr.pc
%{_libdir}/pkgconfig/seamonkey-nss.pc
%endif
%{mozillaidldir}

%if %{build_xmlterm}
%files xmlterm
%defattr(-, root, root)
%{_bindir}/xmlterm
%{_bindir}/xcat
%{_bindir}/xls
%{mozillalibdir}/chrome/xmlterm.jar
%{mozillalibdir}/components/*xmlterm*
%{_datadir}/applications/mandriva-%{name}-xmlterm.desktop
%endif

%files js-debugger -f %{_tmppath}/mozilla-js-debugger.list
%defattr(-,root,root)

%files dom-inspector -f %{_tmppath}/mozilla-dom-inspector.list
%defattr(-,root,root)
#dir %{mozillalibdir}/res/inspector

%files spellchecker -f %{_tmppath}/mozilla-spellchecker.list
%defattr(-,root,root)
%{mozillalibdir}/dictionaries

%if %build_enigmail
%files enigmail -f %{_tmppath}/mozilla-enigmail.list
%defattr(-,root,root)

%files enigmime -f %{_tmppath}/mozilla-enigmime.list
%defattr(-,root,root)
%endif

%if %{build_nspr_nss}

%files -n %{lib_nspr_name} -f %{_tmppath}/mozilla-nspr.list
%defattr(-, root, root)

%files -n %{devel_nspr_name} -f %{_tmppath}/mozilla-nspr-devel.list
%defattr(-, root, root)
%dir %{mozillaincludedir}
%dir  %{mozillaincludedir}/nspr
%dir  %{mozillaincludedir}/nspr/private
%dir  %{mozillaincludedir}/nspr/md
%dir  %{mozillaincludedir}/nspr/obsolete
%{_libdir}/pkgconfig/mozilla-nspr.pc
%{_datadir}/aclocal/nspr.m4

%files -n %{lib_nss_name} -f  %{_tmppath}/mozilla-nss.list
%defattr(-, root, root)
%{_libdir}/*.chk

%files -n %{devel_nss_name} -f %{_tmppath}/mozilla-nss-devel.list
%defattr(-, root, root)
%dir  %{mozillaincludedir}/nss
%{_libdir}/pkgconfig/mozilla-nss.pc
%endif

