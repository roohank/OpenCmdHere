# OpenCmdHere

An NVDA add-on that opens an elevated Command Prompt in the current Explorer folder with a single keyboard shortcut.

**Repository:** [https://github.com/roohank/OpenCmdHere](https://github.com/roohank/OpenCmdHere)

## Features

- Opens Command Prompt as Administrator in the current Explorer folder.
- Falls back to `C:\Windows\System32` if no Explorer window is active.
- Uses a conflict-free default shortcut (`NVDA + Control + Windows + C`) that can be customized by the user.
- Provides audio feedback via NVDA's speech.

## Keyboard Shortcut

| Key Combination | Action |
|---|---|
| `NVDA + Control + Windows + C` | Open Command Prompt as Administrator in the current folder |

## How to Use

1. Open any folder in Windows Explorer.
2. Press `NVDA + Control + Windows + C`.
3. NVDA will announce "Opening Command Prompt...".
4. A UAC prompt will appear. Confirm it.
5. Command Prompt will open in the current folder with administrator privileges.

If no Explorer window is active, Command Prompt will open in `C:\Windows\System32`.

### Changing the Shortcut

If you prefer a different key combination:

1. Open the NVDA menu (`NVDA + N`).
2. Go to **Preferences** → **Input Gestures**.
3. In the tree view, find **OpenCmdHere**.
4. Select **Open Command Prompt as Administrator in the current Explorer folder**.
5. Click **Add**, press your desired key combination, and confirm.
6. Click **OK**.

## Requirements

- NVDA version 2019.3 or later.
- Windows 10 or Windows 11.

## Installation

1. Download the latest `OpenCmdHere.nvda-addon` file from the [Releases](https://github.com/roohank/OpenCmdHere/releases) page.
2. Press `Enter` on the file or double-click it.
3. Follow the on-screen instructions in NVDA to install the add-on.
4. Restart NVDA when prompted.

## Building from Source

If you want to build the add-on yourself:

1. Clone this repository:

   ```bash
   git clone https://github.com/roohank/OpenCmdHere.git
2. 
Make sure the folder structure looks like this:
text
Copy
Download
OpenCmdHere/
├── manifest.ini
├── README.md
├── LICENSE
├── doc/
│   └── en/
│       └── readme.html
└── globalPlugins/
    └── openCmdHere.py
3. 
Select manifest.ini, doc, and the globalPlugins folder.
4. 
Right-click → Send to → Compressed (zipped) folder.
5. 
Rename the resulting .zip file to OpenCmdHere.nvda-addon.
License
This add-on is released under the GNU General Public License v2.0. See the LICENSE file for details.
Author
• 
Roohan — GitHub: @roohank
Changelog
Version 1.0
• 
Initial release.