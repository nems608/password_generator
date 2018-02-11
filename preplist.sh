#!/bin/bash
list=$1

# Remove non-ascii characters
grep -P '^[[:ascii:]]*$' $list > $list~
mv $list~ $list

# Remove non-alpha characters
grep -P '^[[:alpha:]]*$' $list > $list~
mv $list~ $list
