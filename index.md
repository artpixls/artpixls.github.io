---
title: Home
---
<!-- ![ART](logo.png) -->

<!-- ## About -->

Welcome to the home page of ART, a [free, open-source](https://www.gnu.org/philosophy/philosophy.html), cross-platform 
raw image processing program. 
ART is a derivative of the popular [RawTherapee](http://rawtherapee.com),
trading a bit of customization and control over various processing parameters for a simpler and (hopefully) easier to use interface,
while still maintaining the power and quality of RawTherapee.

## Features

At a first glance, ART appears very similar to RawTherapee. 
Compared to the latter, ART differs in the following main aspects:

- The user interface and the underlying processing pipeline have been significantly restructured, with many tools removed, some new tools added, and several tools rewritten and/or refactored. 

- Various new tools for performing local edits have been added, with support for various masking modes (both drawn and parametric).

- A new automatic perspective correction tool (taken from [darktable](http://darktable.org)) has been added.

- Better metadata handling (thanks to the [exiv2](http://exiv2.org) and [exiftool](http://exiftool.org) libraries), with (optional) support for reading and writing XMP sidecar files.

- Support for using [LibRaw](https://www.libraw.org) for decoding raw files.

- Support for [ACES CLF LUTs](https://docs.acescentral.com/specifications/clf/) using [OpenColorIO](https://opencolorio.org/).

- Support for [CTL scripts](https://acescentral.com/knowledge-base-2/ctl/) using the [ACES CTL interpreter](https://github.com/ampas/CTL).

- Star ratings and colour labels can be loaded and stored from/to XMP sidecar files.

- Snapshots are now permanent, saved in the processing profiles.

- Processing profiles have `.arp` extension instead of `.pp3`, to avoid conflicts with RawTherapee.

- The "inspector mode" tool of the file browser has been significantly enhanced.

## Status

The current version is 1.24.1. It was released on October 10th 2024.
[Change log](https://bitbucket.org/agriggio/art/branches/compare/1.24.1%0D1.23).

## Contact

[ART discussion group](https://discuss.pixls.us/c/software/ART).

## License 
ART is released under the [GNU General Public License version 3](https://www.gnu.org/licenses/gpl.html).