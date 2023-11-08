#
# spec file for package liberate-formula
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           liberate-formula
Version:        0.1
Release:        0
Summary:        Formula to liberate servers and convert them to SLL
License:        GPL-3.0
Group:          System/Packages
Source:         liberate-formula-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%define fname liberate

%description
Formula to liberate servers and convert them to SLL

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/share/susemanager/formulas/states/%{fname}/files
mkdir -p %{buildroot}/usr/share/susemanager/formulas/metadata/%{fname}
cp -R %{fname}/* %{buildroot}/usr/share/susemanager/formulas/states/%{fname}
cp form.yml %{buildroot}/usr/share/susemanager/formulas/metadata/%{fname}
cp metadata.yml %{buildroot}/usr/share/susemanager/formulas/metadata/%{fname}

%files
%defattr(-,root,root,-)
/usr/share/susemanager

%changelog
