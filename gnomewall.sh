#!/bin/bash
#
# Author: Egidio Docile <egdoc.dev@gmail.com>
#
# Sets a selected jpeg or png picture both as gnome wallpaper and screensaver
# background. If multiple pictures are selected only the first is used.
set -e
set -u

for i in $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS; do
  if [[ "$(file "${i}")" =~ JPEG|PNG ]]; then
    for key in desktop/background desktop/screensaver; do
      eval dconf write "/org/gnome/${key}/picture-uri" \"\'"${i}"\'\"
      dconf write "/org/gnome/${key}/picture-options" \"\'scaled\'\"
    done
    break
  fi
done
