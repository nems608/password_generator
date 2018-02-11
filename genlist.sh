#!/bin/bash

cp /usr/share/dict/words ./

# Remove non-ascii characters
grep -P '^[[:ascii:]]*$' words > words~
mv words~ words

# Remove non-alpha characters
grep -P '^[[:alpha:]]*$' words > words~
mv words~ words
