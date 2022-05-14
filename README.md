# fedora-pkg

Temporary space for Fedora spec during Budgie Desktop review process.

## Steps for Building

- Generate the src package: `fedpkg --release NUM mockbuild --no-clean --no-cleanup-after`
- Build and don't do cleanup so we can create the binary packages:  `mock --no-clean -N -r fedora-NUM-x86_64 --postinstall xyz.src.rpm`

You will need to at least build budgie-desktop-view and budgie-screensaver before budgie-desktop. budgie-control-center can be done separately.
