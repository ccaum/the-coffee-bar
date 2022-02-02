#!/bin/bash

flag=$1
environment=$2

#Get current state of the feature flag
environment_string=".items[0].environments.${environment}.on"
is_currently_on=`curl -s -H "Authorization: ${LD_API_TOKEN}" -H "Content-Type: application/json"  "https://app.launchdarkly.com/api/v2/flags/default/${flag}" | jq ".environments.${environment}.on"`

if [ $is_currently_on == "true" ]; then
    curl -s -X PATCH -H "Authorization: ${LD_API_TOKEN}" -H "Content-Type: application/json; domain-model=launchdarkly.semanticpatch" -d "{ \"environmentKey\": \"${environment}\", \"instructions\": [ {\"kind\": \"turnFlagOff\"} ] }"  https://app.launchdarkly.com/api/v2/flags/default/auto-dispenser
else
    curl -s -X PATCH -H "Authorization: ${LD_API_TOKEN}" -H "Content-Type: application/json; domain-model=launchdarkly.semanticpatch" -d "{ \"environmentKey\": \"${environment}\", \"instructions\": [ {\"kind\": \"turnFlagOn\"} ] }"  https://app.launchdarkly.com/api/v2/flags/default/auto-dispenser
fi
