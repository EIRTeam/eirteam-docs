.. _doc_input_glyphs_getting_started:

Getting started
===============

.. warning:: To be able to use this module you need to have `this PR <https://github.com/godotengine/godot/pull/78539>`_ 
    in your engine. This is necessary because Steam Input sets the environment variable `SDL_GAMECONTROLLER_IGNORE_DEVICES` and
    expects you to respect it by ignoring the controllers it gives you.
    
    Even if you are not using Steam Input, the PR is still suggested as it gives you some metadata that could be useful for debugging.

The input glyph module allows you to automatically change the displayed glyphs in your
game to match the controller the user is using at this time.

The system will automatically switch the glyphs around when a button is pressed on any controller (keyboard support is pending).

By default, it will use Steamworks glyphs extracted from Steamworks, which are identified using the same method as SDL uses.

You can also force specific glyphs to be used, it is suggested to expose this to your users
see :ref:`InputGlyphsSingleton.forced_input_type <class_InputGlyphsSingleton_property_forced_input_type>` for more info.

The default glyph themes can be set in the Project Settings.

.. _doc_input_glyphs_getting_started_steamworks_integration:

Steamworks integration
----------------------

You can also seamlessly integrate with the Steamworks module very easily, all you need
to do is to have both modules in your engine. When you call :ref:`HBSteamInput.init() <class_HBSteamInput_method_init>` it will
automatically initialize the input glyphs module to use Steamworks as the source for your glyphs.

.. warning:: Make sure you have the :ref:`PR mentioned before <doc_input_glyphs_getting_started>` merged, otherwise
    the input glyphs system won't be able to identify which controllers are bound to which steamworks input handles.

