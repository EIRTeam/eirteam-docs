.. _doc_input_glyph_styling:

Glyph styling
=============

The styling of glyphs is controlled by the :ref:`InputGlyphsStyle <enum_InputGlyphsSingleton_InputGlyphStyle>` bit flags
which are accepted by many of the input glyph methods.

Themes
------

There are three "themes" available to use in your glyphs, these are:

- | :ref:`Knockout <class_InputGlyphsSingleton_constant_GLYPH_STYLE_KNOCKOUT>`: Face buttons will have colored labels/outlines on a knocked out background.
  | Rest of inputs will have white detail/borders on a knocked out background.
- :ref:`Light <class_InputGlyphsSingleton_constant_GLYPH_STYLE_LIGHT>`: Black detail/borders on a white background.
- :ref:`Dark <class_InputGlyphsSingleton_constant_GLYPH_STYLE_DARK>`: White detail/borders on a black background.

ABXY-specific styling
---------------------

By default, ABXY/PS equivalent glyphs have a solid fill w/ color matching the physical buttons on the device.

You can apply extra styling features by mixing and matching the bit flags:

- :ref:`Neutral Color <class_InputGlyphsSingleton_constant_GLYPH_STYLE_NEUTRAL_COLOR_ABXY>`: ABXY Buttons will match the base style color instead of their normal associated color.
- :ref:`Neutral Color <class_InputGlyphsSingleton_constant_GLYPH_STYLE_SOLID_ABXY>`: ABXY Buttons will have a solid fill.

Comparison
----------

Below is a comparison table with different style options.

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * -
     - ABXY normal
     - ABXY neutral color
     - ABXY solid
     - ABXY neutral color + solid
     - Normal glyph
   * - Knockout
     - .. image:: img/glyphs/knockout/shared_color_button_a.svg
          :width: 128
     - .. image:: img/glyphs/knockout/shared_button_a.svg
          :width: 128
     - .. image:: img/glyphs/knockout/shared_color_outlined_button_a.svg
          :width: 128
     - .. image:: img/glyphs/knockout/shared_outlined_button_a.svg
          :width: 128
     - .. image:: img/glyphs/knockout/xbox_rb.svg
          :width: 128
   * - Light
     - .. image:: img/glyphs/light/shared_color_button_a.svg
          :width: 128
     - .. image:: img/glyphs/light/shared_button_a.svg
          :width: 128
     - .. image:: img/glyphs/light/shared_color_outlined_button_a.svg
          :width: 128
     - .. image:: img/glyphs/light/shared_outlined_button_a.svg
          :width: 128
     - .. image:: img/glyphs/light/xbox_rb.svg
          :width: 128
   * - Dark
     - .. image:: img/glyphs/dark/shared_color_button_a.svg
          :width: 128
     - .. image:: img/glyphs/dark/shared_button_a.svg
          :width: 128
     - .. image:: img/glyphs/dark/shared_color_outlined_button_a.svg
          :width: 128
     - .. image:: img/glyphs/dark/shared_outlined_button_a.svg
          :width: 128
     - .. image:: img/glyphs/dark/xbox_rb.svg
          :width: 128