#!/usr/bin/env bash

run_test() {
    local test_name="$1"
    local result_file="${test_name}.result"
    
    uv run main.py "$test_name" > "$result_file"
    sed -i 's/)\s*$/\n)/g' "$result_file"
    sed -i 's/(stat/\n\t(stat/g' "$result_file"
    sed -i 's/(bool_stat/\n\t(bool_stat/g' "$result_file"
    sed -i 's/if/\n\tif/g' "$result_file"
    sed -i 's/else/\n\telse/g' "$result_file"
}

run_test test.ail
run_test test.df.ail
# run_test test2.ail # This test does not run because of from2data
