.. _doc_ffmpeg_getting_started:

Getting started
===============

.. image:: img/cover.jpg

The FFmpeg module allows you to integrate FFmpeg for video playback into Godot.
The code is inspired by osu's video decoder, but improved with new features, such as support for audio playback.

Downloads
---------

The latest downloads can be found `here <https://github.com/EIRTeam/EIRTeam.FFmpeg/releases>`__.

Build
-----

You can build the extension yourself by cloning the `repository <https://github.com/EIRTeam/EIRTeam.FFmpeg>`__ and running ``./build.sh``.
The following parameters can be passed in order:

.. list-table:: Settings
   :header-rows: 1

   * - 
     - Setting
     - Default Value
     - Description
   * - 1
     - ``TARGET``
     - all
     - What kind of build to perform. Can be editor, template_release, template_debug, or all to perform all three other kinds
   * - 2
     - ``PLATFORM``
     - linux
     - What OS to build for
   * - 3
     - ``SCONS_VERSION``
     - 4.4.0
     - Which version of `SCons <https://scons.org/>`__ to use
   * - 4
     - ``FFMPEG_RELATIVE_PATH``
     - ffmpeg-master-latest-linux64-lgpl-godot
     - Where ffmpeg will be installed (or if ``SKIP_FFMPEG_IMPORT`` is true, where it already is installed)
   * - 5
     - ``FFMPEG_URL_OR_PATH``
     - `https://github.com/EIRTeam/FFmpeg-Builds/releases/download/latest/${FFMPEG_RELATIVE_PATH}.tar.xz <https://github.com/EIRTeam/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-lgpl-godot.tar.xz>`__
     - Where an FFMPEG build can be found (ignored if ``SKIP_FFMPEG_IMPORT`` is true)
   * - 6
     - ``FFMPEG_TARBALL_PATH``
     - ffmpeg.tar.xz
     - Where to download or copy the ffmpeg tarball to (ignored if ``SKIP_FFMPEG_IMPORT`` is true)
   * - 7
     - ``SKIP_FFMPEG_IMPORT``
     - false
     - Skip downloading/copying and extracting ffmpeg and assume that ``FFMPEG_RELATIVE_PATH`` already has ffmpeg installed to it.
   * - 8
     - ``SCONS_FLAGS``
     - debug_symbols=no
     - Flags to pass on to the `SCons <https://scons.org/>`__ command




Installation
------------

Installation is as simple as placing the addons folder from the extension at the root of your Godot project, Godot
should automatically pick it up.

Usage
-----

Any compatible file will be automatically picked up by the engine when you add it to your project, you can also make an instance of
``FFmpegVideoStream`` and set the ``file`` property to the path of the file you want to play.

Performance
-----------

Performance should be better than the old godot-videodecoder, but it's not ideal, there's no
hardware decoding support (yet, not sure if it's even possible) and it doesn't make use of YCbCr when available, which would save
a complete conversion step.

Another potential optimization would be to allocate and write directly to a godot ``Vector<uint8_t>`` type, this is because a ``Vector<uint8_t>`` is needed
to update textures, which is a godot internal copy on write container that cannot be created without copying the whole frame to it.

The FFmpeg library
------------------

The extension comes with a stripped down build of the ffmpeg library that is automatically built to use an old as
possible version of glibc, that way it's compatible with all systems, this is downloaded from `here <https://github.com/EIRTeam/ffmpeg-builds/>`__ during the compilation process.

This version also removes most codecs, the available codecs and demuxers are printed on startup.

If you want to use your own ffmpeg library, it's likely that you can simply replace the ``.so`` and ``.dll`` files with your build of a similar version.

The LGPL builds found `here <https://github.com/BtbN/FFmpeg-Builds/releases>`__ should also be compatible.

Supporting development
----------------------

This module was kindly released by EIRTeam as a part of the open source initiative to drive more funds to continue
development of `Project Heartbeat <https://store.steampowered.com/app/1216230/Project_Heartbeat/>`__ and to sustain myself, if you want to support development, please donate to our `Patreon <https://www.patreon.com/EIRTeam>`_.

.. image:: ../../img/patreon_support.png
    :target: https://www.patreon.com/EIRTeam
