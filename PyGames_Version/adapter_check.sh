#!/bin/bash


echo $(route | grep '^default' | grep -o '[^ ]*$')

