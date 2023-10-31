#!/usr/bin/env bash

export $(grep -v '^#' .env | xargs)

uvicorn smp_importer:app --reload
