#!/bin/bash

set -e

git clone https://$GIT_TOKEN@github.com/vial-kb/via-keymap-precompiled.git
cd via-keymap-precompiled
git config user.email "vial@xyz.is"
git config user.name "Vial Bot"
cp ../via_keyboard_stack.json .
git add .
git commit -m "Update at $(date)" || true
git push
