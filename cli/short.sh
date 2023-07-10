#!/bin/bash

# From: https://github.com/nelsontky/gh-pages-url-shortener/issues/49#issue-745134937
[[ ! -z "$@" ]] && (gh issue create --repo rooyca/short-db --title "$@" --body "" | sed -e 's/github.com\/rooyca\/short-db\/issues/rooyca.github.io\/short-db/g') || (echo "Forgot URL?"; exit 1)