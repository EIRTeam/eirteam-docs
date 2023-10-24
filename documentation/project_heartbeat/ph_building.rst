.. _doc_ph_building:

Building Project Hearbteat
==========================

In late 2023 work was started on a port of PH to Godot 4, this means that building the game is different depending on what
branch of the engine you are using.

Current development of the game is done on the 4.0 version of the Godot Engine, this is the recommended branch of the game
to develop new features against and will replace the stable version eventually.

However, due to the complexity of the game it is necessary to use a customized version of the engine. This customized version
lives under the shinobu_gd4 branch of the engine repository. Which can be found `here <https://github.com/EIRTeam/godot/tree/shinobu_gd4>`_.

Obtaining the engine code
-------------------------

Building this version of the engine is simple, first make sure you have cloned the correct branch and that you initialized the submodules,
these contain essential godot engine modules that make some features of the game tick::

    git clone --recurse-submodules https://github.com/EIRTeam/godot.git -b shinobu_gd4

After you have the engine, it's time to compile it.

Building the engine
-------------------

Building the engine is as simple as building the original godot engine, I suggest you check out the `building from source <https://docs.godotengine.org/en/stable/contributing/development/compiling/index.html>`_
page of the Godot documentation to see what dependencies you need.

For building the binary that's shipped with the game (AKA, optimized and without the Godot editor) you can run::

    scons production=yes target=template_release

For general development, I recommend::

    scons target=editor fast_unsafe=no optimize=speed_trace

For engine code development use:

    scons target=editor fast_unsafe=no optimize=debug

The official Linux build is compiled on Ubuntu 22.04 to achieve old glibc compatibility, that way the game will work on older operating systems.

The official windows build is compiled on Arch using mingw-w64 and the latest gcc, this is to achieve higher performance on the compiled binary and for ease of development.

Obtaining the game's code
-------------------------

To checkout the Godot 4 branch, clone the game's code, make sure you have git lfs!::

    git clone https://github.com/EIRTeam/Project-Heartbeat.git -b godot4

Improving engine compile times
------------------------------

SCons and by extension, Godot, are known to have terrible compile times, in order to iterate faster on native engine changes you can apply a bunch of optimizations.

Firstly, you should install pyston or pypy, since those provide a nice performance boost over the original python.

You should use gcc and the mold linker since those provide the highest build and linking speed, to do this specify the following on your scons command line::

    linker=mold

If you have lots of ram, you can do single compilation unit (SCU) builds,
please make sure you test building the engine without SCU before PRing any changes.
This is because SCU builds by nature include headers from earlier .cpp files in the translation unit, therefore won't catch all the includes you will need in a regular build.

To do an SCU build, simple add this to your scons command line::

    scu_build=yes

Finally, you can use the fast_unsafe option to improve build times further::

    dev_unsafe=yes
