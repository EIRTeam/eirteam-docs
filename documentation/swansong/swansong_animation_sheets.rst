.. _doc_swansong_animation_sheets:

Animation sheets
================

.. note:: Animations marked with (W) must use warp motion.
.. note:: Animations marked with (FIK) must use feet IK.
.. note:: Animations marked with (L) must loop.


Biped per-character
-------------------

These are animations where sharing them between character is discouraged, that's because these are the animations that
differentiate between characters the most.

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Name
     - Description
     - Duration
   * - Idle (FIK) (L)
     - Standing pose, this pose should communicate something about how the character is and other environmental factors
       guch as the weight of their gear.
     - 40-50 frames
   * - Walk (FIK) (L)
     - Slow walking, like you would see in a non-agitated every day walking scenario, must be done in
       Contact-L -> Contact-R -> Contact-L form.
     - **MUST** be 60 frames long for the procedural stride system.
   * - Running (FIK) (L)
     - Running, in a rush but without looking like the character is using up all their energy.
     - **MUST** be 60 frames long for the procedural stride system.

Player specific
---------------

.. list-table::
    :header-rows: 1
    :stub-columns: 1
    :widths: 25 50 15

    * - Name
      - Description
      - Duration
    * - Sprint heavy (FIK) (L)
      - Running animation with more weight in the stride and a more curved back, used for the animation system to create a
        "bounce" effect when starting a sprint.
      - **MUST** be 60 frames long for the procedural stride system.
    * - Wallrun (W)
      - The character reaches a wall and starts runnning up it.
      - ~50 frames.
    * - Edge slide down (W)
      - The character crouches reaches the ledge with their right hand and uses it as a pivot to slide down it,
        use for sliding off low to the ground ledges.
      - ~40 frames.
    * - Standing to ledge grab (W)
      - The start is similar to edge slide down, however instead of sliding off the edge and landing the character pivots
        from the hand to turn aroud 180 degrees and grab the ledge.
      - ~40 frames.
    * - Vault (W)
      - The character runs towards the object jumps and uses their hand as a support on the object itself, the character then
        uses their momentum to jump over the object.
      - ~70 frames.
    * - Ledge grabbed idle (L)
      - Idle animation of the character hanging off a ledge with their feet on the wall. Acquiring a posture similar to a frog or a cat.
      - 40-50 frames
    * - Ledge grabbed dangling idle (L)
      - Idle animation of the character hanging off a ledge with their feet not supported by anything, the head
        height should be lower than the normal ledge grabbed idle.
      - 40-50 frames
    * - Crouched idle (FIK)
      - Idle standing pose for the character while crouched, also used for beam walking.
      - 40-50 frames
    * - Crouched walk (FIK)
      - Character walking while crouched. The character will rise their hip a little bit. Also used for beam walking.
      - **MUST** be 60 frames long for the procedural stride system.
    * - Crouched spring (FIK)
      - Character running while crouched. The character will rise their hip even more compared to the walk. Also used for beam walking.
      - **MUST** be 60 frames long for the procedural stride system.
    * - Back eject (W)
      - Character pushes against a wall and uses it to turn around, effectively turning around 180 degrees.
      - ~50 frames.
    * - Short hop (W)
      - From a standing position, the character jumps forward closing a small gap.
      - ~30 frames.
    * - Down jump (W)
      - Character jumps down from the current standing position, it should give a feeling that the character is throwing
        itself off a high point instead of simply being magically moved.
      - ~50 frames.
    * - Down jump idle (L)
      - Animation played after the character has done a down jump and is currently falling.
      - Any.
    * - Hard landing (W)
      - Hard hit of the ground, the character should be visibly in pain.
      - ~70 frames.
    * - Rolling landing (W)
      - Character hits the ground from a fall and performs a typical parkour roll.
      - ~40 frames.
    * - Sprint turn (W)
      - Character suddenly stops running and changes its direction 180 degrees.
      - ~50 frames.