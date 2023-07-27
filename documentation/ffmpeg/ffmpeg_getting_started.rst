.. _doc_ffmpeg_getting_started:

Getting started
===============

.. image:: img/cover.jpg

The FFmpeg module allows you to integrate FFmpeg for video playback into Godot.
The code is inspired by osu's video decoder, but improved with new features, such as support for audio playback.

Downloads
---------

The latest downloads can be found `here <https://github.com/EIRTeam/EIRTeam.FFmpeg/releases>`__.

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