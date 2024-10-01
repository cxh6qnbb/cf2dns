name: Read Repo Variables

on:
  push:
    branches:
      - main

jobs:
  print-variable:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v2
        
      - name: Set MY_VAR from secret
        run: |
          echo "MY_VAR=${{ secrets.KEY }}" >> $GITHUB_ENV

      - name: Output MY_VAR
        run: |
          echo "MY_VAR is: $MY_VAR"
