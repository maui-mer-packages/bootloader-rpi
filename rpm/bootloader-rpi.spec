Name:       bootloader-rpi

Summary:    Raspberry Pi bootloader files
Version:    0.0.4
Release:    1
Group:      Kernel/Linux Kernel
License:    GPLv2 and Broadcom Proprietary
URL:        https://github.com/raspberrypi/firmware
Source0:    bootloader-rpi-%{version}.tar.xz

%description
Bootloader files for RaspberryPi

%package kernel
Summary:    Default kernel for RaspberryPi Broadcom VideoCore
Group:      Kernel/Linux Kernel

%description kernel
Kernel from firmware git for RaspberryPi Broadcom VideoCore.


%prep
%setup -q -n %{name}-%{version}/upstream


%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}
cp -a boot %{buildroot}
mkdir -p %{buildroot}/lib
cp -a modules %{buildroot}/lib


%files
%defattr(-,root,root,-)
/boot/bootcode.bin
/boot/fixup_cd.dat
/boot/fixup_x.dat
/boot/start_cd.elf
/boot/start_x.elf
/boot/COPYING.linux
/boot/fixup.dat
/boot/LICENCE.broadcom
/boot/start.elf

%files kernel
%defattr(-,root,root,-)
/boot/kernel.img
/lib/modules/*
