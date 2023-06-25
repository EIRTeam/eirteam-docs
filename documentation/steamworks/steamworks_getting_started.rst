.. _doc_steamworks_getting_started:

Getting started
===============

The steamworks module allows you to interact with the Steam API in a seamless way,
note this is not a 1:1 translation of the API as it is inspired by `Facepunch.Steamworks <https://github.com/Facepunch/Facepunch.Steamworks>`_,
if you want something like that, check out Gramps' `GodotSteam <https://github.com/Gramps/GodotSteam/>`_ bindings.

Error handling
--------------

In some cases, you can get more info about errors by calling :ref:`Steamworks.get_last_error() <class_Steamworks_method_get_last_error>`
right after an :ref:`Error<enum_@GlobalScope_Error>` is returned.

Initializing
------------

To initialize steamworks simply call :ref:`Steamworks.init() <class_Steamworks_method_init>`, you may want to .

Input glyphs integration
------------------------

You can also seamlessly integrate with the input glyphs module very easily, all you need
to do is to have both modules in your engine. When you call :ref:`HBSteamInput.init() <class_HBSteamInput_method_init>` it will
automatically initialize the input glyphs module to use Steamworks as the source for your glyphs.

.. warning:: Make sure you read the warning in the :ref:`documentation for the input glyphs module <doc_input_glyphs_getting_started_steamworks_integration>`,
    as you will need to make sure your game. respects SDL ignore environment variables and other things.
