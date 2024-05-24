.. _doc_ph_replay_format_proposal:

PH Replays
==========================

This document describes a proposal for storing replays for Project Heartbeat

Replay package
--------------

PH replays are contained within a file similar to a ZIP file with UTF-8 file namings

The structure is the following:

* root/
    * replay.json
        Contains basic replay information metadata, does not include the actual replay data.
        
    * replay.phr
        Contains actual replay information.

    * song.json
        Contains a copy of the original song.json meta file.

Replay info metadata (replay.json)
----------------------------------

Should be a JSON file with the following structure:

* root
    * song_id: String
        Local ID of the song.
    
    * song_ugc_id: String (optional)
        UGC service ID of the song, if available.

    * song_ugc_service: String (optional)
        UGC service this song comes from (currently only "Steam Workshop").

    * song_title: String
        Song title

    * song_title_romanized: String
        Song title (romanized version).
    
    * difficulty: String
        Difficulty (chart name) of the played song.

    * user_id: String
        Service ID of the player that played this replay
        Might be:
        - SteamID64 (for Steam users).
        - Windows/Linux user name for when Steam was not available when creating the replay.
            
    * user_service: String
        Service the player for this replay came from (should be "steam" or "local" for non logged in users).

    * chart_hash: String
        A SHA-1 generated from the contents of the original chart .json file.

Replay file (replay.phr)
------------------------

All in little endian.

All strings are utf-8 and have their length prefixed as a uint16.

* Magic number: ``0x50`` ``0x48`` ``0x52`` (``PHR``).
* Version: uint8
* Song ID: String
* Song difficulty String
* Song chart hash: String

* Gamepad device count: uint8
* Gamepad device metadatas:
    * Device id: uint8
    * Device name: String
    * Device SDL GUID: String (may be empty)

* Event count: uint32
* Events

EVENT_TYPE: uint8
-----------------

.. list-table::
   :widths: 5 25 75
   :header-rows: 1

   * - Value
     - Name
     - Description
   * - 0
     - GAMEPAD_JOY_AXIS
     - Single axis gamepad
   * - 1
     - GAMEPAD_JOY
     - Two axis gamepad
   * - 2
     - GAMEPAD_BUTTON
     - Gamepad button
   * - 3
     - KEYBOARD_KEY
     - Keyboard key

ACTION_BITFIELD: uint8
^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 5 25
   :header-rows: 1

   * - Value
     - Name
   * - 0x1
     - NOTE_UP
   * - 0x2
     - NOTE_LEFT
   * - 0x4
     - NOTE_DOWN
   * - 0x8
     - NOTE_RIGHT
   * - 0x10
     - SLIDE_LEFT
   * - 0x20
     - SLIDE_RIGHT

* Event type: uint8
* Event game timestamp, in microseconds: int64
* Action: Replay action bitfield
    Main action for this event
* Actions: Replay action bitfield
    Actions triggered by this individual hardware press
* Pressed: uint8
    Whether this is a press or release event
* Event data:
    .. code-block:: cpp

        union {
            double joystick_position[2]; // Second value will be 0.0 in case of single axis events
            uint8_t gamepad_button_idx;
            uint8_t keyboard_key;
        }
