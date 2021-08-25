%global debug_package %{nil}

Name: git-lfs
Epoch: 100
Version: 3.1.1
Release: 1%{?dist}
Summary: Git extension for versioning large files
License: MIT
URL: https://github.com/git-lfs/git-lfs/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: golang-1.18
BuildRequires: glibc-static
BuildRequires: git
Requires: git

%description
Git Large File Storage (LFS) replaces large files such as audio samples,
videos, datasets, and graphics with text pointers inside Git, while
storing the file contents on a remote server like GitHub.com or GitHub
Enterprise.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
mkdir -p bin
    set -ex && \
        export CGO_ENABLED=1 && \
        go build \
            -mod vendor -buildmode pie -v \
            -ldflags "-s -w" \
            -o ./bin/git-lfs .

%install
install -Dpm755 -d %{buildroot}%{_bindir}
install -Dpm755 -t %{buildroot}%{_bindir}/ bin/git-lfs

%files
%license LICENSE.md
%{_bindir}/*

%changelog
