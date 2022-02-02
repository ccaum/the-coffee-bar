#!/bin/sh

service=$1

cat flags.json| jq -r ".flags.\"${service}\".value"
